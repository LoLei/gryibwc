"""gryibwc - setup.py"""
import setuptools

LONG_DESC = open('README.md').read()

setuptools.setup(
    name="gryibwc",
    version="0.9.4",
    author="Lorenz Leitner",
    author_email="lrnz.ltnr@gmail.com",
    description="Get a word count for books read in a year",
    long_description_content_type="text/markdown",
    long_description=LONG_DESC,
    url="https://github.com/lolei/gryibwc",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["gryibwc"],
    entry_points={"console_scripts": ["gryibwc=gryibwc.gryibwc:main"]},
    python_requires=">=3"
    )
