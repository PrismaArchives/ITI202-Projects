import pathlib
import shutil

#Sets current working directory and then prints it
current_dir = pathlib.Path().cwd()
print(current_dir)

#creates a folder called folder_week11 by first establishing the path then making the folder using that path
folder_week11_path = current_dir / 'folder_week11/'
folder_week11_path.mkdir()

#creates a file called week11.txt by first establishing the path then making the file using that path
week11_file_path = folder_week11_path / 'week11.txt'
week11_file_path.touch()

#information to be written to the week11.txt file
file_text = "Test: Writing to file."

#writes to the file then prints what is in the file to ensure it wrote properly
week11_file_path.write_text(file_text)
print(week11_file_path.read_text())

#Creates path and directory for backup files
backup_folder_path = folder_week11_path / 'file_backups' 
backup_folder_path.mkdir()

#copies over data in from week 11 file into the backup folder including metadata
shutil.copy2(week11_file_path, backup_folder_path / 'week11_backup.txt')

#searches and prints the path for any .txt file in the folder_week11 path directory or subdirectories
for f in folder_week11_path.rglob('*.txt'):
    print(f)