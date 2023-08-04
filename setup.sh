#!/bin/bash
set -e
cd "$(dirname "$0")"

# Tasks
installPackages() {
	pip install -r requirements.txt
}

setupHooks(){
	hooksPath="./.githooks"
	git config core.hooksPath "$hooksPath"
	chmod 775 "$hooksPath"/*
}

# Main
installPackages
setupHooks
