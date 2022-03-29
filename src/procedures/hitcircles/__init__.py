from PIL import Image
from glob import glob

from shutil import copyfile

opacity = 1.0


def parse_approachcircle():
    img = Image.open("src/procedures/hitcircles/approachcircle.png")

    if opacity >= 1.0:
        img = img.convert("RGBA")

        data = []
        for (r, g, b, a) in img.getdata():
            data.append((r, g, b, int(a * opacity)))

        img.putdata(data)

    img.save("dist/approachcircle@2x.png")


def parse_followpoint():
    copyfile("src/procedures/etc/1x1.png", "dist/followpoint.png")


def parse_hitcircles():
    copyfile("src/procedures/hitcircles/hitcircle.png", "dist/hitcircle@2x.png")
    copyfile(
        "src/procedures/hitcircles/hitcircleoverlay.png",
        "dist/hitcircleoverlay@2x.png",
    )


#
# main
#

parse_approachcircle()
parse_followpoint()
parse_hitcircles()
