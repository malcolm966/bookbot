import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name = 'run_python_file',
    description='执行python 文件',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'file_path': types.Schema(
                type=types.Type.STRING,
                description='python文件路径'
            ),
            'args': types.Schema(
                type=types.Type.ARRAY,
                items= types.Schema(type=types.Type.STRING), 
                description='执行python文件时,的命令行参数'
            ),
        },
        required=['file_path'],
    ),
) 




def run_python_file(working_directory, file_path:str, args=None):
    try:
        working_dir_abs =  os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        working_dir_abs =  os.path.abspath(working_directory)
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        command = ["python", absolute_file_path]
        if args:
            command.extend(args)
        result = subprocess.run(args=command, cwd=working_directory, capture_output=True, text= True,  timeout=30)
        output_parts = []

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout}")
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr}")
        return '\n'.join(output_parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"