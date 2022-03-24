#!/usr/bin/env bash

set -eo pipefail

echo "--- Contracts Test Workflow"
source ./env.sh

sym local-network start --nodes 4 -l 10

pip3 install --upgrade pip
pip3 install symbiont-io.pytest-assembly==2.0.4.dev9

DEFAULT_NETWORK_CONFIG="$HOME/.symbiont/assembly-dev/dev-network/default/network-config.json"
pytest hello_test.py --connection-file "$DEFAULT_NETWORK_CONFIG" --contract-path ../ -
