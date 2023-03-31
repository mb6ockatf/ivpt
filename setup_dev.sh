#!/usr/bin/env bash
#
# This script is supposed to be sourced
#
# by @mb6ockatf, Mon 27 Mar 2023 03:23:45 PM MSK

echo "setup venv"
python3 -m venv venv
echo "activate venv"
. venv/bin/activate
echo "install required packages to venv"
python3 -m pip install -r requirements.txt

