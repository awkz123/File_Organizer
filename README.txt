📁 File Organizer
Automatically organize files in a specified folder (e.g., Downloads) into categorized subfolders such as Images, Documents, Videos, and more. Supports command-line usage and GUI interfaces (Tkinter or Streamlit).

✅ Features
Sorts files into folders by type:
Images, Documents, Videos, Audio, Archives, Code, and Others.

Handles nested directories (recursive).

Dry Run mode to preview changes without moving files.

Graphical User Interface (GUI) using:

🖥️ Tkinter (desktop GUI)

🌐 Streamlit (web interface)

Generates a file_organizer.log file to track activity and errors.

1. Command Line Interface (CLI)
# Basic usage (organizes your Downloads folder)
python fil_name.py

# Specify a folder
python fil_name.py --path "D:/MyFolder"

# Preview changes only (dry-run)
python fil_name.py --dry-run --path "D:/MyFolder"

2. Tkinter GUI (Desktop)
python fil_name.py --gui
Lets you browse and select a folder.

Option to run in Dry Run mode via checkbox.

3. Streamlit GUI (Web-based)
python a.py --streamlit
Then open the URL it shows (usually http://localhost:8501) in your browser.

❗ Note: Streamlit must be installed.

🗂 File Types Supported
Category	Extensions
Images	.jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg
Documents	.pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx
Videos	.mp4, .mov, .avi, .mkv, .flv, .wmv
Audio	.mp3, .wav, .aac, .flac, .ogg
Archives	.zip, .tar, .gz, .rar, .7z
Code	.c, .cpp, .java, .py, .js, .html
Others	Any other file types

📄 Log File
File: file_organizer.log

Logs every file moved, skipped, or error encountered.

💡 Example
Before:
Copy
Edit
Downloads/
├── file1.jpg
├── file2.pdf
├── file3.mp4
After:
Copy
Edit
Downloads/
├── Images/
│   └── file1.jpg
├── Documents/
│   └── file2.pdf
├── Videos/
│   └── file3.mp4
🙋 FAQ
Q: Can I add more file types?
Yes, modify the TYPE_MAP dictionary in the script.

Q: Will it delete or overwrite files?
No. It moves files safely and logs actions.

Q: What is Dry Run?
Preview what files would be moved — no changes are made.
