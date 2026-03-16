import shutil

with open("test_file.txt", "w") as f:
    f.write("lalalala")

shutil.copy("test_file.txt", "test/dirs/dir1/test_file.txt")
print("copied to dir1")

shutil.move("test_file.txt", "test/dirs/dir2/test_file.txt")
print("moved to dir2")