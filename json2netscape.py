from airium import Airium
from argparse import ArgumentParser
from loguru import logger
import json
import time

class Json2Netscape:
    def __init__(self, args):
        self.fnames = args.fnames
        self.outfile = args.outfile
        self.final_data = {}
        self.final_html = Airium()

    def run(self):
        # gather links in final_data
        for fname in self.fnames:
            logger.info('processing file: %s' % fname)
            try:
                with open(fname, encoding='utf8') as f:
                    self.process_json(f)
            except Exception as e:
                logger.critical('error opening file: %s' % e)

        # generate and write in netscape html format
        with open(self.outfile, 'w', encoding='utf8') as f:
            f.write(self.generate_html())

    def generate_html(self):
        a = self.final_html
        a('<!DOCTYPE NETSCAPE-Bookmark-file-1>')
        a('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">')
        a('<TITLE>Bookmarks</TITLE>')

        for ent in self.final_data.items():
            a('<DT>') # <DT> does not have a closing pair
            with a.A(HREF=ent[0], TAGS='', ADD_DATE=int(time.time())):
                if ent[1] == '':
                    # if the description is empty, use the link itself
                    a(ent[0])
                else:
                    a(ent[1])

        return str(a)

    def process_json(self, fstream):
        """process the json input file

        The json file is expected in the following format:

            {
                "link": "description",
                ...
            }
        """
        data = json.load(fstream)
        logger.info('file has %d entries' % len(data))
        # this feature is available on python 3.9+
        self.final_data = self.final_data | data


if __name__ == '__main__':
    parser = ArgumentParser(description='Convert from json to netscape bookmark format.')
    parser.add_argument(dest='fnames', metavar='fname', nargs='+')
    parser.add_argument('-o', dest='outfile', required=True)
    args = parser.parse_args()

    Json2Netscape(args).run()