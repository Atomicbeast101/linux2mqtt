#!/bin/bash

##############################################################################################
# Author: Atomicbeast101
# Description: Setup Python environment & run program.
##############################################################################################

echo "Setting up environment..."
./setup.sh

# Run from CMD or "docker run"/"kubectl run"
exec "$@"
