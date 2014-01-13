import inkex
import simpletransform
import re
"""
SpineSorter is used to move all nodes that match a given regex into a line.
"""
class SpineSorter(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        
        self.OptionParser.add_option('-r', '--idRegex', action='store', type='string', dest='idRegex', default='g', help='Regex to check ID against?')
        self.OptionParser.add_option('-x', '--separationX', action='store', type='int', dest='separationX', default=100, help='Horizontal spacing?')
        
    def effect(self):
        self.sortNodes()
            
    def sortNodes(self):
        """
        Sorts the nodes matched by the regex passed in from inkscape in a line
        """
        xOffset = 0
        
        #Loops through all elements in the document
        for element in self.document.getiterator():
            
            elementID = str(element.get('id'))
            matchID = re.search(self.options.idRegex, elementID, re.I|re.M)            
            
            if matchID:
                #Find the bounding box of the node and use it to information
                #used to sort the nodes
                bBox = simpletransform.computeBBox([element])
                width = (bBox[1] - bBox[0])
                x = (bBox[1] + bBox[0])/2.0
                y = (bBox[3] + bBox[2])/2.0
                
                #Move node to the next available position in the sorted line
                transformation = 'translate(' + str(xOffset-x + width/2) + ', ' + str(-y) + ')'
                transform = simpletransform.parseTransform(transformation)
                simpletransform.applyTransformToNode(transform, element)
                
                #Update the location of the next free space in the sorted line
                xOffset += width + self.options.separationX  
        
effect = SpineSorter()
effect.affect() 