# Adding and updating locales

For every language you want to translate into you need a
locales/[language]/LC_MESSAGES/collective.task.po
(e.g. locales/de/LC_MESSAGES/collective.task.po)

For German

```console
$ mkdir de
```

For updating locales

```console
./bin/update_locale
```

## Note

The script uses gettext package for internationalization.

Install it before running the script.

## On macOS

```console
brew install gettext
```

## On Windows

see https://mlocati.github.io/articles/gettext-iconv-windows.html
