#!/usr/bin/env python3

import json
import sys
import argparse
import requests
import datetime


class Nodeos(object):
    """
        A Python Script to check the block time on Nodeos.

        You can specify the URL for your nodeos instance.

    """

    # TODO : Lots of cleanup, add more methods, make compat with Icinga2 + Nagios
    # TODO : Consume args

    def __init__(self, url=None):
        self.url = url
        self.check()

    def check(self):
        # No URL
        if self.url is None:
            print("No URL Passed")
            url = 'http://mainnet.eosnairobi.io/v1/chain/get_info'
            try:
                r = requests.get(url)
                now = datetime.datetime.now()
                utc_time = datetime.datetime.utcnow()
                response = json.loads(r.text)
                raw_block_time = response.get('head_block_time')
                block_time = datetime.datetime.strptime(
                    raw_block_time, "%Y-%m-%dT%H:%M:%S.%f")
                diff = (utc_time - block_time).total_seconds()
                data = {"block_time": raw_block_time,
                        "current_local_time": now,  "difference": diff}
                print(data)
            except Exception as e:
                print(str(e))
        else:
            print("URL Passed")


if __name__ == '__main__':
    Nodeos()
