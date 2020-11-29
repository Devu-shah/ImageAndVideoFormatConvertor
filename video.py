import os
from moviepy.editor import *
import time

print("\nTHIS PROGRAM IS CASE SENSITIVE!\n")

print("\nCopyright to Devansh Shah;"
	"\nEmail: theprogrammerdevansh@gmail.com"
	"\nInstagram: programming_with_devansh\n")

drive_name = str(input("In which Drive Does your video is there?: "))
subfolno = int(input("How many subfolders are there to reach your video?: "))

print("Note: The audio file, after the process is completed, will be in the folder you have provided...\n")
f1 = str(input("Type Folder name: "))
f2 = str(input("Type Folder name (Leave Blank if not applicable): "))
f3 = str(input("Type Folder name (Leave Blank if not applicable): "))
f4 = str(input("Type Folder name (Leave Blank if not applicable): "))
f5 = str(input("Type Folder name (Leave Blank if not applicable): "))
f6 = str(input("Type Folder name (Leave Blank if not applicable): "))
	
file_name = str(input("Give the file's name which is in mp4: "))
audio_file_name = str(input("Give audio file's name which you want to be: "))

if f2 == "" and f3 == "" and f4 == "" and f5 == "" and f6 == "":
	video = VideoFileClip(os.path.join(f"{drive_name}:\\{f1}\\{file_name}.mp4"))
	video.audio.write_audiofile(os.path.join(f"{drive_name}:\\{f1}\\{file_name}.mp3"))

elif f3 == "" and f4 == "" and f5 == "" and f6 == "":
	video = VideoFileClip(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{file_name}.mp4"))
	video.audio.write_audiofile(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{file_name}.mp3"))

elif f4 == "" and f5 == "" and f6 == "":
	video = VideoFileClip(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{f3}\\{file_name}.mp4"))
	video.audio.write_audiofile(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{f3}\\{file_name}.mp3"))

elif f5 == "" and f6 == "":
	video = VideoFileClip(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{f3}\\{f4}\\{file_name}.mp4"))
	video.audio.write_audiofile(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{f3}\\{f4}\\{file_name}.mp3"))

elif f6 == "" :
	video = VideoFileClip(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{f3}\\{f4}\\{f5}\\{file_name}.mp4"))
	video.audio.write_audiofile(os.path.join(f"{drive_name}:\\{f1}\\{f2}\\{f3}\\{f4}\\{f5}\\{file_name}.mp3"))

elif drive_name == exit or f1 == exit or f2 == exit or f3 == exit or f4 == exit or f5 == exit or f6 == exit:
	exit()

else:
	print("Input Invalid")