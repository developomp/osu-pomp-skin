from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

#
# main
#

font = ImageFont.truetype("src/fonts/NotoSans-Regular.ttf", 80)

# i: 0 ~ 9
for i in range(10):
    image = Image.new("RGBA", (45, 100))
    draw = ImageDraw.Draw(image)

    draw.text((0, -7), f"{i}", fill="white", font=font)

    image.save(f"dist/default-{i}@2x.png")
