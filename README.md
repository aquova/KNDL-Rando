# KNDL-Rando

Kirby: Nightmare in Dream Land Randomizer

Randomization program for Kirby: Nightmare in Dream Land (KNDL) for GBA

https://github.com/aquova/KNDL-Rando

Written by Austin Bricker (aquova), 2017-2018

`https://twitter.com/aquova_`

## -- Overview --

Contained are programs to randomize the enemy abilities in Kirby: Nightmare in Dream Land. There are three programs contained within this repository which are to be used with a US version of Kirby: Nightmare in Dream Land for GBA.

First is a .lua script intended to be used with BizHawk or similar lua-compatible emulator. The lua script edits the RAM in real time, ensuring a completely random ability each time an enemy is swallowed. Keep in mind this is a work in progress, and some bugs have been known to occur.

Secondly, there is a program that edits the ROM, allowing it to be distributed and used with any emulator, as detailed below.
However, while the abilites are randomized, they are always constant within that ROM.
Ex. If a fire enemy now gives you the spark ability, ALL fire enemies will always give you the spark ability.

## -- Features --

- Randomizes which ability you gain from swallowing an enemy
- Change Kirby and Meta Knight's colors to several different options, including all the colors from *Kirby and the Amazing Mirror*

## -- Usage --

In addition to the files included in the repository, you will also need a US copy of the Kirby: Nightmare in Dream Land ROM (which is left to the user to obtain). Follow the instructions in the subcategories below for your operating system/preference.

#### --- Windows ---

Run `KNDL-Randomize-PC.exe`, found on the 'Releases' page. Select the options you desire, and select the location of your .gba KNDL ROM. Finish by clicking the 'Randomize' button. The randomized ROM will be saved into the same folder as the original, with the seed appended onto the end of the file name.

#### --- macOS ---

Run `KNDL-Randomize-Mac.app`, found on the 'Releases' page. Select the options you desire, and select the location of your .gba KNDL ROM. Finish by clicking the 'Randomize' button. The randomized ROM will be saved into the same folder as the original, with the seed appended onto the end of the file name.

#### --- Linux/Python ---

Linux users, or users who don't want to build it themselves, will have to build the binaries.

1. Install Python3, Qt5, and PyQt5 using your favorite package manager.

2. While in the 'src' directory, run the following command in Terminal:

`python3 KNDL-Randomize.py`

This will open the same application as the PC and Mac binaries.

#### --- Lua Compatible Emulator ---

If your emulator supports Lua scripts (such as Bizhawk), you are welcome to instead use the `KNDL-Script.lua` script. This script edits the RAM in real time, allowing for complete randomization of Kirby's abilities, meaning that eating enemies of the same type may give different results. This script is in an incomplete state at the moment.

## -- Known Issues / Future Plans --

- Enemies normally without abilities are not randomized
- Mini-bosses are not randomized
- The Star Rod, while available, is very experimental, and has many visual bugs.
- Meta Knight's sword will default back to its original color during certain animations. This is due to the game handling his palette differently on occasion, and is unlikely to be fixed.

## -- Version History --

v1.1.0 - Slighty modified GUI, added several more Kirby palettes. Added support for changing Meta Knight's palettes. Added spray can icons in the GUI. Remove 'KNDL-Simple' program.

v1.0.1 - Fixed visual glitch of color going back to default during certain animations

v1.0.0 - I've added support for changing Kirby's color to those from The Amazing Mirror

v0.1.0 - Initial Release. All enemies with an ability are randomized. Mini-bosses and enemies normally without abilities are not supported. Star Rod is available, but very glitchy.

## -- Special Thanks --

The author of MapDeluxe, which helped me learn how to spawn in different enemies for testing.

DrSchnaps and Spriter's Resource for the palettes from *Kirby and the Amazing Mirror*, as well as some custom palettes.
