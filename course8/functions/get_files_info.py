
import os
from google.genai import types





schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

def get_files_info(working_directory, directory="."):
    files_info = str()
    try:
    
        working_dir_abs =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        directory_name = 'current' if directory == '.' else directory
        files_info += (f'Result for {directory_name} directory:\n')
        if not valid_target_dir:
            files_info += (f'\tError: Cannot list "{directory}" as it is outside the permitted working directory\n')
        elif not os.path.isdir(target_dir):
            files_info += (f'\tError: "{target_dir}" is not a directory\n') 
        else:

            for i in os.listdir(target_dir):
                abs = os.path.join(target_dir, i) 
                print(i)
                file_size = os.path.getsize(abs)
                is_dir = os.path.isdir(abs)
                files_info += (f'  - {i}: file_size={file_size} bytes, is_dir={is_dir}\n')
    except Exception as e:
        files_info += (f'\tError: "{e}" is not a directory\n')
        print(e.with_traceback)
    return files_info