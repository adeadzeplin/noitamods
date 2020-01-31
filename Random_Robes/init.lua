--dofile( "mods/Random_robes/files/loadouts.lua" )
--dofile( "data/scripts/perks/perk.lua" )
dofile("mods/Random_Robes/Spritemanipulator.lua")
dofile("data/scripts/lib/utilities.lua")

function OnPlayerSpawned( player_entity ) -- this runs when player entity has been created

SetRandomSeed(0,1000)

print("AAAAAAAAAAAAAAAAAAAAAAAA")
local cloth , edge = generateColorPalate() 


local cape = EntityGetWithName("cape")
    edit_component(cape, "VerletPhysicsComponent", function(comp,vars)

        vars.cloth_color = cloth
        vars.cloth_color_edge = edge
    end)

end

 