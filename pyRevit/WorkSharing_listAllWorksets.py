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

__doc__ = 'List all worksets in the model.'

from Autodesk.Revit.DB import Workset, FilteredWorksetCollector, WorksetKind
from Autodesk.Revit.UI import TaskDialog

uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document

cl = FilteredWorksetCollector(doc)
worksetlist = cl.OfKind(WorksetKind.UserWorkset)

if doc.IsWorkshared:
    for ws in worksetlist:
        print('WORKSET: {0} ID: {1}'.format(ws.Name.ljust(50), ws.Id))
else:
    __window__.Close()
    TaskDialog.Show('pyRevit', 'Model is not workshared.')
