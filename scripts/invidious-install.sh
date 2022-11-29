#!/bin/sh

cd $1
git clone https://github.com/iv-org/invidious.git
cd invidious
curl -fs https://raw.githubusercontent.com/ggemre/hab-install/main/data/invidious/docker-compose.yml -o docker-compose.yml
rm -rf screenshots README.md TRANSLATION .gitignore .gitattributes .editorconfig mocks CHANGELOG.md .github .gitmodules LICENSE
