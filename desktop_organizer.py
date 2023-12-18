import os
import shutil

def organize_desktop():
    current_dir = os.path.expanduser(r"C:\Users\hp\OneDrive\Desktop")  # Path to your desktop

    folders = {
        "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
        "Documents": [".txt", ".pdf", ".docx", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Music": [".mp3", ".wav", ".ogg", ".flac"],
        "Others": []  # Default folder for other file types
    }

    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, file)):
            file_extension = os.path.splitext(file)[1]
            moved = False
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    src = os.path.join(current_dir, file)
                    dest = os.path.join(current_dir, folder, file)
                    os.rename(src, dest)
                    moved = True
                    break
            if not moved:
                src = os.path.join(current_dir, file)
                dest = os.path.join(current_dir, "Others", file)
                os.rename(src, dest)

    print("Organizing completed!")

# Run the organizer function
organize_desktop()
