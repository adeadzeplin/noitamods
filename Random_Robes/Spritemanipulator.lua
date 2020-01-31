dofile("mods/Random_Robes/png.lua")


--template_colors

template_main = {240, 240, 240, 255}
template_edge = {200, 200, 200, 255}
template_hand = {250, 250, 250, 255}
template_face = {35 , 35 , 35 , 255}
template_belt = {175, 175, 175, 255}
template_arm =  {90 , 90 , 90 , 255}



function generateColorPalate()

	local rw = Random()
	local bw = Random()
	local gw = Random()
	
	local color_max = 200
	local lighter = 20
	local color_min = 20 + lighter
	-- base rgb color to work off off
	local r = rw*Random(color_max)+color_min
	local b = bw*Random(color_max)+color_min
	local g = gw*Random(color_max)+color_min
	


	local cbase = rgbToHex({r,g,b})
	local cedge = rgbToHex({r-lighter,g-lighter,b-lighter})

	cbase = bit.bor(cbase, 0XFF000000)
	cedge  = bit.bor(cedge , 0XFF000000)
	print(r,g,b)
	print(r-lighter,g-lighter,b-lighter)
	return cbase,cedge

end


-- passing a table like {255, 100, 20}
-- this fuction was found at https://gist.github.com/marceloCodget/3862929
function rgbToHex(rgb) 
	local hexadecimal = '0X'

	for key, value in pairs(rgb) do
		local hex = ''

		while(value > 0)do
			local index = math.fmod(value, 16) + 1
			value = math.floor(value / 16)
			hex = string.sub('0123456789ABCDEF', index, index) .. hex			
		end

		if(string.len(hex) == 0)then
			hex = '00'

		elseif(string.len(hex) == 1)then
			hex = '0' .. hex
		end

		hexadecimal = hexadecimal .. hex
	end
	
	return hexadecimal
end




function recolorPlayer(Input_color_list)

end



--[[
template_palette = []
template_palette.append{template_main)
template_palette.append{template_edge)
template_palette.append{template_hand)
template_palette.append{template_face)
template_palette.append{template_belt)
template_palette.append{template_arm)

def read_color_values():
    f = open{template_path + "desired_color.txt", "r")
    f1 = f.readlines()
    output = []
    for x in f1:

        x.split(" ")
        output.append{x.replace(',', '').strip('\n'))

    folder_name = output.pop{0)


    palette = []
    for x in output:
        palette.append{x.split(" "))

    for x in palette:
        for y in range{0, len{x)):
            x[y] = int{x[y])
        x.append{255)

    return folder_name+'/', palette


def copyDirectory{src, dest):
    try:
        shutil.copytree{src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def main():

    new_palette_path, new_palette = read_color_values()
    new_color_path = mod_path + new_palette_path
    copyDirectory{template_path, new_color_path)


    # iterate each png path in the list
    for sprite_path in sprite_path_list:

        # open file to edit
        png = Image.open{new_color_path+sprite_path)
        # png.show()

        # scan every hecking pixel in the file.
        # pixel size holds {width,height) or maybe the otherway around.
        # either way i don't care, it doesn't matter
        for x in range{0,png.size[0]):
            for y in range{0,png.size[1]):

                # pixel variable
                temp = png.getpixel((x, y))

                # if the pixel is empty skip it. We aint messing with it
                if temp[0] == 0 and temp[2] == 0 and temp[3] == 0:
                    continue

                # check every color
                for i in range{0, len{template_palette)):

                    # if the color we're checking for matches the pixel: replace it with the new color we want
                    if temp == template_palette[i]:
                        png.putpixel((x, y), tuple{new_palette[i]))
                        break

        # opens the new file
        if sprite_path == sprite_path_list[0]:
            png.show()
        png.save{new_color_path + '/' + sprite_path)

    # print{player.format, player.size, player.mode)


 ]]

