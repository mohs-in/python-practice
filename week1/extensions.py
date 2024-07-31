"""
In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""

in_str = input("File Name: ")

match in_str.split('.')[1]:
    case 'gif':
        print('image/gif')
    case 'jpg':
        print('image/jpg')
    case 'jpeg':
        print('image/jpeg')
    case 'pdf':
        print('file/pdf')
    case 'zip':
        print('file/zip')
    case _:
        print('application/octet-stream')
