from pathlib import Path
import os
import shutil

parent_path = Path("C:/Users/ginge/OneDrive - University of South Wales/Desktop")
dir_list = os.listdir(parent_path)
script_name = "desktop_organiser.py"

documents = []
images = []
other = []

new_dirs = ['Documents', 'Images', 'Other']

documents_destination = os.path.join(parent_path, 'Documents')
images_destination = os.path.join(parent_path, 'Images')
other_destination = os.path.join(parent_path, 'Other')


for file in dir_list:
    split_tup = os.path.splitext(file)
    file_name = split_tup[0]
    extension = split_tup[1]


    if extension == '.png' or extension == '.jpg' or extension == '.gif':
        images.append(file)
    elif extension == '.pdf' or extension == '.docx' or extension == '.txt':
        documents.append(file)
    else:
        for char in extension:
            if char == ".":
                other.append(file)


# Check if folders exist if not create them on the Desktop
for new_dir in new_dirs:
    temp_path = os.path.join(parent_path, new_dir)
    if os.path.exists(temp_path):
        print(f"{temp_path} already exists...")
    else:
        os.mkdir(temp_path)


# Move document files
if not documents:
    print("No documents found to be organised.")
else:
    for file in documents:
        temp_source = os.path.join(parent_path, file)
        destination = shutil.move(temp_source, documents_destination)
    
# Move image files
if not images:
    print("No images found to be orgranised.")
else:
    for file in images:
        temp_source = os.path.join(parent_path, file)
        destination = shutil.move(temp_source, images_destination)

# Move  files
if not other:
    print("No other files found to be organised.")
else:
    for file in other:
        if file == script_name:
            print("No other files found to be organised.")
            continue
        temp_source = os.path.join(parent_path, file)
        destination = shutil.move(temp_source, other_destination)
    


def main():
    return None

if __name__ == "__main__":
    main()