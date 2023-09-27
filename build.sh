#!/bin/bash

# Redirect debug output and errors to errorlog.txt
exec > errorlog.txt 2>&1

# Set the root directory of your course subjects
root_directory="C:/git/DanielCiccC.github.io"

python image_renamer.py

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

# rename the html docs
# python main/build/renamer.py COMP3506/docs/textbook_wk2.html


# echo "All HTML documents have been copied from $sourceDirectory to $destinationDirectory."
MESSAGE=$(git ls-files -domz | xargs -0 echo The following have been changed: )
git add .
git commit -m "$MESSAGE"
git push

echo "Build Complete"