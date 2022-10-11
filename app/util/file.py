import os

from werkzeug.utils import secure_filename


def save_file(file, path, file_name):
    if os.path.isdir(path):
        try:
            file.save(path + secure_filename(file_name))
            return True
        except Exception:
            print("Error: 파일 저장을 실패 하였습니다.")
            return False
    else:
        return False
