"""Installer for the collective.outputfilters.tinymceaccordion package."""

from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CONTRIBUTORS.md").read(),
        open("CHANGES.md").read(),
    ]
)

setup(
    name="collective.outputfilters.tinymceaccordion",
    version="2.0.0.dev0",
    description="Addon for Plone 6 - Plone Outputfilter to transform TinyMCE Markup to Bootstrap5 Accordion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone CMS",
    author="1letter",
    author_email="1letter@gmx.de",
    url="https://github.com/collective/collective.outputfilters.tinymceaccordion",
    project_urls={
        "PyPI": "https://pypi.org/project/collective.outputfilters.tinymceaccordion/",
        "Source": "https://github.com/collective/collective.outputfilters.tinymceaccordion",
        "Tracker": "https://github.com/collective/collective.outputfilters.tinymceaccordion/issues",
        # 'Documentation': 'https://collective.outputfilters.tinymceaccordion.readthedocs.io/en/latest/',
    },
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "setuptools",
        "Products.CMFPlone",
        "Products.GenericSetup",
        "beautifulsoup4",
        "plone.base",
        "plone.outputfilters",
        "plone.registry",
        "zope.component",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
    ],
    extras_require={
        "test": [
            "zest.releaser[recommended]",
            "zestreleaser.towncrier",
            "zest.pocompile",
            "plone.app.testing",
            "pytest",
            "pytest-cov",
            "pytest-plone>=0.5.0",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.outputfilters.tinymceaccordion.locales.update:update_locale
    """,
)
