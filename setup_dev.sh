#!/usr/bin/env bash
# This script should be sourced
# by @mb6ockatf, Sat 29 Apr 2023 09:53:32 PM MSK

echo "setup venv"
python3 -m venv venv
echo "activate venv"
. venv/bin/activate
echo "install required packages to venv"
python3 -m pip install -r requirements.txt