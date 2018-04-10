#encoding=utf-8
from dataConnect import *
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from operator import itemgetter
pdfmetrics.registerFont(TTFont('msyh','msyh.TTF'))
class getdatas():
    def __init__(self):
        pass
    #商店销售数量
    def get_shopcounts(self):
        styles=getSampleStyleSheet()
        styleT=styles['Normal']
        styleT.fontName='xinwei'
        styleT.fontSize=20
        db=dbexecute()
        info=db.select("select num,peakarea,peaktime,peakvalue,halfWidth,resolution,columnvalue,percent  from 1_1521426504_analysis order by num asc;")
        num=[]
        peakarea=[]
        peaktime=[]
        peakvalue=[]
        halfwidth=[]
        resolution=[]
        columnvalue=[]
        percent=[]
        for i in info:
            num.append((i[0]))
            peakarea.append(eval(i[1]))
            peaktime.append(eval(i[2]))
            peakvalue.append(eval(i[3]))
            halfwidth.append(eval(i[4]))
            resolution.append(eval(i[5]))
            columnvalue.append(eval(i[6]))
            percent.append(eval(i[7])*100)
        datas=zip(num,peakarea,peaktime,peakvalue,halfwidth,resolution,columnvalue,percent)
        datas.insert(0,("组分","峰面积","峰顶时间","峰值","半峰宽","分离度","柱效","含量(%)"))
        db.close()
        return datas

    def get_datecounts(self):
        db=dbexecute()
        info=db.select("select mAu,tim from 1_1521426504_filter order by tim asc;")
        mau=[]
        tim=[]
        for i in info :
            mau.append(eval(i[0]))
            tim.append(eval(i[1]))
        print len(mau)
        datas=zip(tim,mau)
        datas=sorted(datas,key=itemgetter(0))
        db.close()
        return datas


