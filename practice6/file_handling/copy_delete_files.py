import shutil
import os

shutil.copy("transcript.txt", "copy.txt")

# if os.path.exists("copy.txt"):
#     os.remove("copy.txt")
#     print("deleted")