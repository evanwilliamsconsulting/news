# -*- coding: utf-8 -*-
#
# File: Lines.py
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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import  ReferenceBrowserWidget

from Products.Newspaper.richly import RichColumnar


schema = Schema((

    StringField(
                name='actor',
        	widget=StringField._properties['widget'](
        	    label='Actor',
        	    label_msgid='Dialogues_label_actor',
        	    i18n_domain='Dialogues',
        	),
                ),
    StringField(
        name='statement',
        widget=StringField._properties['widget'](
            label='Statement',
            label_msgid='Dialogues_label_statement',
            i18n_domain='Dialogues',
        ),
    ),
    TextField(
        name='elaboration',
        allowable_content_types=('text/rtf', 'text/structured', 'text/html', 'application/msword','text/plain'),
        widget=RichWidget(
            label='Wordage',
            label_msgid='Dialogues_label_verbage',
            i18n_domain='Dialogues',
        ),
        default_output_type='text/rtf',
    ),
    IntegerField(
        name='columnSize',
	widget=IntegerWidget(
		label='columnSize',
		label_msgid='Dialogues_label_results',
		i18n_domain='Dialogues',
	),
    ),        
),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Lines_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Lines(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ILines)

    meta_type = 'Lines'
    _at_rename_after_creation = True

    schema = Lines_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    def callPDFPDTBySameName(self,c,x,y,REQUEST,parent,top,pagenumber):
        """
        Test
	"""
	textobject = c.beginText()
	textobject.setFont("Times-Roman",22)
	textobject.setTextOrigin(x,y)
	verbage = self.getElaboration()
	output = []
	theParagraph = True 
	theCarrotStart = False
	theCarrotEnd = False
	theTagOpen = True
	theTag = ""
	theWordage = " "
	gotTheTag = False
	gotEndTag = False
	nasty = 'Â'
	verblen = len(verbage)
	m = -1
	# while within a paragraph
	total = 0
	i = 0
	indent = False
	gotEndTag = False
	theWordage = verbage 
	moreChars = int(105*2)
	indent = True
	theNewWordage = ""
	theNewWordage = theWordage
	just = RichColumnar(theNewWordage,105)
	lines = just.getLines()
	totalLines = just.countLines()
	p = 0 
	i = 0
	isHyperlink=False
	nextLineBold = False
	breakOccurred = False
	afterBreak = ""
	# if a Break Occurred special processing
	while p <= totalLines and i<100:
		if i >= 0:
			theLine = afterBreak
			theLine += just.returnLine(p)
			afterBreak = ""
			afterBreak = ""
			if theLine.find('http') > -1:
				hyperlink = theLine.split("/");
				hyperLine = ""
				for link in hyperlink:
					hyperLine += link
					hyperLine += "/"
				hyperLine = hyperLine[:-4]
				if len(hyperLine) > 105-12:
					httpPosition = hyperLine.find('http')
					beginning = hyperLine[0:httpPosition]
					firstLine = hyperLine[httpPosition:self.getCharsPerLine()-12]
					secondLine = hyperLine[self.getCharsPerLine()-11:]	
					savex = x
					self.drawALine(c,x,y,beginning,False,True)
					x += httpPosition * 4.5
					self.drawBold(c,x,y,firstLine,False,True)
					x = savex
					y -= 12
					self.drawBold(c,x,y,secondLine,False,True)
				else:
					self.drawBold(c,x,y,hyperLine,False,True)
			elif theLine=="BREAK":
				#self.drawALine(c,x,y,"",False,True)
				#y -= 6
				breakOccurred = True
			elif breakOccurred:
				afterBreak = theLine
				if len(afterBreak) < 105 / 2:
					afterBreak = ""
					savex = x
					x += 25
					self.drawALine(c,x,y,theLine,False,True)
					x = savex
				else:
					self.drawALine(c,x,y,theLine,False,True)
					afterBreak = ""
				breakOccurred = False
			elif theLine=="BOLD":
				nextLineBold = True
			else:
				if len(theLine) <=30:
					self.drawALine(c,x,y,theLine,False,True)
				else:
					if nextLineBold:
						self.drawBold(c,x,y,theLine,False,False)
						nextLineBold = False
					else:
						self.drawALine(c,x,y,theLine,False,False)
			y -= 12 
			self.previousP = p
			p += 1
			i += 1
		total += i
		containerLeft = parent.getLeft()
		#newx = x + containerLeft
		newx = x + containerLeft
	c.drawText(textobject)
	return (x,y)

    def drawALine(self,c,x,y,theLine,indent=False,space=True,adjust=0):
	words = theLine.split()
	totalWordLength = 0
	allwords=[]
	for word in words:
		allwords.append(word)
	for word in allwords:
		#print "error"
		#print word
		theWord = ""
		nasty = '\xC0\x82'
		#for letter in word:
		#    if letter <  nasty:
		#        theWord += letter
		#theWord = theWord.decode('latin-1')
		#theWord = unicode(word,'latin-1')
		totalWordLength += c.stringWidth(word,"Times-Roman",11)
	if indent:
		lineLength = (3.8 * (105-adjust))-8 
	else:
		lineLength = 3.8 * (105-adjust )
	if len(allwords) > 3:
		whiteSpace = (lineLength - totalWordLength) / (len(allwords)-1)
		#whiteSpace = (lineLength - totalWordLength) / (len(allwords) - 1)
	else:
		whiteSpace = 10
	textobject = c.beginText()
	textobject.setFont("Times-Roman",11)
	for word in allwords:
		theWord = ""
		nasty = '\xC0\x82'
		for letter in word:
			theWord += letter
		#theWord = theWord.decode('latin-1')
		#theWord = unicode(word,'latin-1')
		stringWidth = c.stringWidth(word,"Times-Roman",11)
		textobject.setTextOrigin(x,y)
		textobject.textLine(word)
		x += stringWidth
		if space==True:
			x += 2
		else:
			x += whiteSpace 
	c.drawText(textobject)
	#print "drawText"
	#print textobject
	y+=4
	return (x,y)

registerType(Lines, PROJECTNAME)
# end of class Lines

##code-section module-footer #fill in your manual code here
##/code-section module-footer

