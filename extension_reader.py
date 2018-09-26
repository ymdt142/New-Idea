import os
import shutil
drive=input("Enter the drive and get all files extension")
for path,dirfol,file in os.walk(drive+":"):
	for item in file:
		b=item.split(".")
		print(b[-1])