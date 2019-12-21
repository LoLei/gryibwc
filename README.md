# gryibwc
**G**oodreads **Y**ear **I**n **B**ooks **W**ord **C**ount  
Get a word count for all books read in a year. :book:

Word count might be more accurate than pages, 
since the page count depends on formatting and whatnot.
However, the word counts are estimated based on the length 
of the audio book version, which is still comparable across books.
In any case, it makes for an interesting comparison of years.

## Installation
`pip install gryibwc`

## Usage
```
$ gryibwc -h
usage: gryibwc [-h] [--version] [--fast] userid year

positional arguments:
  userid      goodreads user id
  year        desired year

optional arguments:
  -h, --help  show this help message and exit
  --version   show program's version number and exit
  --fast      skip wait time - risk getting banned
```
Output e.g.:
```
Overall word count for year 2019: 4731925
```

The ID of the Goodreads user can be found in the profile URL.  
E.g.: `https://www.goodreads.com/user/show/26026244-lorenz`  
=> ID: `26026244`

Also you need to specify an API key in the `PUBLIC_KEY` environment
variable. Get your key [here](https://www.goodreads.com/api/keys).

## Dependencies
* Beautiful Soup
* https://github.com/LoLei/goodreads-api-client-python
  * Be sure to use my fork since the main API request is
    not implemented in the original source
