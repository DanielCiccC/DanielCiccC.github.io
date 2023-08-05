import sys
import os

def replace_undefined(filename):

    with open('C:/git/DanielCiccC.github.io/' + filename, 'r', encoding='utf-8') as file:
        print('C:/git/DanielCiccC.github.io/' + filename)
        content = file.read()

    # Replace the first two instances of 'undefined' with the filename
    new_content = content.replace('undefined', filename.split('/')[-1].split('.')[0], 2)

    with open('C:/git/DanielCiccC.github.io/' + filename, 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <html_filename>")
        sys.exit(1)

    html_filenames = sys.argv[1:]
    for filename in html_filenames:
        if filename.split('.')[1] == 'html':
            replace_undefined(filename)
            print(f"Replaced 'undefined' in {filename} with its name.")