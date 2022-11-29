#!/bin/sh

sudo apt update
sudo apt upgrade
./stop.py
sudo docker rmi -f $(docker images -aq)
./start.py
