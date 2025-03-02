import sys
import os
import re

def replace_undefined(filename):
    with open('C:/git/DanielCiccC.github.io/' + filename, 'r', encoding='utf-8') as file:
        print('C:/git/DanielCiccC.github.io/' + filename)
        content = file.read()

    # Replace the first two instances of 'undefined' with the filename
    new_content = content.replace('undefined', filename.split('/')[-1].split('.')[0], 2)

    with open('C:/git/DanielCiccC.github.io/' + filename, 'w', encoding='utf-8') as file:
        file.write(new_content)

def remove_stylesheet_link(filename):
    filepath = f'C:/git/DanielCiccC.github.io/{filename}'
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the pattern to match the specific link tag
    pattern = r'<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/goessner/mdmath/themes/publication/style.css">'
    
    # Remove the link tag if it exists
    new_content = re.sub(pattern, '', content)

    # Write the modified content back to the file
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(new_content)

    print(f"Removed stylesheet link from {filename} if it existed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <html_filename>")
        sys.exit(1)

    html_filenames = sys.argv[1:]
    for filename in html_filenames:
        if filename.split('.')[1] == 'html':
            replace_undefined(filename)
            print(f"Replaced 'undefined' in {filename} with its name.")
            remove_stylesheet_link(filename)
