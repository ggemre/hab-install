# hab-install

Installation and management scripts for multiple docker containers.

### Overview of services

| Service | Port | Description |
| --- | --- | --- |
| Flame | 5005 | Dashboard for apps and bookmarks |
| Jellyfin | 8096 | Media server |
| Jellyseerr | 5055 | Request and recommendation client for Jellyfin |
| Invidious | 3000 | Video streaming platform |
| Nextcloud | 8080 | Cloud based file storage |
| Prowlarr | 9696 | Index manager for PVRs |
| Radarr | 7878 | PVR for movies |
| Sabnzbd | 9091 | Download client for newsgroups |
| Sonarr | 8989 | PVR for TV shows |
| Uptime Kuma | 3001 | Status monitor for services |

### Scripts

Found in the `scripts` directory are several files written to make server maintenance and administration easier. Every script comes with a help option that explains the purpose, usage, and available flags. For help simply use the `-h` or `--help` flag.

`./install.py`

Installs all services that the user selected from a list.

`./start.py`

Starts each docker container.

`./stop.py`

Stops each docker container. Optional flags:

`./stop.py -s` or `./stop.py --shutdown` also shuts down the server after stopping the containers.

`./update-environment.py`

Updates the .env files for the docker containers. Optional flags:

`./update-environment.py -f FILE` or `./update-environment.py --file FILE` uses the provided FILE to set the environment files.

`./update-environment.py -u USER` or `./update-environment.py --username USER` sets the username to USER.

`./update-environment.py -p PASS` or `./update-environment.py --password PASS` sets the password to PASS.

If no options are passed, update-environment will prompt the user for each input to use as environment variables.
