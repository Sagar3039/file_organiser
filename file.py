import os
import shutil
import keyboard
from datetime import datetime
import re

# Define the source and target folders
downloads_folder = r"C:\Users\Sagar\Downloads"
images_folder = r"C:\Users\Sagar\Pictures\Images"
videos_folder = r"C:\Users\Sagar\Videos"
documents_folder = r"C:\Users\Sagar\Documents"
other_files_folder = r"C:\Users\Sagar\Otherfiles"  # Updated location for other files
logs_folder = r"C:\Users\Sagar\Documents\FileOrganizerLogs"

# Ensure target folders exist
os.makedirs(images_folder, exist_ok=True)
os.makedirs(videos_folder, exist_ok=True)
os.makedirs(documents_folder, exist_ok=True)
os.makedirs(other_files_folder, exist_ok=True)
os.makedirs(logs_folder, exist_ok=True)

# File extensions for categorization
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv']
document_extensions = ['.pdf', '.docx', '.txt', '.xlsx', '.pptx']
executable_extensions = ['.exe', '.bat', '.msi', '.dll']

def organize_files():
    files_moved = 0
    log_message = f"File Organizer Log - {datetime.now()}\n"

    # Loop through files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            destination_folder = None
            is_web_series = False

            # Check for Web Series naming convention (e.g., "ShowName - Episode01.mp4")
            web_series_pattern = r"(.*?)(\s*-\s*Episode\d+)"
            match = re.search(web_series_pattern, filename)
            if match:
                is_web_series = True
                series_name = match.group(1).strip()
                episode_name = match.group(2).strip()
                destination_folder = os.path.join(videos_folder, series_name)

            # Categorize the file based on extension
            if file_ext in image_extensions and not is_web_series:
                destination_folder = images_folder
            elif file_ext in video_extensions and not is_web_series:
                destination_folder = videos_folder
            elif file_ext in document_extensions and not is_web_series:
                destination_folder = documents_folder
            elif file_ext in executable_extensions:
                destination_folder = other_files_folder  # .exe, .bat, etc., go to "Otherfiles"
            else:
                destination_folder = other_files_folder  # Any other file goes to "Otherfiles"

            # Ensure the destination folder exists
            if destination_folder:
                os.makedirs(destination_folder, exist_ok=True)

                # Check if a file with the same name exists
                destination_path = os.path.join(destination_folder, filename)
                if os.path.exists(destination_path):
                    # Create a subfolder if a file with the same name exists
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    subfolder = os.path.join(destination_folder, f"{filename}_{timestamp}")
                    os.makedirs(subfolder, exist_ok=True)
                    destination_path = os.path.join(subfolder, filename)

                shutil.move(file_path, destination_path)
                files_moved += 1
                log_message += f"Moved: {filename} -> {destination_path}\n"
            
            # If it's a web series file
            if is_web_series:
                os.makedirs(destination_folder, exist_ok=True)
                destination_path = os.path.join(destination_folder, episode_name)
                
                # Ensure there is no conflict and move the file
                if os.path.exists(destination_path):
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    destination_path = os.path.join(destination_folder, f"{episode_name}_{timestamp}")
                shutil.move(file_path, destination_path)
                files_moved += 1
                log_message += f"Moved: {filename} -> {destination_path}\n"

    # Log the results
    log_message += f"Total files moved: {files_moved}\n{'-'*40}"
    log_file = os.path.join(logs_folder, f"organizer_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")
    with open(log_file, 'w') as log:
        log.write(log_message)

    # Display log in the console
    print(f"Files organized! {files_moved} files were moved.")
    print(f"Log saved at {log_file}")

# Hotkey binding for organizing files
keyboard.add_hotkey("alt+f", organize_files)

print("File Organizer Tool running... Press ESC to quit.")
keyboard.wait("esc")
