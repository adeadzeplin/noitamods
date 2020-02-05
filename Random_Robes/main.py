from PIL import Image
from include import *
from discriminator import the_racist

def CreateNewSkin():

    new_color_path, new_palette = update_color_values()


    # iterate each png path in the list
    for sprite_path in sprite_path_list:

        # open file to edit
        png = Image.open(new_color_path+sprite_path)
        # png.show()

        # scan every hecking pixel in the file.
        # pixel size holds (width,height) or maybe the otherway around.
        # either way i don't care, it doesn't matter
        for x in range(0,png.size[0]):
            for y in range(0,png.size[1]):

                # pixel variable
                temp = png.getpixel((x, y))

                # if the pixel is empty skip it. We aint messing with it
                if temp[0] == 0 and temp[2] == 0 and temp[3] == 0:
                    continue

                # check every color
                for i in range(0, len(template_palette)):

                    # if the color we're checking for matches the pixel: replace it with the new color we want
                    if temp == template_palette[i]:
                        png.putpixel((x, y), tuple(new_palette[i]))
                        break

        # opens the new file
        if sprite_path == sprite_path_list[0]:
            # png.show()
            pass
        png.save(new_color_path + '/' + sprite_path)

    # print(player.format, player.size, player.mode)




if __name__ == "__main__":
    for x in range(0,30):
        CreateNewSkin()

    ##update tracker file
    updateTrackerfile()

    ##edit lua files to have the right info regarding the generated files
    edit_lua_files()
    



