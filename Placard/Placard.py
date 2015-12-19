# -*- coding: utf-8 -*-
#
# File: Placard.py
#
# Copyright (c) 2015 by unknown <unknown>
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

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Placard.config import *


import string 
from StringIO import StringIO

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from PIL import *


from plone.app.blob.field import BlobField, ImageField
from Products.Archetypes.atapi import *
from Products.Archetypes.Widget import ReferenceWidget
from zope.interface import implements
import interfaces
import locale

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Name',
        widget=StringField._properties['widget'](
            label='Name',
            label_msgid='Placard_label_Name',
            i18n_domain='Placard',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Placard_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Placard(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPlacard)

    meta_type = 'Placard'
    _at_rename_after_creation = True

    schema = Placard_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    def pdfinside(self,REQUEST): 
        """
        Test
        """
        skin = self.portal_skins.invoicing_templates
        showTemplate=skin.showIssue
	output = StringIO()
	c = canvas.Canvas(output,pagesize=(1152,735),bottomup=0)
	x=35
	y=50
	#self.renderMasthead(c,x,y)
        textobject = c.beginText()
        textobject.setTextOrigin(x,y)
	pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
	pdfmetrics.registerFont(TTFont('Verdan','trebuc.ttf'))
        textobject.setFont('Verdan',40)
	#textobject.textLine("New Holland Press - INVOICE")
        y+=20	
        textobject.setFont('FilosReg',18)
        #textobject.textLine("21 Lincoln Ave. Princeton, NJ 08540")
	y+=50
	parent = self.aq_inner.aq_parent
	restaurantName = self.getName()
        textobject.setFont('Verdan',24)
	textobject.setTextOrigin(x,y)
	#textobject.textLine(restaurantName)
	y += 50
	textobject.setTextOrigin(x,y)
	textobject.setFont('FilosReg',12)
	#for aLine in self.listFolderContents():
	#    if aLine.getDiscount() > 0:
        #        isDiscount = True
        #if isDiscount:
	#    textobject.setTextOrigin(x,y)
        #    textobject.setFont('FilosReg',12)
	#    textobject.textLine("Discount")
	#textobject.setTextOrigin(x,y)
        #textobject.setFont('FilosBold',12)
	#textobject.textLine("Total")
	meals = self.listFolderContents(contentFilter={"portal_type":"Meal"})
	for meal in meals:
		if meal.getPageno() == 2:
			top = meal.getTop()
			left = meal.getLeft()
			use_y = top + 14
			use_x = left + 10
			meal.callPDFPDTBySameName(c,use_x,use_y,REQUEST,self,y,2)
	graphics = self.listFolderContents(contentFilter={"portal_type":"Graphic"})
	for graphic in graphics:
		if graphic.getPageno() == 2:
			graphic.callPDFPDTBySameName(c,x,y,REQUEST,self,y,2)
	c.drawText(textobject)
	c.showPage()
	c.save()
	response = REQUEST.RESPONSE
        response.setHeader('Content-type','application/pdf')
	result = output.getvalue()
	output.close()
	return result 

    def pdfoutside(self,REQUEST): 
        """
        Test
        """
        skin = self.portal_skins.invoicing_templates
        showTemplate=skin.showIssue
	output = StringIO()
	c = canvas.Canvas(output,pagesize=(1152,735),bottomup=0)
	x=35
	y=50
	#self.renderMasthead(c,x,y)
        textobject = c.beginText()
	pdfmetrics.registerFont(TTFont('Verdan','trebuc.ttf'))
        textobject.setTextOrigin(x,y)
	pdfmetrics.registerFont(TTFont('FilosBold','FilosBol.ttf'))
	pdfmetrics.registerFont(TTFont('FilosReg','FilosReg.ttf'))
        textobject.setFont('FilosBold',40)
	#textobject.textLine("New Holland Press - INVOICE")
        y+=20	
        textobject.setFont('FilosReg',18)
        #textobject.textLine("21 Lincoln Ave. Princeton, NJ 08540")
	y+=50
	parent = self.aq_inner.aq_parent
	restaurantName = self.getName()
        textobject.setFont('FilosBold',24)
	textobject.setTextOrigin(x,y)
	#textobject.textLine(restaurantName)
	y += 50
	textobject.setTextOrigin(x,y)
	textobject.setFont('FilosReg',12)
	#for aLine in self.listFolderContents():
	#    if aLine.getDiscount() > 0:
        #        isDiscount = True
        #if isDiscount:
	#    textobject.setTextOrigin(x,y)
        #    textobject.setFont('FilosReg',12)
	#    textobject.textLine("Discount")
	#textobject.setTextOrigin(x,y)
        #textobject.setFont('FilosBold',12)
	#textobject.textLine("Total")
	meals = self.listFolderContents(contentFilter={"portal_type":"Meal"})
	for meal in meals:
		print meal
		if meal.getPageno() == 1:
			top = meal.getTop()
			left = meal.getLeft()
			use_y = top + 14
			use_x = left + 10
			meal.callPDFPDTBySameName(c,x,y,REQUEST,self,y,1)
	graphics = self.listFolderContents(contentFilter={"portal_type":"Graphic"})
	for graphic in graphics:
		print graphic
		if graphic.getPageno() == 1:
			graphic.callPDFPDTBySameName(c,x,y,REQUEST,self,y,1)
	textblocks = self.listFolderContents(contentFilter={"portal_type":"TextBlock"})
	for textblock in textblocks:
		print textblock 
		if textblock.getPageno() == 1:
			textblock.callPDFPDTBySameName(c,x,y,REQUEST,self,y,1)
	c.drawText(textobject)
	c.showPage()
	c.save()
	response = REQUEST.RESPONSE
        response.setHeader('Content-type','application/pdf')
	result = output.getvalue()
	output.close()
	return result 

registerType(Placard, PROJECTNAME)
# end of class Placard

##code-section module-footer #fill in your manual code here
##/code-section module-footer

