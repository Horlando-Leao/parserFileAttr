import os
import shutil
from typing import List
import magic as file_attr_analyzer

code_mimetypes = {
    "text/rtf": 'rtf',
    "application/msword": 'doc',
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": 'docx',
    "application/pdf": 'pdf',
    "application/octet-stream": 'zip',
    "application/zip": 'zip'
}


def create_folder(foldernames: list):
    for foldername in foldernames:
        os.makedirs(os.path.dirname(foldername), exist_ok=True)


def rename_wit_mimetype_in_file(path_file: str, path_rename: str, mimetype: str):
    name_file = path_file.split(os.sep)[-1]
    try:
        shutil.copy(path_file, f'{os.path.join(path_rename, name_file)}.{mimetype}')
    except Exception as exc:
        raise ValueError(f'Não foi possivel renomear arquivo "{path_file}" para {path_file}.{mimetype}. STACK:\n {exc}')


def renames_files_mimetype(files_mime: List[List[str]], path_rename: str, exception=False):
    for file, mime in files_mime:
        try:
            rename_wit_mimetype_in_file(path_file=file, path_rename=path_rename, mimetype=mime)
        except ValueError as value:
            if exception:
                raise ValueError(value)
            else:
                print(value)
    return True


def list_files(path_root: str) -> List[str]:
    """
    Find all files in folder and return list of files
    :rtype: list
    :param path_root: Path folder
    :return: List of files in path_root
    """
    listing_files = []
    for root, dirs, files in os.walk(path_root):
        for filename in files:
            listing_files.append(os.path.join(root, filename))
    return listing_files


def get_mimetype_on_file(path_file: str) -> List[str]:
    mime = code_mimetypes.get(file_attr_analyzer.from_file(os.path.join(path_file), mime=True))
    return [path_file.split('/')[-1], mime]


def get_mimetype_on_files(path_files: list) -> List[List[str]]:
    mimes = []
    for path_file in path_files:
        mimes.append(get_mimetype_on_file(path_file))
    return mimes
