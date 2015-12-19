# -*- coding: utf-8 -*-
#
# File: Graphic.py
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
from plone.app.blob.field import BlobField, ImageField
from zope.interface import implements
import interfaces
import string 
from StringIO import StringIO
import reportlab.pdfgen.canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import *

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter


from reportlab.lib.colors import yellow,red,black,white
from reportlab.lib.units import inch

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Placard.config import *

from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    IntegerField(
	name='left',
	widget=IntegerField._properties['widget'](
	    label='left',
	    label_msgid='Placard_label_left',
	    i18n_domain='Placard',
	),
    ),
    IntegerField(
	name='top',
	widget=IntegerField._properties['widget'](
	    label='top',
	    label_msgid='Placard_label_top',
	    i18n_domain='Placard',
	),
    ),
    IntegerField(
	name='width',
	widget=IntegerField._properties['widget'](
	    label='width',
	    label_msgid='Placard_label_width',
	    i18n_domain='Placard',
	),
    ),
    IntegerField(
	name='height',
	widget=IntegerField._properties['widget'](
	    label='height',
	    label_msgid='Placard_label_height',
	    i18n_domain='Placard',
	),
    ),
    IntegerField(
        name='pageno',
        width=IntegerField._properties['widget'](
	    label='pageno',
	    label_msgid='Placard_label_pageno',
	    i18n_domain='Placard',
	    ),
	),
    ImageField(
        name='picture',
        widget=ImageField._properties['widget'](
            label='Graphic',
            label_msgid='Placard_label_picture',
            i18n_domain='Placard',
        ),
        storage=AttributeStorage(),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PlacardGraphic_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class PlacardGraphic(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPlacardGraphic)

    meta_type = 'Graphic'
    _at_rename_after_creation = True

    schema = PlacardGraphic_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def returnGraphic(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
	    theClass = self.getGraphicclass()
            theDiv += "' class='"
	    theDiv += theClass
	    theDiv += "' style='margin:10px;'"
            theDiv += ">"
	    theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/picture'/>"
	    theDiv += theTag
	    theDiv += "</div>"
	    return theDiv

    def web(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
	    theClass = self.getGraphicclass()
            theDiv += "' class='"
	    theDiv += theClass
	    theDiv += "' style='margin:10px;'"
            theDiv += ">"
	    theDiv += self.pixHTML()
	    theDiv += "</div>"
	    return theDiv
        

    def pixHTML(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
            theDiv += "' class='pix' style='margin-left:30px;position:absolute;top:"
	    theDiv += str(self.getTop())
	    theDiv += "px;left:0"
	    theDiv += "px;'"
            #theDiv += "style='border-color:blue;border-width:2px;border-style:solid;top:"
            left = self.getLeft()
	    top = self.getTop()
            width = self.getWidth()
            height = self.getHeight()
            theDiv += ">"
	    theTag = "<img width='"+str(self.getWidth())+"' height='"+str(self.getHeight())+"' src='"+self.absolute_url()+"/picture'/>"
	    theDiv += theTag
	    theDiv += "</div>"
	    left += width
	    return theDiv

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    pageno = self.getPageno()
	    top = self.getTop()
	    left = self.getLeft()
	    theImage=self.getPicture()
	    theBlob = theImage.getBlob()
	    theString = theBlob.open().read()
	    theStringIO=StringIO(str(theString))
	    im = Image.open(theStringIO)
	    im2 = im.transpose(1)
            theStringIO2=StringIO(im2.tostring())
            parent = self.aq_inner.aq_parent
            width = self.getWidth()
            height = self.getHeight()
	    if pageno == pagenumber:
	    	c.drawImage(ImageReader(im2),left,top,width,height)
	    return (x,y)

    def getSkinName(self):
	   """
           TEST
           """
           return "showGraphic"

    def pdf(self,REQUEST): 
            """
   	    Test
            """
            skin = self.portal_skins.invoicing_templates
            showTemplate=skin.showIssue
	    output = StringIO()
	    c = canvas.Canvas(output,pagesize=letter,bottomup=0)
	    x=35
	    y=50
	    theImage=self.getPicture()
	    theImageData = StringIO()
	    theImageUsage = theImage.file._read_data(theImageData)
	    theImageReader = ImageReader(theImageUsage)
	    (width,height) = theImageReader.getSize()
            parent = self.aq_inner.aq_parent
            width = self.getWidth()
            height = self.getHeight()
	    if self.getTopMargin():
		y+=15
	    c.drawImage(theImageReader,x,y,width,height,anchor='ne')
	    caption = self.getCaption()
	    credit = self.getCredit()
	    pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	    pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
	    if caption is not None:
	        textobject = c.beginText()
		h = self.getHeight()
		if h is None:
			h = 400
	        textobject.setTextOrigin(x,y+h+30)
	        fontsize = 14
	        textobject.setFont("FilosReg", fontsize)
	        textobject.textLine(caption)
	        c.drawText(textobject)
            if credit is not None:
                textobject = c.beginText()
                h = self.getHeight()
                if h is None:
                    h = 400
                w = self.getWidth()
                w = w - 100
                textobject.setTextOrigin(x-w,y+h+15)
                fontsize = 11
                textobject.setFont("FilosReg",fontsize)
                textobject.textLine(credit)
                c.drawText(textobject)
	    c.showPage()
	    c.save()
	    result = output.getvalue()
	    output.close()
	    response = REQUEST.RESPONSE
            response.setHeader('Content-type','application/pdf')
	    return result 

    def publish(self,REQUEST):
            """
            Publish
            """
	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.publishGraphic
	    return showTemplate()

    def getSnapshot(self,width,height):
	    """
	    Snapshot
	    """
	    retcode = "<div id='pix' "
	    actualWidth = width
	    actualHeight = height
	    retcode += "style='width="
	    retcode += str(width)
	    retcode += ";height="
	    retcode += str(height)
	    retcode += "'>"
 	    tag = self.getField('picture').tag(self,height=actualHeight,width=actualWidth)
	    caption = self.getCaption()
	    retcode += tag
	    #retcode += "<div style='color:white;top:-30px;position:relative;'>"
	    #retcode += caption
	    #retcode += "</div>"	
	    retcode += "</div>"	
	    return (retcode,width,height)

    def getType(self):
	    """
	    Test
   	    """
	    return "Graphic"

    def getJSON(self):
	    """
	    Test
   	    """
	    json_item = {}
	    title = self.getId()
	    json_item['Graphic']=title
	    attributes={}
            attributes['caption']=self.getCaption()
            attributes['credit']=self.getCredit()
            attributes['pixclass']=self.getGraphicclass()
	    attributes['width']=self.getWidth()
	    attributes['height']=self.getHeight()
	    pixpath = self.absolute_url() + '/picture'
	    attributes['pixpath']=pixpath
	    json_item['attributes']=attributes
	    json_item['elements']=super(Graphic,self).getJSON()
	    return json_item 

registerType(PlacardGraphic, PROJECTNAME)
# end of class Image

##code-section module-footer #fill in your manual code here
##/code-section module-footer

