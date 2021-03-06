"""
Copyright (c) 2014-2016 Ehsan Iran-Nejad
Python scripts for Autodesk Revit

This file is part of pyRevit repository at https://github.com/eirannejad/pyRevit

pyRevit is a free set of scripts for Autodesk Revit: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3, as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

See this link for a copy of the GNU General Public License protecting this package.
https://github.com/eirannejad/pyRevit/blob/master/LICENSE
"""

__doc__ = 'Lists all rooms in the model whether they are placed or not'

from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
selection = [doc.GetElement(elId) for elId in __revit__.ActiveUIDocument.Selection.GetElementIds()]

cl = FilteredElementCollector(doc)
list = cl.OfCategory(BuiltInCategory.OST_Rooms).WhereElementIsNotElementType().ToElements()

for el in list:
    print('ROOM NAME: {0} ROOM NUMBER: {1} ROOM ID: {2}'.format(
        el.LookupParameter('Name').AsString().ljust(30),
        el.LookupParameter('Number').AsString().ljust(20),
        el.Id
    ))

print('\n\nTOTAL ROOMS FOUND: {0}'.format(len(list)))
