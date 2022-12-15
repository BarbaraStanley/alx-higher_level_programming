#!/bin/bash
# Takes in a URL, sends a request to a URL and displayes the size of the request body
curl -s "${1}" | wc -c
