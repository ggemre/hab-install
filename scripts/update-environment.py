#!/bin/python3

import os
import socket
from argparse import ArgumentParser
from bullet import Input, Password, YesNo

parser = ArgumentParser(
  prog = "update-environment",
  description = "set & modify environment files for all docker containers",
  epilog = "2022 - ggemre"
)

parser.add_argument("-f", "--file", nargs=1, required=False, help="template environment file to use")
parser.add_argument("-u", "--username", nargs=1, required=False, help="given username to set")
parser.add_argument("-p", "--password", nargs=1, required=False, help="given password to set")
args = parser.parse_args()

username = args.username
password = args.password

if args.file == None:
  if username == None:
    user_prompt = Input(prompt="Enter username: ")
    username = user_prompt.launch()
  else:
    username = args.username[0]

  if password == None:
    passwords_match = False
    while not passwords_match:
      pass_prompt0 = Password(prompt="Enter password: ")
      pass_prompt1 = Password(prompt="Re-enter password: ")
    
      pass0 = pass_prompt0.launch()
      pass1 = pass_prompt1.launch()
      if pass0 == pass1:
        passwords_match = True
        password = pass0
      else:
        print("Passwords do not match. Please try again.\n")
  else:
    password = args.password[0]

socket_test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_test.connect(("8.8.8.8", 80))
ip_addr = socket_test.getsockname()[0]
socket_test.close()

app_data_dir = "/home/" + os.getlogin() + "/data/"
apps = os.listdir(app_data_dir)

print("\nHAB_DIR : /home/" + os.getlogin() + "\nHAB_IP : " + ip_addr + "\nUSER : " + username + "\nPASS : " + password + "\n")
confirm_prompt = YesNo("Is the above information correct? ")
confirm = confirm_prompt.launch()

if confirm:
  for app in apps:
    env_file = open(app_data_dir + app + "/.env", "w")
    env_file.write("HAB_DIR=/home/" + os.getlogin() + "\nHAB_IP=" + ip_addr + "\nUSER=" + username + "\nPASS=" + password + "\n")
  env_file.close()
