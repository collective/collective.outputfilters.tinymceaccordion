# Changelog

<!-- towncrier release notes start -->

## 2.0.0 (2025-12-18)


### Breaking changes:

- Switch to PEP 420 native namespace @1letter 


### Internal:

- update package with plone/meta @1letter 

## 1.1.0 (2025-07-15)


### New features:

- If environment variable `ACCORDION_ALWAYS_OPEN` is set, accordion items stay open when another item is opened.
  @mauritsvanrees #16

## 1.0.1 (2025-06-24)


### Bug fixes:

- Fix updating registry records when installing.
  Previously, our configuration changes could be gone after a restart.
  If your accordions don't work, you can deactivate and activate this add-on to fix it.
  @mauritsvanrees #15


### Tests:

- Do not require `plone.app.robotframework` for testing.
  We don't have robot tests.  This avoids running `rfbrowser init` on each test run.
  @mauritsvanrees 

## 1.0.0 (2025-06-23)


### Internal:

- Update README @1letter readme
- Update configuration files @plone 


### Tests:

- move tests to pytest @1letter pytest

## 1.0a7 (2024-04-29)


### Internal:

- Update README @1letter #7

## 1.0a6 (2024-04-28)


### Internal:

- Update README @1letter 

## 1.0a5 (2024-04-28)


### Internal:

- Update README @1letter 

## 1.0a4 (2024-04-28)


### Internal:

- remove unused files @1letter 

## 1.0a3 (2024-04-28)


### Internal:

- Update configuration files @plone 

## 1.0a3 (unreleased)


- Nothing changed yet.


## 1.0a2 (2024-04-19)

- Initial release. @1letter
