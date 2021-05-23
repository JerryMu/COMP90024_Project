#!/bin/bash
app="dataanalysis"

docker build -t ${app} .
docker run -p 5984:5984 ${app}
