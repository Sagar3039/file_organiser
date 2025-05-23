File Organizer Tool 🗂️
This is a Python script designed to automatically organize files in your Downloads folder based on their extensions and file types. The tool is triggered via a hotkey (Alt + F) and moves files to categorized folders (Images, Videos, Documents, and Other Files). It even handles duplicate files by creating subfolders and appends a timestamp to avoid conflicts.

Additionally, the script supports organizing Web Series episodes by detecting naming conventions such as ShowName - Episode01.mp4, and it sorts them into specific folders.

Key Features
Auto-file Organization: Categorizes files based on extensions (images, videos, documents, executables, etc.).

Web Series Handling: Automatically organizes web series episodes in their respective folders.

Duplicate File Handling: If a file with the same name exists, it creates a subfolder and renames the file with a timestamp.

Logs: Keeps a log of all the organized files and saves them in the Documents folder.

Hotkey Support: Trigger file organization with the hotkey Alt + F.

Start on Boot: Can be set to run automatically when Windows starts.

Setup Instructions
Install Dependencies:

Install required Python libraries using pip:

bash
Copy
Edit
pip install keyboard shutil os
Running the Script:

Download the script and run it using Python.

The script will continuously run in the background, waiting for the hotkey trigger.

Make It Run at Startup:

Follow the instructions to add the script to the Startup folder or create a Scheduled Task to run it automatically when Windows starts.

Example Usage
Press Alt + F to organize files in the Downloads folder.

Files will be moved to the respective folders (Images, Videos, Documents, Otherfiles).

Web Series files will be organized by episode.
