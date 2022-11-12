#!/bin/sh

for app in $(ls /home/dme/data); do
  cd /home/dme/data/$app
  sudo docker-compose up -d
done

