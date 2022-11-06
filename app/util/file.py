import os

from werkzeug.utils import secure_filename

from util.constants import ANSWER_IMAGE_DIRECTORY
from util.directory import create_directory


def save_files(files, path):
  create_directory(path)

  for file in files:
    file.save(path + "/" + file.filename)


def save_file(file, path):
  create_directory(path)
  file.save(path + "/" + file.filename)
