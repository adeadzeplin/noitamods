from PIL import Image
from include import *
import statistics
def CreateNewSkin(RGBval):

    new_color_path, new_palette = update_color_values(RGBval)


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


def updateFiles():
    ##update tracker file
    updateTrackerfile()

    ##edit lua files to have the right info regarding the generated files
    edit_lua_files()

    updateUVspritemaps()

def generateValues(maxnumofcolors):

    colorlist =[]
    colpathlist = []
    for x in range(maxnumofcolors):
        orary = gencol()

        R = orary[0]
        G = orary[1]
        B = orary[2]
        avg = statistics.median([R, G, B])
        rdif = abs(avg - R)
        gdif = abs(avg - G)
        bdif = abs(avg - B)
        bias = 20
        if rdif <= bias:
            if bdif <= bias:
                if gdif <= bias:
                    # print("skip")
                    continue

        # print(orary[0],orary[1],orary[2])

        colorlist.append(orary)
        print(len(colorlist))
    colorlist.sort()
    deletedcount = 0

    for i, c in enumerate(colorlist,0):
        for j, c_ in enumerate(colorlist,0):
            if i != j:  #if color isn't itself

                rdif = abs(c[0] - c_[0])
                gdif = abs(c[1] - c_[1])
                bdif = abs(c[2] - c_[2])
                bias = 15
                if rdif <= bias:
                    if bdif <= bias:
                        if gdif <= bias:
                            # print("removed duplicate value")
                            colorlist.pop(j)
                            deletedcount += 1
                            continue
    print(len(colorlist))
    print("deleted :" + str(deletedcount))

    # cfile_out = open(mod_top_path + 'colorholder.txt', "w")
    # for x in colorlist:
    #     mystring = str(x[0]) + " " + str(x[1]) + " " + str(x[2]) + "\n"
    #     cfile_out.write(mystring)
    # cfile_out.close


    min = 0
    max = 0
    for c in colorlist:

        for i in c:
            if i < min:
                min = i
            if i > max:
                max = i
    print(min,max)

    return colorlist







def makeSkins(num):
    YeeOlelist = generateValues(num)
    i = len(YeeOlelist)
    for col in YeeOlelist:

        CreateNewSkin(col)
        print('skins to go: ' + str(i)+ '\n')
        i -= 1




if __name__ == "__main__":
    
    
    
    
    # this Function will attempt to create 100 randomly colored sprites
    # however the way it generates color paletes is pretty bad and takes forever if you want to do a bunch of colors
    # generating the 995 skins for the mod took 30 minutes! super slow and innacurate
    # and I had it attempt to make 10,000 skins and it only made 955
    # this is because if two randomly generated color pallets are too similar to each other the program will just toss out the color and try a different random color
 
    # makeSkins(100)
    
    updateFiles()    # this function will update the game files with the appropriate code based on whatever files are in the mod folder
                     # this is usefull if you want to delete some spritesets that you think look bad and want to delete them






