# README

![Plone Meta Workflow](https://github.com/collective/collective.outputfilters.tinymceaccordion/actions/workflows/meta.yml/badge.svg "Plone Meta Workflow") [![codecov](https://codecov.io/gh/collective/collective.outputfilters.tinymceaccordion/graph/badge.svg?token=Fr1Av8spXo "Code Coverage Workflow")](https://codecov.io/gh/collective/collective.outputfilters.tinymceaccordion) ![PyPI - Versions from Framework Classifiers](https://img.shields.io/pypi/frameworkversions/plone/collective.outputfilters.tinymceaccordion)


- [Who need this addon?](#who-need-this-addon)
- [Registry Settings](#registry-settings)
- [Install Addon via buildout](#install-addon-via-buildout)
- [Install Addon via pip](#install-addon-via-pip)
- [Install a Testenvironment](#install-a-testenvironment)
- [Start the instance](#start-the-instance)
- [Format and Linting](#format-and-linting)
- [Testing](#testing)
- [Testing with coverage](#testing-with-coverage)

> [!IMPORTANT]
> This addon works only with Plone 6.1 and higher
>
> For Plone 6.0 use plone.staticresources >= 2.2.x

## Who need this addon?

This addon provide a transform for HTML Markup. TinyMCE Plugin "accordion" insert the following Markup

```html
<details class="mce-accordion" open="open">
<summary>Accordion Summary 1</summary>
<p>Text in the collapsible 1</p>
</details>
<details class="mce-accordion" open="open">
<summary>Accordion Summary 2</summary>
<p>Text in the collapsible 2</p>
</details>
```

it will be transformed to Bootstrap5 Accordion Markup

```html
<div class="accordion" id="acc-bs0">
 <div class="accordion-item">
  <h2 class="accordion-header" id="heading-0-0">
   <button aria-controls="collapse-0-0" aria-expanded="true" class="accordion-button" data-bs-target="#collapse-0-0" data-bs-toggle="collapse" type="button">
    Accordion Summary 1
   </button>
  </h2>
  <div aria-labelledby="heading-0-0" class="accordion-collapse collapse show" data-bs-parent="#acc-bs0" id="collapse-0-0">
   <div class="accordion-body">
    <p>Text in the collapsible 1</p>
   </div>
  </div>
 </div>
 <div class="accordion-item">
  <h2 class="accordion-header" id="heading-0-1">
   <button aria-controls="collapse-0-1" aria-expanded="true" class="accordion-button" data-bs-target="#collapse-0-1" data-bs-toggle="collapse" type="button">
    Accordion Summary 2
   </button>
  </h2>
  <div aria-labelledby="heading-0-1" class="accordion-collapse collapse show" data-bs-parent="#acc-bs0" id="collapse-0-1">
   <div class="accordion-body">
    <p>Text in the collapsible 2</p>
   </div>
  </div>
 </div>
</div>
```

## Registry Settings

Some values in registry records are set:

`"plone.plugins"`

- accordion

`plone.valid_tags`

- summary
- details
- button

`plone.custom_attributes`

- open
- type
- data-bs-toggle
- data-bs-target
- aria-expanded
- aria-controls
- aria-labelledby
- data-bs-parent

Enable the accordion toolbar button in the `Menu` JSON Structure in the TinyMCE Controlpanel. Per default this addon enable the accordion option in the `insert` menu section.

***Menu***

```json
{
    "insert": {
        "title": "Insert",
        "items": "link media | template hr | accordion"
    },
}
```

Please check the TinyMCE controlpanel that the values are set correct.

## Optional configuration

If environment variable `ACCORDION_ALWAYS_OPEN` is set, accordion items stay open when another item is opened.
See [Bootstrap accordion documentation](https://getbootstrap.com/docs/5.3/components/accordion/#always-open).

## Install Addon via buildout

add `collective.outputfilters.tinymceaccordion` to your egg section in buildout.cfg

## Install Addon via pip

`pip install collective.outputfilters.tinymceaccordion`

## Install a Testenvironment

run `make build`

## Start the instance

run `make start`

## Format and Linting

run `make check`

## Testing

run `make test`

## Testing with coverage

run `make test-coverage`
