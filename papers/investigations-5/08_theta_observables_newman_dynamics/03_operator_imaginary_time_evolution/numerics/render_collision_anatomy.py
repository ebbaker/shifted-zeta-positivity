"""Render the universal local quadratic collision model with ReportLab.

6 November 2026. For Edward Baker, substantial LLM assistance, Astra/max.
This is an analytical schematic, not numerical theta data. Run with a Python
environment containing reportlab. Output is ignored root output/figures/.
The SVG can be rasterized with a standard SVG renderer such as sharp.
"""
from pathlib import Path
from math import sqrt
from reportlab.graphics.shapes import Drawing, Rect, String, Line, Circle, Polygon
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderSVG
from reportlab.lib.colors import HexColor, Color, white

out=Path(__file__).resolve().parents[5]/'output/figures/tnd-operator-collision'
out.mkdir(parents=True,exist_ok=True)
d=Drawing(1000,620)
navy=HexColor('#173544'); teal=HexColor('#067f85'); coral=HexColor('#bd553f'); grey=HexColor('#94a3ab')
d.add(Rect(0,0,1000,620,fillColor=HexColor('#f8fafb'),strokeColor=None))
d.add(String(42,578,'A double collision in imaginary time',fontName='Helvetica-Bold',fontSize=25,fillColor=navy))
d.add(String(42,551,'Local model: h/a = y^2/2 + s, where s = time - collision time.  Increasing time  >',fontSize=13,fillColor=navy))
d.add(String(42,528,'Schematic of the leading local behavior; these are not theta data.',fontSize=11,fillColor=HexColor('#526773')))

for i,(s,title,detail) in enumerate([(-.25,'BEFORE','Two real nodes bound an opposite-sign pocket'),(0,'AT THE COLLISION','One double node; the field remains smooth'),(.25,'AFTER','No nearby real nodes; a complex pair remains')]):
    left=54+i*324
    d.add(String(left,487,title,fontName='Helvetica-Bold',fontSize=14,fillColor=navy))
    d.add(String(left,467,'s = '+str(s),fontSize=11,fillColor=HexColor('#526773')))
    px,py,pw,ph=left+25,285,245,155
    xmap=lambda x:px+(x+1.4)/2.8*pw
    ymap=lambda y:py+(y+.4)/1.8*ph
    if s<0:
        r=sqrt(-2*s); pts=[xmap(-r),ymap(0)]
        for j in range(101):
            x=-r+2*r*j/100; pts.extend([xmap(x),ymap(x*x/2+s)])
        pts.extend([xmap(r),ymap(0)])
        d.add(Polygon(pts,fillColor=HexColor('#f4d3cb'),strokeColor=None))
    lp=LinePlot(); lp.x=px; lp.y=py; lp.width=pw; lp.height=ph
    lp.data=[[(x,x*x/2+s) for x in [-1.4+2.8*j/200 for j in range(201)]]]
    lp.xValueAxis.valueMin=-1.4; lp.xValueAxis.valueMax=1.4
    lp.xValueAxis.valueSteps=[-1,0,1]; lp.xValueAxis.labels.fontSize=9
    lp.yValueAxis.valueMin=-.4; lp.yValueAxis.valueMax=1.4
    lp.yValueAxis.valueSteps=[0,.5,1]; lp.yValueAxis.labels.fontSize=9
    lp.xValueAxis.strokeColor=grey; lp.yValueAxis.strokeColor=grey
    lp.lines[0].strokeColor=teal; lp.lines[0].strokeWidth=2.7
    d.add(lp)
    d.add(Line(px,ymap(0),px+pw,ymap(0),strokeColor=grey,strokeWidth=.6))
    d.add(String(px-22,py+ph+5,'h/a',fontSize=10,fillColor=navy))
    d.add(String(px+80,py-26,'y = x - x*',fontSize=10,fillColor=navy))
    roots=[-sqrt(-2*s),sqrt(-2*s)] if s<0 else [0] if s==0 else []
    for r in roots:d.add(Circle(xmap(r),ymap(0),4,fillColor=coral,strokeColor=white,strokeWidth=1))
    # Complex zero locations, in the same local model.
    cx,cy=left+148,143; scale=64
    d.add(Line(cx-90,cy,cx+90,cy,strokeColor=grey,strokeWidth=.8))
    d.add(Line(cx,cy-63,cx,cy+63,strokeColor=grey,strokeWidth=.8))
    d.add(String(cx+94,cy-3,'Re',fontSize=9,fillColor=navy))
    d.add(String(cx+5,cy+65,'Im',fontSize=9,fillColor=navy))
    d.add(String(left+25,224,'Local zeros in the complex plane',fontSize=10,fillColor=navy))
    if s<0: points=[(-sqrt(-2*s),0),(sqrt(-2*s),0)]
    elif s==0:points=[(0,0)]
    else:points=[(0,-sqrt(2*s)),(0,sqrt(2*s))]
    for x,y in points:d.add(Circle(cx+x*scale,cy+y*scale,5,fillColor=coral,strokeColor=white,strokeWidth=1))
    if s==0:d.add(Circle(cx,cy,9,fillColor=None,strokeColor=coral,strokeWidth=1))
    d.add(String(left,49,detail,fontSize=9,fillColor=navy))
d.add(String(42,17,'The total number of local complex zeros stays two, counted with multiplicity.',fontSize=10,fillColor=HexColor('#526773')))
path=out/'collision_anatomy.svg'
renderSVG.drawToFile(d,str(path))
print(path)
