from pathlib import Path
import csv,json,re,hashlib
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/'output/four_g_merchant_finance_case_2026-10-16'
FOLDER=ROOT/'publications/linkedin/4g_capital_application_2026-10-13'
BUILD=ROOT/'.build/four_g_2026-10-16';BUILD.mkdir(parents=True,exist_ok=True)
MD=FOLDER/'UNDERWRITE_FOR_COLLECTION_4G_CAPITAL_LINKEDIN_ARTICLE_3000_WORDS.md'
backup=BUILD/'article_before_reproducible_case.md'
if not backup.exists():backup.write_bytes(MD.read_bytes())
t=backup.read_text(encoding='utf-8-sig').replace('p???','pₘₐₓ').replace('Hern�n','Hernán')
rows=list(csv.DictReader((DATA/'scenario_summary.csv').open(encoding='utf-8')))
s={(r['scenario'],r['protection']=='True'):r for r in rows}
f=lambda n,p,k:float(s[(n,p)][k])
k=lambda v:f'{v:,.0f}'
B=lambda key:f('baseline',True,key)
D=lambda key:f('delayed_sales',True,key)
U=lambda key:f('delayed_sales',False,key)
S=lambda key:f('support_and_reschedule',True,key)
L=lambda key:f('long_claim_delay',True,key)
C=lambda key:f('correlated_loss',True,key)
claims=list(csv.DictReader((DATA/'delayed_sales/guarantee_claims.csv').open(encoding='utf-8')))
claim=claims[0]
severe_claims=list(csv.DictReader((DATA/'correlated_loss/guarantee_claims.csv').open(encoding='utf-8')))
severe_claim=next(c for c in severe_claims if float(c['post_settlement_recovery_remittance'])>0)
chart=lambda number,filename,caption:f'\n\n![{caption}](../../industry-engagement/4g_2026-10-13/charts/{filename})\n\n*Figure {number}. {caption}*\n\n'
t=t.replace('**Nevil Maloba | 13 October 2026**','**Nevil Maloba | Updated 18 October 2026**')
start=t.index('Consider a hypothetical merchant');end=t.index('## Establish whose cash',start)
t=t[:start]+f'''The reproducible companion now follows twelve synthetic merchants through 180 operating days, up to six lending opportunities and a runoff to day 300. Six merchants have stable trading assumptions, three experience delayed sales under stress and three experience weaker conversion. One merchant has an explicitly ineligible guarantee record. Every loan begins with distributor payment and an equal inventory receipt. The merchant's cash ledger records subsequent settled sales, operating expenses, household withdrawals, repayment and negotiated recovery. This makes the lender's advance, the merchant's goods and the eventual customer cash separately traceable. All commercial amounts, fees, stress responses and claim-processing assumptions belong to this teaching case.

The first baseline cycle starts with KES 20,000 cash and KES 100,000 of stock financed directly to the distributor. A 25% markup on cost produces KES 125,000 of sales, settled by day twenty. Daily operating needs of KES 200 and household needs of KES 150 total KES 4,200 and KES 3,150 over twenty-one days. The assumed contractual fee is KES 5,000. After paying principal and that fee, closing cash is:

C₂₁ = 20,000 + 125,000 − 4,200 − 3,150 − 100,000 − 5,000 = KES 32,650

The principal finances stock directly and appears once in the repayment calculation. Sales revenue and cost of goods sold produce the merchant's trading margin; principal repayment settles financing. The daily ledger also carries inventory and sales receivables, allowing a reader to distinguish a sale, its settlement and the liquidity needed until settlement. Accrued operating expenses and unpaid balances remain visible when cash becomes tight. Household consumption shortfalls have their own measure. At a workout, available cash first meets accrued operating payables; recovery then uses the amount remaining above the minimum operating cash floor. These distinctions matter because a comfortable cash balance can coexist with outstanding obligations or goods whose value still depends on sale.
''' + chart(1,'4G_01_FIRST_CYCLE_CASH_BRIDGE.png','The first cycle reconciles distributor-financed inventory, settled sales, household needs and repayment.')+'''## Repeat borrowing follows observed cash conversion

A repeat opportunity opens after the previous loan settles, the relevant sales receipts arrive and the cooling period ends. The case projects repayment-window cash using the previous completed cycle's observed selling margin, inventory conversion and settlement timing. It approves a limit only when projected cash after expenses and debt service retains the KES 10,000 operating floor. A timely borrower with sufficient surplus can receive an increment, subject to the KES 120,000 teaching cap. A weaker forecast reduces the proposed amount or defers the next loan. This executable gate uses transparent cash arithmetic; the Bayesian extension described below adds a validated distribution around the quantities being forecast.

''' + f'''The baseline generates {int(B('loans_originated'))} loans, including {int(B('repeat_loans'))} repeat loans, and ends with KES {k(B('merchant_closing_cash'))} aggregate merchant cash. The sales-and-settlement shock begins in cycle three and produces {int(D('loans_originated'))} loans and {int(D('defaults'))} defaults. Support combined with a fourteen-day extension produces {int(S('loans_originated'))} loans and {int(S('defaults'))} defaults under its assumed improvement in stock conversion. The simulation specifies that improvement as an input. A prospective study would estimate whether the offered support actually changes sales, cash and repayment, at what cost, and for which merchants. Extension alone has its own scenario so the cost of waiting can be compared with a change in the trading process.
''' + chart(2,'4G_02_MERCHANT_CASH_THROUGH_REPEAT_CYCLES.png','Merchant V01 illustrates how the same starting business develops through baseline, stressed and supported repeat cycles.')+chart(3,'4G_04_REPEAT_LOANS_AND_DEFAULTS.png','Repeat lending and default outcomes vary with sales, margins, support and the timing of the next facility.')+t[end:]
start=t.index('For illustration, a simplified loss-layer calculation is:');end=t.index('## Measure additionality',start)
loss=float(claim['eligible_loss']);allocated=float(claim['allocated_claim']);recovery_share=float(claim['post_settlement_recovery_remittance'])
t=t[:start]+f'''The companion contains an explicit two-layer teaching schedule. A KES 4,440,000 cumulative inclusion budget is divided into a first KES 220,000 loss layer with KES 200,000 maximum protection and a further KES 4,220,000 layer with KES 420,000 maximum protection. These KES values preserve disclosed layer proportions for demonstration; they are a separate scale illustration. The assumed within-layer sharing percentages are 200/220 and 420/4,220. Eligibility, origination cutoffs, processing delays, fees and recovery allocation are independently configurable. Loading the executed agreement would replace those teaching conventions with its specific definitions, beneficiary rights and cash processes.

For cumulative eligible gross loss L, the teaching allocation is:

G(L) = (200/220) × min(L, 220,000) + (420/4,220) × min(max(L − 220,000, 0), 4,220,000)

A new loss receives the increment G(L after the loss) − G(L before the loss). The ledger allocates simultaneous losses in a stated order and records each loan's covered fraction. The inclusion budget counts covered originations cumulatively, so repeat loans consume additional capacity. Recovery reduces the beneficiary's net protection through pre-settlement adjustment or later remittance. The model elects no reinstatement of capacity after recovery. Its parameter file, claim rows and tests expose these choices so another researcher can reproduce the result or change one contractual convention without changing the merchant model.

In the delayed-sales case, loan {claim['loan_id']} defaults on day {claim['default_day']} with KES {k(loss)} unpaid principal. Its teaching allocation is KES {k(allocated)}. Submission occurs on day {claim['submitted_day']}, acceptance on day {claim['accepted_day']} and cash settlement on day {claim['settled_day']}. The workout on day {claim['recovery_day']} produces no borrower recovery after operating payables and the cash floor are respected. The accepted receivable, settled cash and recovery remittance have different dated entries. The model funds the lender throughout that interval rather than treating acceptance as immediate cash.

Across the delayed-sales portfolio, gross written-off principal is KES {k(D('written_off_principal'))}, subsequent borrower recovery is KES {k(D('post_default_recovery'))}, guarantee cash is KES {k(D('guarantee_cash_received'))} and recovery remittance is KES {k(D('recovery_remitted'))}. Retained credit loss therefore equals KES {k(D('retained_credit_loss'))}. The long-claim scenario holds the merchant outcomes fixed and increases settlement delay from thirty to ninety days after acceptance. The ultimate protection amount is the same because this merchant path produces zero workout recovery; the later cash receipt changes the funding cost. The separate correlated-loss scenario reaches the second layer and produces KES {k(C('post_default_recovery'))} of borrower recoveries. For loan {severe_claim['loan_id']}, KES {k(float(severe_claim['post_settlement_recovery_remittance']))} is remitted to the guarantor on day {severe_claim['recovery_day']} after an earlier KES {k(float(severe_claim['settlement_cash']))} claim settlement. Total recovery remittances are KES {k(C('recovery_remitted'))}. This case makes the recovery-sharing convention and residual lender exposure visible.
''' + chart(4,'4G_05_GUARANTEE_SETTLEMENT_AND_RECOVERY.png','Claim settlement changes the date protection becomes available cash. The model also records recovery adjustments and remittances when recoveries occur.')+t[end:]
anchor='## Make the advisory connection operational'
profit=f'''## Reconcile profitability and the funding requirement

The lender model separates principal movement from income. Fees collected contribute revenue. Origination, daily servicing, support, collections, guarantee fees and interest on opening borrowing contribute costs. Written-off principal and later recoveries form the realised credit-loss bridge. Guarantee settlement and recovery remittance then determine the protection contribution. The reported result is a synthetic realised contribution before tax, central overhead allocation and a capital hurdle. Accrued unpaid fees, unresolved default balances, performing principal and accepted unsettled claims appear separately. A reader can therefore reconcile the contribution to cash and remaining assets instead of treating every incoming shilling as profit.

Π = collected fees − operating costs − funding cost − guarantee fees − written-off principal + borrower recoveries + guarantee cash − recovery remittances

Under baseline assumptions, protected contribution is KES {k(B('lender_profit'))}, compared with KES {k(f('baseline',False,'lender_profit'))} without protection. Both use the same merchant paths; the difference reflects protection costs when losses are absent. Under the delayed-sales shock, contribution is KES {k(D('lender_profit'))} with protection and KES {k(U('lender_profit'))} without it. The supported scenario produces KES {k(S('lender_profit'))} after KES {k(S('support_cost'))} of support costs. The correlated-loss scenario produces KES {k(C('lender_profit'))} with protection. This comparison gives management a concrete way to examine the interaction of product margin, customer support, risk sharing and concentrated stress.

Liquidity has its own daily calculation. The case begins with zero lender cash and draws borrowing to meet disbursements and costs, applying a 12% annual teaching funding rate on opening debt. Incoming cash first reduces that borrowing, then accumulates as cash when the balance becomes positive. In the delayed-sales case, peak protected borrowing is KES {k(D('peak_funding'))}. The long claim lag changes contribution by KES {k(D('lender_profit')-L('lender_profit'))} through the funding path. A funding mandate could add commitment limits, liquidity reserves and the required return on committed equity. The current outputs show exactly where those decisions would enter.
''' + chart(5,'4G_03_LENDER_CONTRIBUTION_BY_SCENARIO.png','Lender contribution compares identical merchant outcomes with and without the teaching guarantee, including concentrated stress.') + chart(6,'4G_06_FUNDING_REQUIREMENT_THROUGH_CLAIMS.png','Daily borrowing reflects disbursements, repayments, protection costs and the arrival of guarantee cash.')
t=t.replace(anchor,profit+anchor)
# Replace generic pilot conclusion with a concrete reproducibility link while retaining the original final argument.
anchor='<!-- ARTICLE_BODY_END -->'
repro='''## Reproduce the evidence before a pilot

The companion publishes its assumptions, daily merchant ledgers, loan records, protection events and paired lender cash flows [13]. Its tests reconcile merchant cash, inventory, receivables, principal and lender contribution, and exercise guarantee caps, eligibility, recovery timing and unsettled claims. The article and deck use those outputs directly. A partner can first run the synthetic example, inspect a loan and alter a timing assumption, then map an approved historical extract into the same definitions. The proposed agentic workflow prepares evidence and routes exceptions; validated calculation services generate results, authorised staff approve material decisions, and execution receipts preserve the action taken.

'''
t=t.replace(anchor,repro+anchor)
newref='[13] N. Maloba, "4G-inspired merchant cycle and risk-sharing reproducible case," 2026. [Online]. Available: https://github.com/TheAlchemistNerd/mwendo-pamoja-continuous-underwriting/tree/main/research_lab/four_g_merchant_finance_case\n\n'
t=t.replace('## Publication record',newref+'## Publication record')
body=t.split('<!-- ARTICLE_BODY_START -->')[1].split('<!-- ARTICLE_BODY_END -->')[0]
count=sum(bool(re.search(r'\w',w)) for w in re.sub(r'!\[[^\]]*\]\([^)]*\)','',body).split())
t=re.sub(r'Main article word count:.*?\n\n',f'Main article word count: **{count:,} words**. Updated with the reproducible merchant, lending and guarantee case. Count includes headings and captions, excluding image-link markup and references.\n\n',t,flags=re.S)
MD.write_text(t,encoding='utf-8')
# Word mirrors the saved article with ordinary Unicode text.
doc=Document();sec=doc.sections[0];sec.top_margin=sec.bottom_margin=Inches(.7);sec.left_margin=sec.right_margin=Inches(.8)
for n,size in [('Normal',11),('Title',23),('Heading 1',15),('Heading 2',12)]:
 st=doc.styles[n];st.font.name='Arial';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0);st._element.get_or_add_rPr().rFonts.set(qn('w:eastAsia'),'Arial')
doc.styles['Normal'].paragraph_format.space_after=Pt(7);doc.styles['Normal'].paragraph_format.line_spacing=1.08
sec.header.paragraphs[0].text=''
# Clear template borders and theme font overrides for consistent Arial output.
for style in doc.styles:
 for border in list(style._element.iter(qn('w:pBdr'))):border.getparent().remove(border)
 for rf in style._element.iter(qn('w:rFonts')):
  for attribute in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:
   rf.attrib.pop(qn('w:'+attribute),None)
  for attribute in ['ascii','hAnsi','eastAsia','cs']:rf.set(qn('w:'+attribute),'Arial')
for style_name in ['Header','Footer','Caption']:
 doc.styles[style_name].font.name='Arial'
 doc.styles[style_name].font.color.rgb=RGBColor(0,0,0)
foot=sec.footer.paragraphs[0];foot.alignment=WD_ALIGN_PARAGRAPH.CENTER
foot.add_run('Nevil Maloba   ')
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');foot._p.append(fld)
def rich(p,line):
 for part in re.split(r'(\*\*.*?\*\*|\*[^*]+\*)',line):
  if part.startswith('**') and part.endswith('**'):p.add_run(part[2:-2]).bold=True
  elif part.startswith('*') and part.endswith('*'):p.add_run(part[1:-1]).italic=True
  else:p.add_run(part)
figs=0
for line in t.splitlines():
 if not line.strip() or line.startswith('<!--'):continue
 if line.startswith('!['):
  match=re.match(r'!\[([^\]]*)\]\(([^)]+)\)',line);p=doc.add_paragraph();p.alignment=WD_ALIGN_PARAGRAPH.CENTER
  p.add_run().add_picture(str((FOLDER/match[2]).resolve()),width=Inches(6.5));p.paragraph_format.keep_with_next=True;figs+=1;continue
 style='Normal';text=line
 if line.startswith('# '):style='Title';text=line[2:]
 elif line.startswith('## '):style='Heading 1';text=line[3:]
 elif line.startswith('### '):style='Heading 2';text=line[4:]
 p=doc.add_paragraph(style=style);rich(p,text)
 if line.startswith('*Figure'):
  p.alignment=WD_ALIGN_PARAGRAPH.CENTER
  for run in p.runs:run.font.size=Pt(10)
 if line.startswith('[1]'):p.paragraph_format.space_before=Pt(4)
for paragraph in doc.paragraphs:
 for border in list(paragraph._p.iter(qn('w:pBdr'))):border.getparent().remove(border)
DOCX=MD.with_suffix('.docx')
try:doc.save(DOCX)
except PermissionError:
 DOCX=MD.with_name(MD.stem+'_2026-10-18.docx');doc.save(DOCX)
post=f"Can each lending cycle leave a merchant better able to trade and repay?\n\nMy application of Underwrite for Collection to 4G Capital now includes a reproducible merchant, repeat-lending and guarantee case, drawing on Mwendo Pamoja's operating and financing work.\n\nTwelve synthetic merchants move through distributor-financed stock, sales, settled receipts, business expenses, household needs and repayment. The model follows 180 operating days, up to six cycles and claims and recoveries through day 300.\n\nThree research questions guide it:\n\n1. Which cash-flow evidence supports a sustainable next loan and an appropriate limit?\n2. How do sales delays, repayment extensions and business support change merchant outcomes and lender profitability?\n3. How do guarantee eligibility, settlement timing and recovery sharing affect retained losses and funding needs?\n\nThe first cycle reconciles to KES 32,650 after expenses, household commitments, principal and the assumed fee. Across the baseline, 72 loans produce KES {k(B('lender_profit'))} lender contribution with protection. A sales shock produces 60 loans and three defaults: contribution is KES {k(D('lender_profit'))} with protection and KES {k(U('lender_profit'))} without it.\n\nSupport plus rescheduling produces 66 loans and KES {k(S('lender_profit'))} contribution after support costs, under an explicit assumed improvement in trading. This gives a prospective study a concrete effect to test.\n\nThe IFC partnership provides the institutional context. A configurable teaching agreement traces inclusion, loss layers, claims, cash settlement and recovery remittances. Its parameters can be replaced with the executed terms.\n\nPython calculations, daily ledgers, tests and charts connect each result to its inputs. The article and partnership deck show how this could inform a focused pilot with credit, operations, finance and customer teams.\n\nWhitepaper: https://doi.org/10.5281/zenodo.23343888\n\n#MSMEFinance #CreditRisk #CashFlowLending #4GCapital #FinancialInclusion"
assert len(post)<=2000,len(post)
(FOLDER/'LINKEDIN_POST_2000_CHARACTERS.md').write_text(post+'\n',encoding='utf-8')
(FOLDER/'LINKEDIN_POST_2000_CHARACTERS.txt').write_text(post+'\n',encoding='utf-8')
(BUILD/'article_build_checks.json').write_text(json.dumps({'word_count':count,'figures':figs,'post_characters':len(post),'article_sha256':hashlib.sha256(MD.read_bytes()).hexdigest(),'docx_sha256':hashlib.sha256(DOCX.read_bytes()).hexdigest(),'docx_path':str(DOCX)},indent=2)+'\n')
print('Article words',count,'Word figures',figs,'Post characters',len(post))
