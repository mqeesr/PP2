import os

os.makedirs("test/dirs/dir1", exist_ok=True)
os.makedirs("test/dirs/dir2", exist_ok=True)
os.makedirs("test/dirs/dir3", exist_ok=True)

print(os.listdir("test/dirs"))