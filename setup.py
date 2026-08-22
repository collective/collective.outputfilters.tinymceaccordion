"""Installer for the collective.outputfilters.tinymceaccordion package."""

from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)

# See pyproject.toml for package metadata
setup()
