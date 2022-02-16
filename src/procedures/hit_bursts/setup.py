from PIL import Image
from glob import glob

from log import info


def create_frames(image_path: str, create_k=False):
    """Create frames for each hit burst"""

    file_name = image_path.split("/")[-1]

    # create hit100k too
    if not create_k and "hit100" in file_name:
        create_frames(image_path, True)

    # create hit300 and hit300k
    if "hit300" in file_name:
        create_hit300s(image_path)
        return

    img = Image.open(image_path)

    # i: 0 ~ 45
    for i in range(46):
        if create_k:
            frame_file_path = f"{file_name.removesuffix('.png')}k-{i}@2x.png"
        else:
            frame_file_path = f"{file_name.removesuffix('.png')}-{i}@2x.png"

        if i <= 30:
            # no alterations for frame 0 ~ 30

            img.save(f"./dist/{frame_file_path}")
        else:
            # linear fading for frame 31 ~ 45

            transparent_img = img.convert("RGBA")
            data = img.getdata()

            new_data = []
            for (r, g, b, a) in data:
                a = int(a * (45 - i) / 14)
                new_data.append((r, g, b, a))

            transparent_img.putdata(new_data)  # type: ignore
            transparent_img.save(f"./dist/{frame_file_path}")


def create_hit300s(image_path: str):
    img = Image.open(image_path)
    file_name = image_path.split("/")[-1].removesuffix(".png")

    img.save(f"./dist/{file_name}-0@2x.png")
    img.save(f"./dist/{file_name}k-0@2x.png")


#
# main
#


for image_path in glob("src/procedures/hit_bursts/*.png"):
    create_frames(image_path)
