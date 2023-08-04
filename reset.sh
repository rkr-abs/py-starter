set -e
cd "$(dirname "$0")"

resetGitDir() {
	rm -rf ./.git
}

cleanUp(){
	rm reset.sh
}

initializeGitDir(){
	git init
}

executeSetupScript(){
	sh ./setup.sh
}

initializeCommit(){
	git add .
	git commit -m "Initialized."
}

# Main
resetGitDir
cleanUp
initializeGitDir
executeSetupScript
initializeCommit