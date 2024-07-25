import os
import shutil


def copy_from_source(src, dst):
    if not os.path.exists(src):
        raise ValueError ("Invalid source directory.")

    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)
    
    entries = os.listdir(src)

    for entry in entries:
        filepath = src + entry

        if os.path.isfile(filepath):
            shutil.copy(filepath, dst)
        else:
            copy_from_source(src + entry + "/", dst + entry + "/")

