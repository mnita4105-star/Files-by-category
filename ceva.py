import os
import shutil

# Change this to the path where your files are located
# e.g., "/sdcard/Download"
folder_path = "/sdcard/Download"

# Define your categories
file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents"
}

def organize():
    for filename in os.listdir(folder_path):
        
        ext = os.path.splitext(filename)[1].lower()
        
        if ext in file_types:
            category = file_types[ext]
            target_dir = os.path.join(folder_path, category)
            
            
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            
            shutil.move(os.path.join(folder_path, filename), 
                        os.path.join(target_dir, filename))
            print(f"Moved {filename} to {category}")

if __name__ == "__main__":
    organize()
    print("Cleanup complete!")
