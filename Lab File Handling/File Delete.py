import  os

try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print('File already deleted!')



file_path = "my_first_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)