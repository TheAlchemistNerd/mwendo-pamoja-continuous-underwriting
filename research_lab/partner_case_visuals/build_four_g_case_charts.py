from pathlib import Path
import csv,json,math,re,hashlib
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'output/four_g_merchant_finance_case_2026-10-16'
OUT=ROOT/'publications/industry-engagement/4g_2026-10-13/charts'
OUT.mkdir(parents=True,exist_ok=True)
NAVY='#17394A'; TEAL='#008C91'; BLUE='#427AA1'; ORANGE='#D48A2A'; RED='#B44F48'; GRID='#D9E3E8'; MUTED='#576C77'
W,H=1800,1080

def font(n,bold=False):return ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf',n)
def read(name):return list(csv.DictReader((DATA/name).open(encoding='utf-8')))
def val(r,k):return float(r[k])
def short(x):return f'{x/1e6:.2f}m' if abs(x)>=1e6 else f'{x/1000:.0f}k' if abs(x)>=1000 else f'{x:.0f}'
def base(title,sub):
 im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
 d.text((70,40),title,font=font(39,True),fill=NAVY)
 d.text((70,100),sub,font=font(25),fill=MUTED)
 d.text((70,H-65),'Synthetic KES case | Author-selected assumptions | Daily ledger outputs | 18 October 2026',font=font(24),fill=MUTED)
 return im,d

def axes(d,xmin,xmax,ymin,ymax,ylab,xlab,box=(160,205,1680,870)):
 l,t,r,b=box
 def px(x):return l+(x-xmin)/(xmax-xmin)*(r-l)
 def py(y):return b-(y-ymin)/(ymax-ymin)*(b-t)
 for j in range(6):
  y=ymin+(ymax-ymin)*j/5;yp=py(y)
  d.line((l,yp,r,yp),fill=GRID,width=2)
  d.text((l-20,yp),short(y),font=font(28),fill=MUTED,anchor='rm')
 for j in range(7):
  x=xmin+(xmax-xmin)*j/6;xp=px(x)
  d.text((xp,b+22),f'{x:.0f}',font=font(28),fill=MUTED,anchor='mt')
 d.text((70,145),ylab,font=font(28,True),fill=NAVY)
 d.text(((l+r)/2,b+67),xlab,font=font(25),fill=MUTED,anchor='mt')
 return px,py

def lines(filename,title,sub,series,ylab='KES',xlab='Day',xmin=0,xmax=180,floor=None):
 im,d=base(title,sub);allv=[y for _,pts,_ in series for x,y in pts if xmin<=x<=xmax]
 lo=min(0,min(allv));hi=max(allv)*1.10 or 1
 px,py=axes(d,xmin,xmax,lo,hi,ylab,xlab)
 if floor is not None:
  y=py(floor)
  for x in range(160,1680,22):d.line((x,y,x+12,y),fill=ORANGE,width=2)
 for label,pts,c in series:
  points=[(px(x),py(y)) for x,y in pts if xmin<=x<=xmax]
  if len(points)>1:d.line(points,fill=c,width=5)
 x=270
 for label,_,c in series:
  d.line((x,165,x+35,165),fill=c,width=5);d.text((x+47,165),label,font=font(28),fill=NAVY,anchor='lm');x+=d.textlength(label,font=font(28))+100
 im.save(OUT/filename)

def first_cycle():
 rows=[r for r in read('baseline/merchant_daily.csv') if r['merchant_id']=='S01' and 0<=int(r['day'])<=21]
 sums={k:sum(val(r,k) for r in rows) for k in ['settled_sales_receipts','operating_payments','household_payments','principal_repayment','fee_repayment']}
 values=[20000,sums['settled_sales_receipts'],-sums['operating_payments'],-sums['household_payments'],-sums['principal_repayment'],-sums['fee_repayment']]
 labels=['Opening\ncash','Settled\nsales','Operating\npayments','Household\npayments','Principal\nrepaid','Fee\npaid','Closing\ncash']
 im,d=base('Cash remaining after the first lending cycle','KES 100,000 goes directly to the distributor; it enters inventory, while sales enter merchant cash.')
 total=0;tops=[]
 for v in values:tops.extend([total,total+v]);total+=v
 px,py=axes(d,0,7,0,max(tops)*1.15,'KES','',box=(150,220,1690,840))
 # Hide numeric x ticks with a clean label band.
 d.rectangle((100,850,1750,990),fill='white')
 total=0
 for i,v in enumerate(values+[total]):
  x=190+i*215;bw=130
  if i==6:v=total;start=0;end=total;c=TEAL
  elif i==0:start=0;end=v;total=v;c=BLUE
  else:start=total;end=total+v;total=end;c=TEAL if v>0 else RED
  d.rectangle((x,py(max(start,end)),x+bw,py(min(start,end))),fill=c)
  d.text((x+bw/2,py(max(start,end))-18),f'{abs(v):,.0f}',font=font(25,True),fill=NAVY,anchor='mb')
  d.multiline_text((x+bw/2,860),labels[i],font=font(28),fill=NAVY,anchor='ma',align='center',spacing=6)
 im.save(OUT/'4G_01_FIRST_CYCLE_CASH_BRIDGE.png')
 return {**sums,'closing_cash':total}

summary=read('scenario_summary.csv')
S={(r['scenario'],r['protection']=='True'):r for r in summary}
names=[n for n in ['baseline','delayed_sales','margin_squeeze','forbearance_only','support_and_reschedule','long_claim_delay','correlated_loss'] if (n,True) in S]
labels={'baseline':'Baseline','delayed_sales':'Sales shock','margin_squeeze':'Margin squeeze','forbearance_only':'Extension','support_and_reschedule':'Support + extension','long_claim_delay':'Long claim lag','correlated_loss':'Correlated loss'}
hand=first_cycle()
series=[]
for n,c,label in [('baseline',BLUE,'Baseline'),('delayed_sales',RED,'Sales shock'),('support_and_reschedule',TEAL,'Support + extension')]:
 rows=[r for r in read(n+'/merchant_daily.csv') if r['merchant_id']=='V01']
 series.append((label,[(int(r['day']),val(r,'closing_cash')) for r in rows],c))
lines('4G_02_MERCHANT_CASH_THROUGH_REPEAT_CYCLES.png','Merchant cash through successive lending cycles','V01 cash through day 180; dashed line marks the KES 10,000 operating floor.',series,floor=10000)

def comparison(filename,title,sub,keys,unit='KES'):
 im,d=base(title,sub);l=380;r=1630;t=220;b=900
 vals=[val(S[(n,p)],k) for n in names for _,p,k,_ in keys];maxv=max(vals)*1.19;minv=min(0,min(vals)*1.15)
 def x(v):return l+(v-minv)/(maxv-minv)*(r-l)
 for j in range(6):
  v=minv+(maxv-minv)*j/5;xx=x(v);d.line((xx,t-15,xx,b),fill=GRID,width=2);d.text((xx,b+15),short(v),font=font(26),fill=MUTED,anchor='mt')
 rh=(b-t)/len(names)
 for i,n in enumerate(names):
  y=t+i*rh;d.text((l-25,y+rh*.38),labels[n],font=font(28),fill=NAVY,anchor='rm')
  for j,(_,p,k,c) in enumerate(keys):
   v=val(S[(n,p)],k);yy=y+j*27;d.rectangle((min(x(0),x(v)),yy,max(x(0),x(v)),yy+20),fill=c)
   d.text((x(v)+10,yy+10),f'{v:,.0f}',font=font(24,True),fill='white' if v < 0 else NAVY,anchor='lm')
 xleg=390
 for label,_,_,c in keys:
  d.rectangle((xleg,165,xleg+25,183),fill=c);d.text((xleg+38,173),label,font=font(28),fill=NAVY,anchor='lm');xleg+=470
 d.text((1000,960),unit,font=font(24),fill=MUTED,anchor='mt');im.save(OUT/filename)
comparison('4G_03_LENDER_CONTRIBUTION_BY_SCENARIO.png','Lender contribution under seven trading scenarios','Realised model contribution after funding, operations, losses, recoveries and guarantee cash.', [('Without protection',False,'lender_profit',ORANGE),('With protection',True,'lender_profit',TEAL)])
comparison('4G_04_REPEAT_LOANS_AND_DEFAULTS.png','Loan originations and defaults under seven scenarios','Total originations include each merchant\'s first loan; defaults count loan events.', [('Loans originated',True,'loans_originated',BLUE),('Defaults',True,'defaults',RED)],'Number of loans')
series=[]
for n,c,label in [('delayed_sales',TEAL,'30-day settlement lag'),('long_claim_delay',ORANGE,'90-day settlement lag')]:
 total=0;pts=[]
 for row in read(n+'/lender_daily_protected.csv'):
  total+=val(row,'guarantee_cash_received')-val(row,'recovery_remitted');pts.append((int(row['day']),total))
 series.append((label,pts,c))
lines('4G_05_GUARANTEE_SETTLEMENT_AND_RECOVERY.png','Guarantee cash under two settlement schedules','Cumulative guarantee receipts less recovery remittances; identical delayed-sales borrower path.',series,xmin=90,xmax=240)
series=[]
for mode,c,label in [('unprotected',ORANGE,'Without protection'),('protected',TEAL,'With protection')]:
 rows=read('delayed_sales/lender_daily_'+mode+'.csv');series.append((label,[(int(r['day']),val(r,'closing_funding')) for r in rows],c))
lines('4G_06_FUNDING_REQUIREMENT_THROUGH_CLAIMS.png','Funding required through lending and claim settlement','Closing borrowing balance; each day reconciles disbursements, collections, costs and protection cash.',series,xmax=300)
# The published chart data are an exact extract of model outputs.
(OUT/'4G_CHART_DATA.json').write_text(json.dumps({'first_cycle':hand,'scenario_summary':summary},indent=2)+'\n',encoding='utf-8')
manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in OUT.glob('4G_0*.png')}
(OUT/'4G_CHART_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('Saved',len(manifest),'charts in',OUT)
