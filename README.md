# pre

Python RegEx

    a primitive attempt at my own regex-directed engine library, in python

[regex-wiki](https://en.wikipedia.org/wiki/Regular_expression)
[regex-spec](https://www.math.clemson.edu/~warner/M865/RegexBasics.html)

Features:
    - [ ] pattern matching
    - [ ] search and replace (sed)
    - [ ] pattern compilation
    - [ ] pattern testing
    - [ ] pattern extraction
    - [ ] pattern validation
    - [ ] interactive mode (curses)

## usage

- command line script
    
    Run in cli: `./main.py [-pPso...]<expr> <str>`
        if no options are provided the script will simply return true/false and the
        matching pattern, should one exist.

- python virtual environment

    Run in a virtual python3 environment
        will act similar to cli script functionality

- imported python library

    import into any python script for full programmatic usage.

