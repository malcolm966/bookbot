import os
from config import MAX_CHARS 


def get_file_content(working_directory, file_path):
    try:
        working_dir_abs =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        content = str()

        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{target_dir}"'
        
        with open(target_dir,'r') as f:
            content += f.read(10000)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    except Exception as e:
        return f'Error: {e.__cause__}'

def test():
    result = get_file_content('.', '/Users/malcolm/workspace/github.com/bookbot/course8/functions')
    print(result)

# test()