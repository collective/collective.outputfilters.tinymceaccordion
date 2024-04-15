"""Installer for the collective.outputfilters.tinymceaccordion package."""

from setuptools import find_packages
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
    version="1.0a1",
    description="An add-on for Plone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
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
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.outputfilters"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "z3c.jbot",
        "Products.CMFPlone",
        "Products.GenericSetup",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.publisher",
    ],
    extras_require={
        "test": [
            "Products.CMFPlone",
            "plone.api",
            "plone.app.dexterity",
            "plone.app.robotframework[debug]",
            "plone.app.testing",
            "plone.base",
            "plone.browserlayer",
            "plone.restapi",
            "plone.testing>=5.0.0",
            "robotsuite",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = collective.outputfilters.tinymceaccordion.locales.update:update_locale
    """,
)
