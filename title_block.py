""" Script to automatically create titleblock on open sheet """
from datetime import datetime
from pyautocad import Autocad, APoint

acad = Autocad(create_if_not_exists=True)

layout1 = acad.doc.PaperSpace

DESIGNER = "Douglas Clark"
DIRECTOR = "Anthony Daniels"
SHOW = "Charlie and the Chocolate Factory"
SCALE = '1/2" = 1\''
CURRENTDATE = datetime.now()
CURRENTMONTH = CURRENTDATE.month
CURRENTYEAR = CURRENTDATE.year
CURRENTDAY = CURRENTDATE.day
DATE = f'{CURRENTMONTH}/{CURRENTDAY}/{CURRENTYEAR}'

PROJECT = input("Enter Project Name: ")
PLATE = input("Enter Plate Title: ")
PAGE_NUMBER = input("Enter Page Number: ")

p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20 = [APoint(0.15, 0.15), APoint(0.15, 10.85),
                                                                                             APoint(16.85, 10.85), APoint(
    16.85, 0.15),
    APoint(0.15, 1.65), APoint(
    16.85, 1.65),
    APoint(3.4, 1.65), APoint(
    3.4, 0.15),
    APoint(7.4, 1.65), APoint(7.4, 0.15),
    APoint(11.65, 1.65), APoint(11.65, 0.15),
    APoint(15.65, 1.65), APoint(15.65, 0.15),
    APoint(7.4, 0.65), APoint(15.65, 0.65),
    APoint(7.4, 1.15), APoint(15.65, 1.15),
    APoint(0.15, 0.9), APoint(3.4, 0.9)]


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
show = layout1.AddMText(APoint(.5, 1.5), 3.25, f'{SHOW}')
show.Height = 0.175
acad.doc.SendCommand("JUSTIFYTEXT " + "last" + "\n" +
                     " " + "\n" + "middle center ")

plate = layout1.AddMText(APoint(.5, .75), 3.25, f'{
                         PROJECT}' + "\n" + f'{PLATE}')
plate.Height = 0.175
acad.doc.SendCommand("JUSTIFYTEXT " + f'{plate}' + "\n" +
                     " " + "\n" + "middle center ")

abt = layout1.AddMText(APoint(4.55, 1.5), 3.75, "Arizona\nBroadway\nTheatre")
abt.Height = 0.25
acad.doc.SendCommand("JUSTIFYTEXT " + "last" + "\n" +
                     " " + "\n" + "middle center ")

directedBy = layout1.AddMText(
    APoint(7.6, 1.5), 4.25, f'Directed By: {DIRECTOR}')
directedBy.Height = 0.175


designedBy = layout1.AddMText(
    APoint(11.8, 1.5), 4.25, f'Designed By: {DESIGNER}')
designedBy.Height = 0.175


drawn_by = layout1.AddMText(
    APoint(7.6, 1), 4.25, "Drawn By: Kevin Penner")
drawn_by.Height = 0.175


sm = layout1.AddMText(APoint(11.8, 1), 4.25, "SM: Nico Rossetti")
sm.Height = 0.175

date = layout1.AddMText(APoint(7.6, .5), 4.25, f'Date: {DATE}')
date.Height = 0.175


scale = layout1.AddMText(APoint(11.8, .5), 4.25, f'Scale: {SCALE}')
scale.Height = 0.175

pageNumber = layout1.AddMText(APoint(16.15, 1.15), 1, f'{PAGE_NUMBER}')
pageNumber.Height = 0.5
