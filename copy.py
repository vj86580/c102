import os
import shutil
path = "C:/users/apple/onedrive/desktop/whitehat/shriya/c102"
print("Before copying file : " )
print(os.listdir(path))

source = "C:/users/apple/onedrive/desktop/geometric-shapes-names.png"
destination = "C:/users/apple/onedrive/desktop/whitehat/shriya/c102"

dest = shutil.copy(source,destination)

print("After copying file : ")
print(os.listdir(path))