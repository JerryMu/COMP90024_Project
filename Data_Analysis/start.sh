#!/bin/bash
app="dataanalysis"

docker build -t ${app} .
docker run -p 5000:5000 ${app}
