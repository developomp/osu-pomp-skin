from glob import glob
from shutil import copyfile

#
# main
#

for file_path in glob("src/procedures/meta/*"):
    if "/__init__.py" not in file_path and "/__pycache__" not in file_path:
        file_name = file_path.split("/")[-1]
        copyfile(file_path, f"dist/{file_name}")
