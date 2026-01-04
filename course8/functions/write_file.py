import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name = 'write_file',
    description='往文件中写入内容',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'file_path': types.Schema(
                type=types.Type.STRING,
                description='文件路径'
            ),
            'content': types.Schema(
                type=types.Type.STRING,
                description='写入内容'
            ),
        },
        required=['file_path', 'content'],
    ),
) 


def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs,file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        parent_dir = os.path.dirname(target_dir)
        os.makedirs(parent_dir, exist_ok=True)
        with open(target_dir,'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e.__cause__}'