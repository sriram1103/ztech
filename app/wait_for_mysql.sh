#!/bin/bash

echo "Waiting for mysql start up"

while true
do
    echo > /dev/tcp/db/3306 2>/dev/null
    [[ $? -eq 0 ]] && break
    sleep 30
done

echo "Starting app"
python app.py 
