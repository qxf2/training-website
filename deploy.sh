#!/bin/bash
git pull
ps aux |grep gunicorn |grep tsqa | awk '{ print $2 }' |xargs kill -HUP
