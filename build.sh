#!/bin/bash

# Redirect debug output and errors to errorlog.txt
exec > errorlog.txt 2>&1

# Set the root directory of your course subjects
root_directory="C:/git/DanielCiccC.github.io"

# Loop through all the course subjects
for course in "$root_directory"/*; do
    # Check if the 'notes' and 'docs' directories exist for the current course
    if [ -d "$course/notes/assets" ] && [ -d "$course/docs/assets" ]; then
        # Copy images from 'notes/assets' to 'docs/assets'
        cp "$course/notes/assets"/*.{jpg,jpeg,PNG,png,gif} "$course/docs/assets/"
    else
        echo "Skipping $course: 'notes' or 'docs' directory not found."
    fi
done

# echo "All HTML documents have been copied from $sourceDirectory to $destinationDirectory."
git add .
git commit -m 'Modified documents'
git push