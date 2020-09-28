import gc
import random
# init
import math
from modelData import modelData
from buildModel import buildModel
from comtypes.client import CreateObject
import numpy as np

def is_point_in_path(x, y, poly) -> bool:
    """Determine if the point is in the path.
    # https://en.wikipedia.org/wiki/Even%E2%80%93odd_rule#cite_note-3
    Args:
      x -- The x coordinates of point.
      y -- The y coordinates of point.
      poly -- a list of tuples [(x, y), (x, y), ...]

    Returns:
      True if the point is in the path.
    """
    num = np.shape(poly)[0]
    i = 0
    j = num - 1
    c = False
    for i in range(num):
        if ((poly[i,1] > y) != (poly[j,1] > y)) and \
                (x < poly[i,0] + (poly[j,0] - poly[i,0]) * (y - poly[i,1]) /
                                  (poly[j,1] - poly[i,1])):
            c = not c
        j = i
    return c

modelData = modelData()  # simple data input

iMaxwell = CreateObject("Ansoft.ElectronicsDesktop", clsctx=None, machine=None, interface=None, dynamic=True,
                        pServerInfo=None)
oDesktop = iMaxwell.GetAppDesktop()
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject(modelData.projectName)
oProject.InsertDesign("Maxwell 2D", modelData.designName, modelData.solutionType, "")
oDesign = oProject.SetActiveDesign(modelData.designName)
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.SetModelUnits(
    [
        "NAME:Units Parameter",
        "Units:=", "mm",
        "Rescale:=", False
    ]
)

# analysisSetup(oDesign, modelData)
# designProperties(oDesign, modelData)

oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers",
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:iso_thickness",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "0.17mm"  # NutIsolation
                ]
            ]
        ]
    ])

oDesign.ChangeProperty(
    [
        "NAME:AllTabs",
        [
            "NAME:LocalVariableTab",
            [
                "NAME:PropServers",
                "LocalVariables"
            ],
            [
                "NAME:NewProps",
                [
                    "NAME:wedge_thickness",
                    "PropType:=", "VariableProp",
                    "UserDef:=", True,
                    "Value:=", "0.37mm"  # Deckschieber
                ]
            ]
        ]
    ])

oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
    [
        "NAME:Slot_Iso",
        "CoordinateSystemType:=", "Cartesian",
        "BulkOrSurfaceType:=", 1,
        [
            "NAME:PhysicsTypes",
            "set:=", ["Electromagnetic"]
        ],
        [
            "NAME:AttachedData",
            [
                "NAME:MatAppearanceData",
                "property_data:=", "appearance_data",
                "Red:=", 128,
                "Green:=", 0,
                "Blue:=", 0,
                "Transparency:=", 0
            ]
        ],
        "permittivity:=", "2.1551"
    ])

oDefinitionManager.AddMaterial(
    [
        "NAME:Slot_Wedge",
        "CoordinateSystemType:=", "Cartesian",
        "BulkOrSurfaceType:=", 1,
        [
            "NAME:PhysicsTypes",
            "set:=", ["Electromagnetic"]
        ],
        [
            "NAME:AttachedData",
            [
                "NAME:MatAppearanceData",
                "property_data:=", "appearance_data",
                "Red:=", 128,
                "Green:=", 0,
                "Blue:=", 0,
                "Transparency:=", 0
            ]
        ],
        "permittivity:=", "2.53151"
    ])

oDefinitionManager.AddMaterial(
    [
        "NAME:Slot_Sep",
        "CoordinateSystemType:=", "Cartesian",
        "BulkOrSurfaceType:=", 1,
        [
            "NAME:PhysicsTypes",
            "set:=", ["Electromagnetic"]
        ],
        [
            "NAME:AttachedData",
            [
                "NAME:MatAppearanceData",
                "property_data:=", "appearance_data",
                "Red:=", 128,
                "Green:=", 0,
                "Blue:=", 0,
                "Transparency:=", 0
            ]
        ],
        "permittivity:=", "1.93171"
    ])

oDefinitionManager.AddMaterial(
    [
        "NAME:Conductor_Iso",
        "CoordinateSystemType:=", "Cartesian",
        "BulkOrSurfaceType:=", 1,
        [
            "NAME:PhysicsTypes",
            "set:=", ["Electromagnetic"]
        ],
        [
            "NAME:AttachedData",
            [
                "NAME:MatAppearanceData",
                "property_data:=", "appearance_data",
                "Red:=", 128,
                "Green:=", 0,
                "Blue:=", 0,
                "Transparency:=", 0
            ]
        ],
        "permittivity:=", "4.1721"
    ])

buildModel(oEditor)



drawConductors = True

max_number_of_fails = 100000

lower_y = 2.6

number_of_concutors_slot = 120

upper_y = 14#12.89  #

existing_locations = []

j = 0
i = 0

fails = 0
R = 0.25  # Packing Problem 0.25 mm * 5.65166 = 1.4129 mm
R_iso = R + 0.0225
list_of_lower_conductors = []  # list of conductors for to assign excitations to

# Border inputs
x1 = 0.6
y1 = lower_y
y2 = 4.8
x2 = 3.45
y3 = 14
x3 = 4.65
y4 = 12.9
x4 = 3.2
x5 = 1.75
y5 = 12.9
R_set = np.array([[0, y1],
                  [x1, y1],
                  [x2, y2],
                  [x3, y3],
                  [x4, y4],
                  [x5, y5],
                  [0, y5]])

R_set_mirror = -1*R_set[:,0]
R_set_mirror = np.transpose(np.vstack((R_set_mirror,R_set[:,1])))
R_set_mirror = np.flip(R_set_mirror, axis = 0)
closed_polygon = np.vstack((R_set,R_set_mirror[1:-1,:]))

x_vec = R_set[:, 0]
y_vec = R_set[:, 1]

area1 = 2 * abs(sum(x_vec[idx] * (y_vec[idx + 1] - y_vec[idx - 1]) for idx in range(-1, len(x_vec) - 1))) / 2.0

R_set2 = np.vstack((-1.0 * x_vec, y_vec))
# Probe für das erweiterte set
R_set3 = np.vstack((R_set,np.transpose(R_set2)))

y_center = np.mean(R_set[:, 1], axis=0)


# print(area1)


# Plot border
plotBorder = False
if plotBorder:
    oEditor.CreatePolyline(
        [
            "NAME:PolylineParameters",
            "IsPolylineCovered:=", True,
            "IsPolylineClosed:=", False,
            [
                "NAME:PolylinePoints",
                [
                    "NAME:PLPoint",
                    "X:=", str(x1) + "mm",
                    "Y:=", str(lower_y) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x2) + "mm",
                    "Y:=", str(y2) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x3) + "mm",
                    "Y:=", str(y3) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x4) + "mm",
                    "Y:=", str(y4) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x5) + "mm",
                    "Y:=", str(y5) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(0) + "mm",
                    "Y:=", str(y5) + "mm",
                    "Z:=", "0mm"
                ]
            ],
            [
                "NAME:PolylineSegments",
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 0,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 1,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 2,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 3,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 4,
                    "NoOfPoints:=", 2
                ]
            ],
            [
                "NAME:PolylineXSection",
                "XSectionType:=", "None",
                "XSectionOrient:=", "Auto",
                "XSectionWidth:=", "0mm",
                "XSectionTopWidth:=", "0mm",
                "XSectionHeight:=", "0mm",
                "XSectionNumSegments:=", "0",
                "XSectionBendType:=", "Corner"
            ]
        ],
        [
            "NAME:Attributes",
            "Name:=", "Border",
            "Flags:=", "",
            "Color:=", "(143 175 143)",
            "Transparency:=", 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", "\"vacuum\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:=", True,
            "IsMaterialEditable:=", True,
            "UseMaterialAppearance:=", False,
            "IsLightweight:=", False
        ])

if drawConductors == True:
    while j < number_of_concutors_slot:  # do this as long as all conductors j are placed
        print(fails)
        if fails == max_number_of_fails:
            break
        intersection = False  # reset intersection status

        alpha = 0.2#0.2 oder 0.5
        beta = 2.0#2. oder 0.5

        a = lower_y + 1.015*R_iso  # -5
        c = upper_y - 1.015*R_iso  # 5

        y = np.random.beta(alpha, beta)

        y = y * (c - a) + a

        #y = np.random.uniform(a, c)
        y = np.random.triangular(a, (a + c) / 2, c)

        if y < y2:  # Fist section
            m = (y2 - lower_y) / (x2 - x1)
            b = y2 - m * x2
            border = (y - b) / m  # rearranged line equation
        elif y < y3:  # Second section
            m = (y3 - y2) / (x3 - x2)
            b = y3 - m * x3
            border = (y - b) / m  # rearranged line equation
        elif y < y4:  # Second section
            m = (y4 - y3) / (x4 - x3)
            b = y4 - m * x4
            border = (y - b) / m  # rearranged line equation
        elif y < y5:
            m = (y5 - y4) / (x5 - x4)
            b = y5 - m * x5
            border = (y - b) / m  # rearranged line equation

        x = np.random.beta(alpha, beta)

        a = -border + 1.015*R_iso  # -5
        c = border - 1.015*R_iso  # 5
        x = x * (c - a) + a

        #x = np.random.uniform(a, c)
        x = np.random.triangular(a, (a + c) / 2, c)

        x_test = np.linspace(x-R_iso,x+R_iso,10)
        outer_points_pos = y + np.sqrt(R_iso ** 2 - (x_test - x) ** 2)
        outer_points_neg = y - np.sqrt(R_iso ** 2 - (x_test - x) ** 2)

        outer_points = np.hstack((outer_points_pos,outer_points_neg))
        x_test = np.hstack((x_test,x_test))

        for i in np.arange(np.shape(outer_points)[0]):
            if is_point_in_path(x_test[i],outer_points[i],closed_polygon) == False:
                intersection = True


        # second outer range for condutors
        new_location = (x, y)

        for location in existing_locations:  # check new_location against all old locations
            distance = math.sqrt(((new_location[0] - location[0]) ** 2) + (
                    (new_location[1] - location[1]) ** 2))  # circle equation to determin distance
            # factor if 1.05 to account for circle segmentation
            if distance <= 2 * R_iso * 1.015:
                intersection = True
                fails = fails + 1
                break

        if intersection == False:
            existing_locations.append(new_location)

            conductor = oEditor.CreateCircle(  # place a conductor
                [
                    "NAME:CircleParameters",
                    "IsCovered:=", True,
                    "XCenter:=", str(new_location[0]) + "mm",
                    "YCenter:=", str(new_location[1]) + "mm",
                    "ZCenter:=", "0mm",
                    "Radius:=", str(R) + "mm",
                    "WhichAxis:=", "Z",
                    "NumSegments:=", "20"
                ],
                [
                    "NAME:Attributes",
                    "Name:=", "Lower_Conductor" + str(j + 1),
                    "Flags:=", "",
                    "Color:=", "(143 78 53)",
                    "Transparency:=", 0,
                    "PartCoordinateSystem:=", "Global",
                    "UDMId:=", "",
                    "MaterialValue:=", "\"copper\"",
                    "SurfaceMaterialValue:=", "\"\"",
                    "SolveInside:=", True,
                    "IsMaterialEditable:=", True,
                    "UseMaterialAppearance:=", False,
                    "IsLightweight:=", False
                ])

            oEditor.CreateCircle(  # place a conductor
                [
                    "NAME:CircleParameters",
                    "IsCovered:=", True,
                    "XCenter:=", str(new_location[0]) + "mm",
                    "YCenter:=", str(new_location[1]) + "mm",
                    "ZCenter:=", "0mm",
                    "Radius:=", str(R_iso) + "mm",
                    "WhichAxis:=", "Z",
                    "NumSegments:=", "20"
                ],
                [
                    "NAME:Attributes",
                    "Name:=", "Lower_Conductor_iso" + str(j + 1),
                    "Flags:=", "",
                    "Color:=", "(0 0 0)",
                    "Transparency:=", 0,
                    "PartCoordinateSystem:=", "Global",
                    "UDMId:=", "",
                    "MaterialValue:=", "\"Conductor_Iso\"",
                    "SurfaceMaterialValue:=", "\"\"",
                    "SolveInside:=", True,
                    "IsMaterialEditable:=", True,
                    "UseMaterialAppearance:=", False,
                    "IsLightweight:=", False
                ])

            j = j + 1
            list_of_lower_conductors.append(conductor)

# Upper conductors
max_number_of_fails = 100000

lower_y = 13.14
upper_y = 22.15  #

existing_locations = []
list_of_upper_conductors = []
j = 0
i = 0
fails = 0

# Border inputs
x1 = 1.8
y1 = lower_y
y2 = 14.39
x2 = 4.31
y3 = 18.49
x3 = 5.245
y4 = 20.64
x4 = 4.56
x5 = 1.75
y5 = upper_y

R_set = np.array([[0, y1],
                  [x1, y1],
                  [x2, y2],
                  [x3, y3],
                  [x4, y4],
                  [x5, y5],
                  [0, y5]])

R_set_mirror = -1*R_set[:,0]
R_set_mirror = np.transpose(np.vstack((R_set_mirror,R_set[:,1])))
R_set_mirror = np.flip(R_set_mirror, axis = 0)
closed_polygon = np.vstack((R_set,R_set_mirror[1:-1,:]))

x_vec = R_set[:, 0]
y_vec = R_set[:, 1]

y_center = np.mean(R_set[:, 1], axis=0)

# x = np.array([0, 1, 1])
# y = np.array([0, 0, 1])

area2 = 2 * abs(sum(x_vec[idx] * (y_vec[idx + 1] - y_vec[idx - 1]) for idx in range(-1, len(x_vec) - 1))) / 2.0

# Plot border


if plotBorder:
    oEditor.CreatePolyline(
        [
            "NAME:PolylineParameters",
            "IsPolylineCovered:=", True,
            "IsPolylineClosed:=", False,
            [
                "NAME:PolylinePoints",
                [
                    "NAME:PLPoint",
                    "X:=", str(x1) + "mm",
                    "Y:=", str(lower_y) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x2) + "mm",
                    "Y:=", str(y2) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x3) + "mm",
                    "Y:=", str(y3) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x4) + "mm",
                    "Y:=", str(y4) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(x5) + "mm",
                    "Y:=", str(upper_y) + "mm",
                    "Z:=", "0mm"
                ],
                [
                    "NAME:PLPoint",
                    "X:=", str(0) + "mm",
                    "Y:=", str(upper_y) + "mm",
                    "Z:=", "0mm"
                ]
            ],
            [
                "NAME:PolylineSegments",
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 0,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 1,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 2,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 3,
                    "NoOfPoints:=", 2
                ],
                [
                    "NAME:PLSegment",
                    "SegmentType:=", "Line",
                    "StartIndex:=", 4,
                    "NoOfPoints:=", 2
                ]
            ],
            [
                "NAME:PolylineXSection",
                "XSectionType:=", "None",
                "XSectionOrient:=", "Auto",
                "XSectionWidth:=", "0mm",
                "XSectionTopWidth:=", "0mm",
                "XSectionHeight:=", "0mm",
                "XSectionNumSegments:=", "0",
                "XSectionBendType:=", "Corner"
            ]
        ],
        [
            "NAME:Attributes",
            "Name:=", "Border",
            "Flags:=", "",
            "Color:=", "(143 175 143)",
            "Transparency:=", 0,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", "\"vacuum\"",
            "SurfaceMaterialValue:=", "\"\"",
            "SolveInside:=", True,
            "IsMaterialEditable:=", True,
            "UseMaterialAppearance:=", False,
            "IsLightweight:=", False
        ])

if drawConductors == True:
    while j < number_of_concutors_slot:  # do this as long as all conductors j are placed
        print(fails)
        if fails == max_number_of_fails:
            break
        intersection = False  # reset intersection status

        alpha = 0.2#0.2 oder 0.5
        beta = 2.0#2. oder 0.5

        y = np.random.beta(alpha, beta)

        a = lower_y + 1.015*R_iso  # -5
        c = upper_y - 1.015*R_iso  # 5
        y = y * (c - a) + a

        #y = np.random.uniform(a, c)
        y = np.random.triangular(a, (a + c) / 2, c)

        if y < y2:  # Fist section
            m = (y2 - y1) / (x2 - x1)
            b = y2 - m * x2
            border = (y - b) / m  # rearranged line equation
        elif y < y3:  # Second section
            m = (y3 - y2) / (x3 - x2)
            b = y3 - m * x3
            border = (y - b) / m  # rearranged line equation
        elif y < y4:  # Second section
            m = (y4 - y3) / (x4 - x3)
            b = y4 - m * x4
            border = (y - b) / m  # rearranged line equation
        elif y < upper_y:
            m = (y5 - y4) / (x5 - x4)
            b = y5 - m * x5
            border = (y - b) / m  # rearranged line equation

        # second outer range for condutors

        x = np.random.beta(alpha, beta)
        a = -border + 1.015*R_iso  # -5
        c = border - 1.015*R_iso  # 5
        x = x * (c - a) + a

        #x = np.random.uniform(a, c)
        x = np.random.triangular(a, (a+c)/2, c)

        x_test = np.linspace(x-R_iso,x+R_iso,10)
        outer_points_pos = y + np.sqrt(R_iso ** 2 - (x_test - x) ** 2)
        outer_points_neg = y - np.sqrt(R_iso ** 2 - (x_test - x) ** 2)

        outer_points = np.hstack((outer_points_pos,outer_points_neg))
        x_test = np.hstack((x_test,x_test))

        for i in np.arange(np.shape(outer_points)[0]):
            if is_point_in_path(x_test[i],outer_points[i],closed_polygon) == False:
                intersection = True

        new_location = (x, y)

        for location in existing_locations:  # check new_location against all old locations
            distance = math.sqrt(((new_location[0] - location[0]) ** 2) + (
                    (new_location[1] - location[1]) ** 2))  # circle equation to determin distance
            # factor if 1.05 to account for circle segmentation
            if distance <= 2 * R_iso * 1.015:
                intersection = True
                fails = fails + 1
                break

        if intersection == False:
            existing_locations.append(new_location)

            conductor = oEditor.CreateCircle(  # place a conductor
                [
                    "NAME:CircleParameters",
                    "IsCovered:=", True,
                    "XCenter:=", str(new_location[0]) + "mm",
                    "YCenter:=", str(new_location[1]) + "mm",
                    "ZCenter:=", "0mm",
                    "Radius:=", str(R) + "mm",
                    "WhichAxis:=", "Z",
                    "NumSegments:=", "20"
                ],
                [
                    "NAME:Attributes",
                    "Name:=", "Upper_Conductor" + str(j + 1),
                    "Flags:=", "",
                    "Color:=", "(143 78 53)",
                    "Transparency:=", 0,
                    "PartCoordinateSystem:=", "Global",
                    "UDMId:=", "",
                    "MaterialValue:=", "\"copper\"",
                    "SurfaceMaterialValue:=", "\"\"",
                    "SolveInside:=", True,
                    "IsMaterialEditable:=", True,
                    "UseMaterialAppearance:=", False,
                    "IsLightweight:=", False
                ])

            oEditor.CreateCircle(  # place a conductor
                [
                    "NAME:CircleParameters",
                    "IsCovered:=", True,
                    "XCenter:=", str(new_location[0]) + "mm",
                    "YCenter:=", str(new_location[1]) + "mm",
                    "ZCenter:=", "0mm",
                    "Radius:=", str(R_iso) + "mm",
                    "WhichAxis:=", "Z",
                    "NumSegments:=", "20"
                ],
                [
                    "NAME:Attributes",
                    "Name:=", "Upper_Conductor_iso" + str(j + 1),
                    "Flags:=", "",
                    "Color:=", "(0 0 0)",
                    "Transparency:=", 0,
                    "PartCoordinateSystem:=", "Global",
                    "UDMId:=", "",
                    "MaterialValue:=", "\"Conductor_Iso\"",
                    "SurfaceMaterialValue:=", "\"\"",
                    "SolveInside:=", True,
                    "IsMaterialEditable:=", True,
                    "UseMaterialAppearance:=", False,
                    "IsLightweight:=", False
                ])

            j = j + 1
            list_of_upper_conductors.append(conductor)

# Exitations
oModule = oDesign.GetModule("BoundarySetup")
for conductors in list_of_lower_conductors:
    oModule.AssignVoltage(
        [
            "Name:" + conductors,
            "Objects:=", [conductors],
            "Value:=", "-1V",
            "CoordinateSystem:=", ""
        ]

    )

for conductors in list_of_upper_conductors:
    oModule.AssignVoltage(
        [
            "Name:" + conductors,
            "Objects:=", [conductors],
            "Value:=", "1V",
            "CoordinateSystem:=", ""
        ]

    )

oModule.AssignVoltage(
    [
        "NAME:Slot",
        "Objects:=", ["Slot_Core"],
        "Value:=", "0V",
        "CoordinateSystem:=", ""
    ])

# Region
oEditor.CreateRegion(
    [
        "NAME:RegionParameters",
        "+XPaddingType:=", "Percentage Offset",
        "+XPadding:=", "0",
        "-XPaddingType:=", "Percentage Offset",
        "-XPadding:=", "0",
        "+YPaddingType:=", "Percentage Offset",
        "+YPadding:=", "0",
        "-YPaddingType:=", "Percentage Offset",
        "-YPadding:=", "30",
        "+ZPaddingType:=", "Percentage Offset",
        "+ZPadding:=", "0",
        "-ZPaddingType:=", "Percentage Offset",
        "-ZPadding:=", "0"
    ],
    [
        "NAME:Attributes",
        "Name:=", "Region",
        "Flags:=", "Wireframe#",
        "Color:=", "(143 175 143)",
        "Transparency:=", 0,
        "PartCoordinateSystem:=", "Global",
        "UDMId:=", "",
        "MaterialValue:=", "\"vacuum\"",
        "SurfaceMaterialValue:=", "\"\"",
        "SolveInside:=", True,
        "IsMaterialEditable:=", True,
        "UseMaterialAppearance:=", False,
        "IsLightweight:=", False
    ])

# AnalyseSetup for Release 19.2.0
oDesign = oProject.SetActiveDesign(modelData.designName)
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("Electrostatic",
                    [
                        "NAME:Setup1",
                        "Enabled:=", True,
                        "MaximumPasses:=", 15,
                        "MinimumPasses:=", 2,
                        "MinimumConvergedPasses:=", 1,
                        "PercentRefinement:=", 30,
                        "SolveFieldOnly:=", False,
                        "PercentError:=", 0.01,
                        "SolveMatrixAtLast:=", True,
                        "PercentError:=", 1,
                        "NonLinearResidual:=", 0.001
                    ])

del oEditor
del oDesign
del oProject
del oDesktop
del iMaxwell
gc.collect()
