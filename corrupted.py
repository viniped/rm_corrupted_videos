import subprocess
from pathlib import Path
import os
from colorama import Fore
import pyfiglet
import random

class Banner:
    def __init__(self, banner):
        self.banner = banner
        self.lg = Fore.LIGHTGREEN_EX
        self.w = Fore.WHITE
        self.cy = Fore.CYAN
        self.ye = Fore.YELLOW
        self.r = Fore.RED
        self.n = Fore.RESET

    def print_banner(self):
        colors = [self.lg, self.r, self.w, self.cy, self.ye]
        f = pyfiglet.Figlet(font='slant')
        banner = f.renderText(self.banner)
        print(f'{random.choice(colors)}{banner}{self.n}')
        print(f'{self.r}  Version: v0.0.1 https://github.com/viniped \n{self.n}')

def show_banner():
    banner = Banner('R M Corrupted Videos')
    banner.print_banner()

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

# Display the banner
show_banner()

# Ask the user to input the folder path
folder_path = input("Please enter the folder path: ")

# Validate the folder path
if not os.path.isdir(folder_path):
    print("Invalid folder path.")
else:
    # Call the function to delete videos without duration
    delete_videos_without_duration(folder_path)    
    print("Deletion completed.")
