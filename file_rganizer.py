import os
import shutil
import logging
from pathlib import Path
import argparse

# Mapping of file extensions to folder names
TYPE_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.tar', '.gz', '.rar', '.7z'],
    'Code':['.c','.cpp','.java','.py','.js','.html']
}

OTHER_FOLDER = 'Others'

# Setup logging
logging.basicConfig(
    filename='file_organizer.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organize_downloads(folder_path: Path, dry_run=False):
    if not folder_path.exists() or not folder_path.is_dir():
        logging.error(f"Invalid directory: {folder_path}")
        print(f"Error: {folder_path} is not a valid directory.")
        return

    for root, _, files in os.walk(folder_path):
        current_path = Path(root)
        for file in files:
            file_path = current_path / file
            ext = file_path.suffix.lower()
            moved = False

            for category, extensions in TYPE_MAP.items():
                if ext in extensions:
                    dest_folder = folder_path / category
                    dest_folder.mkdir(exist_ok=True)
                    dest = dest_folder / file_path.name
                    if not dry_run:
                        shutil.move(str(file_path), str(dest))
                    logging.info(f"Moved {file_path} to {dest}")
                    print(f"Moved {file_path} to {category}/")
                    moved = True
                    break

            if not moved:
                dest_folder = folder_path / OTHER_FOLDER
                dest_folder.mkdir(exist_ok=True)
                dest = dest_folder / file_path.name
                if not dry_run:
                    shutil.move(str(file_path), str(dest))
                logging.info(f"Moved {file_path} to {dest}")
                print(f"Moved {file_path} to {OTHER_FOLDER}/")

#if you want to use streamlit
def launch_streamlit_gui():
    st.title("Downloads Folder Organizer")
    st.write("Automatically organize files into subfolders based on file type.")

    folder_path = st.text_input("Enter the folder path:", str(Path.home() / "Downloads"))
    dry_run = st.checkbox("Dry Run (Preview Only)")
    run = st.button("Organize Files")

    if run:
        path_obj = Path(folder_path)
        if path_obj.exists() and path_obj.is_dir():
            organize_downloads(path_obj, dry_run=dry_run)
            st.success("Organization complete. Check logs for details.")
        else:
            st.error("Invalid directory. Please check the path.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Organize files by type.")
    parser.add_argument('--gui', action='store_true', help="Launch Tkinter GUI")
    parser.add_argument('--streamlit', action='store_true', help="Launch Streamlit GUI")
    parser.add_argument('--dry-run', action='store_true', help="Preview changes without moving files")
    parser.add_argument('--path', type=str, help="Path to organize (used in CLI mode)")
    args = parser.parse_args()

    if args.streamlit:
        import streamlit as st 
        launch_streamlit_gui()
    elif args.gui:
        launch_tkinter_gui()
    else:
        target_path = Path(args.path) if args.path else Path.home() / 'Downloads'
        organize_downloads(target_path, dry_run=args.dry_run)
