# -*- coding: utf-8 -*-
#
# File: PixLink.py
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
from Products.CMFCore import permissions

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

from Products.Newspaper.config import *

from Products.Newspaper.Element import Element
from Products.Newspaper.Element import Element_schema


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='pixclass',
	default='pixclass',
        widget=StringField._properties['widget'](
            label='PixLink class',
            label_msgid='Newspaper_label_pixclass',
            i18n_domain='Newspaper',
        ),
    ),
    ReferenceField(
    	name='picturereference',
        widget=InAndOutWidget(
        	label='Picture Reference',
        	label_msgid='Newspaper_label_picturereference',
        	i18n_domain='Newspaper',
        ),
        allowed_types=('Picture',),
        multiValued=1,
        relationship='pictureLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PixLink_schema = Element_schema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class PixLinkJSON(BrowserView):
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
	json_item['PixLink']=title
	attributes={}
        attributes['caption']=self.context.getCaption()
        attributes['credit']=self.context.getCredit()
	attributes['width']=self.context.getWidth()
	attributes['height']=self.context.getHeight()
	picture = self.context.getPicture()
	pixpath = picture.absolute_url() + "/picture"
	attributes['pixpath']=pixpath
	json_item['attributes']=attributes
	pretty = json.dumps(json_item)    
	return pretty 

class PixLink(Element):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPixLink)

    meta_type = 'PixLink'
    _at_rename_after_creation = True

    schema = PixLink_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    aliases = {
        '(Default)'	:	'base_view',
	'view'		:	'base_view',
	'edit'		:	'base_edit',
	'base'	        :       'base_view',
	'pdf'		:	'pdf_view',
	'form'		:	'form_view',
	}

    security.declareProtected(permissions.View,'view')
    def view(self,REQUEST):
	"""
	Test
	"""
        skin = self.portal_skins.newspaper_templates
        showTemplate=skin.showPixLink
	parent = self.aq_inner.aq_parent
	picture = self.getPicture()
        return showTemplate.pt_render(REQUEST,picture)


    # Methods
    def returnPixLink(self):
	    """
	    Test
	    """
	    theImage = self.getId()
	    theDiv = "<div id='"
            theDiv += theImage
	    theClass = self.getPixLinkclass()
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
	    theClass = self.getPixLinkclass()
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

    def getPicture(self):
	    """
	    Turn the Picture Reference into a Picture
	    """
	    picture = self.getPicturereference()
	    return picture[0]

    def getCredit(self):
	    """
		Retrieve the caption from the picture
	    """
	    picture = self.getPicturereference()
	    return picture[0].getCredit()

    def getCaption(self):
	    """
		Retrieve the caption from the picture
	    """
	    picture = self.getPicturereference()
	    return picture[0].getCaption()

    def picture(self):
	    """
		the picture
	    """
	    picture = self.getPicture()
	    return picture.getPicture()

    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber,outline):
	    """
	    Test
	    """
	    xorig = x
	    yorig = y
            height = self.getHeight()
	    (x,y) = self.getPosition()
	    y = 1200 - height - y
	    picture = self.getPicturereference()
	    #for pix in picture:
	    #	break
	    pix = picture[0]
	    theImage=pix.getPicture()
	    theBlob = theImage.getBlob()
	    theString = theBlob.open().read()
	    theStringIO=StringIO(str(theString))
	    im = Image.open(theStringIO)
	    im2 = im.transpose(1)
            theStringIO2=StringIO(str(im2.tostring()))		
            parent = self.aq_inner.aq_parent
            width = self.getWidth()
            height = self.getHeight()
	    c.drawImage(ImageReader(StringIO(theString)),x,y,width,height)
	    caption = pix.getCaption()
	    if caption is not None:
	        textobject = c.beginText()
		textobject.setFillColorRGB(0,0,0)
		h = self.getHeight()
		if h is None:
			h = 400
	        textobject.setTextOrigin(x,y-30)
	        fontsize = 12
	        textobject.setFont("Times-Roman", fontsize)
	        textobject.textLine(caption)
	        c.drawText(textobject)
	    credit = pix.getCredit()
	    if credit is not None:
	        textobject = c.beginText()
		h = self.getHeight()
		w = self.getWidth()
		w = w - 100
		if h is None:
			h = 400
	        textobject.setTextOrigin(x+30,y-15)
	        fontsize = 11
	        textobject.setFont("Times-Roman", fontsize)
	        textobject.textLine(credit)
	        c.drawText(textobject)
	    return (x,y)

    def getSkinName(self):
	   """
           TEST
           """
           return "showPixLink"

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
	    showTemplate=skin.publishPixLink
	    return showTemplate()

    def getSnapshot(self,width,height):
	    """
	    Snapshot
	    """
	    picture = self.getPicture()
	    return picture.getSnapshot(width,height)

    def getType(self):
	    """
	    Test
   	    """
	    return "PixLink"

    def getJSON(self):
	    """
	    Test
   	    """
	    json_item = {}
	    title = self.getId()
	    json_item['PixLink']=title
	    attributes={}
            attributes['caption']=self.getCaption()
            attributes['credit']=self.getCredit()
	    attributes['width']=self.getWidth()
	    attributes['height']=self.getHeight()
	    picture = self.getPicture()
	    pixpath = picture.absolute_url() + '/picture'
	    attributes['pixpath']=pixpath
	    json_item['attributes']=attributes
	    json_item['elements']=super(PixLink,self).getJSON()
            json_item['type']='Pix'
            json_item['name']=title
	    return json_item 

registerType(PixLink, PROJECTNAME)
# end of class Image

##code-section module-footer #fill in your manual code here
##/code-section module-footer

