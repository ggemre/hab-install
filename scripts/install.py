#!/bin/python3

import os
from argparse import ArgumentParser
from bullet import Check

app_choices = ["Flame", "Invidious", "Jellyfin", "Jellyseerr", "Nextcloud", "Prowlarr", "Radarr", "Sabnzbd", "Sonarr", "Uptime Kuma"]

app_prompt = Check(check="*", prompt="Select applications to install: ", choices=app_choices, margin=1)
apps = app_prompt.launch()

app_data_dir = "/home/" + os.getlogin() + "/data/"

for app in apps:
  app_name = app.lower().replace(" ", "-")
  os.system("curl https://raw.githubusercontent.com/ggemre/hab-install/main/data/" + app_name + "/docker-compose.yml -o " + app_data_dir + app_name + "/docker-compose.yml")
