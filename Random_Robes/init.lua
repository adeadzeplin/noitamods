dofile( "mods/starting_loadouts/files/loadouts.lua" )
dofile( "data/scripts/perks/perk.lua" )

function OnPlayerSpawned( player_entity ) -- this runs when player entity has been created
	local init_check_flag = "start_loadouts_init_done"
	if GameHasFlagRun( init_check_flag ) then
		return
	end
	GameAddFlagRun( init_check_flag )

	-- ---
	local x,y = EntityGetTransform( player_entity )
	SetRandomSeed( x + 344, y - 523 )
	
	local loadout_rnd = Random( 1, #loadout_list )
	local loadout_choice = loadout_list[loadout_rnd]
	
	
	local cape = nil
	local player_arm = nil
	
	local loadout_cape_color = loadout_choice.cape_color
	local loadout_cape_color_edge = loadout_choice.cape_color_edge

	-- find the quick inventory, player cape and arm
	local player_child_entities = EntityGetAllChildren( player_entity )
	if ( player_child_entities ~= nil ) then
		for i,child_entity in ipairs( player_child_entities ) do
			local child_entity_name = EntityGetName( child_entity )
			
			if ( child_entity_name == "cape" ) then
				cape = child_entity
			end
			
			if ( child_entity_name == "arm_r" ) then
				player_arm = child_entity
			end
		end
	end
	
	-- set player sprite (since we change only one value, ComponentSetValue is fine)
	local player_sprite_component = EntityGetFirstComponent( player_entity, "SpriteComponent" )
	local player_sprite_file = "mods/starting_loadouts/files/" .. loadout_choice.folder .. "/player.xml"
	ComponentSetValue( player_sprite_component, "image_file", player_sprite_file )
	
	-- set player arm sprite
	local player_arm_sprite_component = EntityGetFirstComponent( player_arm, "SpriteComponent" )
	local player_arm_sprite_file = "mods/starting_loadouts/files/" .. loadout_choice.folder .. "/player_arm.xml"
	ComponentSetValue( player_arm_sprite_component, "image_file", player_arm_sprite_file )
	
	-- set player cape colour (since we're changing multiple variables, we'll use the edit_component() utility)
	edit_component( cape, "VerletPhysicsComponent", function(comp,vars) 
		vars.cloth_color = loadout_cape_color
		vars.cloth_color_edge = loadout_cape_color_edge
	end)
	
	-- set player ragdoll
	local player_ragdoll_component = EntityGetFirstComponent( player_entity, "DamageModelComponent" )
	local player_ragdoll_file = "mods/starting_loadouts/files/" .. loadout_choice.folder .. "/ragdoll/filenames.txt"
	ComponentSetValue( player_ragdoll_component, "ragdoll_filenames_file", player_ragdoll_file )


end

-- Stainable sprites should have a corresponding SPRITE_NAME_uv_src.png next to the sprite file, and the folder containing the sprite should be passed to ModDevGenerateSpriteUVsForDirectory().
-- For example for 'player.png' the corresponding UV source file is called 'player_uv_src.png'
-- ModDevGenerateSpriteUVsForDirectory() must be called in init.lua file scope. It doesn't do anything outside noita_dev.exe.
------------------------
------------------------
ModDevGenerateSpriteUVsForDirectory( "mods/Random_Robes/files/rng28221" )
ModDevGenerateSpriteUVsForDirectory( "mods/Random_Robes/files/rng32124" )
ModDevGenerateSpriteUVsForDirectory( "mods/Random_Robes/files/rng49481" )
ModDevGenerateSpriteUVsForDirectory( "mods/Random_Robes/files/rng61982" )
ModDevGenerateSpriteUVsForDirectory( "mods/Random_Robes/files/rng74956" )
