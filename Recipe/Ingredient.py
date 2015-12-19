# -*- coding: utf-8 -*-
#
# File: Ingredient.py
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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.Recipe.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    TextField(
        name='Details',
        widget=TextAreaWidget(
            label='Details',
            label_msgid='Recipe_label_Details',
            i18n_domain='Recipe',
        ),
    ),
    FloatField(
        name='Quantity',
        widget=FloatField._properties['widget'](
            label='Quantity',
            label_msgid='Recipe_label_Quantity',
            i18n_domain='Recipe',
        ),
    ),
    ReferenceField(
        name='measure',
        widget=InAndOutWidget(
            label='Measure',
            label_msgid='Measure_label_containers',
            i18n_domain='Measure',
        ),
        allowed_types=('Measure',),
        multiValued=1,
	keepReferencesOnCopy=1,
        relationship='ingredientMeasure',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Ingredient_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Ingredient(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IIngredient)

    meta_type = 'Ingredient'
    _at_rename_after_creation = True

    schema = Ingredient_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Ingredient, PROJECTNAME)
# end of class Ingredient

##code-section module-footer #fill in your manual code here
##/code-section module-footer

