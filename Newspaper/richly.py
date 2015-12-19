""" Puts Verbage into Columns and Provides Index by Lines

"""

import re
import os
from hyphenate import Hyphenator

__version__ = '1.0.20070709'

class RichColumnar:

	checkTag = False
	expectClose = False
	checkHyperlink = False
	expectHyperlink = False
	waitClose = False
	tagMightBe = ''
	isSpecial = False
	specialCode = ''

	def __init__(self, verbage, columnSize):
		self.verbage = verbage 
		self.verbage += '\n'
		self.length = len(verbage)
		self.end = self.length
		self.start = 0
		self.current = 0
		self.lineid = 0
		self.lines = {}
		self.count = 0
		self.columnSize = columnSize 
		self.currentChar = ""
		self.currentWord = ""
		self.currentLine = ""
		#f = open("/home/newholland/webapps/nhpdev/zinstance/products/Newspaper/en.dic","r")
		#d = os.getcwd()
		f = open("/opt/newholland/press/products/Newspaper/en.dic","r")
		rae = f.read()
		f.close()
		mh = Hyphenator(rae)
		self.returnText(mh)

	def getLines(self):
		return self.lines


	def getCurrent(self):
		theResult=self.verbage[self.current]
		return theResult

	def next(self,statein):
		if self.current >= self.end-1:
			return "END"
		else:
			self.current += 1
			self.count = self.current
			return statein

	def setColumnSize(self,chars):
		self.columnSize = chars

	def getColumnSize(self):
		return self.columnSize

	def countLines(self):
		return self.lineid

	def getLines(self):
		return self.lines

	def setCountLines(self,theCount):
		self.count = theCount

	def returnLines(self):
		return self.lines

	def returnLine(self,i):
		return self.lines[i]

	def walk(self,statein):
		self.currentWord+=self.getCurrent()
		self.currentChar = self.getCurrent()
		state=self.next(statein)
		return state

	def columnFull(self):
		if len(self.currentLine)+len(self.currentWord)>self.getColumnSize()-5:
			return True
		else:
			return False

	def getLineId(self):
		return self.lineid

	def getCurrentLine(self):
		return self.currentLine

	def parseable(self,goodword,char):
		"""
		parse the characters and trap tags, later special chars too

		Okay now it's later and I am adding special chars.

		A special char starts with a & and ends with a ;

		It contains a code in the middle.

		There are three cases for tags:

		1. <open>
		2. </open>
		3. <open/>

		All cases start with a check for '<'
		Then as long as '/' does not occur we read in the tag.
		If '/' occurs we stop reading in the tag and wait for the '>'
		If '>' occurs we stop reading in the tag immediately.

		The below code would match <one/two> as onetwo
		The below code would cause an error if an opentag occurred and there was never a close.
		"""
		nextchar=''
		flush = False
		result = goodword
		if self.expectClose:
			if char=='>': # we closed, this must have been a <br/>
				self.expectClose = False # so clean up and return to normal
				flush = True
			else:
				self.waitClose = True
				self.expectClose = False
				self.tagMightBe += char
		elif self.checkTag:
			if char == '/':
				self.expectClose = True # we expect the tag to go by again but don't count
				self.checkTag = False
			elif char == '>': # close an open tag and return results
				self.checkTag = False
				flush=True
			else:
				self.tagMightBe += char
		elif char == '<': # wait and expect a tag?
			self.checkTag = True
			self.expectClose = False
			self.tagMightBe = ''
		elif self.isSpecial == True:
			if char == ";":
				self.isSpecial = False
				if self.specialCode == "amp":
					nextchar = '&'	
					result += nextchar
			self.specialCode += char
		elif char == '&': # this must be a special character!
			self.isSpecial = True
			self.specialCode = ''
		else:
			self.tagMightBe = ''
			if char==' ':
				flush = True
				nextchar=char
			elif char==">":
				nextchar=''
			else:	
				nextchar=char
			result += nextchar
		#return goodword+nextchar,flush,self.tagMightBe
		return result,flush,self.tagMightBe

	# this would be a lot better if a proper tag that had come back had a tag handler
	# so that the core formatting code doesn't get messed up.
	def returnText(self,mh):
		"""
		Return the Verbage
		"""
		state = 'START'
		state = self.walk(state)
		trythis = self.verbage
		trylen = len(self.verbage)
		l = 0
		j = 0
		word=''
		w = 0
		new = ''
		line=''
		lineid=0
		hy = []
		theword = ''
		isHyperlink = True
		numberOfWordsOnLine = 0
		restOfWord = ''
		fetchNext = True
		while l<trylen:
			# do the current number of chars
			# plus the length of the current word
			# fit on the line
			# factor ths spaces
			# the line will not show up otherwise!
			if j+w>self.columnSize-numberOfWordsOnLine:
                                self.lines[lineid]=line
                                lineid+=1
                                line=''
                                j=0
                                word = ''
                                w = 0
				numberOfWordsOnLine = 0
			if len(restOfWord) > 0:
				theword = restOfWord
				j = 0
				word = ''
				w = 0
				restOfWord = ''
				parseComplete = True
				tag = ""
				fetchNext = False
			else:
				theword, parseComplete, tag = self.parseable(theword,trythis[l])
				fetchNext = True
			br = False
			if parseComplete:
				if tag.strip()=="p":
					self.lines[lineid]=line+word+theword
					lineid+=1	
					self.lines[lineid]="BREAK"
					new=''
					lineid+=1
					line=''
					word=''	
					theword=''
					numberOfWordsOnLine = 0
					j = 15
					w = 0
				# does word already contain a hyphen?
				#print theword
				#print tag
				elif tag.strip()=="br": #Don't have two in a row.
					self.lines[lineid]=line+word+theword
					new=''
					lineid+=1
					line=''
					word=''	
					theword=''
					numberOfWordsOnLine = 0
				#print theword
				if theword.find(" "):
					splitword=theword.split(" ")
					useword=splitword[0]
					useword+=" "
				else:
					useword=theword
				hy = mh.hyphenate_word(useword)
				theword = ''
				hylen = len(hy)
				#word += new
				m = 0
				w = len(word)
				#word += hy[0]
				while m<hylen:
					# If the current line length so far j
					# plus the length of the current addition
					# is greater than the columnSize
					# then add a hyphen and reset.	
					if j+len(hy[m])>self.columnSize:
						line+='-'
						self.lines[lineid]=line
						lineid+=1
						line=''
						new = ''
						# put a word on the 'stack'
						# equal to the remainder
						# of the hyphenation
						restOfWord = hy[m]
						m += 1
						while m < hylen:
							restOfWord += hy[m]	
						j=0
						# make sure we break
						m = hylen
					else:
						line+=hy[m]
						j += len(hy[m])
					m += 1
				w = len(word)
				m = 0
				#print word
				numberOfWordsOnLine += 1
				j += 1
				word = ''
				new = ''
			if fetchNext:
				l += 1
		# trim the last char off the last word
		lastline = line+word+theword
		self.lines[lineid]=lastline
		self.lineid=lineid
