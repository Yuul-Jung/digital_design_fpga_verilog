# 좌표를 직접 제어하는 SVG 생성 도우미 (rule_md flowchart-rules 기준)
FONT="'IBM Plex Sans KR','Noto Sans KR','Malgun Gothic',sans-serif"
MONO="'IBM Plex Mono','DejaVu Sans Mono',monospace"
INK='#15171C'; ACC='#4635B1'; SOFT='#EDEAFA'; LINE='#3A3D46'; IO='#E8F3EC'; IOS='#21824F'; GRAY='#F4F4F2'; MUTE='#5B5E68'
class S:
    def __init__(s,w,h,title,desc):
        s.w,s.h=w,h; s.e=[]
        s.head=(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d" font-family="{FONT}">'
          f'<title id="t">{title}</title><desc id="d">{desc}</desc>'
          f'<defs><marker id="ah" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker></defs>'
          f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="14" fill="#FFFFFF" stroke="#DADBD6" stroke-width="2"/>')
    def text(s,x,y,t,size=17,anchor='middle',fill=INK,weight=400,mono=False,italic=False):
        f=MONO if mono else FONT
        t=str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
        st=' font-style="italic"' if italic else ''
        s.e.append(f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{fill}" font-weight="{weight}" font-family="{f}"{st}>{t}</text>')
    def box(s,x,y,w,h,lines,fill=SOFT,stroke=ACC,size=17,rx=8,monofirst=True):
        s.e.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="2.5"/>')
        n=len(lines); lh=size*1.35; y0=y+h/2-(n-1)*lh/2+size*0.35
        for i,l in enumerate(lines):
            mono=monofirst and i==0 and l.isascii()
            s.text(x+w/2,y0+i*lh,l,size=size if i==0 else size-2,weight=600 if i==0 else 400,mono=mono,fill=INK if i==0 else MUTE)
    def port(s,x,y,w,h,label,direction='in',size=16):
        # 평행사변형(입출력)
        k=12
        pts=f'{x+k},{y} {x+w},{y} {x+w-k},{y+h} {x},{y+h}'
        s.e.append(f'<polygon points="{pts}" fill="{IO}" stroke="{IOS}" stroke-width="2.5"/>')
        s.text(x+w/2,y+h/2+size*0.35,label,size=size,mono=label.isascii(),weight=600)
    def circle(s,cx,cy,r,top,bottom=None,size=20):
        s.e.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SOFT}" stroke="{ACC}" stroke-width="2.5"/>')
        if bottom is None: s.text(cx,cy+size*0.35,top,size=size,weight=600,mono=True)
        else:
            s.text(cx,cy-4,top,size=size,weight=600,mono=True)
            s.e.append(f'<line x1="{cx-r+12}" y1="{cy+6}" x2="{cx+r-12}" y2="{cy+6}" stroke="{ACC}" stroke-width="1.5"/>')
            s.text(cx,cy+27,bottom,size=size-4,mono=True,fill=MUTE)
    def path(s,d,arrow=True,dash=False,color=LINE,width=2.2):
        m=' marker-end="url(#ah)"' if arrow else ''
        da=' stroke-dasharray="6 5"' if dash else ''
        s.e.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{m}{da} stroke-linejoin="round"/>')
    def poly(s,pts,arrow=True,**k):
        d='M'+' L'.join(f'{x},{y}' for x,y in pts); s.path(d,arrow,**k)
    def dot(s,x,y): s.e.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{LINE}"/>')
    def lab(s,x,y,t,size=15,anchor='middle',mono=True,fill=ACC,bg=True):
        # 연결선 라벨(흰 배경으로 선과 분리)
        if bg:
            wpx=sum(size*(1.0 if ord(c)>0x1100 else 0.62) for c in t)+8
            ax={'middle':x-wpx/2,'start':x-4,'end':x-wpx+4}[anchor]
            s.e.append(f'<rect x="{ax:.1f}" y="{y-size+1}" width="{wpx:.1f}" height="{size+6}" fill="#FFFFFF"/>')
        s.text(x,y+2,t,size=size,anchor=anchor,mono=mono,fill=fill,weight=600)
    def save(s,p):
        open(p,'w').write(s.head+''.join(s.e)+'</svg>\n')
