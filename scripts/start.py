#!/bin/python3

import os
import progressbar

app_data_dir = "/home/" + os.getlogin() + "/data/"
apps = os.listdir(app_data_dir)

widgets = ["starting server: ", progressbar.Bar("="), " (", progressbar.ETA(), ")"]
bar = progressbar.ProgressBar(max_value=100, widgets=widgets).start()
progress = 0

for app in apps:
  os.system("cd " + app_data_dir + app + "; sudo docker-compose --log-level CRITICAL up -d >/dev/null 2>&1")
  progress += (100 / len(apps))
  bar.update(progress)

bar.finish()
print("\nhab is now up and running")
