#!/bin/bash
app="webserver"

docker build -t ${app} .
docker run -p 5000:5000 ${app}
