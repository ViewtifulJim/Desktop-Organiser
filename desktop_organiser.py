import shutil
import os
from pathlib import Path
import ctypes

# Function to get Desktop path (Windows-specific)
def get_desktop_path():
    csidl = 0
    buf = ctypes.create_unicode_buffer(260)
    ctypes.windll.shell32.SHGetFolderPathW(0, csidl, 0, 0, buf)
    return Path(buf.value)

parent_path = get_desktop_path()
print(f"Desktop Path: {parent_path}")

dir_list = os.listdir(parent_path)
script_name = "desktop_organiser.py"

documents = []
images = []
other = []

# Define destination folders
new_dirs = ['DesktopCleanUp', 'Documents', 'Images', 'Other']
desktop_cleanup_destination = os.path.join(parent_path, 'DesktopCleanUp')
documents_destination = os.path.join(parent_path, 'Documents')
images_destination = os.path.join(parent_path, 'Images')
other_destination = os.path.join(parent_path, 'Other')

# Categorize files
for file in dir_list:
    file_path = os.path.join(parent_path, file)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    file_name, extension = os.path.splitext(file)

    if extension in ['.png', '.jpg', '.gif']:
        images.append(file)
    elif extension in ['.pdf', '.docx', '.txt']:
        documents.append(file)
    elif file != script_name:  # Avoid moving the script itself
        other.append(file)

# Create necessary folders if they don't exist
for new_dir in new_dirs:
    temp_path = os.path.join(parent_path, new_dir)
    os.makedirs(temp_path, exist_ok=True)

# Move document files
if documents:
    for file in documents:
        shutil.move(os.path.join(parent_path, file), documents_destination)
else:
    print("No documents found to be organized.")

# Move image files
if images:
    for file in images:
        shutil.move(os.path.join(parent_path, file), images_destination)
else:
    print("No images found to be organized.")

# Move other files
if other:
    for file in other:
        shutil.move(os.path.join(parent_path, file), other_destination)
else:
    print("No other files found to be organized.")

# Move subfolders (Documents, Images, Other) into DesktopCleanUp
for folder in [documents_destination, images_destination, other_destination]:
    target_path = os.path.join(desktop_cleanup_destination, os.path.basename(folder))
    
    if os.path.exists(target_path):
        print(f"Skipping move: '{target_path}' already exists.")
    else:
        shutil.move(folder, desktop_cleanup_destination)

# Remove empty folders left on Desktop
for folder in [documents_destination, images_destination, other_destination]:
    if os.path.exists(folder) and not os.listdir(folder):
        os.rmdir(folder)
        print(f"Removed empty folder: {folder}")

