import random
from datetime import datetime
random.seed(datetime.now())
import shutil

def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

skincolors = (
    (255, 251, 240, 255),  # -- really white
    (252, 218, 124, 255),  # -- generic white boi
    (217, 170, 41, 255),  # -- tan boi
    (168, 130, 25, 255),  # -- deep tan boi
    (87, 66, 9, 255),  # -- coco boi

)

beltcolors = (
    (220, 220, 220),# Light grey
    (82, 61, 11),   # brown belt
    (48, 36, 7),    # Dark Brown belt
    (0, 0, 0),      # Black Belt
    (209, 155, 61), # Beige Belt
    (161, 161, 161) # Grey belt
)

#template_colors
template_main = (240, 240, 240, 255)
template_edge = (200, 200, 200, 255)
template_hand = (250, 250, 250, 255)
template_face = (35 , 35 , 35 , 255)
template_belt = (175, 175, 175, 255)
template_arm =  (90 , 90 , 90 , 255)

# CHANGE THIS TO WHEREEVER YOUR MOD FOLDER IS LOCATED##################################
mod_top_path = '/Program Files (x86)/Steam/steamapps/common/Noita/mods/Random_Robesv2/'
#######################################################################################
mod_path = mod_top_path + 'files/'
template_path = mod_path + 'template/'
colortracker_path = mod_path + 'colortracker.txt'
generated_path = mod_top_path + "data/generated/"
UVspritemap_path = generated_path + 'sprite_uv_maps/'

template_palette = []
template_palette.append(template_main)
template_palette.append(template_edge)
template_palette.append(template_hand)
template_palette.append(template_face)
template_palette.append(template_belt)
template_palette.append(template_arm)


sprite_path_list = []
sprite_path_list.append('player.png')
sprite_path_list.append('player_arm.png')
sprite_path_list.append('ragdoll/head.png')
sprite_path_list.append('ragdoll/left_arm.png')
sprite_path_list.append('ragdoll/left_hand.png')
sprite_path_list.append('ragdoll/left_thigh.png')
sprite_path_list.append('ragdoll/right_arm.png')
sprite_path_list.append('ragdoll/right_hand.png')
sprite_path_list.append('ragdoll/right_thigh.png')
sprite_path_list.append('ragdoll/torso.png')

def gencol():
    red_w = random.random()
    blu_w = random.random()
    gre_w = random.random()

    color_max = 200
    lighter = 25
    color_min = 25 + lighter

    r = int(red_w * random.randrange(0,color_max) + color_min)
    b = int(blu_w * random.randrange(0,color_max) + color_min)
    g = int(gre_w * random.randrange(0,color_max) + color_min)

    return [r,g,b]
def generateColorPalate(RGBval):


    r = RGBval[0]
    g = RGBval[1]
    b = RGBval[2]
    lighter = 25

    a = 255




    main_c = (r,g,b,a)

    edge_c = (r-lighter,g-lighter,b-lighter,a)

    hand_c = skincolors[random.randrange(0, len(skincolors))]
    face_c = (35 , 35 , 35 , 255)
    belt_c = beltcolors[random.randrange(0, len(beltcolors))]# make a list of colors
    arm_c = edge_c

    pallete = []
    pallete.append(main_c)
    pallete.append(edge_c)
    pallete.append(hand_c)
    pallete.append(face_c)
    pallete.append(belt_c)
    pallete.append(arm_c)


    # doodoopath = 'rng'+ str(random.randint(1,100000))
    doodoopath = 'RGB'+ str(r) + '_' + str(g) + '_' + str(b)
    return doodoopath, pallete