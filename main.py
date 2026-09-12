import os 
import shutil

images = 0
document = 0 
videos = 0
others = 0
folder = input("Wheres the folder path? ")

sub_images = 0
sub_documents = 0
sub_videos = 0
sub_others = 0

os.mkdir(folder)
         
if os.path.exists(folder):
    print("The file exists!")
else:
    print("The file does not exist.")

list_of_files = os.listdir()
print(list_of_files)

path = os.path.join('directory', 'subdirectory', 'filename')
print(path)

print("The current directory:", os.getcwd())