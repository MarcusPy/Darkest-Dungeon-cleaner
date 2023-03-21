import os, shutil

# made to help clean up unwanted files taken from DarkestDungeon/<...>/monsters when making a mod

unwanted_folders         = [ 'anim', 'fx', 'ui' ] # remove folder and its content
unwanted_file_extensions = [ '.art.darkest' ]     # remove all files ending with this extension from a folder
unwanted_files           = [ 'tint.png' ]         # remove specific files from a folder

working_path = os.getcwd() + '/'
monster_folders = [ mob for mob in os.listdir(working_path) if os.path.isdir(working_path+mob) ]

for monster in monster_folders:
    temp_path = working_path + monster + '/'
    monster_variations_folders = [ var for var in os.listdir(temp_path) if os.path.isdir(temp_path+var) ]
    for variation in monster_variations_folders:
        temp_path = temp_path + '/' + variation
        for extension in unwanted_file_extensions:
            temp_path = working_path + monster + '/' + variation + '/' + f'{variation}{extension}'
            try:
                os.remove(temp_path)
            except FileNotFoundError:
                continue
        for file in unwanted_files:
            temp_path = working_path + monster + '/' + variation + '/' + file
            try:
                os.remove(temp_path)
            except FileNotFoundError:
                continue
    for folder in unwanted_folders:
        temp_path = working_path + monster + '/' + folder
        try:
            shutil.rmtree(temp_path)
        except FileNotFoundError:
            continue