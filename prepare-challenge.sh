#!/bin/bash
EXPORT_DIR=challenge
DOCKER_IMG=numfui-${VERSION}-docker.tar

set -e

rm -rf $EXPORT_DIR
mkdir -p $EXPORT_DIR
echo building image...
docker build . -t numfui:$VERSION
echo saving image...
docker image save numfui:$VERSION > $EXPORT_DIR/${DOCKER_IMG}
echo compressing image...
gzip $EXPORT_DIR/${DOCKER_IMG}
echo copying markdown files...
cp writeup.md $EXPORT_DIR
cp about-challenge.md $EXPORT_DIR
