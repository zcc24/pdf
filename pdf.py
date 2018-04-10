#encoding=utf-8
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))
from graphs import *
from dataPackage import *
from reportlab.platypus import SimpleDocTemplate,Paragraph,PageTemplate,FrameBreak
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
import time

class MyPDFdoc():
    def __init__(self,filename):
        self.filename=filename
        self.doc=SimpleDocTemplate(self.filename,pagesize=(12*inch,16*inch))
    def drawPDF(self):
        stylesheet = getSampleStyleSheet()
        normalStyle = stylesheet['Normal']
        stories=[]
        curr_date = time.strftime("%Y-%m-%d", time.localtime())
        enter='<br/><br/><br/><br/><br/>'
        rpt_title = '<para autoLeading="off" fontSize=17 align=center><b><font face="msyh">%s色谱分析报告</font></b><br/><br/><br/></para>'%(curr_date)
        stories.append(Paragraph(rpt_title,normalStyle))
        image_title='<para autoLeading="off" fontSize=13 align=center><b><font face="msyh">色谱图</font></b><br/></para>'
        tip='<para autoLeading="off" fontSize=11 align=right><b><font face="msyh">x：时间  y：mAu</font></b><br/></para>'
        stories.append(Paragraph(image_title,normalStyle))
        stories.append(Paragraph(tip, normalStyle))
        data = getdatas().get_datecounts()
        b1 = graphs().drawline(4 * inch, 3 * inch, *data)
        stories.append(b1)
        stories.append(Paragraph(enter, normalStyle))
        table_title = '<para autoLeading="off" fontSize=13 align=center><b><font face="msyh">谱峰信息表</font></b><br/><br/><br/></para>'
        stories.append(Paragraph(table_title, normalStyle))
        data=getdatas().get_shopcounts()
        t1=graphs().drawtable(*data)
        stories.append(t1)
        #不同日期销售数据

        self.doc.build(stories)
if __name__=="__main__":
    pdf=MyPDFdoc('mypdf.pdf')
    pdf.drawPDF()

