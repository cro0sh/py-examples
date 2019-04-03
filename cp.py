

import shutil

import os
##os.chmod('/dev/sdc1', 0o777)
##shutil.copy2('/home/c/Downloads/dog.jpg', '/dev/sdc1') # complete target filename given
##shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext
from shutil import copyfile


import os
def change_permissions_recursive(path, mode):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in [os.path.join(root,d) for d in dirs]:
            os.chmod(dir, mode)
        for file in [os.path.join(root, f) for f in files]:
            os.chmod(file, mode)

change_permissions_recursive('/media/c/Seagate Backup Plus Drive', 0o777)

copyfile('/home/c/Downloads/dog.jpg', '/media/c/Seagate Backup Plus Drive/dog.jpg')
