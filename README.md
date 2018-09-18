# InkscapeSpineExporter

Inkscape extension to aid in the development of Spine (http://esotericsoftware.com/) animations.

## Details

When developing animations for Spine I tend to create a character completely within inkscape. To animate the character all the individual parts of this character need to be exported on their own. To my (limited) knowledge there is no quick way to do this. The InkscapeSpineExporter extension aims to streamline this process by batch exporting all parts of these characters or models to png's.

## Usage

Place all .py and .inx files in your personal Inkscape extensions folder (Typically AppData\Roaming\inkscape\extensions). Open Inkscape and under the extensions menu there is a submenu called 'Spine' with the 'Spine Exporter' option. With the svg document you wish to export open, open the Spine Exporter. Specify a directory which you want to export the files to and the dpi you wish to export with. The ID Regex option is used to find the groups you wish to export. This usage is better explained if you look at the example. With remove prefix you can specify a part of the ID prefix you wish to remove from the saved image names. Click apply and all matched groups will be exported to individual png files which can then be used in Spine.

## Example

Open the SoldierExample.svg document in Inkscape. All the groups I want to export have had their ID's renamed and prefixed with the word 'Group-'. You can see this by clicking on a given group and hitting Ctrl+Shift+o. Go to the extension menu and find the 'Spine' submenu and click 'Spine Exporter'. Set the ID Regex to 'Group-' and the remove prefix to 'Group-'. Choose a folder to export to and hit apply. The extension will find all nodes with ID's that start with 'Group-' and will export these groups as individual png images.
