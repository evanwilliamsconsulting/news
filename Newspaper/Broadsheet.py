# -*- coding: utf-8 -*-
#
# File: Broadsheet.py
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
from Products.Archetypes.Schema import Schema
from Products.Archetypes.Field import *
from Products.Archetypes.Widget import *
from Products.Archetypes.atapi import *
from zope.interface import implements
from plone.portlets.interfaces import ILocalPortletAssignable
import interfaces

from Products.Five.browser import BrowserView

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

from Products.Five.browser import BrowserView

import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
        name='pageNo',
        widget=IntegerField._properties['widget'](
            label='Pageno',
            label_msgid='Newspaper_label_pageNo',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='pageWidth',
        widget=IntegerField._properties['widget'](
            label='Pagewidth',
            label_msgid='Newspaper_label_pageWidth',
            i18n_domain='Newspaper',
            ),
        ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Broadsheet_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Broadsheet(NewsFolder.__class__): pass

class BroadsheetListpos(BrowserView):
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
	json_item['Broadsheet']=title
	items = self.context.listposshort()
	pretty = json.dumps(items)    
	return pretty 


class BroadsheetJSON(BrowserView):
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
	json_item['Broadsheet']=title
	items = self.context.listposshort()
	json_item['broadsheet']=items
	pretty = json.dumps(json_item)    
	return pretty 

class BroadsheetView(BrowserView):
    """ A View of the Widget """
    def __init__(self, context, request):
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
	"""  call """
	index = self.request.index
	self.blocks = self.context.showblocks(index)

class EditView(BrowserView):
    """ A View of the Widget """
    def __init__(self, context, request):
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
    #def __call__():
    #

class Broadsheet(OrderedBaseFolder,ExtensibleMetadata,BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBroadsheet,ILocalPortletAssignable)

    meta_type = 'Broadsheet'
    _at_rename_after_creation = True

    schema = Broadsheet_schema

    #__metaclass__=M_Broadsheet

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    something = 'ferf'
    top = 0
    left = 0
    width = 0
    height = 0

    # for Update bounding box
    nT = nL = nW = nH = nB = nR = 0
    nName = ""

    # Methods

    def getIssueUrl(self):
        """
        Test 
        """
        parent = self.aq_inner.aq_parent
        #link = parent.getId()
        link = "" 
        return link

    def view(self,REQUEST):
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.justBroadsheet
        return showTemplate(REQUEST)

    def show(self): 
        """
        Test
        """
        return self.web()

    def pageNumber(self):
        """
        Return Page Number
        """
        pageno = self.getPageNo()
        if pageno == 1:
            textValue = "One"
        elif pageno == 2:
            textValue = "Two"
        elif pageno == 3:
            textValue = "Three"
        else:
            textValue = "Four"
        theReturn = "<a href='"
        theReturn += self.absolute_url()
        theReturn += "'>"
        theReturn += textValue
        theReturn += "</a>"
        return theReturn

    def linky(self):
        """
        API Universal per product to return link to this pages's view
        """
        return self.absolute_url()

    def what(self,REQUEST):
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.justBroadsheet
        return showTemplate(REQUEST)

    def just(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.justBroadsheet
        return showTemplate()

    def blocks(self):
        """
        Test
        """
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        return blocks

    def Blocks(self):
        """
        Test
        """
        Blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        Containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        All = self.listFolderContents()
        return All 

    def Pages(self):
        """
        Test
        """
        parent = self.aq_inner.aq_parent
        return parent.pages()

    def listContainers(self):
        """
        """
        return self.returnInput()

    def returnInput(self):
        """
        Test
        """
        stringValue = ""
        items = self.listFolderContents(contentFilter={"portal_type":"Container"})
        #items=self.contentItems()
        return items

    def callPDTBySameName(self,show,REQUEST,parent,top,left):
        """
        Test
        """
        thePath = '/opt/development/newholland/press/products/Newspaper/skins/newspaper_templates/' + self.Title() + '.pd'
        containercontainer = PDFPageTemplate(self.Title(),thePath)
        showTemplate=containercontainer.continueWEB(REQUEST,parent,thePath,'0','0','0','0','0','0')
        return showTemplate[0]

    def web(self):
        """
        """
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        retval = "<div>"
        for block in blocks:
            retval+=block.web()
        retval += "</div>"
        retval += "<div>"
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        for container in containers:
            retval+=container.web()
        retval += "</div>"
        return retval

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
        """
        Test
        """
        #textobject = c.beginText()
        #textobject.setTextOrigin(x,y)
        #textobject.setFont('FilosBold',12)
        #textobject.textLine("Broadsheet")
        #c.drawText(textobject)
        ##print self.Title()
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        for block in blocks:
            #print block
            block.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber,outline)
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        for container in containers:
            #print container
            container.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber,outline)
        rectangles = self.listFolderContents(contentFilter={"portal_type":"Rectangle"})
        for rectangle in rectangles:
            #print container
            rectangle.callPDFPDTBySameName(c,x,y,REQUEST,parent,top,pagenumber,outline)
        return (x,y)

    def editsnap(self):
        """
        Test
        """
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
        retval = "<div id='hFinderFiles'>"
        red = 0x40;
        green = 0x40;
        blue = 0x40;
        iter = 0;
        for block in items:
            iter  += 1
            top=block.getTop()
            left=block.getLeft()
            width = block.getWidth()
            height = block.getHeight()
            width *= .4 
            height *= .4 
            top *= .4 
            left *= .4 
            someval = "<div "
            cssclass = "hFinderDirectory" + str(iter)
            someval += "class='" + cssclass + "' title='/"+block.id+"' id='" + block.id + "' "
            someval += "style='"
            rgb = format((blue<<16)|(green<<8)|red, '06x')
            blue += 40
            red += 40
            green += 40
            someval += "background-color:#"+rgb+";"
            someval += "position:absolute;"
            someval += "top:"+str(top)+"px;"
            someval += "left:"+str(left)+"px;"
            someval += "width:"+str(width)+"px;"
            someval += "height:"+str(height)+"px;"
            someval += "z-index:20;"
            someval += "border-style:none;border-width:1px;"
            someval += "'>"
            someval += "<div>"
            width *= .8
            someval += block.getEditsnap(top,left,width,height,1)
            someval += "</div>"
            someval += "</div>"
            retval += someval
        retval += "</div>"
        retval += "<div id='hFinderEnd'></div>"
        return retval
#

    def listposshort(self):
	"""
	TEST
	"""
	json_item = {}
	# Where is box in relation to previous bounding box?
	isBelow = False
	isRight = False
	isAbove = False
	isLeft = False
	additionalBottom = additionalTop = additionalLeft = additionalRight = 0
	# Previous coordinates
	pL = pB = pW = pH = 0
	pT = pR = 10

	hOverlap = vOverlap = Overlap = False
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	firstTime = True
	additionalX = additionalY = 0
	# Bounding coordinates
	bR = bB = bW = bH = 0
	bT = bL = 10
	dW = 0
	dL = 0
	dT = 0
	dH = 0
	dR = 0
	dB = 0
	previousHeight = 0
	theHeight = 0
	diff = 0
	prevTop = 100
	order = 1
	freeSpace = []
	oldFreeSpace = []
	newFreeSpace = []
	for block in items:
		print block.id
		position = {}
		freeSpace = []
		isBelow = False
		isRight = False
		isAbove = False
		isLeft = False
		additionalBottom = additionalTop = additionalLeft = additionalRight = 0
		top = block.getTop()
		topoffset = top - 10
		top = 10
		left = block.getLeft()
		width = block.getWidth()
		height = previousHeight
		numberOfColumns = block.getNumberOfColumns()
		theHeight = previousHeight
		previousHeight = block.getHeight()
		height = block.getHeight()
		print height
		print top,left,height,width,numberOfColumns
		#previousHeight = top
		right = left + width
		bottom = top + height
		#if left >= pL and left <= pR:
		#	hOverlap = True
		#if right <= pR and right >= pL:
		#	hOverlap = True
		#if top >= pT and top <= pB:
		#	vOverlap = True
		#if bottom <= pB and bottom >= pT:
		#	vOverlap = True
		#if hOverlap and vOverlap:
		#	Overlap = True
		#if Overlap == True:
		#       |-------------------|
		#	|                   |
		#       |           |-----------|
		#	|	    |       |   |
                #       |           |       |   |
		#       |-----------|-------|---|
		#                   |           |
		#                   |-----------|
		#	additionalY = height - (bB - top)
		#	additionalX = width - (bR - left)
		#else:
			# There is no overlap.
			# That's great!
			# Determine for each dimension
			# if new box is above or below or left or right
			# prior to recalculating bounding box.
			
			# First vertical.
			# if height + top is greater than the previous bounding bottom
			# then new box is below old bounding box.
		    
			# If we are doing all this do we also need isOverlap
			# Yes but maybe not to calculate as above!
		
		# Here is where we jammd the this block
		thereWasNoFit = True
		bT = pT
		bL = pR 
		bW = width
		bH = height
		bB = bT + bH + 10
		bR = bL + bW + 10
		dL = bL
		testNumberOfColumns = numberOfColumns
		for space in oldFreeSpace:
			oT = space[0]
			oL = space[1]
			oH = space[2]
			oW = space[3]
			dW = oW
			if width <= oW and height <= oH:
				thereWasNoFit = False
				bT = oT
				bL = oL
				bW = oW
				bH = height
				dL = oL
				bB = bT + bH + 10
				bR = bL + bW + 10

		if thereWasNoFit == True:
			for space in oldFreeSpace:
				oT = space[0]
				oL = space[1]
				oH = space[2]
				oW = space[3]
				dW = oW
				testNumberOfColumns = numberOfColumns
				while testNumberOfColumns > 0:
					testWidth = (width / numberOfColumns) * testNumberOfColumns
					if testWidth <= oW and height <= oH:
						thereWasNoFit = False
						bT = oT
						bL = oL
						bW = oW
						bH = height
						dL = oL
						bB = bT + bH + 10
						bR = bL + bW + 10
						break
					testNumberOfColumns -= 1	

		if thereWasNoFit == True:
			for space in oldFreeSpace:
				oT = space[0]
				oL = space[1]
				oH = space[2]
				oW = space[3]
				dW = oW
				if width<= oW:
					thereWasNoFit = False
					bT = oT
					bL = oL
					bW = oW
					bH = height
					dL = oL
					bB = bT + bH + 10
					bR = bL + bW + 10
					break
				elif height <= oH:
					thereWasNoFit = False
					bT = oT
					bL = oL
					bW = oW
					bH = height
					dL = oL
					bB = bT + bH + 10
					bR = bL + bW + 10
					break

		bW = width
		position['top']=bT
		position['left']=dL
		position['width']=bW
		if testNumberOfColumns == 0:
			position['cols']=1;
			bH = int(height)
		else:
			position['cols']=testNumberOfColumns
			bH = int(height/testNumberOfColumns)
		dH = bH
		position['height']=bH
		bB = bT + bH

		prevTop = block.getTop()
		print prevTop
		position['order']=order
		order += 1
		sB = abs(bB - pB)
		sR = abs(bR - pR)
		sT = abs(bT - pT)
		sL = abs(bL - pL)
		freeSpace = []
		freeSpaceTop = (bT,bL + bW ,5000-bT-10,1000- bW - bL +10)
		freeSpace.append(freeSpaceTop)
		freeSpaceTop = (bB+10,dL,5000-bB-20,1000 - bW -bL + 10)
		freeSpace.append(freeSpaceTop)
		
		for space in oldFreeSpace:
			# if this is the block above don't add
			if not (bT == space[0] and bL == space[1]):
				newFreeSpace.append(space)
		for space in freeSpace:
			oT = space[0]
			oL = space[1]
			oH = space[2]
			oW = space[3]
			if dL >= oL:
				oSpace = (bT+dH+10,oL,5000-bB-10,width)
				newFreeSpace.append(oSpace)
			elif bT >= oT:
				oSpace = (oT,bL+width+10,5000-bT,1000-width)
				newFreeSpace.append(oSpace) 
			else:
				newFreeSpace.append(space)
		oldFreeSpace = newFreeSpace
		freeSpace = newFreeSpace
		newFreeSpace = []
		free = {}
		freeCount = 1
		for space in freeSpace:
			free[freeCount]=space
			freeCount += 1
		position['free']=free
		freeSpace = []
		position['name']=block.id
		json_item[block.id]=position
		pH = bH
		pL = dL
		pB = bB
		pT = bT
		pR = bR
		pW = width
	json_item2 = {}
	for order in range(1,1+len(json_item)):
		for item in json_item:
			theItem = json_item[item]
			if theItem['order']==order:
				name = theItem['name']
				json_item2[order]=theItem
	return json_item2

    
    def listpos(self):
	"""
	TEST
	"""
	# Where is box in relation to previous bounding box?
	isBelow = False
	isRight = False
	isAbove = False
	isLeft = False
	additionalBottom = additionalTop = additionalLeft = additionalRight = 0
	# Previous coordinates
	pT = pL = pR = pB = pW = pH = 0

	hOverlap = vOverlap = Overlap = False
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
	retval = "<div>";
	retval += "<table><tr>"
	retval += "<td>Id</td><td>Top</td><td>Left</td><td>Width</td><td>Height</td><td>Right</td><td>Bottom</td><td>Overlap</td>"
	retval += "<td>pTop</td><td>pLeft</td><td>pWidth</td><td>pHeight</td><td>pRight</td><td>pBottom</td>"
	retval += "<td>bTop</td><td>bLeft</td><td>bWidth</td><td>bHeight</td><td>bRight</td><td>bBottom</td>"
	retval += "</tr>"
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	firstTime = True
	additionalX = additionalY = 0
	# Bounding coordinates
	bT = bL = bR = bB = bW = bH = 0
	for block in items:
		isBelow = False
		isRight = False
		isAbove = False
		isLeft = False
		additionalBottom = additionalTop = additionalLeft = additionalRight = 0
		top = block.getTop()
		left = block.getLeft()
		width = block.getWidth()
		height = block.getHeight()
		right = left + width
		bottom = top + height
		#if left >= pL and left <= pR:
		#	hOverlap = True
		#if right <= pR and right >= pL:
		#	hOverlap = True
		#if top >= pT and top <= pB:
		#	vOverlap = True
		#if bottom <= pB and bottom >= pT:
		#	vOverlap = True
		#if hOverlap and vOverlap:
		#	Overlap = True
		#if Overlap == True:
		#       |-------------------|
		#	|                   |
		#       |           |-----------|
		#	|	    |       |   |
                #       |           |       |   |
		#       |-----------|-------|---|
		#                   |           |
		#                   |-----------|
		#	additionalY = height - (bB - top)
		#	additionalX = width - (bR - left)
		#else:
			# There is no overlap.
			# That's great!
			# Determine for each dimension
			# if new box is above or below or left or right
			# prior to recalculating bounding box.
			
			# First vertical.
			# if height + top is greater than the previous bounding bottom
			# then new box is below old bounding box.
		    
			# If we are doing all this do we also need isOverlap
			# Yes but maybe not to calculate as above!
		if (height + top) > bB:
		    isBelow = True
		    additionalBottom = height + top - bB
		if top < bT:
		    isAbove = True
		    additionalTop = bT - top
		if (width + left) > bR:
		    isRight = True
		    additionalRight = width + left - bR
		if left < bL:
		    isLeft = True
		    additionalLeft = bL - left
		if isRight:
		    bW += additionalRight
		    bR = right
		if isLeft:
		    bW += additionalLeft
		    bL = left
		if isAbove:
		    bH += additionalTop
		    bT = top
		if isBelow:
		    bH += additionalBottom
		    bB = bottom
		retval += "<tr>"
		retval += "<td>"
		retval += block.id
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getTop())
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getLeft())
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getWidth())
		retval += "</td>"
		retval += "<td>"
		retval += str(block.getHeight())
		retval += "</td>"
		retval += "<td>"
		retval += str(right)
		retval += "</td>"
		retval += "<td>"
		retval += str(bottom)
		retval += "</td>"
		retval += "<td>"
		if Overlap == True:
			retval += "Overlap"	
		retval += "</td>"
		if firstTime:
			firstTime = False
			bL = left
			bT = top
		retval += "<td>"
		retval += str(pT)
		retval += "</td>"
		retval += "<td>"
		retval += str(pL)
		retval += "</td>"
		retval += "<td>"
		retval += str(pW)
		retval += "</td>"
		retval += "<td>"
		retval += str(pH)
		retval += "</td>"
		retval += "<td>"
		retval += str(pR)
		retval += "</td>"
		retval += "<td>"
		retval += str(pB)
		retval += "</td>"
		retval += "<td>"
		retval += str(bT)
		retval += "</td>"
		retval += "<td>"
		retval += str(bL)
		retval += "</td>"
		retval += "<td>"
		retval += str(bW)
		retval += "</td>"
		retval += "<td>"
		retval += str(bH)
		retval += "</td>"
		retval += "<td>"
		retval += str(bR)
		retval += "</td>"
		retval += "<td>"
		retval += str(bB)
		retval += "</td>"
		freeSpaces = self.getFreeSpaces(block.id,1000,0)
		retval += "</tr>"
		retval += "<td>Free Space</td><td colspan='19'>"
		retval += "%s" % freeSpaces
		retval += "</td>"
		retval += "</tr>"
		pH = height
		pL = left
		pB = bottom
		pT = top
		pR = right
		pW = width
	retval += "</table>"
	retval += "</div>"
	return retval

    def updateBoundingBox(self,name,nT,nL,nW,nH):
	"""
	TEST
	"""
	self.nT = nT
	self.nL = nL
	self.nW = nW
	self.nH = nH
	self.nName = name
	self.nB = nT + nH
	self.nR = nL + nW

    def getPreviousBoundingBox(self,name,bT,bL):
	"""
	TEST
	"""
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	previousBoundingBox = (0,0,0,0,0,0)
	for block in items:
		if block.id == name:
			return previousBoundingBox
		else:
			previousBoundingBox = self.getBoundingBox(name,bT,bL)
	return previousBoundingBox

    def getBoundingBox(self,name,usetop=10,useleft=10):
	"""
	TEST
	"""
	# Where is box in relation to previous bounding box?
	isBelow = False
	isRight = False
	isAbove = False
	isLeft = False
	additionalBottom = additionalTop = additionalLeft = additionalRight = 0
	# Previous coordinates
	pT = pL = pR = pB = pW = pH = 0

	hOverlap = vOverlap = Overlap = False
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
	retval = (0,0,0,0,0,0)
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
	firstTime = True
	additionalX = additionalY = 0
	# Bounding coordinates
	bT = usetop
	bL = useleft
	bW = 0
	bH = 0
	bB = bT
	bR = bL
	#print "Start Bounding Box Algorithm"
	for block in items:
		#print block.id
		isBelow = False
		isRight = False
		isAbove = False
		isLeft = False
		additionalBottom = additionalTop = additionalLeft = additionalRight = 0
		#print "boundingBox, top: " + str(bT) + "left: " + str(bL) + "width: " + str(bW) + "height: " + str(bH)
		top = block.getTop() - 150
		left = block.getLeft()
		width = block.getWidth()
		height = block.getHeight()
		#print "top: " + str(top) + " left: " + str(left) + " width: " + str(width)  + " height: " + str(height)
			#       |-------------------|
			#	|                   |
			#       |           |-----------|
			#	|	    |       |   |
        	        #       |           |       |   |
			#       |-----------|-------|---|
			#                   |           |
			#                   |-----------|
			#	additionalY = height - (bB - top)
			#	additionalX = width - (bR - left)
			#else:
			# There is no overlap.
			# That's great!
			# Determine for each dimension
			# if new box is above or below or left or right
			# prior to recalculating bounding box.
			
			# First vertical.
			# if height + top is greater than the previous bounding bottom
			# then new box is below old bounding box.
		    
			# If we are doing all this do we also need isOverlap
			# Yes but maybe not to calculate as above!
		checkHeight = height + top + bT
		#print "check Height: " + str(checkHeight)
		if checkHeight > bB:
			isBelow = True
			additionalBottom = height + top + bT - bB
			#if top < bT: -- impossible!
		    	#	isAbove = True
		    	#	additionalTop = bT - top
		checkWidth = width + left + bL
		#print "check Width: " + str(checkWidth)
		if checkWidth > bR:
			isRight = True
			additionalRight = width + left + bL - bR
			#if left < bL: --impossible
		    	#	isLeft = True
		    	#	additionalLeft = bL - left
		if isRight:
			#print "is Right"
			bW += additionalRight
			bR += additionalRight
		if isBelow:
			#print "is Below"
			bH += additionalBottom
			bB += additionalBottom
		if name == block.id:
			#print "Bounding Box"
			retval = (bT,bL,bW,bH,bB,bR)
			#print retval
			return retval
	return retval

    def getFreeSpaces(self,name,widthMax=0,heightMax=0,usetop=10,useleft=10):
	# returns a list of (T,L,W,H) representing Free Space
	# W or H is 0 if infinite to right or bottom.
	# say you already have a bounding box
	# that is a previous bounding box
	# and the current box used to expand the
	# previous bounding box to the current bounding box
	# 
	# There are likely to be empty spaces
	# as well as the spaces around the new bounding box
	# the free space list
	# is the difference between the new bounding box
	# and the old bounding box
	# with respect to the infinite space around
	# the new bounding box.
	#
	#  _____________________________ 
	# |                 |           |
	# |      prev       |           |
	# -------------------           |
	# |                             |
	# |__________current____________|
	#
	#
	# There are a number of ways that the space can be
	# listed: free space will list from top to bottom as follows:
	#
	#                   ____________
	#                   |           |
	# and 
	#
	# _______________________________
	# |                              |
        #
	# and
	#
	# ________________________________
	# |
	# |_______________________________
	#  
	#                   ______________
	#                   |
	#                   |
	#                   |
	#                   |_____________
	#
	# this is all great except that we have made a top left assumption again
	# also depending on whether the page is to be
	# right expansive or bottom expansive this may include only two
	# of the four cases
	(bT,bL,bW,bH,bB,bR) = self.getBoundingBox(name,usetop,useleft)
	(pbT,pbL,pbW,pbH,pbB,pbR) = self.getPreviousBoundingBox(name,usetop,useleft)
	# how do we then compute the symmetric difference as above?
	# bounding box always completely includes the previous bounding box
	sB = abs(bB - pbB)
	sR = abs(bR - pbR)
	sT = abs(bT - pbT)
	sL = abs(bL - pbL)
	# List of open spaces
	freeSpace = []
	# Assume that we are going vertical right now!
	freeSpaceTop = (bT,bR,sR+bR,sB+bB)
	freeSpace.append(freeSpaceTop)
	freeSpaceTop = (bB,bL,sR+bR,sB+bB)
	freeSpace.append(freeSpaceTop)
	freeSpaceBottom = (bB,bR,sR+bR,sB+bB)
	freeSpace.append(freeSpaceBottom)
	return freeSpace
	
    def diagnostic(self,index):
        """
        Test
        """
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = {}
        for container in containers:
	    items[container.id]=container
        for block in blocks:
	    items[block.id]=block
        red = 0x40;
        green = 0x40;
        blue = 0x40;
        iter = 0;
	listpos = self.listposshort()
	#retval = "<div style='position:absolute;'>";
	retval = "";
	free = []
        for position in listpos:
	    print iter
	    print index
	    if int(iter) == int(index):
	    	print "return"
	    	break
            iter  += 1
	    item = listpos[position]
	    idd = item['name']
	    top = int(item['top'])
	    left = int(item['left'])
	    width = int(item['width'])
	    height = int(item['height'])
	    useCols = item['cols'];
	    totalNumberOfColumns = items[idd].getNumberOfColumns()
	    print "totalNumberOfColumns"
	    print totalNumberOfColumns
	    print useCols
		
	    width = int(( width / totalNumberOfColumns)*useCols)
	    free = item['free']
	    descriptive = "<div "
	    descriptive += "style='"
	    descriptive += "background-color:pink;height:80px;width:"
	    descriptive += str(width)
	    descriptive += "px'>"
	    descriptive += "<span>"
	    descriptive += str(iter)
	    descriptive += "</span>" 
	    descriptive += "<span> width: " + str(width) + "height: " + str(height)
	    descriptive += "</span>" 
	    descriptive += "<span>"
	    descriptive += "<span> top: " + str(top) + "left: " + str(left)
	    descriptive += "</span>" 
	    descriptive += "</div>"	  
            someval = "<div "
            cssclass = "hFinderDirectory" + str(iter)
            #someval += "title='/"+block.id+"' id='" + block.id + "' "
            #someval += "class='" + cssclass + "' title='/"+block.id+"' id='" + block.id + "' "
            someval += "style='"
            someval += "position:absolute;"
            someval += "top:"+str(top)+"px;"
            someval += "left:"+str(left)+"px;"
            someval += "width:"+str(width)+"px;"
            someval += "height:"+str(height)+"px;"
            someval += "z-index:20;"
            someval += "border-color:black;border-style:none;border-width:1px;"
            someval += "'>"
	    someval += descriptive
	    #if show=="yes":
            #someval += "<div>"
            snapWidth = width 
            snapHeight = height
	    theItem = items[item['name']]
            #someval += "</div>"
            someval += "<div>"
            snapWidth = width 
            snapHeight = height - 20
            #someval += theItem.getEditsnap(top,left,snapWidth,snapHeight)
            #someval += block.getEditsnap(snapWidth,snapHeight)
            someval += "</div>"
            someval += "</div>"
            retval += someval
	for freeItem in free:
	    space = free[freeItem]
	    spaceTop = space[0]
	    spaceLeft = space[1]
	    spaceHeight = space[2]
	    spaceWidth = space[3]
	    freeSpaceDiv =  "<div "
	    freeSpaceDiv += "style='"
	    freeSpaceDiv += "top:"
	    freeSpaceDiv += str(spaceTop)
	    freeSpaceDiv += "px;left:"
	    freeSpaceDiv += str(spaceLeft)
	    freeSpaceDiv += "px;height:"
	    freeSpaceDiv += str(spaceHeight)
	    freeSpaceDiv += "px;width:"
	    freeSpaceDiv += str(spaceWidth)
	    freeSpaceDiv += "px;position:absolute;border-style:dotted;border-color:red;border-width:1px;"
	    freeSpaceDiv += "'>"
	    freeSpaceDiv += str(iter)
	    freeSpaceDiv += "-"
	    freeSpaceDiv += str(freeItem)
	    freeSpaceDiv += "</div>"
	    retval+= freeSpaceDiv
	    retval += ""
        return retval

    def showblocks(self):
        """
        Test
        """
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = {}
        for container in containers:
	    items[container.id]=container
        for block in blocks:
	    items[block.id]=block
        red = 0x40;
        green = 0x40;
        blue = 0x40;
        iter = 0;
	listpos = self.listposshort()
	#retval = "<div style='position:absolute;'>";
	retval = "";
	free = []
	saveHeight = 0
	startTop = 0
        startLeft = 0
        for position in listpos:
	    #print iter
	    #print index
	    #if int(iter) == int(index):
	    #	print "return"
	    #	break
            iter  += 1
	    item = listpos[position]
	    top = int(item['top'])
	    if startTop == 0:
		startTop = top
	    left = int(item['left'])
	    if startLeft == 0:
                startLeft = left
	    width = int(item['width'])
	    height = int(item['height'])
	    saveHeight += height
	    useColumns = item['cols']
	    free = item['free']
	    descriptive = "<div "
	    descriptive += "style='"
	    descriptive += "background-color:pink;height:auto;width:"
	    descriptive += str(width)
	    descriptive += "'>"
	    descriptive += "<span>"
	    descriptive += str(iter)
	    descriptive += "</span>" 
	    descriptive += "<span> width: " + str(width) + "height: " + str(height)
	    descriptive += "</span>" 
	    descriptive += "<span>"
	    descriptive += "<span> top: " + str(top) + "left: " + str(left)
	    descriptive += "</span>" 
	    descriptive += "</div>"	  
            someval = "<div "
            cssclass = "hFinderDirectory" + str(iter)
            #someval += "title='/"+block.id+"' id='" + block.id + "' "
            #someval += "class='" + cssclass + "' title='/"+block.id+"' id='" + block.id + "' "
            someval += "style='"
            someval += "position:relative;"
            someval += "top:"+str(top)+"px;"
            someval += "left:"+str(left)+"px;"
            someval += "width:"+str(width)+"px;"
            #someval += "height:"+str(height)+"px;"
            someval += "height:auto;"
            someval += "z-index:20;"
            someval += "border-color:black;border-style:none;border-width:1px;"
            someval += "'>"
	    #someval += descriptive
	    #if show=="yes":
            someval += "<div>"
            snapWidth = width 
            snapHeight = height
	    theItem = items[item['name']]
            #someval += theItem.getEditsnap(top,left,snapWidth,snapHeight,useColumns)
            someval += theItem.getSnapshot(snapWidth,snapHeight)
            someval += "</div>"
            someval += "</div>"
            retval += someval
	#for freeItem in free:
	#    space = free[freeItem]
	#    spaceTop = space[0]
	#    spaceLeft = space[1]
	#    spaceHeight = space[2]
	#    spaceWidth = space[3]
	#    freeSpaceDiv =  "<div "
	#    freeSpaceDiv += "style='"
	#    freeSpaceDiv += "top:"
	#    freeSpaceDiv += str(spaceTop)
	#    freeSpaceDiv += "px;left:"
	#    freeSpaceDiv += str(spaceLeft)
	#    freeSpaceDiv += "px;height:auto;"
	#    #freeSpaceDiv += str(spaceHeight)
	#    #freeSpaceDiv += "px;width:"
	#    freeSpaceDiv += "width:"
	#    freeSpaceDiv += str(spaceWidth)
	#    freeSpaceDiv += "px;position:absolute;border-style:dotted;border-color:red;border-width:1px;"
	#    freeSpaceDiv += "'>"
	#    freeSpaceDiv += str(iter)
	#    freeSpaceDiv += "-"
	#    freeSpaceDiv += str(freeItem)
	#    freeSpaceDiv += "</div>"
	#    retval+= freeSpaceDiv
	#    retval += ""
	saveHeight += top 
	someDiv =  "<div "
	someDiv += "style='"
	someDiv += "top:"
	someDiv += str(startTop)
	someDiv += "px;left:"
	someDiv += str(startLeft)
	someDiv += "px;height:"
	someDiv += str(saveHeight)
	someDiv += "px;width:auto;border:none;border-width:1pt;"
	someDiv += "'>"
	someDiv += retval
	someDiv += "</div>"
        return someDiv 

    def listsnap(self):
        """
        Test
        """
        blocks = self.listFolderContents(contentFilter={"portal_type":"Block"})
        containers = self.listFolderContents(contentFilter={"portal_type":"Container"})
        items = []
        for container in containers:
            items.append(container)
        for block in blocks:
            items.append(block)
        red = 0x40;
        green = 0x40;
        blue = 0x40;
        iter = 0;
	listpos = self.listposshort()
	retval = "<div style='position:absolute;'>";
        for block in items:
            iter  += 1
	    position = listpos[iter]
	    top = int(position['top'])
	    left = int(position['left'])
	    width = int(position['width'])
	    height = int(position['height'])
	    order = int(position['order'])
	    descriptive = "<div "
	    descriptive += "style='"
	    descriptive += "background-color:pink;height:80px;width:"
	    descriptive += str(width)
	    descriptive += "'>"
	    descriptive += "<span>"
	    descriptive += block.id
	    descriptive += "</span>" 
	    descriptive += "<span> width: " + str(width) + "height: " + str(height)
	    descriptive += "</span>" 
	    descriptive += "<span>"
	    descriptive += "<span> top: " + str(top) + "left: " + str(left)
	    descriptive += "</span>" 
	    descriptive += "<span> order: " + str(order)
	    descriptive += "</span>" 
	    descriptive += "</div>"	  
            someval = "<div "
            cssclass = "hFinderDirectory" + str(iter)
            someval += "title='/"+block.id+"' id='" + block.id + "' "
            #someval += "class='" + cssclass + "' title='/"+block.id+"' id='" + block.id + "' "
            someval += "style='"
            rgb = format((blue<<16)|(green<<8)|red, '06x')
            blue += 40
            red += 40
            green += 40
            someval += "position:absolute;background-color:#"+rgb+";"
            someval += "top:"+str(top)+"px;"
            someval += "left:"+str(left)+"px;"
            someval += "z-index:20;"
            someval += "border-style:solid;border-width:1px;"
            someval += "'>"
	    someval += descriptive
            someval += "<div>"
            snapWidth = width 
            snapHeight = height
            someval += block.getEditsnap(top,left,snapWidth,snapHeight)
            someval += "</div>"
            someval += "</div>"
            retval += someval
	    break
	retval += "</div>"
        return retval

    def getTitle(self):
	return self.Title

    def breadcrumbs(self,REQUEST):
        # We do this here do maintain the rule that we must be wrapped
        container = self.aq_inner

        base = tuple(getMultiAdapter((container, REQUEST),
                                     name='absolute_url').breadcrumbs())

        return base


registerType(Broadsheet, PROJECTNAME)
# end of class Broadsheet

##code-section module-footer #fill in your manual code here
##/code-section module-footer
