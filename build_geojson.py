import sys
import fileinput
import json
import os
import requests

output = {
        "type": "FeatureCollection",
        "features": []
        }

def create_feature(coords, addr, comment):
    return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    coords[0],
                    coords[1]
                    ]
                },
            "properties": {
                "marker-symbol": "restaurant",
                "highlight": comment,
                "address": addr
                }
            }

APIKEY=os.environ["APIKEY"]

for line in fileinput.input(openhook=fileinput.hook_encoded("utf-8")):
    line=line.strip()

    if '|' in line:
        addr=line[:line.index('|')]
    else:
        try:
            addr=line[:line.rindex('-')]
        except:
            addr=line

    while True:
        params = {
                'lang': 'en',
                'in': 'countryCode:DEU',
                'limit': 1,
                'q': addr,
                'apiKey': APIKEY,
                'qq': 'city=Berlin'
                }

        r = requests.get('https://geocode.search.hereapi.com/v1/geocode',
                params=params)

        js = r.json()

        if len(js["items"]) == 0:
            if '-' in addr:
                addr = addr[:addr.rindex('-')]
            else:
                print("can't handle", addr, file=sys.stderr)
                break
        else:
            break

    if len(js["items"]):
        obj=js["items"][0]
        comment=line[len(addr):].strip(' ,|-')

        output["features"].append(
                create_feature(comment=comment,
                    addr=obj["address"]["label"],
                    coords=list(reversed(obj["position"].values()))))

print(json.dumps(output, indent=2, ensure_ascii=False))
