# osu-pomp-skin

**WIP**

My custom skin for the game [osu!](osu.ppy.sh) (yes, the exclamation mark is part of the name).

## Characteristics

- semi-transparent approach circles to make reading high [AR](https://osu.ppy.sh/wiki/en/Beatmapping/Approach_rate) easier
- minimalism
  - not even a health bar
- osu!standard only
- centered acc meter
- made specifically for osu!lazer
- [HD images](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/FAQ/en.md#hd-images) only

## Commands

> Assumes that these commands are called from the project root

Install dependencies:

```bash
pip install -r requirements.txt
```

Build skin:

```bash
python src
```

## What's in it?

Though no images have a `@2x` postfix, they are all HD images, and the postfix will be added automatically during the build process.

### [hitcircles](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/osu!/en.md#hit-circles)

### [cursor](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/Interface/en.md#cursor)

### [hit bursts](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/Interface/en.md#hit-bursts)

### [default numbers](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/osu!/en.md#default-numbers)

### [slider](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/osu!/en.md#slider)

### [spinner](https://github.com/ppy/osu-wiki/blob/master/wiki/Skinning/osu!/en.md#spinner)

## Resources

- [osu! wiki page about skinning](https://osu.ppy.sh/wiki/en/Skinning)
- some assets are from [vaxei's skin](https://drive.google.com/file/d/1JRDbxtEVFYMgt9ls4rvIRs2v0IfBddFO/view)
- some assets are from [flyingtuna's skin](https://drive.google.com/file/d/1SVtUUvo4o2DUwQ1Pf2Xb0v4eDblvvovq/view)
- some assets are from [whitecat's skin](https://drive.google.com/file/d/1A9Ktx7MY-UP5iOGTTHsyQP622zDOKqfe/view)

## License

The source code of this project\* is available under the MIT License.

\*excluding files in the [`fonts`](./fonts) and the [`resource`](./resource) directory.

Fonts:

- [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro): Open Font License (OFL)
- [Noto Sans](https://fonts.google.com/noto/specimen/Noto+Sans): Open Font License (OFL)
