#!/bin/sh

for app in $(ls /home/dme/data); do
  cd /home/dme/data/$app
  sudo docker-compose down
done

sudo shutdown
