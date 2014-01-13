InkscapeSpineExporter
=====================

Inkscape extension to aid in the development of Spine (http://esotericsoftware.com/) animations.

#Details

When developing animations for Spine I tend to create a character completely within inkscape. To animate the character all the individual parts of this character need to be exported on their own. To my (limited) knowledge there is no quick way to do this. The InkscapeSpineExporter extension aims to streamline this process by first sorting all indivual sub parts of the character and then batch exporting them to png.

#Usage

Place all .py and .inx files in your personal Inkscape extensions folder. Open Inkscape and under the extensions menu there is a submenu called 'Mine' with 'Spine Sorter' and 'Spine Exporter' options. With the svg document you wish to export open first run Spine Sorter. This sorts all nodes with ID matched by a specified regex into a line with each node separated by the number of pixels specified. Next run the Spine Exporter and specify a directory (some directories do not work for some reason, best results were seen when specifying the same directory as the main document) which you want to export the files to and use the same regex as for the Spine Sorter. The nodes will be exported to individual png files which can then be used in Spine. Hit Ctrl+Z a couple times to return the document to normal un sorted form.

#Example

Open the SoldierExample.svg document in Inkscape. All the main groups I want to export have had their ID's renamed and prefixed with the word 'Group'. You can see this by clicking on a given group and hitting Ctrl+Shift+o. Go to the extension menu and find the 'Spine' submenu and click 'Spine Sorter'. Choose 100 as the horizontal spacing and set the regex to 'Group' without the quotes and Apply. Once this is complete run the 'Spine Exporter' extension in the 'Spine' extension submenu and specify a folder to export the images to and give the same 'Group' regex and hit Apply. The different parts of the Soldier should be exported to individual png images.
