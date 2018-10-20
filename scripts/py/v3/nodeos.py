#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

import logger
import psutil

memory_total_bytes = float(psutil.virtual_memory().total)
memory_total_gb = memory_total_bytes / 1024 / 1024 / 1024


class Monitor:
    def __init__(self, url):
        self.url = str(url)

    def monitor(self):
        try:
            # TODO : Add function here to check and process
            pass
        except Exception as e:
            logger.error('error: {}'.format(e))


def usage():
    global url
    parser = argparse.ArgumentParser(description='Nodeos block time monitor')
    # parser.add_argument('-u', '--url', default=url, help='host url to check')
    args = parser.parse_args()
    url = args.url


def main():
    Monitor(url).monitor()


if __name__ == '__main__':
    usage()
    main()
