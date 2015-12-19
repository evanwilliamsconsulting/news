# -*- coding: utf-8 -*-
#
# File: Hyphenate.py
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
from zope.interface import implements
import interfaces
import re
from richly import RichColumnar 

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import  ReferenceBrowserWidget

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate

from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.units import inch


from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.CompoundField.ArrayField import ArrayField
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.ArrayWidget import ArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CompoundField.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header
    #def testset(self, value):
 #       self.Schema()['names'].fields()[1].set(self,value)

schema = Schema((

    ReferenceField(
        name='article',
        widget=InAndOutWidget(
            label='Article',
            label_msgid='Newspaper_label_article',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Wordage',),
        multiValued=1,
        relationship='containerLocation',
    ),
    IntegerField(
        name='charsPerLine',
        widget=IntegerField._properties['widget'](
            label='charsPerLine',
            label_msgid='Newspaper_label_charsPerLine',
            i18n_domain='Newspaper',
        ),
    ),
    ArrayField(
        StringField(
            name='line',
            widget=StringField._properties['widget'](
                label='Line',
                label_msgid='Newspaper_label_line',
                i18n_domain='Newspaper',
            ),
        ),
        IntegerField(
            name='lineno',
            widget=IntegerField._properties['widget'](
                label='Line Number',
                label_msgid='Newspaper_label_lineno',
                i18n_domain='Newspaper',
            ),
        ),
        widget=EnhancedArrayWidget(
            label='Array:lines',
            label_msgid='Newspaper_label_array:lines',
            i18n_domain='Newspaper',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Hyphenate_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Hyphenate(BaseContent, BrowserDefaultMixin):
    """
    """
    added = False

    security = ClassSecurityInfo()

    implements(interfaces.IHyphenate)

    meta_type = 'Hyphenate'
    _at_rename_after_creation = True

    schema = Hyphenate_schema 

    textContinued = False

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Methods
    def contains(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    showTemplate=skin.showColumn
	    return showTemplate()

    def show(self): 
	    """
	    Test
	    """
    	    skin = self.portal_skins.newspaper_templates
	    justTemplate=skin.justColumn
	    return justTemplate()

    def getColumnWidth(self):
    	    """
    	    TEST
    	    """
            charsPerLine = self.getCharsPerLine()
            #print charsPerLine
    	    columnWidth=6*charsPerLine
    	    strColumnWidth=str(columnWidth)
    	    return strColumnWidth
    
    def just(self):
	    """
	    Load lines from article
	    """
            self.Schema()['lines'].fields()[1].set(self,"1234",1)


registerType(Hyphenate, PROJECTNAME)
# end of class Column

##code-section module-footer #fill in your manual code here
##/code-section module-footer

