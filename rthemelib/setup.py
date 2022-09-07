"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

# The version of this tool is based on the following steps:
# https://packaging.python.org/guides/single-sourcing-package-version/
VERSION = {}

setup(
    name="rthemelib",
    author="PizzaLovingNerd",
    url="https://github.com/risiOS/rtheme",
    description="Library for Python Programs to interact with rtheme.",
    version="0.1",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=[
        "setuptools>=45.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: System",
        "Programming Language :: Python :: 3.10"
    ],
)
