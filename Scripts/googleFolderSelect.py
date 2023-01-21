from Google import Create_Service
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from docx import Document
import time

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = '13julqBiMDaTy6GC7f_V2YYfc1EO-9PQl'

#Authorize the API
scope = ['https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/drive.file']
file_name = 'client_key.json'
creds = ServiceAccountCredentials.from_json_keyfile_name(file_name,scope)
client = gspread.authorize(creds)

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

#Fetch the sheet
worksheet = client.open('IT212_Schedule').sheet1

def get_id(fname):
    query = f"parents = '{folder_id}'"
    response = service.files().list(q=query, fields= 'files(id,name)').execute()
    files = response.get('files')
    if files:
        google_file_name=  files[0].get(fname)
        google_file_id = files[0].get('id')
    else:
        print("File Not Found")
    return google_file_id

def create_folder(fname):

    file_metadata = {
        'name': fname,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [folder_id],
    }
    service.files().create(body=file_metadata).execute()

#columns and index
letters = ["A","B","C","E","F","G","H","I"]

r = 0               # Keeps track of rows
weekCount = 1       # Keeps track of weeks
lab = 1             # Keeps track of labs
hw = 1              # Keeps track of homeworks
lec = 1             # Keeps track of lectures
w = 2               # Keep track of biweekly count
rowRange = len(worksheet.get_all_values()) # Number of rows

remainder = (rowRange - 1) % 2

maxRow = (((rowRange - 1) // 2) + remainder)

# Parse through worksheet to manipulate cells
for row in range(maxRow):

    # Create folder for each week of classes with its necessary contents

    if r < rowRange:
        weekPath = 'Week ' + str(weekCount)
        weekCount += 1
        create_folder(weekPath)
        for week in range(2):
            i = 1
            while i < len(letters):
                c1 = worksheet.acell(letters[i] + str(w)).value
                c2 = worksheet.acell('F' + str(w)).value
                c3 = worksheet.acell('H' + str(w)).value
                c4 = worksheet.acell('I' + str(w)).value
                c5 = worksheet.acell('C' + str(w)).value
                c6 = worksheet.acell('G' + str(w)).value
                c7 = worksheet.acell('E' + str(w)).value
                if i == 1:
                    if c1 is not None:
                        file1 = drive.CreateFile({'parents': [{'id': get_id(weekPath)}],'title': 'reading' + str(lec) +".txt", 'mimeType':'text/csv'})
                        if c7 is not None:
                            file1.SetContentString(c7 + " ")
                        if c2 is not None:
                            file1.SetContentString(c2 + " ")
                        if c3 is not None:
                            file1.SetContentString(' HW' + c3 + ' is due ' + worksheet.acell['A' + str(w)].value)
                        if c4 is not None:
                            file1.SetContentString(' Lab' + c4 + ' is due ' + worksheet.acell['A' + str(w)].value)
                        file1.Upload()
                        lec += 1
                        if c5 is not None:
                            file1 = drive.CreateFile({'parents': [{'id': get_id(weekPath)}],'title': 'Lab' + str(lab) +".docx", 'mimeType':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})
                            lab +=1
                            file1.Upload()
                        if c6 is not None:
                            file1 = drive.CreateFile({'parents': [{'id': get_id(weekPath)}],'title': 'HW' + str(hw) +".docx", 'mimeType':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})
                            hw += 1
                            file1.Upload()                       
                    elif c1 is None:
                        file1 = drive.CreateFile({'parents': [{'id': get_id(weekPath)}],'title': 'reading' + str(lec) +".txt", 'mimeType':'text/csv'})
                        if c7 is not None:
                            file1.SetContentString(c7 + " ")
                        if c2 is not None:
                            file1.SetContentString(c2 + " ")
                        if c3 is not None:
                            file1.SetContentString(' HW' + c3 + ' is due ' + worksheet.acell['A' + str(w)].value)
                        if c4 is not None:
                            file1.SetContentString(' Lab' + c4 + ' is due ' + worksheet.acell['A' + str(w)].value)
                        lec += 1
                        file1.Upload()   
                        if c5 is not None:
                            file1 = drive.CreateFile({'parents': [{'id': get_id(weekPath)}],'title': 'Lab' + str(lab) + ".docx", 'mimeType':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})
                            lab += 1
                            file1.Upload()
                        if c6 is not None:
                            file1 = drive.CreateFile({'parents': [{'id': get_id(weekPath)}],'title': 'HW' + str(hw) + ".docx", 'mimeType':'application/vnd.openxmlformats-officedocument.wordprocessingml.document'})
                            hw += 1
                            file1.Upload()
                    i+=1
                w += 1
        r +=2
                        
                    
                