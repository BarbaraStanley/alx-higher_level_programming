#!/usr/bin/bash 
#  a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of a 200 status code response
curl -s -L "$1"
