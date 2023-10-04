# BG3 Install Mods Manually 

How to install BG3 Mods Manually on Windows or Mac.

Before we start you should start the game at least once to create the requisit files and folders. Shutdown the game before starting the mods.

## Windows

For Windows we can use the environment variable for C:/Users/%USER%/AppData/Local %LOCALAPPDATA%. 

Make a directory called Mods in the %LOCALAPPDATA%/Larian Studios/Baldur's Gate 3 folder

```bash
md %LOCALAPPDATA%/Larian Studios/Baldur's Gate 3/Mods
```

Extract Foo_Mod.zip and copy the Foo_Mod.pak file to %LOCALAPPDATA%/Larian Studios/Baldur's Gate 3/Mods folder. 

```bash
cp Foo_Mod.pak %LOCALAPPDATA%/Larian Studios/Baldur's Gate 3/Mods/Foo_Mod.pak
```

Open %LOCALAPPDATA%/Larian Studios/Baldur's Gate 3/PlayerProfiles/Public/modsettings.lsx in a text editor and follow the instructions in the [modsettings.lsx](#modsettingslsx) section. If this file doesn't exist run the game to the main menu and then quit the game.

## Mac

For Mac we can use the alias for /Users/$USER/Documents  ~/Documents.

```bash
mkdir -p ~/Documents/Larian\ Studios/Baldur\'s\ Gate\ 3/Mods
```

Extract Foo_Mod.zip and copy the Foo_Mod.pak file to ~/Documents/Larian Studios/Baldur's Gate 3/Mods folder. 

```bash
cp Foo_Mod.pak ~/Documents/Larian\ Studios/Baldur\'s\ Gate\ 3/Mods/Foo_Mod.pak
```

Hopefully if the modder was nice there is an info.json that contains important values we will use to construct our settings. If your mod doesn't have an info.json you can find the uuid of the mod using strings.

```bash
strings Foo_Mod.pak | grep -A 1 OUUID
```

THe UUID is the line under OUUID*

```text
OUUID*
d6089398-48bb-475b-88e6-aec2c3cd4821
--
OUUID"
Template
```


The name and UUID can be found in the file Mods/%MODNAME%/meta.lsx 

Open ~/Documents/Larian\ Studios/Baldur\'s\ Gate\ 3/PlayerProfiles/Public/modsettings.lsx in a text editor and follow the instructions in the [modsettings.lsx](#modsettingslsx) section. If this file doesn't exist run the game to the main menu and then quit the game.


## modsettings.lsx


The modsettings.lsx should look like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="3" revision="0" build="0"/>
    <region id="ModuleSettings">
        <node id="root">
            <children>
                <node id="ModOrder"/>
                <node id="Mods">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="GustavDev"/>
                            <attribute id="MD5" type="LSString" value=""/>
                            <attribute id="Name" type="LSString" value="GustavDev"/>
                            <attribute id="UUID" type="FixedString" value="28ac9ce2-2aba-8cda-b3b5-6e922f71b6b8"/>
                            <attribute id="Version64" type="int64" value="36028797018963968"/>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
```

In the ModOrder section you will add <children> elements in between the <node> elements and add the ModOrder section from Foo_Mod. Do not forget to change  <node id="ModOrder"/> to <node id="ModOrder">. For the base Mod section you can just add it as the <children> elements exist.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<save>
    <version major="4" minor="0" revision="10" build="302"/>
    <region id="ModuleSettings">
        <node id="root">
            <children>
                <node id="ModOrder">
                    <children>
                        <!-- ModOrder entry goes here !-->
                    </children>
                </node>
                <node id="Mods">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="GustavDev"/>
                            <attribute id="MD5" type="LSString" value=""/>
                            <attribute id="Name" type="LSString" value="GustavDev"/>
                            <attribute id="UUID" type="FixedString" value="28ac9ce2-2aba-8cda-b3b5-6e922f71b6b8"/>
                            <attribute id="Version64" type="int64" value="36028797018963968"/>
                        </node>
                        <!-- Mod entry goes here !-->
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>

Add the entries to the ModOrder section and the Mods section. 
Do not mess with the GustavDev entry as it is the main game entry.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<save>
    <version major="4" minor="0" revision="10" build="302"/>
    <region id="ModuleSettings">
        <node id="root">
            <children>
                <node id="ModOrder">
                    <children>
                        <!-- ModOrder entry goes here !-->
                        <node id="Module">
                            <attribute id="UUID" type="FixedString" value="d6089398-48bb-475b-88e6-aec2c3cd4821"/>
                        </node>
                        <!-- end ModOrder entry !-->
                    </children>
                </node>
                <node id="Mods">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="GustavDev"/>
                            <attribute id="MD5" type="LSString" value=""/>
                            <attribute id="Name" type="LSString" value="GustavDev"/>
                            <attribute id="UUID" type="FixedString" value="28ac9ce2-2aba-8cda-b3b5-6e922f71b6b8"/>
                            <attribute id="Version64" type="int64" value="36028797018963968"/>
                        </node>
                        <!-- Mod entry goes here !-->
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSWString" value="Foo_Mod"/>
                            <attribute id="MD5" type="LSString" value=""/>
                            <attribute id="Name" type="FixedString" value="Foo_Mod"/>
                            <attribute id="UUID" type="FixedString" value="d6089398-48bb-475b-88e6-aec2c3cd4821"/>
                            <attribute id="Version" type="int64" value="798529837423467756"/>
                        </node>
                        <!-- end Mod entry !-->
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
```

Save and close the file. The mod should load when you start the game. 

