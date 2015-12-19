# -*- coding: utf-8 -*-
#
# File: TextBlock.py
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

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


from reportlab.lib.colors import yellow,red,black,white
from reportlab.lib.units import inch

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Placard.config import *

from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((
    StringField(
        name='Text',
        widget=StringField._properties['widget'](
            label='Name',
            label_msgid='Placard_label_Text',
            i18n_domain='Placard',
        ),
    ),
)
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PlacardTextBlock_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema
class PlacardTextBlock(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPlacardTextBlock)

    meta_type = 'PlacardTextBlock'
    _at_rename_after_creation = True

    schema = PlacardTextBlock_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods 

registerType(PlacardTextBlock, PROJECTNAME)
# end of class Image

##code-section module-footer #fill in your manual code here
##/code-section module-footer

