import os

# dir()- folder
print(dir(os))

# current working directory - cwd
os.getcwd()

# create new folder - mkdir()
os.mkdir("nivu")
os.mkdir("naitvik")
os.mkdir("vandana")
os.mkdir("shriya")

# get list of all folders/directories - ls
os.listdir()

path = "C:/users/apple/onedrive/desktop/whitehat/mayank"
isExist = os.path.exists(path)
print(isExist)

path1 = "C:/users/apple/onedrive/desktop/whitehat/mayank/c239"
isExist = os.path.exists(path1)
print(isExist)