#!/bin/python3

import os
import progressbar
from argparse import ArgumentParser
from bullet import Check


app_choices = ["Flame", "Invidious", "Jellyfin", "Jellyseerr", "Nextcloud", "Prowlarr", "Radarr", "Sabnzbd", "Sonarr", "Uptime Kuma"]

app_prompt = Check(check="*", prompt="Select applications to install: ", choices=app_choices, margin=1)
apps = app_prompt.launch()

app_data_dir = "/home/" + os.getlogin() + "/data/"

widgets = ["installing server: ", progressbar.Bar("="), " (", progressbar.ETA(), ")"]
bar = progressbar.ProgressBar(max_value=100, widgets=widgets).start()
progress = 0

for app in apps:
  app_name = app.lower().replace(" ", "-")
  
  if app_name == "invidious":
    os.system("./invidious-install.sh " + app_data_dir + "/DUMMYDIR/" + " >/dev/null 2>&1")
  else:
    os.system("curl -fsS --create-dirs https://raw.githubusercontent.com/ggemre/hab-install/main/data/" + app_name + "/docker-compose.yml -o " + app_data_dir + "/DUMMYDIR/" + app_name + "/docker-compose.yml")

  progress += 100 / len(apps)
  bar.update(progress)

  print("Server successfully installed.")
