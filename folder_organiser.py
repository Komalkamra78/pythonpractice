from distutils.file_util import move_file
from msilib.schema import MoveFile
import os

def IfNotFound(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def MoveFiles(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

files = os.listdir()
files.remove("folder_organiser.py")
# print(files)
IfNotFound("Images")
IfNotFound("Docs")
IfNotFound("Media")
IfNotFound("Others")

ImgExt = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in ImgExt]
# print (images)

DocExt = [".txt", ".doc", ".docx", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in DocExt]
# print (docs)

mediaExt = [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]

other = []
for file in files:
    a = os.path.splitext(file)[1].lower()
    if (a not in ImgExt and a not in DocExt and a not in mediaExt and os.path.isfile(file)):
        other.append(file)
# print(other)

MoveFiles("Images", images)
MoveFiles("Docs", docs)
MoveFiles("Media", medias)
MoveFiles("Others", other)
