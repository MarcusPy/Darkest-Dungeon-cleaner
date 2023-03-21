# Darkest-Dungeon-cleaner
Useful if you tend to copy the entire DarkestDungeon/<...>/monsters folder to mod but then have to get rid of files you don't intend to modify.
You can specify what should be removed according to the intructions within the script file.

#Example:
You want to modify monsters/ancestor_big/ancestor_big_D/ancestor_big_D.info.darkest, but what to get rid of other files that will be copied over from main game directory (anim, fx, tint.png, ancestor_big_D.art.darkest). Just fill up the 3 unwanted_<something> lists with objects you want to be removed and run the script. By default every file or folder is included, except for <variation>.info.darkest

Obviously requires Python. Built on 3.11.1
