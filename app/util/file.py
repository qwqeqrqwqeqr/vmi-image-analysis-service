import os

from werkzeug.utils import secure_filename

from util.constants import ANSWER_IMAGE_DIRECTORY
from util.directory import create_directory


def save_files(files):
    create_directory(ANSWER_IMAGE_DIRECTORY)

    for file in files:
        file.save(ANSWER_IMAGE_DIRECTORY + "/" + file.filename)


