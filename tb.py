""" Script to automatically create titleblock on open sheet """
import sys
from datetime import datetime
from pyautocad import Autocad, APoint


def create_tb(project, plate_title, page_number):
    """Create title block in current document"""

    acad = Autocad(create_if_not_exists=True)

    layout1 = acad.doc.PaperSpace

    DESIGNER = "Christian Fleming"
    DIRECTOR = "Danny Gorman"
    SHOW = "Gentleman's Guide\nto Love and Murder"
    SCALE = '3/8" = 1\''
    CURRENTDATE = datetime.now()
    CURRENTMONTH = CURRENTDATE.month
    CURRENTYEAR = CURRENTDATE.year
    CURRENTDAY = CURRENTDATE.day
    DATE = f'{CURRENTMONTH}/{CURRENTDAY}/{CURRENTYEAR}'

    PROJECT = project
    PLATE = plate_title
    PAGE_NUMBER = page_number

    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = [APoint(0.375, 0.375), APoint(0.375, 10.625),
                                                                                                 APoint(16.625, 10.625), APoint(
        16.625, 0.375),
        APoint(0.375, 1.375), APoint(
        16.625, 1.375),
        APoint(3.4, 1.375), APoint(
        3.4, 0.375),
        APoint(7.4, 1.375), APoint(
        7.4, 0.375),
        APoint(11.65, 1.375), APoint(
        11.65, 0.375),
        APoint(15.65, 1.375), APoint(
        15.65, 0.375),
        APoint(7.4, 0.708), APoint(
        15.65, 0.708),
        APoint(7.4, 1.041), APoint(
        15.65, 1.041),
        APoint(0.375, 0.875), APoint(3.4, 0.875)]

    if PAGE_NUMBER == 1:
        trcorner = APoint(p2[0] + 3, p2[1])

        DISTANCE = 0.333
        i = 1
        while i <= 10:
            point1 = APoint(p2[0], p2[1] - (DISTANCE * i))
            point2 = APoint(trcorner[0], trcorner[1] - (DISTANCE * i))
            point3 = APoint(trcorner[0], trcorner[1] - (DISTANCE * (i - 1)))
            mline1 = layout1.AddLine(point1, point2)
            mline2 = layout1.AddLine(point2, point3)
            mline1.layer = "0"
            mline2.layer = "0"
            i += 1

    # create titleblock shape
    line1 = layout1.AddLine(p1, p2)
    line2 = layout1.AddLine(p2, p3)
    line3 = layout1.AddLine(p3, p4)
    line4 = layout1.AddLine(p1, p4)
    line5 = layout1.AddLine(p5, p6)
    line6 = layout1.AddLine(p7, p8)
    line7 = layout1.AddLine(p9, p10)
    line8 = layout1.AddLine(p11, p12)
    line9 = layout1.AddLine(p13, p14)
    line10 = layout1.AddLine(p15, p16)
    line11 = layout1.AddLine(p17, p18)
    line12 = layout1.AddLine(p19, p20)

    # Add Static Text
    show = layout1.AddMText(APoint(.5, 1.3), 3.25, f'{SHOW}')
    show.Height = 0.125
    acad.doc.SendCommand("JUSTIFYTEXT " + "last" + "\n" +
                         " " + "\n" + "middle center ")

    plate = layout1.AddMText(APoint(.5, .8), 3.25, f'{
        PROJECT}' + "\n" + f'{PLATE}')
    plate.Height = 0.125
    acad.doc.SendCommand("JUSTIFYTEXT " + f'{plate}' + "\n" +
                         " " + "\n" + "middle center ")

    abt = layout1.AddMText(APoint(4.55, 1.3), 3.75,
                           "Arizona\nBroadway\nTheatre")
    abt.Height = 0.2
    acad.doc.SendCommand("JUSTIFYTEXT " + "last" + "\n" +
                         " " + "\n" + "middle center ")

    directedBy = layout1.AddMText(
        APoint(7.6, 1.3), 4.25, f'Directed By: {DIRECTOR}')
    directedBy.Height = 0.125

    designedBy = layout1.AddMText(
        APoint(11.8, 1.3), 4.25, f'Designed By: {DESIGNER}')
    designedBy.Height = 0.125

    drawn_by = layout1.AddMText(
        APoint(7.6, .95), 4.25, "Drawn By: Kevin Penner")
    drawn_by.Height = 0.125

    sm = layout1.AddMText(APoint(11.8, .95), 4.25, "SM: Nico Rossetti")
    sm.Height = 0.125

    date = layout1.AddMText(APoint(7.6, .65), 4.25, f'Date: {DATE}')
    date.Height = 0.125

    scale = layout1.AddMText(APoint(11.8, .65), 4.25, f'Scale: {SCALE}')
    scale.Height = 0.125

    pageNumber = layout1.AddMText(APoint(16, 1.15), 1, f'{PAGE_NUMBER}')
    pageNumber.Height = 0.5


project = input("Project: ")
plate = input("Plate: ")
page = input("Page: ")


create_tb(project, plate, page)
