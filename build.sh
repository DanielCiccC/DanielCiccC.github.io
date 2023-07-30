#!/bin/bash

# Set the source and destination directories
sourceDirectory="BSAN4201/notes"
destinationDirectory="BSAN4201/docs"

# Create the destination directory if it doesn't exist
# mkdir -p "$destinationDirectory"

# # Copy all HTML files from the source to the destination directory
# cp "$sourceDirectory"/*.html "$destinationDirectory"

# echo "All HTML documents have been copied from $sourceDirectory to $destinationDirectory."
git add .
git commit -m 'Modified documents'
git push