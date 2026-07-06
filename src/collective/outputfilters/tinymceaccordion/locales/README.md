# update locales

run both commands

```
uvx i18ndude rebuild-pot --pot src/collective/outputfilters/tinymceaccordion/locales/collective.outputfilters.tinymceaccordion.pot --create collective.outputfilters.tinymceaccordion ./src/collective/outputfilters/tinymceaccordion
```

```
uvx i18ndude sync --pot ./src/collective/outputfilters/tinymceaccordion/locales/collective.outputfilters.tinymceaccordion.pot ./src/collective/outputfilters/tinymceaccordion/locales/*/LC_MESSAGES/collective.outputfilters.tinymceaccordion.po
```