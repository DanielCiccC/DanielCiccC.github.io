import os
import re
import shutil
import sys


def process_markdown_files(directory):
    # Iterate through files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            # Read the content of the markdown file
            with open(os.path.join(directory, filename), 'r', encoding='UTF-8') as md_file:
                md_content = md_file.read()

            # Use a regular expression to find image references in markdown
            img_references = re.findall(r'\((image-\d+\.png)\)', md_content)

            number = 0
            try:
                with open(os.path.join(directory, 'assets', 'img_num.txt'), 'r') as img_num:
                    number = int(img_num.read())
            except Exception:
                print("img_num.txt file not found")
                exit()

            for alt_text, img_filename in img_references:
                # Create the 'assets' subdirectory if it doesn't exist
                if not os.path.exists(os.path.join(directory, 'assets')):
                    os.mkdir(os.path.join(directory, 'assets'))

                # Rename the image file and update the markdown content
                new_img_path = os.path.join(directory, 'assets', f'IMG{number}.PNG')
                org_img_path = os.path.join(directory, img_filename)
                new_img_path_local = os.path.join('assets', f'IMG{number}.PNG')
                
                os.rename(org_img_path, new_img_path)
                md_content = md_content.replace(f'[{alt_text}]({img_filename})', f'[{alt_text}]({new_img_path_local})')
                number += 1
            # Write the updated markdown content back to the file
            with open(os.path.join(directory, filename), 'w', encoding='UTF-8') as md_file:
                md_file.write(md_content)

            with open(os.path.join(directory, 'assets', 'img_num.txt'), 'w') as img_num:
                img_num.write(str(number))

            print(f"Processed {filename} in {directory}")

    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory>")
        sys.exit(1)
    directory = sys.argv[1]
    process_markdown_files(directory)