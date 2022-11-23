#!/bin/python3

import os
import progressbar
from argparse import ArgumentParser

parser = ArgumentParser(
  prog = "stop",
  description = "stop all docker containers",
  epilog = "2022 - ggemre"
)

parser.add_argument("-s", "--shutdown", action="store_true", help="shutdown server in addition to docker")
args = parser.parse_args()

app_data_dir = "/home/" + os.getlogin() + "/data/"
apps = os.listdir(app_data_dir)

widgets = ["stopping server: ", progressbar.Bar("="), " (", progressbar.ETA(), ")"]
bar = progressbar.ProgressBar(max_value=100, widgets=widgets).start()
progress = 0

for app in apps:
  os.system("cd " + app_data_dir + app + "; sudo docker-compose --log-level CRITICAL down >/dev/null 2>&1")
  progress += (100 / len(apps))
  bar.update(progress)

bar.finish()

if args.shutdown:
  os.system("sudo shutdown")

print("\nhab is now down")

