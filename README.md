# Ultimate Cheap Eats Berlin

This started as a [map](https://github.com/diaasami/uceb/blob/main/locations_reddit.geojson) of Ultimate Cheap Eats Berlin, based on [this reddit thread](https://www.reddit.com/r/berlin/comments/oxois3/ultimate_cheap_eats_in_berlin_thread/?utm_source=share&utm_medium=web2x&context=3)

Later, it was expanded to include another [map](https://github.com/diaasami/uceb/blob/main/locations_under10.geojson) of "excellent and affordable meals with under 10 EUR", from this [FB thread](https://www.facebook.com/groups/FreeAdviceBerlin/?multi_permalinks=5366750133380703&comment_id=5370157079706675)
The list of locations is in [input_under10.txt](https://github.com/diaasami/uceb/blob/main/input_under10.txt)

## Technical details

Input files are named input_\*.txt and when modified, they get geocoded automatically into a locations_\*.geojson file via a [github action](https://github.com/diaasami/uceb/blob/main/.github/workflows/gen-geojson.yml), a [Makefile](https://github.com/diaasami/uceb/blob/main/.github/workflows/Makefile) and a [python script](https://github.com/diaasami/uceb/blob/main/build_geojson.py).

The Makefile processes files that are updated only, thereby avoiding unnecessary geocoding calls.
