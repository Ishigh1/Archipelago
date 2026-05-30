# Into the Breach randomizer setup guide

## Required Software
- Archipelago
- Into the Breach
- [ITB ModLoader](https://github.com/itb-community/ITB-ModLoader)
  - Place the extracted "randomizer" folder that can be found in the releases of [ITB randomizer for AP](https://github.com/Ishigh1/ITB-randomizer-for-AP/releases) in the mods folder on Into the Breach

## Apworld setup
This apworld uses an external library to randomize the squads if the option is enabled. The provided libraries are only for windows.
If the provided libraries don't work, or you don't want to install them, you can get the [apworld](https://github.com/Ishigh1/ITB-randomizer-for-AP/releases) directly, but the option `randomize_squads` must be set to `false`

To do the full setup, extract everything found in the itb_apworld_and_dependancies archive that can be downloaded in the releases of [ITB randomizer for AP](https://github.com/Ishigh1/ITB-randomizer-for-AP/releases)your local Archipelago install, merging folders if asked.
Ignore the apworld download from this link as the apworld should already be placed in `custom_worlds`.
Note: if you previously installed this apworld by putting it in the lib folder (these are the previous install instructions), you may freely go to lib/worlds and delete into_the_breach.apworld there

## Mod setup
- You will need a new profile for that, think of a name for it and check if there is no profile folder of that name in your ITB data folder (in Documents/My Games/into the breach). If there is one, delete it
- Launch the game (the following instructions are to be done in-game)
- Create your new profile if you care about your current one
- Go in mod content>configure mods then enable the randomizer mod, Mod Loader Extensions > modApiExt and Mod Loader Extensions > memedit
  - If it is asking to disable mods to do calibration: 
    - Close the game
    - Download and unzip the [latest memedit release](https://github.com/itb-community/memedit/releases/tag/1.2.0) into your Into The Breach/scripts/mod_loader/extensions/modLoaderExtensions/mods/memedit/ 
    - Relaunch the game
- Open the console with ` (if you don't have it on your keyboard, switch to the english one)
- Type the command "makeitso". This command is linked to your current profile, so if you change it afterward, you will need to do the command again.
- Relaunch the game
- You may play now. Note that the selected squad that you start with may be different from the last squad you played with, click "select squad" to see which ones you have access to

## FAQ
### I am getting a "no module named `pysat`" error while generating
It means you didn't install the dependencies to randomize squads. 
- If you're not on Windows, I am sorry, you either need to get the dependencies yourself by running from source or disable that option, I have no better way until Archipelago allows installing dependencies through pip
- Otherwise, check [above](#apworld-setup)

### I am getting an EXCEPTION_ACCESS_VIOLATION error while starting a run
It means you didn't run the makeitso command, check [above](#mod-setup)

### I am getting a Script Error with "attempt to index a global 'modapiext' (a nil value)'" (third line)
In mod content > configure mods, develop Mod Loader Extensions and check if both modApiExt and memedit are ticked (it should have been done in step 4)
If it isn't there, it means you installed the source code of the modloader instead of the release. You need to get "ITB-ModLoader-XXXXXX.zip"
