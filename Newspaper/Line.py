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

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

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

    IntegerField(
        name='linex',
        widget=IntegerField._properties['widget'](
            label='Line X',
            label_msgid='Newspaper_label_Linex',
            i18n_domain='Newspaper',
        ),
    ), 
    IntegerField(
        name='liney',
        widget=IntegerField._properties['widget'](
            label='Line Y',
            label_msgid='Newspaper_label_Liney',
            i18n_domain='Newspaper',
        ),
    ), 
    IntegerField(
        name='length',
        widget=IntegerField._properties['widget'](
            label='Length',
            label_msgid='Newspaper_label_Length',
            i18n_domain='Newspaper',
        ),
    ), 
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Line_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Line(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILine)

    meta_type = 'Line'
    _at_rename_after_creation = True

    schema = Line_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
        """
        Test
        """
        print "LINE"
	x = self.getLinex()
	y = self.getLiney()
	length = self.getLength()
	print x
	print y
	print length
	y = 1175 - y
	xinches = int(x/75)
	yinches = int(y/75)
	linches = int(length/75)
	x2 = xinches + linches
	c.setLineWidth(.8)
	c.setStrokeColorRGB(0,0,0)
	c.line(xinches*inch,yinches*inch,x2*inch,yinches*inch)
        return (x,y)

registerType(Line, PROJECTNAME)
# end of class Headline

##code-section module-footer #fill in your manual code here
##/code-section module-footer

