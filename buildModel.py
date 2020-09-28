# ----------------------------------------------
# Build the model based in the modelDate object
# ----------------------------------------------

class buildModel:
    def __init__(self, oEditor):
        oEditor.CreateUserDefinedPart(
            [
                "NAME:UserDefinedPrimitiveParameters",
                "DllName:=", "RMxprt/SlotCore.dll",
                "Version:=", "12.1",
                "NoOfParameters:=", 19,
                "Library:=", "syslib",
                [
                    "NAME:ParamVector",
                    [
                        "NAME:Pair",
                        "Name:=", "DiaGap",
                        "Value:=", "82mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "DiaYoke",
                        "Value:=", "160mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Length",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Skew",
                        "Value:=", "0deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Slots",
                        "Value:=", "24"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SlotType",
                        "Value:=", "4"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs0",
                        "Value:=", "2mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs01",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs1",
                        "Value:=", "2.5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs2",
                        "Value:=", "14mm"
                    ],
                    [  # oeff
                        "NAME:Pair",
                        "Name:=", "Bs0",
                        "Value:=", "1.8mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs1",
                        "Value:=", "7.2mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs2",
                        "Value:=", "11mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Rs",
                        "Value:=", "4mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "FilletType",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "HalfSlot",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SegAngle",
                        "Value:=", "15deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "LenRegion",
                        "Value:=", "200mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "InfoCore",
                        "Value:=", "0"
                    ]
                ]
            ],
            [
                "NAME:Attributes",
                "Name:=", "Slot_Core",
                "Flags:=", "",
                "Color:=", "(128 128 128)",
                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"iron\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:=", False
            ])

        oEditor.CreateUserDefinedPart(
            [
                "NAME:UserDefinedPrimitiveParameters",
                "DllName:=", "RMxprt/SlotCore.dll",
                "Version:=", "12.1",
                "NoOfParameters:=", 19,
                "Library:=", "syslib",
                [
                    "NAME:ParamVector",
                    [
                        "NAME:Pair",
                        "Name:=", "DiaGap",
                        "Value:=", "82mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "DiaYoke",
                        "Value:=", "160mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Length",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Skew",
                        "Value:=", "0deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Slots",
                        "Value:=", "24"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SlotType",
                        "Value:=", "4"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs0",
                        "Value:=", "2mm + iso_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs01",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs1",
                        "Value:=", "2.5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs2",
                        "Value:=", "14mm - iso_thickness"
                    ],
                    [  # oeff
                        "NAME:Pair",
                        "Name:=", "Bs0",
                        "Value:=", "1.8mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs1",
                        "Value:=", "7.2mm -2*iso_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs2",
                        "Value:=", "11mm -3*iso_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Rs",
                        "Value:=", "4mm -2*iso_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "FilletType",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "HalfSlot",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SegAngle",
                        "Value:=", "10deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "LenRegion",
                        "Value:=", "200mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "InfoCore",
                        "Value:=", "0"
                    ]
                ]
            ],
            [
                "NAME:Attributes",
                "Name:=", "Slot_Iso",
                "Flags:=", "",
                "Color:=", "(8 29 88)",

                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"Slot_Iso\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:=", False
            ])

        oEditor.CreateUserDefinedPart(
            [
                "NAME:UserDefinedPrimitiveParameters",
                "DllName:=", "RMxprt/SlotCore.dll",
                "Version:=", "12.1",
                "NoOfParameters:=", 19,
                "Library:=", "syslib",
                [
                    "NAME:ParamVector",
                    [
                        "NAME:Pair",
                        "Name:=", "DiaGap",
                        "Value:=", "82mm+2mm+2mm+2*iso_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "DiaYoke",
                        "Value:=", "160mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Length",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Skew",
                        "Value:=", "0deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Slots",
                        "Value:=", "24"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SlotType",
                        "Value:=", "4"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs0",
                        "Value:=", "wedge_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs01",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs1",
                        "Value:=", "2.5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs2",
                        "Value:=", "3.0mm" # height 0.5 default
                    ],
                    [  # oeff
                        "NAME:Pair",
                        "Name:=", "Bs0",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs1",
                        "Value:=", "7.2mm-3*wedge_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs2",
                        "Value:=", "7mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Rs",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "FilletType",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "HalfSlot",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SegAngle",
                        "Value:=", "15deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "LenRegion",
                        "Value:=", "200mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "InfoCore",
                        "Value:=", "0"
                    ]
                ]
            ],
            [
                "NAME:Attributes",
                "Name:=", "Slot_Wedge",
                "Flags:=", "",
                "Color:=", "(29 145 192)",
                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"Slot_Wedge\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:=", False
            ])

        oEditor.CreateUserDefinedPart(
            [
                "NAME:UserDefinedPrimitiveParameters",
                "DllName:=", "RMxprt/SlotCore.dll",
                "Version:=", "12.1",
                "NoOfParameters:=", 19,
                "Library:=", "syslib",
                [
                    "NAME:ParamVector",
                    [
                        "NAME:Pair",
                        "Name:=", "DiaGap",
                        "Value:=", "82mm+2mm+2mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "DiaYoke",
                        "Value:=", "160mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Length",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Skew",
                        "Value:=", "0deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Slots",
                        "Value:=", "24"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SlotType",
                        "Value:=", "4"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs0",
                        "Value:=", "wedge_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs01",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs1",
                        "Value:=", "2.5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs2",
                        "Value:=", "0mm"
                    ],
                    [  # oeff
                        "NAME:Pair",
                        "Name:=", "Bs0",
                        "Value:=", "1.8mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs1",
                        "Value:=", "7.2mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs2",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Rs",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "FilletType",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "HalfSlot",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SegAngle",
                        "Value:=", "15deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "LenRegion",
                        "Value:=", "200mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "InfoCore",
                        "Value:=", "0"
                    ]
                ]
            ],
            [
                "NAME:Attributes",
                "Name:=", "Slot_Face",
                "Flags:=", "",
                "Color:=", "(0 128 255)",
                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"iron\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:=", False
            ])



        oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:=", "Slot_Iso",
                "Tool Parts:=", "Slot_Core"
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:=", True
            ])

        oEditor.Delete(
            [
                "NAME:Selections",
                "Selections:="	, "Slot_Face"
            ])


        oEditor.CreateCircle(
            [
                "NAME:CircleParameters",
                "IsCovered:=", True,
                "XCenter:=", "0mm",
                "YCenter:=", "0mm",
                "ZCenter:=", "0mm",
                "Radius:=", "45.5mm",
                "WhichAxis:=", "Z",
                "NumSegments:=", "0"
            ],
            [
                "NAME:Attributes",
                "Name:=", "Circle1",
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
        oEditor.Intersect(
            [
                "NAME:Selections",
                "Selections:=", "Slot_Wedge,Circle1"
            ],
            [
                "NAME:IntersectParameters",
                "KeepOriginals:=", False
            ])

        oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:=", "Slot_Wedge",
                "Tool Parts:=", "Slot_Core,Slot_Iso"
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:=", True
            ])

        # Zwischenisolation
        oEditor.CreateUserDefinedPart(
            [
                "NAME:UserDefinedPrimitiveParameters",
                "DllName:=", "RMxprt/SlotCore.dll",
                "Version:=", "12.1",
                "NoOfParameters:=", 19,
                "Library:=", "syslib",
                [
                    "NAME:ParamVector",
                    [
                        "NAME:Pair",
                        "Name:=", "DiaGap",
                        "Value:=", "82mm+2mm+2mm+2*iso_thickness+21.2mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "DiaYoke",
                        "Value:=", "160mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Length",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Skew",
                        "Value:=", "0deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Slots",
                        "Value:=", "24"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SlotType",
                        "Value:=", "4"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs0",
                        "Value:=", "wedge_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs01",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs1",
                        "Value:=", "2.5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs2",
                        "Value:=", "0.5mm"
                    ],
                    [  # oeff
                        "NAME:Pair",
                        "Name:=", "Bs0",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs1",
                        "Value:=", "10.2mm-3*wedge_thickness+0.2mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs2",
                        "Value:=", "5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Rs",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "FilletType",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "HalfSlot",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SegAngle",
                        "Value:=", "15deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "LenRegion",
                        "Value:=", "200mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "InfoCore",
                        "Value:=", "0"
                    ]
                ]
            ],
            [
                "NAME:Attributes",
                "Name:=", "Slot_Wedge_Mid",
                "Flags:=", "",
                "Color:=", "(29 145 192)",
                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"Slot_Sep\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:=", False
            ])


        oEditor.CreateUserDefinedPart(
            [
                "NAME:UserDefinedPrimitiveParameters",
                "DllName:=", "RMxprt/SlotCore.dll",
                "Version:=", "12.1",
                "NoOfParameters:=", 19,
                "Library:=", "syslib",
                [
                    "NAME:ParamVector",
                    [
                        "NAME:Pair",
                        "Name:=", "DiaGap",
                        "Value:=", "82mm+2mm+2mm+2*iso_thickness+20.7mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "DiaYoke",
                        "Value:=", "160mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Length",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Skew",
                        "Value:=", "0deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Slots",
                        "Value:=", "24"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SlotType",
                        "Value:=", "4"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs0",
                        "Value:=", "wedge_thickness"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs01",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs1",
                        "Value:=", "2.5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Hs2",
                        "Value:=", "0.5mm"
                    ],
                    [  # oeff
                        "NAME:Pair",
                        "Name:=", "Bs0",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs1",
                        "Value:=", "10.7mm-3*wedge_thickness+0.1mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Bs2",
                        "Value:=", "5mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "Rs",
                        "Value:=", "0mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "FilletType",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "HalfSlot",
                        "Value:=", "0"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "SegAngle",
                        "Value:=", "15deg"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "LenRegion",
                        "Value:=", "200mm"
                    ],
                    [
                        "NAME:Pair",
                        "Name:=", "InfoCore",
                        "Value:=", "0"
                    ]
                ]
            ],
            [
                "NAME:Attributes",
                "Name:=", "Slot_Wedge_Mid_tool",
                "Flags:=", "",
                "Color:=", "(29 145 192)",
                "Transparency:=", 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:=", "",
                "MaterialValue:=", "\"Slot_Sep\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:=", True,
                "IsMaterialEditable:=", True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:=", False
            ])

        oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:="	, "Slot_Wedge_Mid",
                "Tool Parts:="		, "Slot_Wedge_Mid_tool"
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:="	, False
            ])
        oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:="		, "Slot_Wedge_Mid",
                "Tool Parts:="		, "Slot_Iso"
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:="	, True
            ])


        oEditor.CreatePolyline(
            [
                "NAME:PolylineParameters",
                "IsPolylineCovered:=", True,
                "IsPolylineClosed:=", True,
                [
                    "NAME:PolylinePoints",
                    [
                        "NAME:PLPoint",
                        "X:="		, "80mm",
                        "Y:="			, "0mm",
                        "Z:="			, "0mm"
                    ],
                    [
                        "NAME:PLPoint",
                        "X:="			, "-79.3155889099048mm",
                        "Y:="			, "-10.4420953776041mm",
                        "Z:="			, "0mm"
                    ],
                    [
                        "NAME:PLPoint",
                        "X:="			, "77.2740661031255mm",
                        "Y:="			, "20.7055236082017mm",
                        "Z:="			, "0mm"
                    ],
                    [
                        "NAME:PLPoint",
                        "X:="			, "0mm",
                        "Y:="			, "0mm",
                        "Z:="			, "0mm"
                    ],
                    [
                        "NAME:PLPoint",
                        "X:="			, "80mm",
                        "Y:="			, "0mm",
                        "Z:="			, "0mm"
                    ]
                ],
                [
                    "NAME:PolylineSegments",
                    [
                        "NAME:PLSegment",
                        "SegmentType:="		, "AngularArc",
                        "StartIndex:="		, 0,
                        "NoOfPoints:="		, 3,
                        "NoOfSegments:="	, "0",
                        "ArcAngle:="		, "-345deg",
                        "ArcCenterX:="		, "0mm",
                        "ArcCenterY:="		, "0mm",
                        "ArcCenterZ:="		, "0mm",
                        "ArcPlane:="		, "XY"
                    ],
                    [
                        "NAME:PLSegment",
                        "SegmentType:="		, "Line",
                        "StartIndex:="		, 2,
                        "NoOfPoints:="		, 2
                    ],
                    [
                        "NAME:PLSegment",
                        "SegmentType:="		, "Line",
                        "StartIndex:="		, 3,
                        "NoOfPoints:="		, 2
                    ]
                ],
                [
                    "NAME:PolylineXSection",
                    "XSectionType:="	, "None",
                    "XSectionOrient:="	, "Auto",
                    "XSectionWidth:="	, "0mm",
                    "XSectionTopWidth:="	, "0mm",
                    "XSectionHeight:="	, "0mm",
                    "XSectionNumSegments:="	, "0",
                    "XSectionBendType:="	, "Corner"
                ]
            ],
            [
                "NAME:Attributes",
                "Name:="		, "Polyline5",
                "Flags:="		, "",
                "Color:="		, "(143 175 143)",
                "Transparency:="	, 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"vacuum\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="		, True,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:="	, False
            ])



        oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:="		, "Slot_Core,Slot_Iso,Slot_Wedge,Slot_Wedge_Mid",
                "Tool Parts:="		, "Polyline5"
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:="	, False
            ])









        # Rotation neu
        oEditor.Rotate(
            [
                "NAME:Selections",
                "Selections:=", "Slot_Core,Slot_Iso,Slot_Wedge,Slot_Wedge_Mid",
                "NewPartsModelFlag:=", "Model"
            ],
            [
                "NAME:RotateParameters",
                "RotateAxis:=", "Z",
                "RotateAngle:=", "-7.5deg+90deg"
            ])
        #
        oEditor.Move(
            [
                "NAME:Selections",
                "Selections:=", "Slot_Core,Slot_Iso,Slot_Wedge,Slot_Wedge_Mid",
                "NewPartsModelFlag:=", "Model"
            ],
            [
                "NAME:TranslateParameters",
                "TranslateVectorX:=", "0mm",
                "TranslateVectorY:=", "-41mm",
                "TranslateVectorZ:=", "0mm"
            ])

        #Potting material
        oEditor.CreateRectangle(
            [
                "NAME:RectangleParameters",
                "IsCovered:="	, True,
                "XStart:="		, "-10mm",
                "YStart:="		, "26mm",
                "ZStart:="		, "0mm",
                "Width:="		, "20mm",
                "Height:="		, "-26mm",
                "WhichAxis:="		, "Z"
            ],
            [
                "NAME:Attributes",
                "Name:="		, "Potting",
                "Flags:="		, "",
                "Color:="		, "(143 175 143)",
                "Transparency:="	, 0,
                "PartCoordinateSystem:=", "Global",
                "UDMId:="		, "",
                "MaterialValue:="	, "\"vacuum\"",
                "SurfaceMaterialValue:=", "\"\"",
                "SolveInside:="		, True,
                "IsMaterialEditable:="	, True,
                "UseMaterialAppearance:=", False,
                "IsLightweight:="	, False
            ])

        oEditor.Subtract(
            [
                "NAME:Selections",
                "Blank Parts:="		, "Potting",
                "Tool Parts:="		, "Slot_Core,Slot_Iso,Slot_Wedge,Slot_Wedge_Mid"
            ],
            [
                "NAME:SubtractParameters",
                "KeepOriginals:="	, True
            ])
        oEditor.SeparateBody(
            [
                "NAME:Selections",
                "Selections:="		, "Potting",
                "NewPartsModelFlag:="	, "Model"
            ],
            [
                "CreateGroupsForNewObjects:=", False
            ])
        oEditor.Delete(
            [
                "NAME:Selections",
                "Selections:="		, "Potting"
            ])
        oEditor.Delete(
            [
                "NAME:Selections",
                "Selections:="		, "Potting_Separate1"
            ])

        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "Potting_Separate3"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 255,
                            "G:="			, 255,
                            "B:="			, 255
                        ]
                    ]
                ]
            ])
        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "Potting_Separate2"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="			, 255,
                            "G:="			, 255,
                            "B:="			, 255
                        ]
                    ]
                ]
            ])

        oEditor.ChangeProperty(
            [
                "NAME:AllTabs",
                [
                    "NAME:Geometry3DAttributeTab",
                    [
                        "NAME:PropServers",
                        "Potting_Separate4"
                    ],
                    [
                        "NAME:ChangedProps",
                        [
                            "NAME:Color",
                            "R:="		, 255,
                            "G:="			, 255,
                            "B:="			, 255
                        ]
                    ]
                ]
            ])


