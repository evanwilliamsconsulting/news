# -*- coding: utf-8 -*-
#
# File: Dialogue.py
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

    IntegerField(
        name='top',
        widget=IntegerField._properties['widget'](
            label='Top',
            label_msgid='CreditsBox_label_top',
            i18n_domain='CreditsBox',
        ),
    ),
    IntegerField(
        name='left',
        widget=IntegerField._properties['widget'](
            label='Left',
            label_msgid='CreditsBox_label_left',
            i18n_domain='CreditsBox',
        ),
    ),
    IntegerField(
        name='width',
        widget=IntegerField._properties['widget'](
            label='Width',
            label_msgid='CreditsBox_label_width',
            i18n_domain='CreditsBox',
        ),
    ),
    StringField(
        name='booktitle',
        widget=StringField._properties['widget'](
            label='Booktitle',
            label_msgid='Dialogues_label_booktitle',
            i18n_domain='Dialogues',
        ),
    ),
    StringField(
        name='note',
        widget=StringField._properties['widget'](
            label='Note',
            label_msgid='Dialogues_label_note',
            i18n_domain='Dialogues',
        ),
    ),
    StringField(
        name='reference',
        widget=StringField._properties['widget'](
            label='Reference',
            label_msgid='Dialogues_label_reference',
            i18n_domain='Dialogues',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Dialogue_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Dialogue(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IDialogue)

    meta_type = 'Dialogue'
    _at_rename_after_creation = True

    schema = Dialogue_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
	    """
	    Test
	    """
	    print "Dialogue"
	    xorig = x
	    yorig = y
	    width= self.getWidth()
	    xt = xorig
	    title = self.getBooktitle()
	    note = self.getNote()
	    reference = self.getReference()
            textobject = c.beginText()
	    textobject.setTextOrigin(xt,y)
	    c.setFont("Times-Roman",11)
	    textobject.textLine(title)
	    c.drawText(textobject)
	    y -= 20
	    textobject.setTextOrigin(xt,y)
	    textobject.textLine(reference)
	    y -= 20
	    c.setFont("Times-Roman",11)
	    textobject.setTextOrigin(xt,y)
	    textobject.textLine(note)
	    y -= 20
	    c.drawText(textobject)
            textobject = c.beginText()
            textobject.setTextOrigin(xt,y)
	    c.setFont("Times-Roman",11)
	    lines = self.listFolderContents(contentFilter={"portal_type":"Lines"})
	    for line in lines:
		(xresult,yresult)=line.callPDFPDTBySameName(c,x,y,REQUEST,parent,y,pagenumber)
		y = yresult - 20
	    c.drawText(textobject)
	    return (x,y)

    def getSnapshot(self,width,height):
	    """
	    Snapshot
	    """
	    tag += "<div>"
	    tag += "Diaglogue"
	    tag += "</div>"
	    return tag

registerType(Dialogue, PROJECTNAME)
# end of class Dialogue

##code-section module-footer #fill in your manual code here
##/code-section module-footer

