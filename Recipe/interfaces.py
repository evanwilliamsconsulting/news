# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class IRecipe(Interface):
    """Marker interface for .Recipe.Recipe
    """

class IIngredient(Interface):
    """Marker interface for .Ingredient.Ingredient
    """

class IMeasure(Interface):
    """Marker interface for .Measure.Measure
    """

class ISteps(Interface):
    """Marker interface for .Steps.Steps
    """

##code-section FOOT
##/code-section FOOT