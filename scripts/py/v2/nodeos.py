#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import requests

URLS = {
    'get_info': 'http://{host}/v1/chain/get_info'
}


parser = argparse.ArgumentParser()
parser.add_argument("url", type=str,
                    help="The URL for the node you want to check")
args = parser.parse_args()


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        exit_code, message = args.url
    except requests.exceptions.RequestException:
        exit_code, message = (2, 'Error cannot connect to host ')
    except Exception as e:
        exit_code, message = (2, e.args[0])

    print(message)
    sys.exit(exit_code)
