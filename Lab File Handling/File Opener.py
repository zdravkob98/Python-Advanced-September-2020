try:
    file = open(r'C:\Users\zdravkob\Desktop\08-File-Handling-Lab-Resources\File Opener\text.txt', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')



