import json
import os
import fileinput
import requests
import re
import json
import sys

#sep = re.compile('[-,]')

output = { "type": "FeatureCollection",
        "features": []
        }

def createFeature(coords, addr, name):
    return { "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    coords[0],
                    coords[1]
                    ]
                },
            "properties": {
                "marker-symbol": "restaurant",
                "name": name,
                "address": addr
                }
            }

APIKEY=os.environ["APIKEY"]

for line in fileinput.input():
    #print(line)
    line=line.strip()
    if '|' in line:
        addr=line[:line.find('|')]
    else:
        try:
            addr=line[:line.rfind('|')]
        except:
            addr=line

    while True:
        params = {
                'lang': 'en',
                'in': 'countryCode:DEU',
                'limit': 2,
                'q': addr,
                'apiKey': APIKEY,
                'qq': 'city=Berlin'
                }
        r = requests.get('https://geocode.search.hereapi.com/v1/geocode',
                params=params)

        js = r.json()

        if len(js["items"]) == 0:
            if '-' in addr:
                addr = addr[:addr.rfind('-')]
            else:
                print("can't handle", addr, file=sys.stderr)
                break
        else:
            break;
    
    if len(js["items"]):
        obj=js["items"][0]

        output["features"].append(
                createFeature(name=addr,
                    addr=obj["address"]["label"],
                    coords=list(reversed(obj["position"].values()))))

print(json.dumps(output, indent=2, sort_keys=True))
