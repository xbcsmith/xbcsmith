#!/usr/bin/env bash

git pull
git checkout master
git fetch
git branch -m master main
git push -u origin main
