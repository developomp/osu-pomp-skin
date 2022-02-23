from glob import glob
from shutil import copyfile

#
# main
#

for file_path in glob("src/procedures/meta/*"):
    if "/__init__.py" in file_path or "/__pycache__" in file_path:
        continue

    file_name = file_path.split("/")[-1]
    copyfile(file_path, f"dist/{file_name}")
