import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    abs_working_directory=os.path.abspath(working_directory)
    abs_full_path= os.path.abspath(os.path.join(working_directory,file_path))

    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_full_path,'r') as f:
            truncate_string=""
            if os.path.getsize(abs_full_path)> MAX_CHARS:
                truncate_string = f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]"'
                
            file_content_string = f.read(MAX_CHARS)
        return file_content_string+truncate_string
    except Exception as e:
        return f'Error: Failed to read file {file_path}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
        
        