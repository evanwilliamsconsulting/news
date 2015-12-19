# -*- coding: utf-8 -*-
#
# File: Font.py
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
from Products.Archetypes.atapi import FileWidget
from plone.app.blob.field import BlobField, ImageField, FileField
from zope.interface import implements
import interfaces
import string 
from StringIO import StringIO
from io import BytesIO
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
from ttfquery import *
from ttfquery import describe as testfont


from reportlab.lib.colors import yellow,red,black,white
from reportlab.lib.units import inch

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.TextAndFonts.config import *

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema


##code-section after-schema #fill in your manual code here
##/code-section after-schema

##code-section after-local-

# end of class Headline

##code-section module-footer #fill in your manual code here
##/code-section module-footer


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='typeface',
        widget=StringField._properties['widget'](
            label='Typeface',
            label_msgid='TextAndFonts_label_typeface',
            i18n_domain='TextAndFonts',
            ),
        ),
    IntegerField(
        name='fontsize',
	default=18,
        widget=IntegerField._properties['widget'](
            label='filesize',
            label_msgid='TextAndFonts_label_filesize',
            i18n_domain='TextAndFonts',
            ),
        ), 
    StringField(
        name='credit',
        widget=StringField._properties['widget'](
            label='Credit',
            label_msgid='TextAndFonts_label_credit',
            i18n_domain='TextAndFonts',
            ),
        ),
    FileField(
        name='font',
        widget=FileWidget(
            label='Font',
            label_msgid='TextAndFonts_label_font',
            i18n_domain='TextAndFonts',
            ),
        storage=AttributeStorage(),
        ),
)
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Font_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Font(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IFont)

    meta_type = 'Font'
    _at_rename_after_creation = True

    schema = Font_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def letter(self,REQUEST): 
        """
        Test
        """
        skin = self.portal_skins.textandfonts_templates
        showTemplate=skin.showFont
        output = StringIO()
        font = self.getFont()
	fontIO = BytesIO()
	fontValue = font.getBlob().open().read()
	fontIO.write(fontValue)
        stringIO = StringIO()
	theFont = fontIO.getvalue()
	theFont2 = theFont.decode('ISO-8859-1')
	#print theFont2
	stringIO.write(theFont)
        #theFont3 = theFont2.encode('ascii')
        #stringIO.write(fontValue2)
        c = canvas.Canvas(output,pagesize=letter,bottomup=0)
        x=35
        y=50
        #self.renderMasthead(c,x,y)
        textobject = c.beginText()
        textobject.setTextOrigin(x,y)
        #print fontIO.getvalue()
        pdfmetrics.registerFont(TTFont('testfont',StringIO(theFont)))
        textobject.setFont('testfont',40)
        textobject.textLine("New Holland Press - INVOICE")
        y+=20	
        textobject.setFont('testfont',18)
        textobject.textLine("21 Lincoln Ave. Princeton, NJ 08540")
        y+=50
        parent = self.aq_inner.aq_parent
        textobject.setFont('testfont',12)
        textobject.setTextOrigin(x,y)
        textobject.textLine("Date:")
        x += 50
        textobject.setTextOrigin(x,y)
        textobject.setFont('testfont',12)
        x = 35
        y += 50
        billto = "Bill to:"
        textobject.setFont('testfont',12)
        textobject.setTextOrigin(x,y)
        textobject.textLine("Bill to:")
        x += 50
        c.drawText(textobject)
        c.showPage()
        c.save()
        result = output.getvalue()
        output.close()
        response = REQUEST.RESPONSE
        response.setHeader('Content-type','application/pdf')
        return result     

registerType(Font, PROJECTNAME)
# end of class Image

##code-section module-footer #fill in your manual code here
##/code-section module-footer

