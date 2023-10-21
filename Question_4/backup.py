import sys
import os
import shutil
from datetime import datetime

def backup_files(source_dir, dest_dir):
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)

            # Check if the destination file already exists
            if os.path.exists(dest_path):
                # Append a timestamp to the file name for uniqueness
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename, file_extension = os.path.splitext(filename)
                new_filename = f"{filename}_{timestamp}{file_extension}"
                dest_path = os.path.join(dest_dir, new_filename)

            shutil.copy(source_path, dest_path)
            print(f"Backed up: {filename} to {dest_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


source_directory = sys.argv[1]
destination_directory = sys.argv[2]
backup_files(source_directory, destination_directory)

# python3 backup.py {source_directory} {destination_directory}
