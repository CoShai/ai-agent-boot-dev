from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file


def print_read_results(working_directory,path,description=""):
    print(f'{description}')
    print(get_file_content(working_directory,path))


def print_write_results(working_directory,file,content):
    print("")
    print(write_file(working_directory,file,content))
    

print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))

