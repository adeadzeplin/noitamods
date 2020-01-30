dofile("data/scripts/lib/utilities.lua")
dofile("mods/Red Cloak/png.lua")
dofile("mods/Red Cloak/deflatelua.lua")
function OnPlayerSpawned(player_entity)



	local pngImage = loadfile("mods/Red Cloak/deflatelua.lua")
	local player_arm = pngImage("mods/Red Cloak/data/enemies_gfx/player_arm.png")
	
	
	
end



