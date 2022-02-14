import os
from typing import List
import func
from inline_args.args_sys import get_params_sys_args
from text_colorized.console import console

__example_command_run = r"Example: python __main__.py --root_path=C:\Users\Downloads\folder_without_mimetype"

sys_args = get_params_sys_args(['--root_path='])

try:
    original_path = sys_args['--root_path=']  # original path absolute of files
except KeyError:
    raise ValueError(f"Set the '--root_path=' original path absolute of files origin\n {__example_command_run}")

console.header('Running Rename with mimetype')

rename_folder = os.path.join(original_path, f'renames{os.sep}')
func.create_folder([rename_folder])

files_path: list = func.list_files(original_path)
files_mime: List[List[str]] = func.get_mimetype_on_files(files_path)
renaming = func.renames_files_mimetype(files_mime=files_mime, path_rename=rename_folder, exception=False)

if renaming:
    console.footer('Finished Rename with mimetype')



