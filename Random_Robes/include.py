
from PIL import Image
import os
from colorlist import *
from fileedit import save_new_rgb_vals,edit_xml_filepaths,edit_txt_filepaths,updateTrackerfile

import shutil


def updateUVspritemaps():
    templateUVgenerated_path = generated_path + "mods.Random_Robesv2.files.template.player.png"

    try:
        shutil.rmtree(UVspritemap_path)
    except:
        print("delete directory FAILED")
        pass
    template_uvsprite_png = Image.open(generated_path + "mods.Random_Robesv2.files.template.player.png")

    ofile = open(colortracker_path, "r")
    filelist = ofile.readlines()
    ofile.close()

    try:
        os.mkdir(UVspritemap_path)
    except:
        print("the new directory couldn't be made")

    for file in filelist:
        shutil.copy(templateUVgenerated_path, UVspritemap_path + 'mods.Random_Robesv2.files.'+ file.strip('\n') +'.player.png')



def update_color_values(RGBVAL):
    # Generate palate & new path
    new_palette_path, new_pallet = generateColorPalate(RGBVAL)
    new_color_path = mod_path + new_palette_path + "/"

    # Populate the new directory
    copyDirectory(template_path, new_color_path)

    # save the newly generated rgb values
    save_new_rgb_vals(new_color_path, new_pallet, new_palette_path)
    # edit the paths in the xml files
    edit_xml_filepaths(new_color_path, new_palette_path)

    # edit the paths in the text files
    edit_txt_filepaths(new_color_path, new_palette_path)

    return  new_color_path, new_pallet #folder_name+'/', palette

def edit_lua_files():

    colors_in = open(colortracker_path, "r")
    list_of_colors = colors_in.readlines()
    colors_in.close()

    # print(list_of_colors)
    line_counter = 0
    lua_list = []
    lua_list.append('loadout_list = {\n')
    line_counter += 1
    for a_color in list_of_colors:
        # '#%02x%02x%02x' % (0, 128, 64)

        current_color = open(mod_path + a_color.strip('\n') + '/rgbvalues.txt', "r")
        cur_c = current_color.readlines()
        current_color.close()
        base_c = cur_c[0].split(", ")
        edge_c = cur_c[1].split(", ")

        # x.split(" ")
        #     output.append(x.replace(',', '').strip(','))

        # print(base_c)
        base_c = '0xFF%02x%02x%02x' % (int(base_c[2]), int(base_c[1]), int(base_c[0]))
        edge_c = '0xFF%02x%02x%02x' % (int(edge_c[2]), int(edge_c[1]), int(edge_c[0]))


        lua_list.append('{ name =  "A' + a_color.strip('\n') + '", folder = "' + a_color.strip('\n') + '", cape_color = ' + base_c + ', cape_color_edge = ' + edge_c + ',},\n' )
        line_counter += 1
    lua_list.append('}')

    lua_output = open(mod_path + 'loadouts.lua',"w")
    lua_output.writelines(lua_list)
    lua_output.close()
    # print(lua_list)

    lua_input = open(mod_top_path + 'init.lua', "r")
    prime_in = lua_input.readlines()
    lua_input.close()
    magic_number = 69
    while(len(prime_in) > magic_number):
        prime_in.pop()

    for j, a_color in enumerate(list_of_colors):
        temp_path = 'ModDevGenerateSpriteUVsForDirectory( "' + 'mods/Random_Robesv2/files/' + a_color.strip('\n') + '" )\n'
        prime_in.append(temp_path)

    lua_output = open(mod_top_path + 'init.lua', "w")
    lua_output.writelines(prime_in)
    lua_output.close()

    # for j, a_color in enumerate(list_of_colors):
    #     dne_Flag = True
    #     temp_path = []
    #     for i, line in enumerate(prime_in, magic_number):
    #         temp_path = 'ModDevGenerateSpriteUVsForDirectory( "' + mod_path + a_color + '" )\n'
    #         if line == temp_path:
    #             list_of_colors.pop(j)
    #             dne_Flag = False
    #             break
    #     if dne_Flag:
    #         prime_in.append(temp_path)
    # f1 = f.readlines()
    # output = []
    #
    # for x in f1:
    #
    #     x.split(" ")
    #     output.append(x.replace(',', '').strip('\n'))
    #
    # folder_name = output.pop(0)
    #
    #
    # palette = []
    # for x in output:
    #     palette.append(x.split(" "))
    #
    # for x in palette:
    #     for y in range(0, len(x)):
    #         x[y] = int(x[y])
    #     x.append(255)