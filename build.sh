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

for dir in */; do
    if [ -d "$dir/notes" ]; then
        echo "Processing $dir..."
        python image_renamer.py "$dir/notes/"
    fi
done

modified_files=$(git diff --name-only HEAD@{1} -- '*.html')
if [ -n "$modified_files" ]; then
    for file in $modified_files; do
        echo "Running renamer.py on $file"
        python main/build/renamer.py "$file"
    done
else
    echo "No modified .html files since the last commit."
fi


# echo "All HTML documents have been copied from $sourceDirectory to $destinationDirectory."
MESSAGE=$(git ls-files -domz | xargs -0 echo The following have been changed: )
git add .
git commit -m "$MESSAGE"
git push

echo "Build Complete"