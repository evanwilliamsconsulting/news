# -*- coding: utf-8 -*-
#
# File: Recipe.py
#
# Copyright (c) 2013 by unknown <unknown>
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

from Products.Recipe.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='Introduction',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Introduction',
            label_msgid='Recipe_label_Introduction',
            i18n_domain='Recipe',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='Conclusion',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Conclusion',
            label_msgid='Recipe_label_Conclusion',
            i18n_domain='Recipe',
        ),
        default_output_type='text/html',
    ),
    StringField(
        name='Author',
        widget=StringField._properties['widget'](
            label='Author',
            label_msgid='Recipe_label_Author',
            i18n_domain='Recipe',
        ),
    ),
    StringField(
        name='TestedIn',
        widget=StringField._properties['widget'](
            label='Testedin',
            label_msgid='Recipe_label_TestedIn',
            i18n_domain='Recipe',
        ),
    ),
    ImageField(
        name='finishedLook',
        widget=ImageField._properties['widget'](
            label='Finishedlook',
            label_msgid='Recipe_label_finishedLook',
            i18n_domain='Recipe',
        ),
        storage=AnnotationStorage(),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Recipe_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Recipe(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRecipe)

    meta_type = 'Recipe'
    _at_rename_after_creation = True

    schema = Recipe_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	"""
	TEST	
	"""



registerType(Recipe, PROJECTNAME)
# end of class Recipe

##code-section module-footer #fill in your manual code here
##/code-section module-footer

