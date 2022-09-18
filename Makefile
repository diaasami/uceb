SHELL = /bin/sh

INPUT = $(wildcard input_*.txt)
OUTPUT = $(subst input,locations,$(subst txt,geojson,$(INPUT)))

all: $(OUTPUT)

.PHONY: all

locations_%.geojson: input_%.txt
	cat '$<' | python ./build_geojson.py > '$@'

clean:
	-rm -f *.geojson
