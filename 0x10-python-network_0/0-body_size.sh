#!/bin/bash
#This script take a URL and display the size of the body
curl -s "$1" | wc -c
