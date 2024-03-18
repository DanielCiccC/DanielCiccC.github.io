import os
import re

def replace_in_file(file_path, pattern, replacement):
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        content = file.read()
    content = re.sub(pattern, replacement, content)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    directory = '.'  # Current directory
    pattern = r'%5C'
    replacement = '/'
    
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.html'):
                file_path = os.path.join(root, file_name)
                replace_in_file(file_path, pattern, replacement)

if __name__ == "__main__":
    main()
