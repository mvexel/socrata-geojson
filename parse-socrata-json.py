#!/usr/bin/env python

from __future__ import print_function
from json import loads
from requests import get
from geojson import FeatureCollection, Feature, Point
import sys

no_location = 0
good = 0
result = []

if len(sys.argv) != 3:
    print('usage: parse-socrata-json.py URL OUTFILE')
    sys.exit(1)

socrates_uri = sys.argv[1]
outfile = sys.argv[2]

r = get(socrates_uri)

if r.status_code != 200:
    print('not a valid URL')
    sys.exit(1)

rows = loads(r.text)

for row in rows:
    if not 'location' in row:
        # item does not have location, move on.
        no_location += 1
        continue
    l = row.pop('location')
    p = Point((float(l['longitude']), float(l['latitude'])))
    result.append(Feature(geometry=p, properties=row))
    good += 1
with open(outfile, 'w') as f:
    print(FeatureCollection(result), file=f)

print('done.\n{good} rows written to {out}.\
\n{no_location} rows without location skipped'.format(
    good=good,
    out=outfile,
    no_location=no_location))
