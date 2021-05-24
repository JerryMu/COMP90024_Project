#!/bin/bash
app="dataanalysis"

docker build -t ${app} .
docker run -d ${app}
