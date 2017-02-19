import glob, os
import shutil
os.chdir('C:\Users\MAHE\Desktop\Download') #changes the current directory
for file in glob.glob("*.mp3"):  #finds all the pathnames with a particular pattern or extension
    src = 'C:\Users\MAHE\Desktop\Download\\' + file    #directory from where you want to move
    dest = 'C:\Users\MAHE\Desktop\songs' #directory to you want to move
    shutil.move(src, dest)  #moves the file from source to destination using shell utilities
