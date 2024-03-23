# osu-pomp-skin

[![license](https://img.shields.io/github/license/developomp/osu-pomp-skin?style=for-the-badge&color=yellow)](./LICENSE)
[![code style: black](https://img.shields.io/badge/black-black?style=for-the-badge&label=code%20style)](https://github.com/psf/black)
[![download skin](https://img.shields.io/badge/download_skin-gray?style=for-the-badge)](https://developomp.github.io/osu-pomp-skin)

My custom skin for the game [osu! (lazer)](https://github.com/ppy/osu) based on [vaxei's skin (blue, instant-fade)](https://drive.google.com/file/d/16YhU5yI4rgHFoK8PzBeFGDQoywWua417/view).

![screenshot](./.github/img/screenshot.avif)

## Characteristics

- minimalistic
  - does not even have a health bar
  - uses the default element in most places
- instant-fade circles
- osu!standard only
- acc meter positioned on top of the screen instead of the bottom
- made specifically for osu!lazer
- uses [HD images](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/FAQ/en.md#hd-images) only
  (although none of the images have a `@2x` suffix, they are all HD images. The suffix is added automatically during the build process)

## Commands

To generate a `.osk` osu skin file, run the following commands.

1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
2. Build skin
   ```bash
   python src
   ```

## Resources

- https://osu.ppy.sh/wiki/en/Skinning

## License

All non-asset files of this project are available under the GPL v3 License.
