#encoding=utf-8
from reportlab.platypus import Table,TableStyle,SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import  letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('xinwei','STXINWEI.TTF'))
class graphs():
    def __init__(self):
        self.styles=getSampleStyleSheet()
        self.styleT=self.styles['Normal']
        self.styleT.fontName='xinwei'
        self.styleT.fontSize=20
    def drawtable(self,*args):
        table=Table(args)
        table.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'msyh'),('INNERGRID',(0,0),(-1,-1),0.25,colors.black),('BOX',(0,0),(-1,-1),0.25,colors.black)]))
        return table


    def drawline(self,width,height,*args):
        drawing=Drawing(width,height)
        ab=LinePlot()
        ab.x=180
        ab.y=0
        ab.height=200
        ab.width=420
        ab.xValueAxis._valueMin = 0
        ab.yValueAxis._valueMin=0
        ab.joinedLines=1
        ab.data=[args]
        ab.lines[0].strokeColor=colors.red
        drawing.add(ab)
        return drawing


