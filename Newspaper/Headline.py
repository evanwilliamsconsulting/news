# -*- coding: utf-8 -*-
#
# File: Headline.py
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
import interfaces
import htmlentitydefs as entity

from Products.Five.browser import BrowserView
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from Products.Newspaper.Element import Element

from Products.Newspaper.Element import Element_schema

from Products.Five.browser import BrowserView
import json

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Headline',
        widget=StringField._properties['widget'](
            label='Headline',
            label_msgid='Newspaper_label_Headline',
            i18n_domain='Newspaper',
            ),
        ),
    StringField(
        name='Topline',
        widget=StringField._properties['widget'](
            label='Topline',
            label_msgid='Newspaper_label_topline',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='Usetopline',
        default=False,
        widget=BooleanField._properties['widget'](
            label='Use Top Line',
            label_msgid='Newspaper_label_usetopline',
            i18n_domain='Newspaper',
            ),
        ),
    IntegerField(
        name='Fontsize',
        widget=IntegerField._properties['widget'](
            label='Fontsize',
            label_msgid='Newspaper_label_Fontsize',
            i18n_domain='Newspaper',
            ),
        ), 
    StringField(
        name='headlineclass',
        default='headlineclass',
        widget=StringField._properties['widget'](
            label='Headline Class',
            label_msgid='Newspaper_label_headclass',
            i18n_domain='Newspaper',
            ),
        ),
    BooleanField(
        name='italic',
        default=False,
        widget=BooleanField._properties['widget'](
            label='italic',
            label_msgid='Newspaper_label_italic',
            i18n_domain='Newspaper',
            ),
        ),
),
)

Headline_schema = schema.copy() + Element_schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class HeadlineJSON(BrowserView):
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
        json_item['Headline']=title
        attributes = {}
        attributes['Headline']=self.context.getHeadline()
        attributes['Fontsize']=self.context.getFontsize()
        attributes['headlineclass']=self.context.getHeadlineclass()
        attributes['italic']=self.context.getItalic()
        json_item['attributes']=attributes
        pretty = json.dumps(json_item)    
        return pretty 

class HeadlineDiagnostic(BrowserView):
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

class HeadlineView(BrowserView):
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

class Headline(Element):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IHeadline)

    meta_type = 'Headline'
    _at_rename_after_creation = True

    schema = Headline_schema 

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def contains(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.showHeadline
        return showTemplate()

    def just(self): 
        """
        Test
        """
        skin = self.portal_skins.newspaper_templates
        justTemplate=skin.justLine
        return justTemplate()

    def show(self):
        """
        Show
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate = skin.showHeadline
        return showTemplate()

    def web(self):
        """
        Web
        """
        return self.getHeadline()

    def solo(self):
        """
        Jam out the line.
        """
        return self.getHeadline()

    def formatted(self):
        """
        The line formatted
        """
        return self.getHeadline()

    def getWidth(self):
        """
        Test
        """
        return 0

    def getHeight(self):
        """
        Test
        """
        return 70

    def getColumnWidth(self):
        """ 
        Test
        """
        theColumn=self.aq_inner.aq_parent
        theWidth=theColumn.getColumnWidth()
        return theWidth

    def setVerbage(self,verbage):
        """
        Test
        """
        self.setLineVerbage(verbage)

    def getLine(self):
        """
        Test
        """
        return self.getLineVerbage()

    def getFont(self):
        """
        getFontSize
        """
        fontSize = 3*self.getFontsize()/4
        fontPercent = int((fontSize/12)*100)
        return str(fontPercent)

    def callPDTBySameName(self,REQUEST,parent,top,left,width,height,start="",end=""):
        """
        Test
        """
        fontSize = str(3*self.getFontsize()/4)
        height = str(2*self.getFontsize())
        result = "<div id='"
        result += self.getId()
        result += "' class='headline' "
        #result += "style='border-style:solid;border-color:purple;border-width:2px;font-size:"
        result += "style='font-size:"
        result += fontSize
        result += "pt;"
        #result += "top:"
        #result += str(self.getTop()+int(top))
        #result += "px;"
        result += "position:relative;'>"
        #result += ">"
        result += start
        result += self.getHeadline()
        result += "</div>"
        top = str(self.getTop()+int(top)+int(height))
        return (result,top,left,width,height)

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
        """
        Test
        """
	fRed = .5
	fGreen = .5
	fBlue = .8
	nLeft = parent.getLeft()
	nTop = parent.getTop()
	left = nLeft
	top = 1185 - nTop
	width = 3
	height = 3
	fRed = 0
	fGreen = 0
	fBlue = 0
	c.setStrokeColorRGB(fRed,fGreen,fBlue)
	c.setFillColorRGB(fRed,fGreen,fBlue)
	rl1 = left
	rt1 = top
	rw1 = width
	rh1 = height
	#c.rect(left,top,width,height,fill=1)
        print "HEADLINE"
        glueX = self.getGlueX()
        glueY = self.getGlueY()
        skin = self.portal_skins.newspaper_templates
        theLine = self.getHeadline()
        print theLine
        textobject = c.beginText()
        parent = self.aq_inner.aq_parent
        xorig = x
        yorig = y
        (x,y) = self.getPosition()
        fontsize = self.getFontsize()
        textobject.setTextOrigin(x,1185-(y+fontsize))
	rl2 = x
	rt2 = 1185 - (y+fontsize)
	rw2 = width
	rh2 = height
	#c.rect(x,1185-(y+fontsize),width,height,fill=0)
	rx = textobject.getX()
	ry = textobject.getY()
	rl3 = x + rx
	rt3 = 1185 + ry - (y+fontsize)
	rw3 = width
	rh3 = height
	#c.rect(x+rx,1185-(y+fontsize)+ry,width,height,fill=0)
        italic = self.getItalic()
        if italic:
            textobject.setFont("Italic", fontsize)
        else:
            textobject.setFont("Times-Roman", fontsize)
        textobject.textLine(theLine)
        usetopline = self.getUsetopline()
        if usetopline:
            topline = self.getTopline()
            textobject.setFont("Times-Roman", 14)
            textobject.setTextOrigin(x,1185-(y+fontsize-20))
            textobject.textLine(topline)
	    rl4 = x
	    rt4 = 1185 - ( y + fontsize - 20)
	    rw4 = width
	    rh4 = height
	    #c.rect(x-8,1185-(y+fontsize-20),width,height,fill=0)
	    rx = textobject.getX()
	    ry = textobject.getY()
	    rl5 = rx + x - 8
	    rt5 = ry + 1185 - ( y + fontsize - 20)
	    rw5 = width
	    rh5 = height
	    #c.rect(rx+x-8,ry+1185-(y+fontsize-20),width,height,fill=0)
        c.drawText(textobject)
	if outline == True:
	    c.rect(rl1,rt1,3,3,fill=0)
	    c.rect(rl2,rt2,3,3,fill=0)
	    c.rect(rl3,rt3,3,3,fill=0)
	    if usetopline:
		c.rect(rl4,rt4,3,3,fill=0)
		c.rect(rl5,rt5,3,3,fill=0)
        offsetX = self.getOffsetX()
        resetY = self.getResetY()
        if offsetX:
            returnx = xorig
        else:
            returnx = x 
        returny = y + fontsize
        return (returnx,returny)

    def getXOffset(self):
        """
        test
        """
        return 0

    def getYOffset(self):
        """
        test
        """
        return 0

    def getSkinName(self):
        """
        test
        """
        return "showHeadline"

    def getSnapshot(self,width,height):
        """
        Snapshot
        """
        fontSize = self.getFontsize()
        fontSize /= 2
        style = "font-size:"+str(fontSize)+"pt;font-weight:bold;"
        theId = self.getId()
        theFlyoutId = theId+"1234"
        headline = "<div id='"+theId+"' class='headline' style='"+style+"'>"
        headline += self.getHeadline()
        thePhysicalPath = self.getPhysicalPath()
        lengthPhysicalPath = len(thePhysicalPath)
        pathToContainer = thePhysicalPath[:lengthPhysicalPath-1]
        physicalPath = '/'.join(pathToContainer)
        theFullId = '"'+physicalPath+'"'
        theFlyoutId2 = '"'+theFlyoutId+'"'
        headline += "</div>"
        width = 0
        height = 4 * fontSize / 3 
        return (headline,width,height)

    def diagostics(self):
        """
        AJAX Fetch Information
        """
        return "AJAX Fetch Information";

    def getContainerDiagnostic(self):
        """
        build onclick event
        """
        thePhysicalPath = self.getPhysicalPath()
        lengthPhysicalPath = len(thePhysicalPath)
        pathToContainer = thePhysicalPath[:lengthPhysicalPath-1]
        physicalPath = '/'.join(pathToContainer)
        theFullId = '"'+physicalPath
        theFlyoutId = '"'+self.getId()+'_diag"'
        theFlyoutId2 = theFullId+'/'+self.getId()+'/showHeadlineDiagnostics"'
        theFullId += '"'
        theClickEvent = 'containerDiagnostic('+theFullId+","+theFlyoutId+','+theFlyoutId2+")"
        return theClickEvent

    def getFlyoutId(self):
        """
        returns the Id for the flyout
        """
        theFlyoutId2 = self.getId()+'_diag'
        return theFlyoutId2

    def getHeadlineId(self):
        """
        get headline id
        """
        theId = self.getId()
        return theId

    def getType(self):
        """
        Test
        """
        return "Headline"

    def getStyle(self):
        """
        getStyle
        """
        style="font-size:"
        style+=self.getFont()
        style+="%"
        return style

    def publish(self,REQUEST):
        """
        Publish
        """
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.publishHeadline
        return showTemplate()

    def getJSON(self):
        json_item = {}
        title = self.getId()
        headline=self.getHeadline()
        s = headline.decode('utf-8')
        t = u""
        for ii in s:
            if ord(ii) in entity.codepoint2name:
                name = entity.codepoint2name.get(ord(ii))
                it = "&" + name + ';'
                t += it	
            else:
                t += ii
        json_item['type']='Headline'
        json_item['name']=title
        json_item['Fontsize']=self.getFontsize()
        json_item['headlineclass']=self.getHeadlineclass()
        json_item['italic']=self.getItalic()
        
        json_item['elements']=super(Headline,self).getJSON()
        return json_item

registerType(Headline, PROJECTNAME)
# end of class Headline

##code-section module-footer #fill in your manual code here
##/code-section module-footer
