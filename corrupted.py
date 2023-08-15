import subprocess
from pathlib import Path
import os
import shutil

# Function to check if a video file has duration attribute
def has_duration(file_path):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', str(file_path)], capture_output=True, text=True)
    duration = result.stdout.strip()
    return duration != ""

# Function to delete video files without duration attribute
def delete_videos_without_duration(folder_path):
    folder_path = Path(folder_path)
    for path in folder_path.rglob('*.mp4'):
        if path.is_file() and not has_duration(path):
            print(f"Deleting {path}")
            os.remove(str(path))

# Ask the user to input the folder path
folder_path = input("Please enter the folder path: ")

# Validate the folder path
if not os.path.isdir(folder_path):
    print("Invalid folder path.")
else:
    # Call the function to delete videos without duration
    delete_videos_without_duration(folder_path)
    print("Deletion completed.")
