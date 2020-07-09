
from colorlist import *
import os


def save_new_rgb_vals(new_color_path,new_pallet,new_palette_path):
    # save the generated values for later
    rgbSave = open(new_color_path + "rgbvalues.txt", "w")
    for x in new_pallet:
        mystring = str(x[0]) + ", " + str(x[1]) + ", " + str(x[2]) + ", 255,\n"
        rgbSave.write(mystring)
    print(new_palette_path)
    rgbSave.close()

def edit_txt_filepaths(new_color_path, new_palette_path):
    # open the pointer file
    pointer_file_path = 'ragdoll/filenames.txt'
    pointer_file_in = open(new_color_path + pointer_file_path, "r")
    lines_of_file = pointer_file_in.readlines()
    pointer_file_in.close()

    # modify the copied data
    for x in range(0, len(lines_of_file)):
        lines_of_file[x] = lines_of_file[x].replace('template', new_palette_path)
    # update the file
    pointer_file_out = open(new_color_path + pointer_file_path, "w")
    pointer_file_out.writelines(lines_of_file)
    pointer_file_out.close()


def updateTrackerfile():

    list_of_directories = os.listdir(mod_path)
    output_list = []
    for output in list_of_directories:
        if output ==  'colortracker.txt' or output == 'loadouts.lua' or output == 'template':
            continue
        output_list.append(output + '\n')
    trackerfile_out = open(colortracker_path, "w")
    trackerfile_out.writelines(output_list)
    trackerfile_out.close


# edits the exml files in the mod folder
def edit_xml_filepaths(new_color_path, new_palette_path):
    # edit xml files to have correct path
    xml_player_path_list = ("player.xml", "player_arm.xml")
    for xml_player_path in xml_player_path_list:
        xmlEdit_in = open(new_color_path + xml_player_path, "r")
        lines_of_file = xmlEdit_in.readlines()
        xmlEdit_in.close()

        # Cut out the line we wanna edit
        edit_path = lines_of_file.pop(1)

        # modify it
        edit_path = edit_path.replace('template', new_palette_path)
        # print(edit_path)

        # put it back
        lines_of_file.insert(1, edit_path)
        xmlEdit_out = open(new_color_path + xml_player_path, "w")
        xmlEdit_out.writelines(lines_of_file)
        xmlEdit_out.close()

