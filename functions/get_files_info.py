import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        full_path_working_directory=os.path.abspath(working_directory)
        full_path=os.path.abspath( os.path.join(working_directory,directory))

        if  not full_path.startswith(full_path_working_directory):
            return f'   Error: Cannot list "{full_path}" as it is outside the permitted working directory'    
        if not os.path.isdir(full_path):
            return f'   Error: "{full_path}" is not a directory'

        items_list=os.listdir(full_path)
        results=""
        for item in items_list:
            full_item_path=os.path.join(full_path,item)
            file_size=os.path.getsize(full_item_path)
            is_dir=os.path.isdir(full_item_path)
            results += (f"- {item}: file_size:{file_size} bytes, is_dir={is_dir}")+'\n'
        return results
    
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)