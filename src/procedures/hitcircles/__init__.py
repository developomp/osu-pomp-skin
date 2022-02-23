from PIL import Image
from glob import glob

from shutil import copyfile


def parse_approachcircle():
    opacity = 0.8

    img = Image.open("src/procedures/hitcircles/approachcircle.png")
    img = img.convert("RGBA")

    data = []
    for (r, g, b, a) in img.getdata():
        data.append((r, g, b, int(a * opacity)))

    img.putdata(data)
    img.save("dist/approachcircle@2x.png")


def parse_followpoint():
    copyfile("src/procedures/etc/1x1.png", "dist/followpoint-0@2x.png")
    copyfile("src/procedures/hitcircles/followpoint.png", "dist/followpoint-1@2x.png")
    copyfile("src/procedures/hitcircles/followpoint.png", "dist/followpoint-2@2x.png")
    copyfile("src/procedures/etc/1x1.png", "dist/followpoint-3@2x.png")


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
