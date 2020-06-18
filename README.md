# python web scraper

this is a simple demonstration web scraper, that scrapes a single page and parses that page for some data

## project setup

this project uses pipenv and runs on python 3.7

to install pipenv or python on macos, please use [hombrew](https://brew.sh/) (installation instructions for hombrew available in the link). Not sure if you have them installed?

try running: `pipenv --version` and `python3 --version`. If you see `command not found:` printed, you need to install the program.

to install python:
`brew install python`

to instal pipenv:
`brew install pipenv`


once you've install pipenv, you install project dependencies by running:

`make bootstrap`

launch the pipenv shell with

`pipenv shell`

finally, run the script with:

`make start`

## Learning

Some of the functions in `scraper.py` are broken, and some aren't implemented. Try fixing the regex, and writing the missing functions!

### Resources to help understand what to do:

### Python Regular Expressions
Google tutorial on python regular expressions:
https://developers.google.com/edu/python/regular-expressions

#### Regex101:
online regex playground - lets you write regexes and test them on sample strings - also allows you to generate code based on the regexes you write. My goto for writing regexes. Maybe sure you select Python in the flavor section to the left.

https://regex101.com/


#### Request

Request lets you request webpages. You can find the full documentatio here: https://requests.readthedocs.io/en/master/

You won't need to use it much beyond the example given in the tutorial.

