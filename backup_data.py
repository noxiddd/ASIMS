from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

uploadlist=['inventory_file.txt','login_info.txt','revenuelog.txt']

for file in uploadlist:
  gfile=drive.CreateFile({'parents': [{'id': '1jufZmKHgYz2-hdb4AYGu0K7oToFp5Mqo'}]})
  gfile.SetContentFile(file)
  gfile.Upload()