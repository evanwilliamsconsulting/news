# -*- coding: utf-8 -*-
#
# File: Bucket.py
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
import interfaces
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

from Products.Newspaper.config import *

from Products.Newspaper.Element import Element
from Products.Newspaper.Element import Element_schema


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate


from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.ttfonts import TTFont

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='shortname',
        widget=StringField._properties['widget'](
            label='Username',
            label_msgid='Newspaper_label_username',
            i18n_domain='Newspaper',
        ),
    ),
    StringField(
        name='content_types',
        widget=StringField._properties['widget'](
            label='What\'s Your Handle',
            label_msgid='Newspaper_label_handle',
            i18n_domain='Newspaper',
        ),
    ),
    TextField(
        name='description',
        allowable_content_types=('text/rtf', 'text/structured', 'text/html', 'application/msword','text/plain'),
        widget=RichWidget(
            label='Wordage',
            label_msgid='Newspaper_label_verbage',
            i18n_domain='Newspaper',
        ),
        default_output_type='text/rtf',
    ),
    ImageField(
        name='picture',
        widget=ImageField._properties['widget'](
            label='Pix',
            label_msgid='Newspaper_label_picture',
            i18n_domain='Newspaper',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Bucket_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()


class BucketJSON(BrowserView):
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
	json_item['Bucket']=title
	json_item['attributes']=self.context.getJSON()
	pretty = json.dumps(json_item)    
	return pretty 

##code-section after-schema #fill in your manual code here
##/code-section after-schema
#class M_Bucket(NewsFolder.__class__): pass

class Bucket(OrderedBaseFolder,ExtensibleMetadata):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IBucket)

    meta_type = 'Bucket'
    _at_rename_after_creation = True

    schema = Bucket_schema

    #__metaclass__=M_Bucket

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header
    
    # Methods
    def getJSON(self):
	"""
	test
	"""
	json_items = {}
        items = self.listFolderContents()
	for item in items:
		itemId = item.getId()
		pos = self.getObjectPosition(itemId)
		json_items[pos]=itemId
	return json_items

registerType(Bucket, PROJECTNAME)
# end of class Bucket

##code-section module-footer #fill in your manual code here
##/code-section module-footer

