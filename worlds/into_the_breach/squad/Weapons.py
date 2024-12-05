weapon_table = {
    # Prime
    "Titan Fist": {
        "Class": "Prime",
        "Name": "Titan Fist",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Punch an adjacent tile, damaging and pushing it.",
        "Upgrade 1": "Dash (Up Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Prime_Punchmech",
        "Tags": {"Forced Move": 0, "Charge": 2, "High Damage": 3}
    },
    "Electric Whip": {
        "Class": "Prime",
        "Name": "Electric Whip",
        "Damage": 2,
        "Power": "(Up)",
        "Effect": "Chain damage through adjacent targets.",
        "Upgrade 1": "Building Chain (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Prime_Lightning",
        "Tags": {"Triple Kill": 0, "Piercing": 0, "Chain": 1}
    },
    "Burst Beam": {
        "Class": "Prime",
        "Name": "Burst Beam",
        "Damage": "3-1",
        "Power": "Free",
        "Effect": "Fire a piercing beam that decreases in damage the further it goes.",
        "Upgrade 1": "Ally Immune (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Prime_Lasermech",
        "Tags": {"Laser": 0, "Triple Kill": 0, "Piercing": 0, "High Damage": 3},
    },
    "Spartan Shield": {
        "Class": "Prime",
        "Name": "Spartan Shield",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Bash the enemy, flipping its attack direction. (Doesn't affect multi-directional attacks)",
        "Upgrade 1": "Gain Shield (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Prime_ShieldBash",
        "Tags": {"Shield": 1}
    },
    "Rock Launcher": {
        "Class": "Prime",
        "Name": "Rock Launcher",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Throw a rock at a chosen target. Rock remains as an obstacle.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Prime_Rockmech",
        "Tags": {"High Damage": 5}
    },
    "Sidewinder Fist": {
        "Class": "Prime",
        "Name": "Sidewinder Fist",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Punch an adjacent tile, damaging and pushing it to the left.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Prime_RightHook",
        "Tags": {"Forced Move": 0, "High Damage": 4}
    },
    "Rocket Fist": {
        "Class": "Prime",
        "Name": "Rocket Fist",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Punch an adjacent tile. Upgrades to launch as a projectile.\n(Has knockback)",
        "Upgrade 1": "Rocket (Up)",
        "Upgrade 2": "+2 Damage (Up Up)",
        "Debug Name": "Prime_RocketPunch",
        "Tags": {"Forced Move": 0, "High Damage": 2}
    },
    "Vice Fist": {
        "Class": "Prime",
        "Name": "Vice Fist",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Grab a unit and toss it behind you.\n(If a unit is thrown onto ACID, ACID will apply first, then damage)",
        "Upgrade 1": "Ally Immune (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Prime_Shift",
        "Tags": {"Forced Move": 0}
    },
    "Flame Thrower": {
        "Class": "Prime",
        "Name": "Flame Thrower",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Push the target tile and light tiles on Fire. Damage units already on Fire. (Starts with 1 range.)",
        "Upgrade 1": "+1 Range (Up)",
        "Upgrade 2": "+1 Range (Up Up Up)",
        "Debug Name": "Prime_Flamethrower",
        "Tags": {"Forced Move": 0, "Fire": 0, "Piercing": 0, "Triple Fire": 4, "Triple Kill": 4}
    },
    "Explosive Vents": {
        "Class": "Prime",
        "Name": "Explosive Vents",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Blast (and push) all adjacent tiles.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Prime_Areablast",
        "Tags": {"Forced Move": 0, "Quadruple Move": 0}
    },
    "Prime Spear": {
        "Class": "Prime",
        "Name": "Prime Spear",
        "Damage": 2,
        "Power": "(Up)",
        "Effect": "Stab multiple tiles and push the furthest hit tile. (Starts with 2-tile range.)",
        "Upgrade 1": "A.C.I.D. Tip (Up)",
        "Upgrade 2": "Adds A.C.I.D. to the furthest hit enemy.\n+1 Range (Up Up)",
        "Debug Name": "Prime_Spear",
        "Tags": {"Forced Move": 0, "Triple Kill": 0, "Piercing": 0, "Acid": 1}
    },
    "Hydraulic Legs": {
        "Class": "Prime",
        "Name": "Hydraulic Legs",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Leap to a tile, damaging self and adjacent tiles (with push).",
        "Upgrade 1": "+1 Damage Each (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Prime_Leap",
        "Tags": {"Charge": 0, "Forced Move": 0, "Quadruple Move": 0}
    },
    "Vortex Fist": {
        "Class": "Prime",
        "Name": "Vortex Fist",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Damage and push all adjacent tiles to the left.",
        "Upgrade 1": "-1 Self Damage (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Prime_SpinFist",
        "Tags": {"Forced Move": 0, "Quadruple Move": 0}
    },
    "Titanite Blade": {
        "Class": "Prime",
        "Name": "Titanite Blade",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Swing a massive sword to damage and push 3 tiles.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Prime_Sword",
        "Tags": {"Triple Push": 0, "High Damage": 3}
    },
    "Mercury Fist": {
        "Class": "Prime",
        "Name": "Mercury Fist",
        "Damage": 4,
        "Power": "Free",
        "Effect": "Smash the ground, dealing huge damage and pushing adjacent tiles.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+1 Damage (Up)",
        "Debug Name": "Prime_Smash",
        "Tags": {"High Damage": 0, "Triple Push": 0}
    },
    "Thermal Discharger": {
        "Class": "Prime",
        "Name": "Thermal Discharger",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Damage up to two or more tiles in a line and push tiles to the left and right of damaged tiles. (Starts with 2-tile range.)",
        "Upgrade 1": "+2 Range (Up Up)",
        "Upgrade 2": "Add Fire (Up Up Up)",
        "Debug Name": "Prime_Flamespreader",
        "Tags": {"Forced Move": 0, "Triple Push": 0, "Piercing": 0, "Fire": 3, "Triple Fire": 5}
    },
    "The Big One": {
        "Class": "Prime",
        "Name": "The Big One",
        "Damage": "3-1",
        "Power": "2 self",
        "Effect": "Fires a huge missile that damages in a large cone shape.\n(Deals 3 damage to the target, 2 to 3 tiles behind it, and 1 to 5 tiles further behind.\nHas knockback.)",
        "Upgrade 1": "-1 Self Damage (Up)",
        "Upgrade 2": "-1 Self Damage (Up Up)",
        "Debug Name": "Prime_WayTooBig",
        "Tags": {"Piercing": 0}
    },
    "Prism Laser": {
        "Class": "Prime",
        "Name": "Prism Laser",
        "Damage": "1-3",
        "Power": "Free",
        "Effect": "Laser that increases in damage for each unit that it hits.",
        "Upgrade 1": "Ally Immune (Up)",
        "Upgrade 2": "No Max Damage (Up Up)",
        "Debug Name": "Prime_PrismLaser",
        "Tags": {"Laser": 0, "Triple Kill": 0, "Piercing": 0, "High Damage": 2}
    },
    "Hydraulic Lifter": {
        "Class": "Prime",
        "Name": "Hydraulic Lifter",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Throw an adjacent unit and damage it. (Starts with 2-tile range.)",
        "Upgrade 1": "+2 Range (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Prime_TC_Punt",
        "Tags": {"Forced Move": 0}
    },
    "Refractor Laser": {
        "Class": "Prime",
        "Name": "Refractor Laser",
        "Damage": "1-3",
        "Power": "(Up)",
        "Effect": "A laser that can bend, dealing more damage to nearby tiles.",
        "Upgrade 1": "Ally Immune (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Prime_TC_BendBeam",
        "Tags": {"Laser": 0, "Chain": 0, "Triple Kill": 0, "Piercing": 0, "High Damage": 3}
    },
    "Spring-Loaded Legs": {
        "Class": "Prime",
        "Name": "Spring-Loaded Legs",
        "Damage": 2,
        "Power": "(Up)",
        "Effect": "Leap and attack a tile (next to your landing point), dealing damage and pushing it.",
        "Upgrade 1": "+2 Range (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Prime_TC_Feint",
        "Tags": {"Forced Move": 0, "Charge": 1, "High Damage": 3}
    },
    "Fissure Fist": {
        "Class": "Prime",
        "Name": "Fissure Fist",
        "Damage": 3,
        "Power": "Free",
        "Effect": "Heavily damage a tile, cracking tiles behind the target on kill.\nSingle-use.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Use (Up)",
        "Debug Name": "Prime_KO_Crack",
        "Tags": {"High Damage": 2}
    },

    # Brute
    "Taurus Cannon": {
        "Class": "Brute",
        "Name": "Taurus Cannon",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fires a powerful projectile that damages and pushes its target.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Brute_Tankmech",
        "Tags": {"Forced Move": 0}
    },
    "Aerial Bombs": {
        "Class": "Brute",
        "Name": "Aerial Bombs",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fly over a target, dropping an explosive smoke bomb.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Range (Up Up)",
        "Debug Name": "Brute_Jetmech",
        "Tags": {"Smoke": 0}
    },
    "Janus Cannon": {
        "Class": "Brute",
        "Name": "Janus Cannon",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fire two projectiles in opposite directions (with push).",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Brute_Mirrorshot",
        "Tags": {"Forced Move": 0, "Triple Kill": 0}
    },
    "Phase Cannon": {
        "Class": "Brute",
        "Name": "Phase Cannon",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Shoot a projectile that phases through Grid Buildings.",
        "Upgrade 1": "Phase Shield (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Brute_PhaseShot",
        "Tags": {"Forced Move": 0, "Shield": 1}
    },
    "Grappling Hook": {
        "Class": "Brute",
        "Name": "Grappling Hook",
        "Power": "Free",
        "Effect": "Use a grapple to pull Mech towards immovable objects, or units to the Mech.",
        "Upgrade 1": "Shield Ally (Up)",
        "Debug Name": "Brute_Grapple",
        "Tags": {"Forced Move": 0, "Shield": 1}
    },
    "Def. Shrapnel": {
        "Class": "Brute",
        "Name": "Def. Shrapnel",
        "Power": "Free",
        "Effect": "Fire a non-damaging projectile that pushes tiles around the target.",
        "Debug Name": "Brute_Shrapnel",
        "Tags": {"Quadruple Move": 0, "Deadly Pull": 0, "Forced Move": 0}
    },
    "Rail Cannon": {
        "Class": "Brute",
        "Name": "Rail Cannon",
        "Damage": "0 - 2",
        "Power": "Free",
        "Effect": "Projectile that does more damage to targets that are further away.",
        "Upgrade 1": "+1 Max Damage (Up)",
        "Upgrade 2": "+2 Max Damage (Up Up)",
        "Debug Name": "Brute_Sniper",
        "Tags": {"Forced Move": 0, "Piercing": 0, "High Damage": 2}
    },
    "Shock Cannon": {
        "Class": "Brute",
        "Name": "Shock Cannon",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fire a projectile that hits 2 tiles, pushing them in opposite directions.",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Brute_Shockblast",
        "Tags": {"Forced Move": 0, "Triple Kill": 0, "Deadly Pull": 0}
    },
    "Ramming Engines": {
        "Class": "Brute",
        "Name": "Ramming Engines",
        "Damage": 2,
        "Power": "1 self",
        "Effect": "Fly in a line and slam into the target, pushing it and hurting yourself.\n(The self-damage is also considered as an attack to terrain)",
        "Upgrade 1": "+1 Damage Each (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Brute_Beetle",
        "Tags": {"Charge": 0, "High Damage": 4, "Forced Move": 0}
    },
    "Unstable Cannon": {
        "Class": "Brute",
        "Name": "Unstable Cannon",
        "Damage": 2,
        "Power": "1 self",
        "Effect": "Powerful projectile that causes damage to the shooter as well as the target (and push each).",
        "Upgrade 1": "+1 Damage Each (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Brute_Unstable",
        "Tags": {"Forced Move": 0, "Triple Kill": 0, "High Damage": 4}
    },
    "Heavy Rocket": {
        "Class": "Brute",
        "Name": "Heavy Rocket",
        "Damage": 3,
        "Power": "Free",
        "Effect": "Fire a projectile that heavily damages a target and pushes adjacent tiles.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+2 Damage (Up Up)",
        "Debug Name": "Brute_Heavyrocket",
        "Tags": {"Triple Move": 0, "High Damage": 2}
    },
    "Splitshot": {
        "Class": "Brute",
        "Name": "Splitshot",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Shoot a projectile that damages and pushes the targeted tile and the tiles to its left and right.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Brute_Splitshot",
        "Tags": {"Triple Move": 0, "Forced Move": 0}
    },
    "Astra Bombs": {
        "Class": "Brute",
        "Name": "Astra Bombs",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Leap over any distance dropping a bomb on each tile you pass.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Brute_Bombrun",
        "Tags": {"Triple Kill": 0}
    },
    "Hermes Engines": {
        "Class": "Brute",
        "Name": "Hermes Engines",
        "Power": "Free",
        "Effect": "Dash in a line, pushing adjacent tiles away.",
        "Debug Name": "Brute_Sonic",
        "Tags": {"Forced Move": 0, "Quadruple Move": 0, "Charge": 0}
    },
    "Reverse Thrusters": {
        "Class": "Brute",
        "Name": "Reverse Thrusters",
        "Damage": "1-2",
        "Power": "1 self",
        "Effect": "Smoke and deal damage to a tile while dashing away. (The further you dash, the more damage it deals. Starts with 2-tile range.)",
        "Upgrade 1": "+1 Range (Up)",
        "Upgrade 2": "+1 Range (Up Up Up)",
        "Debug Name": "Brute_KickBack",
        "Tags": {"Smoke": 0, "High Damage": 4}
    },
    "Fracturing Shells": {
        "Class": "Brute",
        "Name": "Fracturing Shells",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fires a projectile that explodes on contact, damaging and pushing adjacent tiles.",
        "Upgrade 1": "+2 Damage (Up Up Up)",
        "Upgrade 2": "Buildings Immune (Up)",
        "Debug Name": "Brute_Fracture",
        "Tags": {"Quadruple Move": 0, "Forced Move": 0}
    },
    "AP Cannon": {
        "Class": "Brute",
        "Name": "AP Cannon",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Fire a pushing projectile that pierces the first target and damages the second.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Brute_PierceShot",
        "Tags": {"Forced Move": 0, "Piercing": 0, "High Damage": 4, "Triple Kill": 0}
    },
    "Guided Missile": {
        "Class": "Brute",
        "Name": "Guided Missile",
        "Damage": 2,
        "Power": "(Up)",
        "Effect": "A projectile that can turn once before hitting its target.",
        "Upgrade 1": "+1 Damage (Up Up Up)",
        "Upgrade 2": "Smoke Line (Up)",
        "Debug Name": "Brute_TC_GuidedMissile",
        "Tags": {"Forced Move": 0, "Smoke": 1}
    },
    "Ricochet Rocket": {
        "Class": "Brute",
        "Name": "Ricochet Rocket",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Bounce a projectile off one target to hit another (and push each).",
        "Upgrade 1": "+1 Damage (Up Up Up)",
        "Upgrade 2": "Ally Immune (Up)",
        "Debug Name": "Brute_TC_Ricochet",
        "Tags": {"Forced Move": 0, "Triple Kill": 0}
    },
    "Quick-Fire Rockets": {
        "Class": "Brute",
        "Name": "Quick-Fire Rockets",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fire two projectiles in different directions.",
        "Upgrade 1": "Add Push (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Brute_TC_DoubleShot",
        "Tags": {"Forced Move": 1, "Triple Kill": 1}
    },
    "EM Railgun": {
        "Class": "Brute",
        "Name": "EM Railgun",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Pierce through any killed Enemies.\nSingle-use.",
        "Upgrade 1": "+2 Damage (Up)",
        "Upgrade 2": "Building Immune (Up)",
        "Debug Name": "Brute_KO_Combo",
        "Tags": {"Triple Kill": 0, "Piercing": 0, "High Damage": 1}
    },

    # Ranged
    "Artemis Artillery": {
        "Class": "Ranged",
        "Name": "Artemis Artillery",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Powerful artillery strike, damaging a single tile and pushing adjacent tiles.",
        "Upgrade 1": "Buildings Immune (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Ranged_Artillerymech",
        "Tags": {"Forced Move": 0, "Quadruple Move": 0, "Deadly Pull": 0}
    },
    "Rock Accelerator": {
        "Class": "Ranged",
        "Name": "Rock Accelerator",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Launch a rock at a tile, pushing tiles to the left and right.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Debug Name": "Ranged_Rockthrow",
        "Tags": {"Forced Move": 0, "Triple Kill": 0}
    },
    "Cluster Artillery": {
        "Class": "Ranged",
        "Name": "Cluster Artillery",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Protect a tile by damaging and pushing adjacent tiles.",
        "Upgrade 1": "Buildings Immune (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Ranged_Defensestrike",
        "Tags": {"Forced Move": 0, "Quadruple Move": 0, "Deadly Pull": 0}
    },
    "Rocket Artillery": {
        "Class": "Ranged",
        "Name": "Rocket Artillery",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Fires a pushing artillery and creates Smoke behind the shooter.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Ranged_Rocket",
        "Tags": {"Smoke": 0, "Forced Move": 0, "High Damage": 4}
    },
    "Vulcan Artillery": {
        "Class": "Ranged",
        "Name": "Vulcan Artillery",
        "Damage": 0,
        "Power": "Free",
        "Effect": "Light the target on Fire and push adjacent tiles.",
        "Upgrade 1": "Backburn (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Ranged_Ignite",
        "Tags": {"Fire": 0, "Triple Move": 0, "Forced Move": 0, "Deadly Pull": 0,
                 "Triple Fire": 1  # Not exactly true, but the push can move units to fire tiles
                 }
    },
    "Micro-Artillery": {
        "Class": "Ranged",
        "Name": "Micro-Artillery",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Artillery with potential to launch multiple small projectiles (with push).",
        "Upgrade 1": "+2 Tiles (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Ranged_ScatterShot",
        "Tags": {"Forced Move": 0, "Triple Push": 1}
    },
    "Aegon Mortar": {
        "Class": "Ranged",
        "Name": "Aegon Mortar",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Deals damage to two tiles, pushing one forwards and one backwards.",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Ranged_BackShot",
        "Tags": {"Forced Move": 0, "Triple Kill": 0}
    },
    "Cryo-Launcher": {
        "Class": "Ranged",
        "Name": "Cryo-Launcher",
        "Power": "(Up)",
        "Effect": "Freeze yourself and the target.",
        "Debug Name": "Ranged_Ice",
        "Tags": {"Freeze": 0}
    },
    "Smoke Mortar": {
        "Class": "Ranged",
        "Name": "Smoke Mortar",
        "Power": "Free",
        "Effect": "Artillery shot that applies Smoke and pushes two adjacent tiles.",
        "Debug Name": "Ranged_SmokeBlast",
        "Tags": {"Smoke": 0, "Forced Move": 0, "Triple Kill": 0}
    },
    "Burning Mortar": {
        "Class": "Ranged",
        "Name": "Burning Mortar",
        "Damage": "0",
        "Power": "Free",
        "Effect": "Artillery attack that sets 5 tiles on Fire.",
        "Upgrade 1": "No Self Damage (Up Up)",
        "Debug Name": "Ranged_Fireball",
        "Tags": {"Fire": 0, "Triple Fire": 2}
    },
    "Raining Death": {
        "Class": "Ranged",
        "Name": "Raining Death",
        "Damage": 2,
        "Power": "1 self",
        "Effect": "A dangerous projectile that damages everything it passes.",
        "Upgrade 1": "Buildings Immune (Up)",
        "Upgrade 2": "+1 Damage Each (Up Up)",
        "Debug Name": "Ranged_RainingVolley",
        "Tags": {"Triple Kill": 0}
    },
    "Heavy Artillery": {
        "Class": "Ranged",
        "Name": "Heavy Artillery",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Powerful attack that damages a large area.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+1 Damage (Up Up)",
        "Debug Name": "Ranged_Wide",
        "Tags": {"Triple Kill": 0}
    },
    "Gemini Missiles": {
        "Class": "Ranged",
        "Name": "Gemini Missiles",
        "Damage": 3,
        "Power": "(Up)",
        "Effect": "Launch two missiles, damaging and pushing two targets.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "+1 Damage (Up)",
        "Debug Name": "Ranged_Dual",
        "Tags": {"Triple Kill": 0, "Piercing": 0, "High Damage": 1}
    },
    "Tri-Rocket": {
        "Class": "Ranged",
        "Name": "Tri-Rocket",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Damage and push 3 tiles in a line. (Can aim close tile.)",
        "Upgrade 1": "+1 Damage (Up Up Up)",
        "Upgrade 2": "Building Immune (Up)",
        "Debug Name": "Ranged_Crack",
        "Tags": {"Triple Push": 0, "Forced Move": 0, "Piercing": 0}
    },
    "Bomb Dispenser": {
        "Class": "Ranged",
        "Name": "Bomb Dispenser",
        "Power": "Free",
        "Effect": "Launch a Walking Bomb. Unused bombs dismantle after the enemy turn.",
        "Upgrade 1": "2 Bombs (Up Up Up)",
        "Debug Name": "Ranged_DeployBomb",
        "Tags": {"Many Summons": 0, "Triple Kill": 0}
    },
    "Arachnoid Injector": {
        "Class": "Ranged",
        "Name": "Arachnoid Injector",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Damage target, creating a friendly robot spider on kill.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "Acidic (Up)",
        "Debug Name": "Ranged_Arachnoid",
        "Tags": {"Hoard Summons": 0, "Forced Move": 0, "Acid": 1}
    },
    "Smoldering Shells": {
        "Class": "Ranged",
        "Name": "Smoldering Shells",
        "Damage": 1,
        "Power": "(Up)",
        "Effect": "Damage and apply Fire to a tile while adding Smoke to adjacent tiles (vertical).",
        "Upgrade 1": "More Smoke (Up Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Ranged_SmokeFire",
        "Tags": {"Fire": 0, "Smoke": 0}
    },
    "Rebounding Volley": {
        "Class": "Ranged",
        "Name": "Rebounding Volley",
        "Damage": 2,
        "Power": "(Up)",
        "Effect": "Artillery attack that can bounce to an additional target. (Pull the first and push the second.)",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "Building Immune (Up)",
        "Debug Name": "Ranged_TC_BounceShot",
        "Tags": {"Forced Move": 0, "Triple Kill": 0, "Piercing": 0}
    },
    "Quick-Fire Artillery": {
        "Class": "Ranged",
        "Name": "Quick-Fire Artillery",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Fire two artillery shots in different directions.",
        "Upgrade 1": "Ally Immune (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "Ranged_TC_DoubleArt",
        "Tags": {"Forced Move": 0, "Triple Kill": 0}
    },
    "Cascading Resonator": {
        "Class": "Ranged",
        "Name": "Cascading Resonator",
        "Damage": 2,
        "Power": "1 self",
        "Effect": "Killed enemies explode; victims of splash damage also explode on death.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Upgrade 2": "+Building Immune (Up)",
        "Debug Name": "Ranged_KO_Combo",
        "Tags": {"Triple Kill": 0, "Piercing": 0}
    },

    # Science
    "Attraction Pulse": {
        "Class": "Science",
        "Name": "Attraction Pulse",
        "Power": "Free",
        "Effect": "Fires a projectile, pulling target towards you 1 tile.",
        "Debug Name": "Science_Pullmech",
        "Tags": {"Forced Move": 0, "Deadly Pull": 0}
    },
    "Grav Well": {
        "Class": "Science",
        "Name": "Grav Well",
        "Power": "Free",
        "Effect": "Artillery weapon that pulls its target towards you.",
        "Debug Name": "Science_Gravwell",
        "Tags": {"Forced Move": 0}
    },
    "Repulse": {
        "Class": "Science",
        "Name": "Repulse",
        "Power": "Free",
        "Effect": "Push all adjacent tiles.",
        "Upgrade 1": "Shield Self (Up)",
        "Upgrade 2": "Shield Friendly (Up Up)",
        "Debug Name": "Science_Repulse",
        "Tags": {"Triple Push": 0, "Shield": 1, "Forced Move": 0}
    },
    "Teleporter": {
        "Class": "Science",
        "Name": "Teleporter",
        "Power": "Free",
        "Effect": "Swap places with a nearby tile. (Note: if you are webbed and swap places with another unit, the other unit will become webbed.)",
        "Upgrade 1": "+1 Range (Up)",
        "Upgrade 2": "+2 Range (Up Up)",
        "Debug Name": "Science_Swap",
        "Tags": {"Forced Move": 0, "Teleport": 3, }
    },
    "A.C.I.D. Projector": {
        "Class": "Science",
        "Name": "A.C.I.D. Projector",
        "Power": "Free",
        "Effect": "Fire a projectile that applies A.C.I.D. and pushes.",
        "Debug Name": "Science_AcidShot",
        "Tags": {"Acid": 0, "Forced Move": 0}
    },
    "Confuse Shot": {
        "Class": "Science",
        "Name": "Confuse Shot",
        "Power": "Free",
        "Effect": "Fire a projectile that flips a target's attack direction.",
        "Debug Name": "Science_Confuse",
        "Tags": {}
    },
    "Smoke Pellets": {
        "Class": "Science",
        "Name": "Smoke Pellets",
        "Power": "Free",
        "Effect": "Surround yourself with Smoke to defend against nearby enemies.\nSingle-use.",
        "Upgrade 1": "Ally Immune (Up)",
        "Upgrade 2": "+1 Use (Up)",
        "Debug Name": "Science_SmokeDefense",
        "Tags": {"Smoke": 1}
    },
    "Shield Projector": {
        "Class": "Science",
        "Name": "Shield Projector",
        "Power": "Free",
        "Effect": "Shield tiles from damage.\n2 uses per battle.",
        "Upgrade 1": "+1 Use (Up Up)",
        "Upgrade 2": "+3 Area (Up Up)",
        "Debug Name": "Science_Shield",
        "Tags": {"Shield": 0}
    },
    "Fire Beam": {
        "Class": "Science",
        "Name": "Fire Beam",
        "Power": "Free",
        "Effect": "Fire a beam that applies Fire in a line.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Debug Name": "Science_FireBeam",
        "Tags": {"Laser": 0, "Fire": 0, "Triple Fire": 0}
    },
    "Frost Beam": {
        "Class": "Science",
        "Name": "Frost Beam",
        "Power": "(Up)",
        "Effect": "Fire a beam that Freezes everything in a line.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up Up)",
        "Debug Name": "Science_FreezeBeam",
        "Tags": {"Laser": 0, "Freeze": 2}
    },
    "Shield Array": {
        "Class": "Science",
        "Name": "Shield Array",
        "Power": "Free",
        "Effect": "Apply a Shield on nearby tiles.\nSingle-use.",
        "Upgrade 1": "+1 Size (Up)",
        "Upgrade 2": "+1 Use (Up)",
        "Debug Name": "Science_LocalShield",
        "Tags": {"Shield": 0, "Chain": 1}
    },
    "Push Beam": {
        "Class": "Science",
        "Name": "Push Beam",
        "Power": "Free",
        "Effect": "Pushes all units in a line.\nSingle-use.",
        "Upgrade 1": "Unlimited Use (Up)",
        "Debug Name": "Science_PushBeam",
        "Tags": {"Triple Push": 0, "Piercing": 0, "Forced Move": 1}
    },
    "Firestorm Generator": {
        "Class": "Science",
        "Name": "Firestorm Generator",
        "Power": "Free",
        "Effect": "Flaming artillery that drops fire on the way to its target (and push the target). (Starts with 2-tile range.)",
        "Upgrade 1": "+1 Range (Up)",
        "Upgrade 2": "+2 Range (Up Up)",
        "Debug Name": "Science_RainingFire",
        "Tags": {"Forced Move": 0, "Fire": 0, "Triple Fire": 1}
    },
    "Area Shift": {
        "Class": "Science",
        "Name": "Area Shift",
        "Power": "Free",
        "Effect": "Push self and all adjacent tiles.",
        "Upgrade 1": "Shield Self (Up)",
        "Upgrade 2": "Shield Ally (Up Up)",
        "Debug Name": "Science_MassShift",
        "Tags": {"Forced Move": 0, "Triple push": 0, "Shield": 1, "Deadly Pull": 1}
    },
    "Explosive Warp": {
        "Class": "Science",
        "Name": "Explosive Warp",
        "Power": "Free",
        "Effect": "Teleport to target and push nearby tiles away.",
        "Upgrade 1": "+2 Range (Up)",
        "Upgrade 2": "+2 Range (Up)",
        "Debug Name": "Science_TelePush",
        "Tags": {"Forced Move": 0, "Triple Push": 0, "Charge": 1}
    },
    "Shield Placer": {
        "Class": "Science",
        "Name": "Shield Placer",
        "Power": "Free",
        "Effect": "Shield target and push adjacent tiles away.",
        "Upgrade 1": "+1 Range (Up)",
        "Upgrade 2": "+1 Range (Up Up)",
        "Debug Name": "Science_Placer",
        "Tags": {"Shield": 0, "Forced Move": 0, "Triple Push": 0, "Deadly Pull": 0}
    },
    "Enrage Shot": {
        "Class": "Science",
        "Name": "Enrage Shot",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Force targeted unit to attack adjacent tile.",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up)",
        "Debug Name": "Science_TC_Enrage",
        "Tags": {}
    },
    "Control Shot": {
        "Class": "Science",
        "Name": "Control Shot",
        "Power": "Free",
        "Effect": "Temporarily control a unit, moving it a short distance (2 tiles).",
        "Upgrade 1": "+1 Move (Up)",
        "Upgrade 2": "+1 Move (Up Up)",
        "Debug Name": "Science_TC_Control",
        "Tags": {"Forced Move": 0}
    },
    "Force Swap": {
        "Class": "Science",
        "Name": "Force Swap",
        "Damage": 0,
        "Power": "(Up)",
        "Effect": "Force a nearby unit to swap places with any other unit.",
        "Upgrade 1": "Heal Ally (Up)",
        "Upgrade 2": "Hurt Enemy (Up Up)",
        "Debug Name": "Science_TC_SwapOther",
        "Tags": {"Forced Move": 0, "Heal": 1}
    },
    "Seismic Capacitor": {
        "Class": "Science",
        "Name": "Seismic Capacitor",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Damage and flip target. If target is killed, crack adjacent tiles.",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up Up Up)",
        "Debug Name": "Science_KO_Crack",
        "Tags": {"Crack": 0}
    },
    "Gravity Mirror": {
        "Class": "Science",
        "Name": "Gravity Mirror",
        "Power": "Free",
        "Effect": "Fire a gravity well in 4 directions, pushing or pulling every unit. (Only available through debug)",
        "Debug Name": "Science_TC_Gravity",
        "Tags": {"Forced Move": 0, "Triple Push": 0, "Deadly Pull": 0}
    },

    # Any class
    "Boosters": {
        "Class": "Any",
        "Name": "Boosters",
        "Power": "Free",
        "Effect": "Jump forward and push adjacent tiles away.",
        "Debug Name": "Support_Boosters",
        "Tags": {"Forced Move": 0, "Triple Push": 0, "Charge": 0}
    },
    "Smoke Bombs": {
        "Class": "Any",
        "Name": "Smoke Bombs",
        "Power": "Free",
        "Effect": "Fly over the targets while dropping Smoke.",
        "Upgrade 1": "+1 Range (Up)",
        "Upgrade 2": "+1 Range (Up)",
        "Debug Name": "Support_Smoke",
        "Tags": {"Smoke": 0}
    },
    "Heat Converter": {
        "Class": "Any",
        "Name": "Heat Converter",
        "Power": "Free",
        "Effect": "Freeze the tile in front but light the tile behind on Fire in the process.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Debug Name": "Support_Refrigerate",
        "Tags": {}
    },
    "Self-Destruct": {
        "Class": "Any",
        "Name": "Self-Destruct",
        "Damage": "Kill",
        "Power": "Free",
        "Effect": "Mech explodes, killing self and anything adjacent to Mech.\nSingle-use.",
        "Debug Name": "Support_Destruct",
        "Tags": {"Triple Kill": 0}
    },
    "Targeted Strike": {
        "Class": "Any",
        "Name": "Targeted Strike",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Call in an air strike on a single tile anywhere on the map.\nSingle-use.",
        "Debug Name": "Support_Force",
        "Tags": {"Forced Move": 0, "Deadly Pull": 0}
    },
    "Smoke Drop": {
        "Class": "Any",
        "Name": "Smoke Drop",
        "Power": "Free",
        "Effect": "Drops Smoke on 5 tiles anywhere on the map.\nSingle-use.",
        "Debug Name": "Support_SmokeDrop",
        "Tags": {"Smoke": 0}
    },
    "Repair Drop": {
        "Class": "Any",
        "Name": "Repair Drop",
        "Power": "Free",
        "Effect": "Heal all player units (including disabled Mechs).\nSingle-use.",
        "Debug Name": "Support_Repair",
        "Tags": {"Heal": 0}
    },
    "Missile Barrage": {
        "Class": "Any",
        "Name": "Missile Barrage",
        "Damage": 1,
        "Power": "(Up)",
        "Effect": "Fires a missile barrage that hits every enemy on the map.\nSingle-use.",
        "Upgrade 1": "+1 Damage (Up Up)",
        "Debug Name": "Support_Missiles",
        "Tags": {"Triple Kill": 0}
    },
    "Wind Torrent": {
        "Class": "Any",
        "Name": "Wind Torrent",
        "Power": "Free",
        "Effect": "Push all units in a single direction.\nSingle-use.",
        "Upgrade 1": "Unlimited Uses (Up)",
        "Debug Name": "Support_Wind",
        "Tags": {"Triple Push": 0, "Chain": 0, "Deadly Pull": 0, "Piercing": 0, "Forced Move": 1, }
    },
    "Ice Generator": {
        "Class": "Any",
        "Name": "Ice Generator",
        "Power": "(Up)",
        "Effect": "Freeze yourself and nearby tiles.\nSingle-use.",
        "Upgrade 1": "+1 Size (Up)",
        "Upgrade 2": "+1 Size (Up Up)",
        "Debug Name": "Support_Blizzard",
        "Tags": {"Chain": 1, "Freeze": 3, }
    },
    "Mass Confusion": {
        "Class": "Any",
        "Name": "Mass Confusion",
        "Power": "Free",
        "Effect": "Cause nearby enemies to flip their attack direction.\nSingle-use.",
        "Upgrade 1": "+1 Size (Up)",
        "Upgrade 2": "+1 Use (Up)",
        "Debug Name": "Support_Confuse",
        "Tags": {"Chain": 1}
    },
    "Grid Repulse": {
        "Class": "Any",
        "Name": "Grid Repulse",
        "Power": "Free",
        "Effect": "Overload the grid, causing a building to push away nearby units.",
        "Upgrade 1": "Add Shield (Up)",
        "Debug Name": "Support_GridDefense",
        "Tags": {"Forced Move": 0, "Deadly Pull": 0, "Piercing": 0, "Shield": 1, }
    },
    "Grid Assault": {
        "Class": "Any",
        "Name": "Grid Assault",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Overload the grid causing a building to damage and push an adjacent tile.",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up)",
        "Debug Name": "Support_TC_GridAtk",
        "Tags": {"Forced Move": 0, "Deadly Pull": 0}
    },
    "Bombing Run": {
        "Class": "Any",
        "Name": "Bombing Run",
        "Damage": 2,
        "Power": "Free",
        "Effect": "Call in bombers, dealing damage to every tile in a row or column.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Upgrade 2": "Building Immune (Up)",
        "Debug Name": "Support_TC_Bombline",
        "Tags": {"Triple Kill": 0}
    },
    "Grid Charger": {
        "Class": "Any",
        "Name": "Grid Charger",
        "Damage": 1,
        "Power": "(Up)",
        "Effect": "Killing an enemy will charge the Power Grid 1 point.",
        "Debug Name": "Support_KO_GridCharger",
        "Tags": {}
    },
    "Flood Drill": {
        "Class": "Any",
        "Name": "Flood Drill",
        "Power": "(Up)",
        "Effect": "Convert any liquid Tile to a Hole, spreading the liquid to adjacent tiles.\nSingle-use.",
        "Upgrade 1": "+1 Use (Up)",
        "Debug Name": "Support_Waterdrill",
        "Tags": {}
    },
    "Light Tank": {
        "Class": "Any",
        "Name": "Light Tank",
        "Power": "(Up Up)",
        "Effect": "Deploy a small tank to help in combat.\nSingle-use.",
        "Health": 1,
        "Move": 3,
        "Upgrade 1": "+2 Health (Up)",
        "Upgrade 2": "+2 Damage (Up Up Up)",
        "Debug Name": "DeploySkill_Tank",
        "Tags": {"Summon": 0}
    },
    "Shield-Tank": {
        "Class": "Any",
        "Name": "Shield-Tank",
        "Power": "(Up Up)",
        "Effect": "Deploy a Shield-Tank that can give Shields to allies.\nSingle-use.",
        "Health": 1,
        "Move": 3,
        "Upgrade 1": "+2 Health (Up)",
        "Upgrade 2": "Projectile (Up)",
        "Debug Name": "DeploySkill_ShieldTank",
        "Tags": {"Summon": 0, "Shield": 0}
    },
    "A.C.I.D. Tank": {
        "Class": "Any",
        "Name": "A.C.I.D. Tank",
        "Power": "(Up Up)",
        "Effect": "Deploy a Tank that can apply A.C.I.D. to targets.\nSingle-use.",
        "Health": 1,
        "Move": 3,
        "Upgrade 1": "+2 Health (Up)",
        "Upgrade 2": "Push (Up)",
        "Debug Name": "DeploySkill_AcidTank",
        "Tags": {"Summon": 0, "ACID": 0, "Forced Move": 1}
    },
    "Pull-Tank": {
        "Class": "Any",
        "Name": "Pull-Tank",
        "Power": "(Up Up)",
        "Effect": "Deploy a Pull-Tank that can pull targets with a projectile.\nSingle-use.",
        "Health": 1,
        "Move": 3,
        "Upgrade 1": "+2 Health (Up)",
        "Upgrade 2": "Flying (Up)",
        "Debug Name": "DeploySkill_PullTank",
        "Tags": {"Deadly Pull": 0, "Forced Move": 0, "Summon": 0}
    },
    "Ice-Tank": {
        "Class": "Any",
        "Name": "Ice-Tank",
        "Power": "(Up Up)",
        "Effect": "Deploy an Ice-Tank to that can freeze its targets. (Only available through debug)\nSingle-use.",
        "Health": 3,
        "Move": 3,
        "Upgrade 1": "N/A (Up)",
        "Upgrade 2": "N/A (Up)",
        "Debug Name": "DeploySkill_IceTank",
        "Tags": {"Summon": 0}
    },
    # Vek
    "Ramming Speed": {
        "Class": "Vek",
        "Name": "Ramming Speed",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Dash across the map, damaging and pushing the target tile.",
        "Upgrade 1": "Smoke Behind (Up)",
        "Upgrade 2": "Tile behind you gains Smoke.",
        "Debug Name": "Vek_Beetle",
        "Tags": {"Charge": 0, "Forced Move": 0, "Smoke": 1}
    },
    "Needle Shot": {
        "Class": "Vek",
        "Name": "Needle Shot",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Throw needles at the enemy, pushing the furthest hit tile. (Starts with 1-tile range.)",
        "Upgrade 1": "Range & Damage (Up Up)",
        "Upgrade 2": "Range & Damage (Up Up)",
        "Debug Name": "Vek_Hornet",
        "Tags": {"Triple Kill": 2, "Forced Move": 0, "Piercing": 2, }
    },
    "Explosive Goo": {
        "Class": "Vek",
        "Name": "Explosive Goo",
        "Damage": 1,
        "Power": "Free",
        "Effect": "Artillery attack that damages a tile and pushes adjacent tiles away.",
        "Upgrade 1": "+1 Tile (Up)",
        "Upgrade 2": "Increases damage by 2. (Up Up)",
        "Debug Name": "Vek_Scarab",
        "Tags": {"Triple Push": 0, "Forced Move": 0, "Deadly Pull": 0, "Piercing": 1, }
    },

    # Passives
    "Flame Shielding": {
        "Class": "Passive",
        "Name": "Flame Shielding",
        "Power": "Free",
        "Effect": "All Mechs are immune to Fire.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_FlameImmune",
        "Tags": {}
    },
    "Storm Generator": {
        "Class": "Passive",
        "Name": "Storm Generator",
        "Power": "Free",
        "Effect": "All Smoke deals damage to enemy units every turn.",
        "Upgrade 1": "+1 Damage (Up Up Up)",
        "Debug Name": "Passive_Electric",
        "Tags": {"Electric Smoke": 0, "Electric Smoke 2": 3}
    },
    "Viscera Nanobots": {
        "Class": "Passive",
        "Name": "Viscera Nanobots",
        "Power": "Free",
        "Effect": "Mechs heal 1 damage when they deal a killing blow.",
        "Upgrade 1": "+1 Heal (Up Up)",
        "Upgrade 2": "Increase healing to 2.",
        "Debug Name": "Passive_Leech",
        "Tags": {"Heal": 0}
    },
    "Networked Armor": {
        "Class": "Passive",
        "Name": "Networked Armor",
        "Power": "(Up)",
        "Effect": "All Mechs gain +1 HP.",
        "Upgrade 1": "+1 Health (Up Up)",
        "Upgrade 2": "Increases health bonus to 2.",
        "Debug Name": "Passive_Defenses",
        "Tags": {}
    },
    "Repair Field": {
        "Class": "Passive",
        "Name": "Repair Field",
        "Power": "Free",
        "Effect": "Repairing one Mech will affect all Mechs.\n(Includes disabled Mechs. Repairing a disabled Mech will save the pilot.)",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_MassRepair",
        "Tags": {"Heal": 0}
    },
    "Auto-Shields": {
        "Class": "Passive",
        "Name": "Auto-Shields",
        "Power": "Free",
        "Effect": "Buildings gain a Shield after taking damage.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_AutoShields",
        "Tags": {"Shield": 0}
    },
    "Stabilizers": {
        "Class": "Passive",
        "Name": "Stabilizers",
        "Power": "(Up)",
        "Effect": "Mechs no longer take damage when blocking emerging Vek.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_Burrows",
        "Tags": {}
    },
    "Psionic Receiver": {
        "Class": "Passive",
        "Name": "Psionic Receiver",
        "Power": "Free",
        "Effect": "Mechs use bonuses from Vek Psion.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_Psions",
        "Tags": {}
    },
    "Kickoff Boosters": {
        "Class": "Passive",
        "Name": "Kickoff Boosters",
        "Power": "Free",
        "Effect": "Mechs gain +1 move if they start their turn adjacent to each other.",
        "Upgrade 1": "+1 Movement (Up Up)",
        "Upgrade 2": "Movement bonus is increased by 1.",
        "Debug Name": "Passive_Boosters",
        "Tags": {}
    },
    "Medical Supplies": {
        "Class": "Passive",
        "Name": "Medical Supplies",
        "Power": "Free",
        "Effect": "All Pilots survive death.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_Medical",
        "Tags": {}
    },
    "Vek Hormones": {
        "Class": "Passive",
        "Name": "Vek Hormones",
        "Power": "Free",
        "Effect": "Enemies do +1 Damage against other enemies.",
        "Upgrade 1": "+1 Damage (Up)",
        "Upgrade 2": "+1 Damage (Up) (Up)",
        "Debug Name": "Passive_FriendlyFire",
        "Tags": {"Hormones": 3}
    },
    "Force Amp": {
        "Class": "Passive",
        "Name": "Force Amp",
        "Power": "(Up)",
        "Effect": "All Vek take +1 damage from Bumps and blocking emerging Vek.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_ForceAmp",
        "Tags": {}
    },
    "Critical Shields": {
        "Class": "Passive",
        "Name": "Critical Shields",
        "Power": "Free",
        "Effect": "If Power Grid is reduced to 1, all buildings gain a Shield.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_CritDefense",
        "Tags": {"Shield": 0}
    },
    "Ammo Generator": {
        "Class": "Passive",
        "Name": "Ammo Generator",
        "Power": "(Up)",
        "Effect": "+1 Use to all Limited Use Weapons. (Only available through debug)",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_Ammo",
        "Tags": {}
    },
    "Forestry Nano": {
        "Class": "Passive",
        "Name": "Forestry Nano",
        "Power": "Free",
        "Effect": "Vek spawn Forest when they die on Ground. (Only available through debug)",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_FastDecay",
        "Tags": {"Fire": 0}
    },
    "Nanofilter Mending": {
        "Class": "Passive",
        "Name": "Nanofilter Mending",
        "Power": "Free",
        "Effect": "Standing on Smoke repairs mechs and removes Smoke.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_HealingSmoke",
        "Tags": {"Smoke Heal": 0}
    },
    "Heat Engines": {
        "Class": "Passive",
        "Name": "Heat Engines",
        "Power": "Free",
        "Effect": "Standing on Fire removes Fire and gives the mech \"Boost\".",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_FireBoost",
        "Tags": {"Fire Boost": 0}
    },
    "Networked Shielding": {
        "Class": "Passive",
        "Name": "Networked Shielding",
        "Power": "(Up Up)",
        "Effect": "Mechs cannot take damage during the Player Turn.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_PlayerTurnShield",
        "Tags": {}
    },
    "Void Shocker": {
        "Class": "Passive",
        "Name": "Void Shocker",
        "Power": "(Up Up)",
        "Effect": "If a Vek deals no damage to buildings or units when attacking, it takes 1 damage.",
        "Upgrade 1": "",
        "Upgrade 2": "",
        "Debug Name": "Passive_VoidShock",
        "Tags": {}
    }
}
