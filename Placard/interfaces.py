# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IPlacardSet(Interface):
    """Marker interface for .Placard.PlacardSet
    """

class IPlacard(Interface):
    """Marker interface for .Placard.Placard
    """

class IPlacardGraphic(Interface):
    """Marker interface for .Placard.PlacardGraphic
    """

class IPlacardTextBlock(Interface):
    """Marker interface for .Placard.PlacardTextBlock
    """

##code-section FOOT
##/code-section FOOT
