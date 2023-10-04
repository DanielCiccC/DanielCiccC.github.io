import os
import re
import shutil

# Define the directory where your markdown files are located
directory = 'DECO3801/notes/'  # You can change this to your desired directory

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        # Read the content of the markdown file
        with open(directory + filename, 'r', encoding='UTF-8') as md_file:
            md_content = md_file.read()

        # Use a regular expression to find image references in markdown
        img_references = re.findall(r'\[(.*?)\]\((image-\d+\.png)\)', md_content)
        
        with open(directory + 'assets/img_num.txt', 'r') as img_num:
            number = int(img_num.read())

        for alt_text, img_filename in img_references:
            # Create the 'assets' subdirectory if it doesn't exist
            if not os.path.exists('assets'):
                os.mkdir('assets')

            # Rename the image file and update the markdown content
            new_img_path = os.path.join(directory, 'assets', f'IMG{number}.PNG')
            org_img_path = os.path.join(directory, img_filename)
            new_img_path_local = os.path.join('assets', f'IMG{number}.PNG')
            os.rename(org_img_path, new_img_path)
            md_content = md_content.replace(f'[{alt_text}]({img_filename})', f'[{alt_text}]({new_img_path_local})')
            number += 1
        # Write the updated markdown content back to the file
        with open(directory + filename, 'w', encoding='UTF-8') as md_file:
            md_file.write(md_content)
            
        with open(directory + 'assets/img_num.txt', 'w') as img_num:
            img_num.write(str(number))

        print(f"Processed {filename}")

print("Done.")