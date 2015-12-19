# -*- coding: utf-8 -*-
#
# File: Steps.py
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

    IntegerField(
        name='stepNumber',
        widget=IntegerField._properties['widget'](
            label='Stepnumber',
            label_msgid='Recipe_label_stepNumber',
            i18n_domain='Recipe',
        ),
    ),
    TextField(
        name='Instructions',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Instructions',
            label_msgid='Recipe_label_Description',
            i18n_domain='Recipe',
        ),
        default_output_type='text/html',
    ),
    ReferenceField(
        name='Ingredient',
	allowedTypes=('Ingredient',),
	relationship='IngredientMeasure',
	keepReferencesOnCopy=1,
        widget=ReferenceBrowserWidget(
            label='Measure',
            label_msgid='Recipe_label_measure',
            i18n_domain='Recipe',
        ),
    ),
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Steps_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Steps(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISteps)

    meta_type = 'Steps'
    _at_rename_after_creation = True

    schema = Steps_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Steps, PROJECTNAME)
# end of class Steps

##code-section module-footer #fill in your manual code here
##/code-section module-footer

