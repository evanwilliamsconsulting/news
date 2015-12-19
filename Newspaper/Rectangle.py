# -*- coding: utf-8 -*-
#
# File: Rectangle.py
#
# Copyright (c) 2011 by unknown <unknown>
# Generator: ArchGenXML Version 2.6
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName
from interfaces import IRectangle,IBlock
import interfaces
from BlockishSchema import BlockishSchema

from Products.Five.browser import BrowserView
from Acquisition import aq_inner,aq_parent

from Products.SmartColorWidget.Widget import SmartColorWidget

import json
##code-section module-header #fill in your manual code here
##/code-section module-header

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema
RectangleSchema = Schema((
    IntegerField(
	name='left',
	widget=IntegerField._properties['widget'](
	    label='left',
	    label_msgid='Newspaper_label_left',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='top',
	widget=IntegerField._properties['widget'](
	    label='top',
	    label_msgid='Newspaper_label_top',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='rwidth',
	widget=IntegerField._properties['widget'](
	    label='width',
	    label_msgid='Newspaper_label_width',
	    i18n_domain='Newspaper',
	),
    ),
    IntegerField(
	name='rheight',
	widget=IntegerField._properties['widget'](
	    label='height',
	    label_msgid='Newspaper_label_height',
	    i18n_domain='Newspaper',
	),
    ),
    StringField(
        name='caption',
	widget=StringWidget(
		label='Caption',
		label_msgid='Newspaper_label_caption',
		i18n_domain='Newspaper',
	),
    ),
    StringField('color',
        default='#00FFFF',
        searchable=0,
        required=0,
        widget=SmartColorWidget(
             label='Color',
        )
    ),    
),
)

Rectangle_schema = OrderedBaseFolderSchema.copy() + \
    RectangleSchema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RectangleJSON(BrowserView):
    """ JSON Encoded Issue """
    def __init__(self,context,request):
        """ Initialize context and request as view multiadaption parameters.

        Note that the BrowserView constructor does this for you.
        This step here is just to show how view receives its context and
        request parameter. You do not need to write __init__() for your
        views.
        """
        self.context = context
        self.request = request

    # by default call will call self.index() method which is mapped
    # to ViewPageTemplateFile specified in ZCML
    def __call__(self):
   	self.request.response.setHeader("Content-type","application/json")
	json_item = {}
	title = self.context.getId()
	json_item['Rectangle']=title
	items = self.context.listFolderContents()
	json_items = {}
	for item in items:
		itemId = item.getId()
		pos = item.getObjectPosition(itemId)
		json_items[pos]=item.getJSON()
	json_item['Items']=sorted(json_items,reverse=True)
	pretty = json.dumps(json_item)    
	return pretty 

class RectangleDiagnostics(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request

class FullRectangleView(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request

class RectangleView(BrowserView):
    """
    """
    def __init__(self,context,request):
        """
        """
        self.context = context
        self.request = request



class Rectangle(OrderedBaseFolder,  BrowserDefaultMixin):
    """
    A container is itself a Block.
    Or a Block can Reference a Rectangle that is elsewhere.
    Or a Block can Contain a Rectangle.
    """
    x = 0
    y = 0
    security = ClassSecurityInfo()

    implements(interfaces.IRectangle,interfaces.IBlock)

    meta_type = 'Rectangle'
    _at_rename_after_creation = True

    schema = Rectangle_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def getPreviousElement(self,currentId):
	"""
	Returns the ID of the previous element
	"""
	ids = self.getObjectIds()
	previousId = None
	for id in ids:
	    if id == currentId:
		return previousId
	    else:
		previousId = id
	return None

    def getJSON(self):
	"""
	test
	"""
	json_result = {}
	json_item = {}
	elements = {}
	title = self.getId()
	items = self.listFolderContents()
	json_items = {}
	#
	broadsheet = self.aq_inner.aq_parent
	(bT,bL,bW,bH,bB,bR) = broadsheet.getBoundingBox(self.id)
	# New Rectangle must be positioned outside of Bounding Box.
	
        top = self.getTop()
        left = self.getLeft()
	width = self.getWidth()
	height = self.getHeight()
	useheight = height
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        numberOfColumns = 0
        for item in items:
            numberOfColumns += 1
	    useheight = int(height/numberOfColumns)
	# test bounding box
	useheight += 100
	freeSpaces = broadsheet.getFreeSpaces(self.id,1200,0)
	print "free Spaces"
	print freeSpaces
	# use first Free Space
	top = bT
	left = bL
	# if first choose first
	for freeSpace in freeSpaces:
	    fT=freeSpace[0]
	    fL=freeSpace[1]
	    fW=freeSpace[2]
	    fH=freeSpace[3]
	    if fW == 0:
#		if fH > useheight:
		top = fT
		left =fL
		break 
	    if fH == 0:
	#	if fW > width:
		top = fT
		left = fL
		break
	# update top and left with new coordinates
	# so that bounding box will be recomputed
	# with new position
	broadsheet.updateBoundingBox(self.id,top,left+100,width,useheight)	
	#
	for item in items:
		itemId = item.getId()
		#json_items[itemId]=item.getJSON()
		pos = self.getObjectPosition(itemId)
		json_items[pos]=item.getJSON()
	json_item['elements']=json_items
	#json_item['top']=self.getTop()
	#json_item['left']=self.getLeft()
	json_item['top']=top
	json_item['left']=left
	json_result['Rectangle']=json_item
	return json_result
	
    def theId(self):
        """
        TEST
        """
        return self.getId()

    def style(self):
	"""
	TEST
	"""
	style="position:relative"
	return style

    def theLinky(self):
        """
        return a link to this container's standard view
        """
        theLink = self.absolute_url()
        return theLink

    security.declarePublic('showRectangle')
    def showRectangle(self):
        """
        TEST 
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate = skin.showRectangle
        return showTemplate()

    def getElements(self):
	"""
	Returns a list of elements in the container
	"""
	elements = self.listFolderContents() 
	return elements

    def getPreviousElement(self,givenElement):
	"""
	Returns previous element in the list
	"""
	previousElement = None
	for element in self.getElements():
	    if element==givenElement:
		return previousElement
	    previousElement=element
	return None

    security.declarePublic('setWidth')
    def setWidth(self,width):
	"""
	TEST
	"""
	self.width=width

    security.declarePublic('setHeight')
    def setWidth(self,height):
	"""
	TEST
	"""
	self.height=height

    security.declarePublic('getWidth')
    def getWidth(self):
        """
        TEST
        """
        width = 0
	pixWidth = 0
	richWidth = 0
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        for item in items:
            pixWidth=item.getWidth()	
	    return pixWidth
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        numberOfColumns = 0
        for item in items:
            richWidth+=item.getWidth()	
            numberOfColumns += 1
	return richWidth

    security.declarePublic('getHeight')
    def getHeight(self):
        """
        TEST
        """
        height = 0
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        for item in items:
            height+=item.getHeight()	
        items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
        for item in items:
            height+=item.getHeight()	
        items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
        for item in items:
            height+=item.getHeight()	
	richHeight = 0
	numberOfColumns = 0
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        for item in items:
            richHeight+=item.getHeight()	
	    numberOfColumns += 1
	    break
	if numberOfColumns > 0:
	    height += int(richHeight/numberOfColumns)
        return height

    def contains(self): 
        """
        Test
        """
        items = self.listItems()
        return items

    def toggleDivTagsOn(self):
        """
        return true if Div Tags are on.
        """
        return self.getToggleDivTagsOn() 

    def just(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        justTemplate=skin.justRectangle
        return justTemplate()

    def getLines(self,columnid):
        return self['columnid'].getLines()

    def listColumns(self):
        """
        hey!
        """
        return self.returnInput()

    def topItem(self):
        """
        TEST
        """
        skin = self.portal_skins.newspaper_templates
        topTemplate=skin.topRectangle
        return topTemplate()

    def topList(self):
        """
        TEST
        """
        skin = self.portal_skins.newspaper_templates
        topList=skin.topList
        return topList()


    def listKeys(self):
        """
        hey!
        """
        returnObjects = []
        keys = self.keys()
        for key in keys:
            returnObjects.append(self[key])
        return returnObjects

    def returnInput(self):
        """
        Test
        """
        stringValue = ""
        items = self.listFolderContents(contentFilter={"portal_type":"Column"})
        #items = self.contentItems()
        #for item in items:
        #    stringValue += item[1].just()
        #return stringValue
        #urls=[]
        #for item in items:
    #	if item.getHeadline() == True:
    #            urls.append(item)
    #    for item in items:
    #	if item.getHeadline() == False:
    #            urls.append(item)
        return items

    def getImage(self):
        """
        Test
        """
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        return items[0].getPicture()


    def web(self):
        """
        Test
        """
        result = ""
        for item in self.listFolderContents():
            result += item.web()
        return result

    def getPosition(self):
	"""
	Returns the position of the Rectangle.
	"""
	left = self.getLeft()
	top = self.getTop()
	return (left,top)


    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
        """
        Test
        """
        y = y  + 40	
        left = self.getLeft()
        top = self.getTop()
	width = self.getRwidth()
	height = self.getRheight()
	color = str(self.getColor())
	caption = self.getCaption()
	#print color
	sRed = color[1:3]
	sGreen = color[3:5]
	sBlue = color[5:7]
	#print "%s" % sRed
	#print "%s" % sGreen
	#print "%s" % sBlue
	iRed = int(sRed,16)
	iGreen = int(sGreen,16)
	iBlue = int(sBlue,16)
	#print "%i" % iRed
	#print "%i" % iGreen
	#print "%i" % iBlue
	fRed = float(iRed) / 255
	fGreen = float(iGreen) / 255
	fBlue = float(iBlue) / 255
	#print "%f" % fRed
	#print "%f" % fGreen
	#print "%f" % fBlue
        #print self.Title()
        self.pagenumber=pagenumber
        #skin = self.portal_skins.newspaper_templates
        skinTool = getToolByName(self, 'portal_skins')
        #containercontainer = skinTool.newspaper_templates.test.getPhysicalPath()
        #containercontainer = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/'+self.Title()
        #print containercontainer
        #obj = PDFPageTemplate(self.Title(),containercontainer)
        print "Rectangle: %s" % self.Title()
        #result=obj.continuePDF(c,left,top,REQUEST,self,pagenumber)
	c.setFillColorRGB(fRed,fGreen,fBlue)
	c.rect(left,top,width,height,fill=1)
	c.setFillColorRGB(0,0,0)
	# Caption
        textobject = c.beginText()
        parent = self.aq_inner.aq_parent
        xtext = left + width / 4
        fontsize = 18
        textobject.setTextOrigin(left+10,top+10)
        textobject.setFont("Times-Roman", fontsize)
        textobject.textLine(caption)
        c.drawText(textobject)
        return (x,y)

    def getXOffset(self):
        """
        Test
        """
        return 0

    def getYOffset(self):
        """
        Test
        """
        return 0

    def pdf(self):
        """
        PDF
        """
        return "PDF"

    def block(self):
        """
        BLOCK
        """
        return "BLOCK"

    def listItems(self):
        """
        hey
        """
        parent = self.aq_inner.aq_parent
        items = parent.listFolderContents(contentFilter={"portal_type":"Broadsheet"})
        return items

    def snapshot(self):
        """
        """
        width = self.getWidth()
        height = self.getHeight() 
        return self.getSnapshot(width,height)

    def getEditsnap(self,top,left,width,height,useNumberOfColumns=0):
        """
        snap content
        """
        snapshot="<div>"
        items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        numberOfColumns = 0
	richWidth = 0
        for item in items:
            numberOfColumns += 1
	if useNumberOfColumns == 0:
	    	richWidth += item.getWidth()
	else:
		countColumns = 0
		for item in items:
			richWidth += item.getWidth()
			countColumns += 1
			if countColumns == useNumberOfColumns:
				break;
	useHeight = int(height/useNumberOfColumns)
        for item in items:
	    item.setNumberOfColumns(useNumberOfColumns)
            snapresult = item.getSnapshot(richWidth,height)
            snapshot += snapresult[0]
            break
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        snapshot += "</div>"
        return snapshot


    def getDimensions(self):
	"""
	returns the system given position
	"""
	top = self.getTop()
	left = self.getLeft()
	width = self.getWidth()
	height = self.getHeight()
	return top, left, width, height

    def getSnapshot(self,width,height):
        """
        snap content
        """
	broadsheet = self.aq_inner.aq_parent
	(bT,bL,bW,bH,bB,bR) = broadsheet.getBoundingBox(self.id)
	# New Rectangle must be positioned outside of Bounding Box.
	
        top = self.getTop()
        left = self.getLeft()
	width = self.getWidth()
	height = self.getHeight()
	# test bounding box
	freeSpaces = broadsheet.getFreeSpaces(self.id,1200,0)
	print "free Spaces"
	print freeSpaces
	# use first Free Space
	top = bT
	left = bL
	# if first choose first
	for freeSpace in freeSpaces:
	    fT=freeSpace[0]
	    fL=freeSpace[1]
	    fW=freeSpace[2]
	    fH=freeSpace[3]
	    if fW == 0:
#		if fH > height:
		top = fT
		left =fL
		break 
	    if fH == 0:
	#	if fW > width:
		top = fT
		left = fL
		break
	# update top and left with new coordinates
	# so that bounding box will be recomputed
	# with new position
	broadsheet.updateBoundingBox(self.id,top,left+100,width,height)	
	useheight = height
	snapitem = ""
        items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapitem += snapresult[0]
	    #snapshot += "HEADLINE"
        items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapitem += snapresult[0]
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        numberOfColumns = 0
        for item in items:
            numberOfColumns += 1
	    useheight = int(height/numberOfColumns)
        for item in items:
        	snapresult = item.getSnapshot(width,useheight,numberOfColumns)
        	snapitem  += snapresult[0]
            	break
    #snapshot += "RICH"
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapitem += snapresult[0]
        snapshot = "<div 'background-color:white;opacity:1;'>"
	snapshot += snapitem;
        snapshot += "</div>"
        return snapshot


    security.declarePublic('getNumberOfColumns')
    def getNumberOfColumns(self):
	"""
	Return the number of Columns
	"""
	numberOfColumns = 0
	items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
	for item in items:
		numberOfColumns += 1
	if numberOfColumns == 0:
		numberOfColumns = 1
	return numberOfColumns
	
    security.declarePublic('full')
    def full(self):
        """
        snap content
        """
        width = 960
        height = 1120
        top = self.getTop()
        left = self.getLeft()
        top = int(1.2 * float(top))
        left = int(1.2 * float(left))
        top = 180
        snapshot = "<div style='position:absolute;top:"
        snapshot += str(top)
        snapshot += "px'>"
        items = self.listFolderContents(contentFilter={"portal_type":"Headline"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        items = self.listFolderContents(contentFilter={"portal_type":"TextColumn"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        items = self.listFolderContents(contentFilter={"portal_type":"RichColumn"})
        numberOfColumns = 0
        for item in items:
            numberOfColumns += 1
        if numberOfColumns == 0:
            numberOfColumns = 1
        widthOfOneColumn = float(width)/numberOfColumns
        for item in items:
            snapresult = item.alltext(width,height)
            snapshot += snapresult
            break
        items = self.listFolderContents(contentFilter={"portal_type":"Pix"})
        for item in items:
            snapresult = item.getSnapshot(width,height)
            snapshot += snapresult[0]
        snapshot += "</div>"
        return snapshot

#    
#    def getSnapshot(self,width,height):
#	"""
#	snapshot
#	"""
#	snapshot = "<div class='container'>"
#	for item in self.listFolderContents():
#	    (snap,returnWidth,returnHeight) = item.getSnapshot(width,height)
#	    snapshot += snap
#	    height -= returnHeight
#	    if height <= 0:
#	        break
#	    snapshot += "<br/>"
#	snapshot += "</div>"
#	return snapshot

registerType(Rectangle, PROJECTNAME)
# end of class Rectangle

##code-section module-footer #fill in your manual code here
##/code-section module-footer
