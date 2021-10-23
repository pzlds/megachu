# Megachu! (めがちゅ!) on Ren'Py

This is a port of the game Megachu! to the visual novel engine Ren'Py.
The game was originally released by FrontWing in 2006.

The motivation behind creating this port is that the original game is not
necessarily designed to run on modern versions of Windows (and much less
on non-Japanese systems), which keeps me (and probably many others) from
playing it.

In addition to that, translating the game to English is now an option as
well, which is not something that was done either officially or as an
existing fan project (as far as I can tell).

If you like the game, please make sure to buy [the original](http://frontwing.jp/product/mega/index.html).
You will need its assets to use this port either way.

## Building / Installation

Assets have been excluded from the repository on purpose to try and limit legal conflicts.

To obtain them from the original game, extract the the original data archives
(`GameData/data*.pack`) using [ExtractData](https://github.com/lioncash/ExtractData)
and copy the extracted files from `data0.pack`, `data1.pack`, `data2.pack` and
(if you installed the v1.01 update) `data3.pack` into a single folder.

Afterwards, run the following command in a terminal:

```
./extract-files.sh /path/to/extracted/files
```

Once all the files have been copied and converted without errors, the project should now be
openable as a normal Ren'Py project.

**Note:** Extraction and conversion of data currently only works on Linux and (probably) macOS,
as it is implemented in a bash script and using some Unix-specific tools.
ExtractData is a Windows-only tool, but it should run just fine in [Wine](https://winehq.org).

## Disclaimer

Megachu!, including the scenario and the assets, is the property of FrontWing. This port is not licensed
or endorsed by FrontWing. As such, this project only includes parts of the scenario due to importing it
separately not being feasible. All other assets are excluded and have to be provided by the user, who
already owns the original game.

This port is purely not for profit and only exists in appreciation for the game.
If anyone from FrontWing (either in it's function as developer or as publisher) objects to this project existing,
please make sure to contact me and I'll happily take it down.


