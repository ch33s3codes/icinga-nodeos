#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys

import requests

import psutil

# Set some ground rules/constants
memory_total_bytes = float(psutil.virtual_memory().total)
memory_total_gb = memory_total_bytes / 1024 / 1024 / 1024
POST_FIXES = {
    'get_info': 'v1/chain/get_info'
}
default_url = 'http://127.0.0.1:8888/{}'.format(POST_FIXES.get('get_info'))


class Monitor:
    def __init__(self, url):
        self.url = str(url)

    def monitor(self):
        try:
            # TODO : Add function here to check and process
            response = requests.get(url, verify=False).json()

            print(response)
            sys.exit(0)
        except requests.exceptions.RequestException:
            exit_code, message = (2, 'Error cannot connect to host {}'.format(url))
            print(message)
            sys.exit(2)
        except Exception as e:
            print(str(e))
            sys.exit(2)


def usage():
    global url
    parser = argparse.ArgumentParser(description='Nodeos block time monitor')
    parser.add_argument(
        '-u', '--url', default=default_url, help='host url to check')
    args = parser.parse_args()
    url = args.url


def notify_telegram():
    # Send notification via Telegram bot
    pass


def main():
    Monitor(url).monitor()


if __name__ == '__main__':
    usage()
    main()
