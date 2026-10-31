#!/bin/bash

##############################################################################################
# Author: Atomicbeast101
# Description: Create Python virtual environment to install packages for development purposes.
##############################################################################################

# Setup virtual environment
python -m venv .venv

# Install packages
.venv/bin/python -m pip install -r requirements.txt
