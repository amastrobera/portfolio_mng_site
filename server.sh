#! /bin/bash
if [ $# -gt 0 ]
then
	cmd=$1
	case $cmd in
		-s|--start)
		echo "starting server ... "
		python -m SimpleHTTPServer &
		shift
		;;
		-e|--end)
		echo "closing server ..."
		pkill "^python$" #super risky!
		shift
		;;
	esac
fi
