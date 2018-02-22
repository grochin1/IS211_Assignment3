# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 3. Regular expressions."""

import csv
import argparse
import urllib2
import re
import datetime

def getLog(url):
    '''Downloads information from url'''
    response = urllib2.urlopen(url)
    return csv.DictReader(response, ['path', 'dt', 'browser', 'status', 'size'])

if __name__ == '__main__':
    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='log file url')
    args = parser.parse_args()
    # log = getLog('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')
    log = getLog(args.url)

    # initializations
    imgRegex = re.compile('.*?\.jpg$|.*?\.png$|.*?\.gif$')
    browsers = {'Chrome':0, 'Safari':0, 'Firefox':0, 'IE':0}
    hours = {str(i).zfill(2):0 for i in range(24)}
    count, hits = 0, 0

    for data in log:
        # part III
        count += 1
        if imgRegex.match(data['path']):
            hits += 1
        # part IV
        browser = data['browser']
        if 'Chrome' in browser: browsers['Chrome'] += 1
        elif 'Safari' in browser: browsers['Safari'] += 1
        elif 'Firefox' in browser: browsers['Firefox'] += 1
        else: browsers['IE'] += 1
        # part VI
        hour = str(datetime.datetime.strptime(data['dt'], '%Y-%m-%d %H:%M:%S').hour)
        hours[hour.zfill(2)] += 1

    print 'image requests account for {:.2f}% of all requests\n'.format(hits*100.0/count)
    print 'browsers: {}\n'.format(str(browsers))
    for k in sorted(hours.iterkeys()):
        print 'Hour {} has {} hits'.format(k, hours[k])