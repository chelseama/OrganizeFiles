import os, time
from pathlib import Path

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}

FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

DIR_TO_BE_SCANNED = ['Desktop', 'Documents', 'Downloads']
ROOT = Path.home()

def categorize(root_path, entry):
    file_name = Path(entry.name)
    file_path = Path(entry)
    file_format = file_name.suffix.lower()

    if file_format in FILE_FORMATS:
        directory_path = root_path.joinpath(Path(FILE_FORMATS[file_format]))
        if not directory_path.exists():
            directory_path.mkdir()   
        new_file_path = directory_path.joinpath(file_name)
        file_path.rename(new_file_path)
    else:
        misc_path = root_path.joinpath(Path('MISC'))
        if not misc_path.exists():
            misc_path.mkdir()
        new_file_path = misc_path.joinpath(file_name)
        file_path.rename(new_file_path)

def organize_files(path=ROOT):
    for entry in os.scandir(path):
        if entry.name.startswith('.'):
            continue
        elif entry.is_dir():
            if entry.name in DIR_TO_BE_SCANNED:
                subdir_path = path.joinpath(entry.path)
                for inner_entry in os.scandir(subdir_path):
                    categorize(path, inner_entry)
        else:
            categorize(path, entry)
        


if __name__ == "__main__":
    organize_files()