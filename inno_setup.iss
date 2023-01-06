#define source_path ReadIni(SourcePath + "\setup.ini", "Data", "source_path")
#define min_windows ReadIni(SourcePath + "\setup.ini", "Data", "min_windows")

#define MyAppName "Archipelago"
#define MyAppExeName "ArchipelagoServer.exe"
#define MyAppIcon "data/icon.ico"
#dim VersionTuple[4]
#define MyAppVersion GetVersionComponents(source_path + '\ArchipelagoServer.exe', VersionTuple[0], VersionTuple[1], VersionTuple[2], VersionTuple[3])
#define MyAppVersionText Str(VersionTuple[0])+"."+Str(VersionTuple[1])+"."+Str(VersionTuple[2])


[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
AppId={{918BA46A-FAB8-460C-9DFF-AE691E1C865B}}
AppName={#MyAppName}
AppCopyright=Distributed under MIT License
AppVerName={#MyAppName} {#MyAppVersionText}
VersionInfoVersion={#MyAppVersion}
DefaultDirName={commonappdata}\{#MyAppName}
DisableProgramGroupPage=yes
DefaultGroupName=Archipelago
OutputDir=setups
OutputBaseFilename=Setup {#MyAppName} {#MyAppVersionText}
Compression=lzma2
SolidCompression=yes
LZMANumBlockThreads=8
ArchitecturesInstallIn64BitMode=x64
ChangesAssociations=yes
ArchitecturesAllowed=x64
AllowNoIcons=yes
SetupIconFile={#MyAppIcon}
UninstallDisplayIcon={app}\{#MyAppExeName}
; you will likely have to remove the following signtool line when testing/debugging locally. Don't include that change in PRs.
SignTool= signtool
LicenseFile= LICENSE
WizardStyle= modern
SetupLogging=yes
MinVersion={#min_windows}

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Types]
Name: "full"; Description: "Full installation"
Name: "hosting"; Description: "Installation for hosting purposes"
Name: "playing"; Description: "Installation for playing purposes"
Name: "custom"; Description: "Custom installation"; Flags: iscustom

[Components]
Name: "core";             Description: "Core Files"; Types: full hosting playing custom; Flags: fixed
Name: "server";           Description: "Server"; Types: full hosting
Name: "generator";        Description: "Generator"; Types: full hosting
#include "generator_components.iss"
Name: "generator/oot";    Description: "Ocarina of Time ROM Setup"; Types: full hosting; ExtraDiskSpaceRequired: 100663296; Flags: disablenouninstallwarning
Name: "generator/zl";     Description: "Zillion ROM Setup"; Types: full hosting; ExtraDiskSpaceRequired: 150000; Flags: disablenouninstallwarning
Name: "generator/pkmn_r"; Description: "Pokemon Red ROM Setup"; Types: full hosting
Name: "generator/pkmn_b"; Description: "Pokemon Blue ROM Setup"; Types: full hosting
Name: "client";           Description: "Clients"; Types: full playing
Name: "client/sni";       Description: "SNI Client"; Types: full playing
#include "sni_components.iss"
Name: "client/factorio";  Description: "Factorio"; Types: full playing
Name: "client/minecraft"; Description: "Minecraft"; Types: full playing; ExtraDiskSpaceRequired: 226894278
Name: "client/oot";       Description: "Ocarina of Time"; Types: full playing
Name: "client/ff1";       Description: "Final Fantasy 1"; Types: full playing
Name: "client/pkmn";      Description: "Pokemon Client"
Name: "client/pkmn/red";  Description: "Pokemon Client - Pokemon Red Setup"; Types: full playing; ExtraDiskSpaceRequired: 1048576
Name: "client/pkmn/blue"; Description: "Pokemon Client - Pokemon Blue Setup"; Types: full playing; ExtraDiskSpaceRequired: 1048576
Name: "client/cf";        Description: "ChecksFinder"; Types: full playing
Name: "client/sc2";       Description: "Starcraft 2"; Types: full playing
Name: "client/zl";        Description: "Zillion"; Types: full playing
Name: "client/text";      Description: "Text, to !command and chat"; Types: full playing

[Dirs]
NAME: "{app}"; Flags: setntfscompression; Permissions: everyone-modify users-modify authusers-modify;

[Files]
#include "files.iss"
Source: "{code:GetOoTROMPath}"; DestDir: "{app}"; DestName: "The Legend of Zelda - Ocarina of Time.z64"; Flags: external; Components: client/oot or generator/oot
Source: "{code:GetZlROMPath}"; DestDir: "{app}"; DestName: "Zillion (UE) [!].sms"; Flags: external; Components: client/zl or generator/zl
Source: "{code:GetRedROMPath}"; DestDir: "{app}"; DestName: "Pokemon Red (UE) [S][!].gb"; Flags: external; Components: client/pkmn/red or generator/pkmn_r
Source: "{code:GetBlueROMPath}"; DestDir: "{app}"; DestName: "Pokemon Blue (UE) [S][!].gb"; Flags: external; Components: client/pkmn/blue or generator/pkmn_b
Source: "{#source_path}\*"; Excludes: "*.sfc, *.log, data\sprites\alttpr, SNI, EnemizerCLI, Archipelago*.exe"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "{#source_path}\SNI\*"; Excludes: "*.sfc, *.log"; DestDir: "{app}\SNI"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: client/sni
Source: "{#source_path}\EnemizerCLI\*"; Excludes: "*.sfc, *.log"; DestDir: "{app}\EnemizerCLI"; Flags: ignoreversion recursesubdirs createallsubdirs; Components: generator/lttp

Source: "{#source_path}\ArchipelagoGenerate.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: generator
Source: "{#source_path}\ArchipelagoServer.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: server
Source: "{#source_path}\ArchipelagoFactorioClient.exe";  DestDir: "{app}"; Flags: ignoreversion; Components: client/factorio
Source: "{#source_path}\ArchipelagoTextClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/text
Source: "{#source_path}\ArchipelagoSNIClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/sni
Source: "{#source_path}\ArchipelagoLttPAdjuster.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/sni/lttp or generator/lttp
Source: "{#source_path}\ArchipelagoMinecraftClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/minecraft
Source: "{#source_path}\ArchipelagoOoTClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/oot
Source: "{#source_path}\ArchipelagoOoTAdjuster.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/oot
Source: "{#source_path}\ArchipelagoZillionClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/zl
Source: "{#source_path}\ArchipelagoFF1Client.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/ff1
Source: "{#source_path}\ArchipelagoPokemonClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/pkmn
Source: "{#source_path}\ArchipelagoChecksFinderClient.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/cf
Source: "{#source_path}\ArchipelagoStarcraft2Client.exe"; DestDir: "{app}"; Flags: ignoreversion; Components: client/sc2
Source: "vc_redist.x64.exe"; DestDir: {tmp}; Flags: deleteafterinstall

[Icons]
Name: "{group}\{#MyAppName} Folder"; Filename: "{app}";
Name: "{group}\{#MyAppName} Server"; Filename: "{app}\{#MyAppExeName}"; Components: server
Name: "{group}\{#MyAppName} Text Client"; Filename: "{app}\ArchipelagoTextClient.exe"; Components: client/text
Name: "{group}\{#MyAppName} SNI Client"; Filename: "{app}\ArchipelagoSNIClient.exe"; Components: client/sni
Name: "{group}\{#MyAppName} Factorio Client"; Filename: "{app}\ArchipelagoFactorioClient.exe"; Components: client/factorio
Name: "{group}\{#MyAppName} Minecraft Client"; Filename: "{app}\ArchipelagoMinecraftClient.exe"; Components: client/minecraft
Name: "{group}\{#MyAppName} Ocarina of Time Client"; Filename: "{app}\ArchipelagoOoTClient.exe"; Components: client/oot
Name: "{group}\{#MyAppName} Zillion Client"; Filename: "{app}\ArchipelagoZillionClient.exe"; Components: client/zl
Name: "{group}\{#MyAppName} Final Fantasy 1 Client"; Filename: "{app}\ArchipelagoFF1Client.exe"; Components: client/ff1
Name: "{group}\{#MyAppName} Pokemon Client"; Filename: "{app}\ArchipelagoPokemonClient.exe"; Components: client/pkmn
Name: "{group}\{#MyAppName} ChecksFinder Client"; Filename: "{app}\ArchipelagoChecksFinderClient.exe"; Components: client/cf
Name: "{group}\{#MyAppName} Starcraft 2 Client"; Filename: "{app}\ArchipelagoStarcraft2Client.exe"; Components: client/sc2

Name: "{commondesktop}\{#MyAppName} Folder"; Filename: "{app}"; Tasks: desktopicon
Name: "{commondesktop}\{#MyAppName} Server"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon; Components: server
Name: "{commondesktop}\{#MyAppName} SNI Client"; Filename: "{app}\ArchipelagoSNIClient.exe"; Tasks: desktopicon; Components: client/sni
Name: "{commondesktop}\{#MyAppName} Factorio Client"; Filename: "{app}\ArchipelagoFactorioClient.exe"; Tasks: desktopicon; Components: client/factorio
Name: "{commondesktop}\{#MyAppName} Minecraft Client"; Filename: "{app}\ArchipelagoMinecraftClient.exe"; Tasks: desktopicon; Components: client/minecraft
Name: "{commondesktop}\{#MyAppName} Ocarina of Time Client"; Filename: "{app}\ArchipelagoOoTClient.exe"; Tasks: desktopicon; Components: client/oot
Name: "{commondesktop}\{#MyAppName} Zillion Client"; Filename: "{app}\ArchipelagoZillionClient.exe"; Tasks: desktopicon; Components: client/zl
Name: "{commondesktop}\{#MyAppName} Final Fantasy 1 Client"; Filename: "{app}\ArchipelagoFF1Client.exe"; Tasks: desktopicon; Components: client/ff1
Name: "{commondesktop}\{#MyAppName} Pokemon Client"; Filename: "{app}\ArchipelagoPokemonClient.exe"; Tasks: desktopicon; Components: client/pkmn
Name: "{commondesktop}\{#MyAppName} ChecksFinder Client"; Filename: "{app}\ArchipelagoChecksFinderClient.exe"; Tasks: desktopicon; Components: client/cf
Name: "{commondesktop}\{#MyAppName} Starcraft 2 Client"; Filename: "{app}\ArchipelagoStarcraft2Client.exe"; Tasks: desktopicon; Components: client/sc2

[Run]

Filename: "{tmp}\vc_redist.x64.exe"; Parameters: "/passive /norestart"; Check: IsVCRedist64BitNeeded; StatusMsg: "Installing VC++ redistributable..."
Filename: "{app}\ArchipelagoLttPAdjuster"; Parameters: "--update_sprites"; StatusMsg: "Updating Sprite Library..."; Components: client/sni/lttp or generator/lttp
Filename: "{app}\ArchipelagoMinecraftClient.exe"; Parameters: "--install"; StatusMsg: "Installing Forge Server..."; Components: client/minecraft

[UninstallDelete]
Type: dirifempty; Name: "{app}"

[InstallDelete]
Type: files; Name: "{app}\ArchipelagoLttPClient.exe"
Type: filesandordirs; Name: "{app}\lib\worlds\rogue-legacy*"
#include "installdelete.iss"

[Registry]
; SNIClient mappings are auto inserted from
#include "registry.iss"

Root: HKCR; Subkey: ".apzl";                                   ValueData: "{#MyAppName}zlpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: ""; Components: client/zl
Root: HKCR; Subkey: "{#MyAppName}zlpatch";                     ValueData: "Archipelago Zillion Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: ""; Components: client/zl
Root: HKCR; Subkey: "{#MyAppName}zlpatch\DefaultIcon";         ValueData: "{app}\ArchipelagoZillionClient.exe,0";                           ValueType: string;  ValueName: ""; Components: client/zl
Root: HKCR; Subkey: "{#MyAppName}zlpatch\shell\open\command";  ValueData: """{app}\ArchipelagoZillionClient.exe"" ""%1""";                  ValueType: string;  ValueName: ""; Components: client/zl

Root: HKCR; Subkey: ".apmc";                                  ValueData: "{#MyAppName}mcdata";         Flags: uninsdeletevalue; ValueType: string;  ValueName: ""; Components: client/minecraft
Root: HKCR; Subkey: "{#MyAppName}mcdata";                     ValueData: "Archipelago Minecraft Data"; Flags: uninsdeletekey;   ValueType: string;  ValueName: ""; Components: client/minecraft
Root: HKCR; Subkey: "{#MyAppName}mcdata\DefaultIcon";         ValueData: "{app}\ArchipelagoMinecraftClient.exe,0";                           ValueType: string;  ValueName: ""; Components: client/minecraft
Root: HKCR; Subkey: "{#MyAppName}mcdata\shell\open\command";  ValueData: """{app}\ArchipelagoMinecraftClient.exe"" ""%1""";                  ValueType: string;  ValueName: ""; Components: client/minecraft

Root: HKCR; Subkey: ".apz5";                                  ValueData: "{#MyAppName}n64zpf";         Flags: uninsdeletevalue; ValueType: string;  ValueName: ""; Components: client/oot
Root: HKCR; Subkey: "{#MyAppName}n64zpf";                     ValueData: "Archipelago Ocarina of Time Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: ""; Components: client/oot
Root: HKCR; Subkey: "{#MyAppName}n64zpf\DefaultIcon";         ValueData: "{app}\ArchipelagoOoTClient.exe,0";                           ValueType: string;  ValueName: ""; Components: client/oot
Root: HKCR; Subkey: "{#MyAppName}n64zpf\shell\open\command";  ValueData: """{app}\ArchipelagoOoTClient.exe"" ""%1""";                  ValueType: string;  ValueName: ""; Components: client/oot

Root: HKCR; Subkey: ".apred";                                    ValueData: "{#MyAppName}pkmnrpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: ""; Components: client/pkmn
Root: HKCR; Subkey: "{#MyAppName}pkmnrpatch";                     ValueData: "Archipelago Pokemon Red Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: ""; Components: client/pkmn
Root: HKCR; Subkey: "{#MyAppName}pkmnrpatch\DefaultIcon";         ValueData: "{app}\ArchipelagoPokemonClient.exe,0";                           ValueType: string;  ValueName: ""; Components: client/pkmn
Root: HKCR; Subkey: "{#MyAppName}pkmnrpatch\shell\open\command";  ValueData: """{app}\ArchipelagoPokemonClient.exe"" ""%1""";                  ValueType: string;  ValueName: ""; Components: client/pkmn

Root: HKCR; Subkey: ".apblue";                                    ValueData: "{#MyAppName}pkmnbpatch";        Flags: uninsdeletevalue; ValueType: string;  ValueName: ""; Components: client/pkmn
Root: HKCR; Subkey: "{#MyAppName}pkmnbpatch";                     ValueData: "Archipelago Pokemon Blue Patch"; Flags: uninsdeletekey;   ValueType: string;  ValueName: ""; Components: client/pkmn
Root: HKCR; Subkey: "{#MyAppName}pkmnbpatch\DefaultIcon";         ValueData: "{app}\ArchipelagoPokemonClient.exe,0";                           ValueType: string;  ValueName: ""; Components: client/pkmn
Root: HKCR; Subkey: "{#MyAppName}pkmnbpatch\shell\open\command";  ValueData: """{app}\ArchipelagoPokemonClient.exe"" ""%1""";                  ValueType: string;  ValueName: ""; Components: client/pkmn

Root: HKCR; Subkey: ".archipelago";                              ValueData: "{#MyAppName}multidata";        Flags: uninsdeletevalue; ValueType: string;  ValueName: ""; Components: server
Root: HKCR; Subkey: "{#MyAppName}multidata";                     ValueData: "Archipelago Server Data";       Flags: uninsdeletekey;  ValueType: string;  ValueName: ""; Components: server
Root: HKCR; Subkey: "{#MyAppName}multidata\DefaultIcon";         ValueData: "{app}\ArchipelagoServer.exe,0";                         ValueType: string;  ValueName: ""; Components: server
Root: HKCR; Subkey: "{#MyAppName}multidata\shell\open\command";  ValueData: """{app}\ArchipelagoServer.exe"" ""%1""";                ValueType: string;  ValueName: ""; Components: server

Root: HKCR; Subkey: "archipelago"; ValueType: "string"; ValueData: "Archipegalo Protocol"; Flags: uninsdeletekey; Components: client/text
Root: HKCR; Subkey: "archipelago"; ValueType: "string"; ValueName: "URL Protocol"; ValueData: ""; Components: client/text
Root: HKCR; Subkey: "archipelago\DefaultIcon"; ValueType: "string"; ValueData: "{app}\ArchipelagoTextClient.exe,0"; Components: client/text
Root: HKCR; Subkey: "archipelago\shell\open\command"; ValueType: "string"; ValueData: """{app}\ArchipelagoTextClient.exe"" ""%1"""; Components: client/text

[Code]
const
  SHCONTCH_NOPROGRESSBOX = 4;
  SHCONTCH_RESPONDYESTOALL = 16;

// See: https://stackoverflow.com/a/51614652/2287576
function IsVCRedist64BitNeeded(): boolean;
var
  strVersion: string;
begin
  if (RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SOFTWARE\Microsoft\VisualStudio\14.0\VC\Runtimes\x64', 'Version', strVersion)) then
  begin
    // Is the installed version at least the packaged one ?
    Log('VC Redist x64 Version : found ' + strVersion);
    Result := (CompareStr(strVersion, 'v14.32.31332') < 0);
  end
  else
  begin
    // Not even an old version installed
    Log('VC Redist x64 is not already installed');
    Result := True;
  end;
end;

var R : longint;

var ootrom: string;
var OoTROMFilePage: TInputFileWizardPage;

var zlrom: string;
var ZlROMFilePage: TInputFileWizardPage;

var redrom: string;
var RedROMFilePage:  TInputFileWizardPage;

var bluerom: string;
var BlueROMFilePage:  TInputFileWizardPage;

function GetSNESMD5OfFile(const rom: string): string;
var data: AnsiString;
begin
  if LoadStringFromFile(rom, data) then
  begin
      if Length(data) mod 1024 = 512 then
      begin
        data := copy(data, 513, Length(data)-512);
      end;
      Result := GetMD5OfString(data);
  end;
end;

function GetMD5OfFile(const rom: string): string;
var data: AnsiString;
begin
  if LoadStringFromFile(rom, data) then
  begin
      Result := GetMD5OfString(data);
  end;
end;

function CheckSNESRom(name: string; hash: string): string;
var rom: string;
begin
  log('Handling ' + name)
  rom := FileSearch(name, WizardDirValue());
  if Length(rom) > 0 then
    begin
      log('existing ROM found');
      log(IntToStr(CompareStr(GetSNESMD5OfFile(rom), hash)));
      if CompareStr(GetSNESMD5OfFile(rom), hash) = 0 then
        begin
        log('existing ROM verified');
        Result := rom;
        exit;
        end;
      log('existing ROM failed verification');
    end;
end;

function CheckRom(name: string; hash: string): string;
var rom: string;
begin
  log('Handling ' + name)
  rom := FileSearch(name, WizardDirValue());
  if Length(rom) > 0 then
    begin
      log('existing ROM found');
      log(IntToStr(CompareStr(GetMD5OfFile(rom), hash)));
      if CompareStr(GetMD5OfFile(rom), hash) = 0 then
        begin
        log('existing ROM verified');
        Result := rom;
        exit;
        end;
      log('existing ROM failed verification');
    end;
end;

function AddRomPage(name: string): TInputFileWizardPage;
begin
  Result :=
    CreateInputFilePage(
      wpSelectComponents,
      'Select ROM File',
      'Where is your ' + name + ' located?',
      'Select the file, then click Next.');

  Result.Add(
    'Location of ROM file:',
    'SNES ROM files|*.sfc;*.smc|All files|*.*',
    '.sfc');
end;


function AddGBRomPage(name: string): TInputFileWizardPage;
begin
  Result :=
    CreateInputFilePage(
      wpSelectComponents,
      'Select ROM File',
      'Where is your ' + name + ' located?',
      'Select the file, then click Next.');

  Result.Add(
    'Location of ROM file:',
    'GB ROM files|*.gb;*.gbc|All files|*.*',
    '.gb');
end;

function AddSMSRomPage(name: string): TInputFileWizardPage;
begin
  Result :=
    CreateInputFilePage(
      wpSelectComponents,
      'Select ROM File',
      'Where is your ' + name + ' located?',
      'Select the file, then click Next.');

  Result.Add(
    'Location of ROM file:',
    'SMS ROM files|*.sms|All files|*.*',
    '.sms');
end;

procedure AddOoTRomPage();
begin
  ootrom := FileSearch('The Legend of Zelda - Ocarina of Time.z64', WizardDirValue());
  if Length(ootrom) > 0 then
    begin
      log('existing ROM found');
      log(IntToStr(CompareStr(GetMD5OfFile(ootrom), '5bd1fe107bf8106b2ab6650abecd54d6'))); // normal
      log(IntToStr(CompareStr(GetMD5OfFile(ootrom), '6697768a7a7df2dd27a692a2638ea90b'))); // byteswapped
      log(IntToStr(CompareStr(GetMD5OfFile(ootrom), '05f0f3ebacbc8df9243b6148ffe4792f'))); // decompressed
      if (CompareStr(GetMD5OfFile(ootrom), '5bd1fe107bf8106b2ab6650abecd54d6') = 0) or (CompareStr(GetMD5OfFile(ootrom), '6697768a7a7df2dd27a692a2638ea90b') = 0) or (CompareStr(GetMD5OfFile(ootrom), '05f0f3ebacbc8df9243b6148ffe4792f') = 0) then
        begin
        log('existing ROM verified');
        exit;
        end;
      log('existing ROM failed verification');
    end;
  ootrom := ''
  OoTROMFilePage :=
    CreateInputFilePage(
      wpSelectComponents,
      'Select ROM File',
      'Where is your OoT 1.0 ROM located?',
      'Select the file, then click Next.');

  OoTROMFilePage.Add(
    'Location of ROM file:',
    'N64 ROM files (*.z64, *.n64)|*.z64;*.n64|All files|*.*',
    '.z64');
end;

function GetOoTROMPath(Param: string): string;
begin
  if Length(ootrom) > 0 then
    Result := ootrom
  else if Assigned(OoTROMFilePage) then
    begin
      R := CompareStr(GetMD5OfFile(OoTROMFilePage.Values[0]), '5bd1fe107bf8106b2ab6650abecd54d6') * CompareStr(GetMD5OfFile(OoTROMFilePage.Values[0]), '6697768a7a7df2dd27a692a2638ea90b') * CompareStr(GetMD5OfFile(OoTROMFilePage.Values[0]), '05f0f3ebacbc8df9243b6148ffe4792f');
      if R <> 0 then
        MsgBox('OoT ROM validation failed. Very likely wrong file.', mbInformation, MB_OK);

      Result := OoTROMFilePage.Values[0]
    end
  else
    Result := '';
end;

function GetZlROMPath(Param: string): string;
begin
  if Length(zlrom) > 0 then
    Result := zlrom
  else if Assigned(ZlROMFilePage) then
    begin
      R := CompareStr(GetMD5OfFile(ZlROMFilePage.Values[0]), 'd4bf9e7bcf9a48da53785d2ae7bc4270');
      if R <> 0 then
        MsgBox('Zillion ROM validation failed. Very likely wrong file.', mbInformation, MB_OK);

      Result := ZlROMFilePage.Values[0]
    end
  else
    Result := '';
end;

function GetRedROMPath(Param: string): string;
begin
  if Length(redrom) > 0 then
    Result := redrom
  else if Assigned(RedRomFilePage) then
    begin
      R := CompareStr(GetMD5OfFile(RedROMFilePage.Values[0]), '3d45c1ee9abd5738df46d2bdda8b57dc')
      if R <> 0 then
        MsgBox('Pokemon Red ROM validation failed. Very likely wrong file.', mbInformation, MB_OK);

      Result := RedROMFilePage.Values[0]
    end
  else
    Result := '';
 end;

function GetBlueROMPath(Param: string): string;
begin
  if Length(bluerom) > 0 then
    Result := bluerom
  else if Assigned(BlueRomFilePage) then
    begin
      R := CompareStr(GetMD5OfFile(BlueROMFilePage.Values[0]), '50927e843568814f7ed45ec4f944bd8b')
      if R <> 0 then
        MsgBox('Pokemon Blue ROM validation failed. Very likely wrong file.', mbInformation, MB_OK);

      Result := BlueROMFilePage.Values[0]
    end
  else
    Result := '';
 end;

#include "code.iss"

procedure InitializeWizard();
begin
  AddOoTRomPage();
  SNESWizard();
  zlrom := CheckRom('Zillion (UE) [!].sms', 'd4bf9e7bcf9a48da53785d2ae7bc4270');
  if Length(zlrom) = 0 then
    ZlROMFilePage:= AddSMSRomPage('Zillion (UE) [!].sms');

  redrom := CheckRom('Pokemon Red (UE) [S][!].gb','3d45c1ee9abd5738df46d2bdda8b57dc');
  if Length(redrom) = 0 then
    RedROMFilePage:= AddGBRomPage('Pokemon Red (UE) [S][!].gb');

  bluerom := CheckRom('Pokemon Blue (UE) [S][!].gb','50927e843568814f7ed45ec4f944bd8b');
  if Length(bluerom) = 0 then
    BlueROMFilePage:= AddGBRomPage('Pokemon Blue (UE) [S][!].gb');
end;


function ShouldSkipPage(PageID: Integer): Boolean;
begin
  Result := ShouldSkipSNESPage(PageID);
  if (assigned(OoTROMFilePage)) and (PageID = OoTROMFilePage.ID) then
    Result := not (WizardIsComponentSelected('generator/oot') or WizardIsComponentSelected('client/oot'));
  if (assigned(ZlROMFilePage)) and (PageID = ZlROMFilePage.ID) then
    Result := not (WizardIsComponentSelected('generator/zl') or WizardIsComponentSelected('client/zl'));
  if (assigned(RedROMFilePage)) and (PageID = RedROMFilePage.ID) then
    Result := not (WizardIsComponentSelected('generator/pkmn_r') or WizardIsComponentSelected('client/pkmn/red'));
  if (assigned(BlueROMFilePage)) and (PageID = BlueROMFilePage.ID) then
    Result := not (WizardIsComponentSelected('generator/pkmn_b') or WizardIsComponentSelected('client/pkmn/blue'));
end;


function NextButtonClick(CurPageID: Integer): Boolean;
begin
  if (assigned(OoTROMFilePage)) and (CurPageID = OoTROMFilePage.ID) then
    Result := not (OoTROMFilePage.Values[0] = '')
  else if (assigned(ZlROMFilePage)) and (CurPageID = ZlROMFilePage.ID) then
    Result := not (ZlROMFilePage.Values[0] = '')
  else
    Result := NextSNESButtonClick(CurPageID);
end;