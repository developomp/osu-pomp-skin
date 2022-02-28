from PIL import Image
from glob import glob


#
# main
#

opacity = 0.25

# find all files
for file_path in glob("src/procedures/followpoints/*.png"):
    img = Image.open(file_path)
    img = img.convert("RGBA")

    # lower opacity

    data = []
    for (r, g, b, a) in img.getdata():
        data.append((r, g, b, int(a * opacity)))

    img.putdata(data)

    # save image

    file_name = file_path.split("/")[-1].removesuffix(".png")
    img.save(f"dist/{file_name}@2x.png")
