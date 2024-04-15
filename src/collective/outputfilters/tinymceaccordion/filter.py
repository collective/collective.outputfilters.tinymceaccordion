from bs4 import BeautifulSoup
from bs4 import NavigableString
from collective.outputfilters.tinymceaccordion.interfaces import ITinyMCEAccordionFilter
from copy import copy
from zope.interface import implementer


def transform_bs5_collapse(html):
    # html = html.replace("\n", "")
    soup = BeautifulSoup(html, "html.parser")

    details = soup.find_all("details")

    accs = []
    accs_index = 0
    accs.insert(accs_index, [])

    # group the details tags
    for detail in details:

        next = detail.find_next_sibling()
        accs[accs_index].append(detail)

        if next and next.name != "details":
            accs_index += 1
            accs.insert(accs_index, [])
            continue

    # build the accordions from details groups
    acc_count = 0
    for acc in accs:

        bs5_acc_id = f"acc-bs{acc_count}"

        bs5_acc = soup.new_tag("div", attrs={"id": bs5_acc_id, "class": "accordion"})

        detail_counter = 0

        for details in acc:

            bs5_acc_heading_id = f"heading-{acc_count}-{detail_counter}"

            bs5_acc_collapse_id = f"collapse-{acc_count}-{detail_counter}"

            bs5_acc_item = soup.new_tag("div", attrs={"class": "accordion-item"})

            # check is open
            aria_expanded = "false"
            collapse_show = ""
            collapsed = "collapsed"
            if details.has_attr("open"):
                collapsed = ""
                aria_expanded = "true"
                collapse_show = "show"

            bs5_acc_header = soup.new_tag(
                "h2",
                attrs={
                    "id": bs5_acc_heading_id,
                    "class": "accordion-header",
                },
            )

            bs5_acc_header_button = soup.new_tag(
                "button",
                attrs={
                    "class": f"accordion-button {collapsed}",
                    "type": "button",
                    "data-bs-toggle": "collapse",
                    "data-bs-target": f"#{bs5_acc_collapse_id}",
                    "aria-expanded": f"{aria_expanded}",
                    "aria-controls": f"{bs5_acc_collapse_id}",
                },
            )

            bs5_acc_collapse = soup.new_tag(
                "div",
                attrs={
                    "id": f"{bs5_acc_collapse_id}",
                    "class": f"accordion-collapse collapse {collapse_show}",
                    "aria-labelledby": f"{bs5_acc_heading_id}",
                    "data-bs-parent": f"#{bs5_acc_id}",
                },
            )

            bs5_acc_collapse_body = soup.new_tag(
                "div",
                attrs={
                    "class": "accordion-body",
                },
            )

            # handle the children
            children = details.contents
            for child in children:
                if child.name == "summary":
                    for summary_child in child.contents:
                        if isinstance(summary_child, NavigableString):
                            bs5_acc_header_button.append(copy(summary_child.string))
                        else:
                            bs5_acc_header_button.append(copy(summary_child))
                else:
                    if isinstance(child, NavigableString):
                        bs5_acc_collapse_body.append(copy(child.string))
                    else:
                        bs5_acc_collapse_body.append(copy(child))

            # concat all elements and merge into the tree
            bs5_acc.append(bs5_acc_item)
            bs5_acc_item.append(bs5_acc_header)
            bs5_acc_item.append(bs5_acc_collapse)
            bs5_acc_header.append(bs5_acc_header_button)
            bs5_acc_collapse.append(bs5_acc_collapse_body)

            if detail_counter == 0:
                details.insert_before(bs5_acc)

            details.decompose()
            detail_counter += 1

        acc_count += 1

    return str(soup)


@implementer(ITinyMCEAccordionFilter)
class TinyMCEAccordionFilter:
    """Converts TinyMCE Accordion Plugin Markup to BS5 Accordion Markup."""

    order = 1953

    def is_enabled(self):
        return self.context is not None

    def __init__(self, context=None, request=None):
        self.context = context
        self.request = request

    def __call__(self, data):
        return transform_bs5_collapse(data)
