# -*- coding: utf-8 -*-
#
# File: AdGroup.py
#
# Copyright (c) 2012 by unknown <unknown>
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


from plone.app.blob.field import BlobField, ImageField
from StringIO import StringIO
from PIL import *
from Products.CMFCore import permissions
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget
from Products.Newspaper.config import *
from Products.Newspaper.PDFPageTemplate import PDFPageTemplate
from Products.CMFCore.utils import getToolByName

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Invoicing.config import *

from Products.Newspaper import interfaces as newspaper


import reportlab.pdfgen.canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
#import string, cStringIO
from PIL import *

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter

import string 


from Products.Five.browser import BrowserView
import json
##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ReferenceField(
        name='AdGroup',
        widget=InAndOutWidget(
            label='AdGroup',
            label_msgid='Newspaper_label_AdGroup',
            i18n_domain='Newspaper',
        ),
        allowed_types=('Advertizement',),
        multiValued=1,
        relationship='adGroupLocation',
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

AdGroup_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class AdGroupJSON(BrowserView):
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
	json_item['AdGroup']=title
	json_items={}
	ads = self.context.getAdGroup()
	for ad in ads:
		adId = ad.getId()
		adJSON = ad.getJSON()
		json_items[adId] = adJSON
	json_item['elements']=json_items
	pretty = json.dumps(json_item)    
	return pretty 

class AdGroup(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IAdGroup)

    meta_type = 'AdGroup'
    _at_rename_after_creation = True

    schema = AdGroup_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

##code-section module-footer #fill in your manual code here
##/code-section module-footer

registerType(AdGroup, PROJECTNAME)
# end of class AdGroup
