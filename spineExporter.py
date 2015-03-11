import inkex
import subprocess
import re
"""
SpineExporter is used to export all nodes matching a given regex to individual
png images.
"""
class SpineExporter(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        
        self.OptionParser.add_option('-r', '--idRegex', action='store', type='string', dest='idRegex', default='g', help='Regex to check ID against?')
        self.OptionParser.add_option('-e', '--exportDir', action='store', type='string', dest='exportDir', default="C:\\", help='Where should the images be exported?')
        self.OptionParser.add_option('-d', '--exportDPI', action='store', type='float', dest='exportDPI', default=90.0, help='Dots per inch (DPI)')
        self.OptionParser.add_option('-x', '--removePrefix', action='store', type='string', dest='removePrefix', default="g", help='Remove the given prefix?')

    def effect(self):
        self.exportNodes()
            
    def exportNodes (self):
        """
        Exports all nodes in the given document matching the specified regex to
        the specified directory
        """
        svgFile = self.args[-1]
        for element in self.document.getiterator():
            elementID = str(element.get('id'))
            
            matchID = re.search(self.options.idRegex, elementID, re.I|re.M)            
            
            if matchID:
		
                # Remove prefix
                exportNameID = elementID;
                if self.options.removePrefix:
                    if elementID.startswith(self.options.removePrefix):
                        exportNameID = elementID[len(self.options.removePrefix):]

                exportFile = self.options.exportDir + "/" + exportNameID + ".png"
                
                command = "inkscape -i \"{0}\" -j -d {1} -e \"{2}\" \"{3}\" ".format(elementID, self.options.exportDPI, exportFile, svgFile)
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                process.wait()
        
effect = SpineExporter()
effect.affect() 
