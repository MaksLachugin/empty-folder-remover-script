import os
import errno, os, stat, shutil


def handleRemoveReadonly(func, path, exc):
    excvalue = exc[1]
    if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
        func(path)
    else:
        raise


def get_folder():
    return input()


def find_in_folder():
    path_to_folder = get_folder()
    if path_to_folder != '':
        os.chdir(path_to_folder)
    deleter()


def deleter(path='.'):
    try:
        path += r'\\'
        for x in os.listdir(path):
            if os.path.isdir(path + x):
                deleter(path + x)
        if len(os.listdir(path)) == 0:
            print(path, os.listdir(path))
            shutil.rmtree(path, ignore_errors=False, onerror=handleRemoveReadonly)
    except:
        pass


find_in_folder()
input()