#!/bin/bash
#  sends a request to that URL, and displays the size of the body
curl -s -I $1 | grep Content-Length | cut -d " " -f 2
