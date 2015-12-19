# -*- coding: utf-8 -*-
#
# File: Actor.py
#
# Copyright (c) 2014 by unknown <unknown>
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

from Products.Dialogues.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='Abbreviation',
        widget=StringField._properties['widget'](
            label='Abbreviation',
            label_msgid='Dialogues_label_Abbreviation',
            i18n_domain='Dialogues',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Actor_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Actor(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IActor)

    meta_type = 'Actor'
    _at_rename_after_creation = True

    schema = Actor_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(Actor, PROJECTNAME)
# end of class Actor

##code-section module-footer #fill in your manual code here
##/code-section module-footer

