#!/usr/bin/env python
# coding: utf-8




import logging
import json
import csv

logging.basicConfig(filename = 'malformed.log', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
TestCsv = open('Test1_CSV.csv', 'w')
TestJson = open('test_2')

for i, line in enumerate(TestJson):
  try:
    data = json.loads(line)
  except json.decoder.JSONDecodeError:
    logging.info('Malformation on Line', i+1, repr(line))
TestJson.close()

csv_writer = csv.writer(TestCsv)
for items in data:
  csv_writer.writerow(items)