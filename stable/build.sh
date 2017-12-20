#!/bin/bash

RELEASE=f${RELEASE:-"$(lsb_release -r | cut -f2)"}

url="https://discordapp.com/api/download?platform=linux&format=tar.gz"
discord_dir="Discord"

# get the latest tgz
url2=$(curl -s "$url" | grep "a href=" | cut -d= -f2 | cut -d'"' -f2)
file=${url2##*/}
[ -s "$file" ] || curl -s -O "$url2"

# add the spec and desktop files
tar xf "$file"
cp ./*.spec ./*.desktop "$discord_dir"

# re-tar and cleanup
tar czf "$file" "$discord_dir"
rm -rf "$discord_dir"

# build
fedpkg --release $RELEASE --module-name discord mockbuild
mv $(find . -type f -name '*x86_64.rpm') ../build
rm -rf ./*.tar.gz ./*.rpm ./results_*
