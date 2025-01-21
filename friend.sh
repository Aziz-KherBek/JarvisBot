#!/bin/bash
if [ "$#" -gt 0 ]; then
	python3 friend.py "$*"
else
	echo "Welcome to the bot!Type exit to quit "
	while true;do
		read -p	">" user_input
		if [[ "${user_input,,}" == "exit" ]]; then
  			echo "Exiting the program..."
  			exit 0
		else
			python3 friend.py "$user_input"
		fi

	done
fi
	
