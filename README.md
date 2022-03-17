# json2netscape

Convert bookmarks in json to netscape bookmark format.

## Dependencies

    loguru (for pretty logs)
    airium (for html generation)

## Usage

    json2netscape.py [-h] -o OUTFILE fname [fname ...]

    Convert from json to netscape bookmark format.

    positional arguments:
    fname

    optional arguments:
    -h, --help  show this help message and exit
    -o OUTFILE

## Json format

The json file is expected in the following format:

    {
        "link": "name",
        ...
    }