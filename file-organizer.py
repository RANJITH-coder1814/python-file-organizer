import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".exe", ".msi", ".py", ".java", ".c", ".cpp"]
}

def create_folders(path):
    for folder in FILE_TYPES:
        folder_path = os.path.join(path, folder)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

def organize_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            moved = False
            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    shutil.move(file_path, os.path.join(path, folder, file))
                    moved = True
                    break

            if not moved:
                other_path = os.path.join(path, "Others")
                if not os.path.exists(other_path):
                    os.mkdir(other_path)
                shutil.move(file_path, os.path.join(other_path, file))

def main():
    print(" Python File Organizer")
    path = input("Enter folder path to organize: ").strip()

    if not os.path.exists(path):
        print(" Invalid Path")
        return

    create_folders(path)
    organize_files(path)

    print(" Files organized successfully!")

if __name__ == "__main__":
    main()
