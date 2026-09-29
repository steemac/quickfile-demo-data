import csv, random, datetime as dt
from decimal import Decimal as D, ROUND_HALF_UP
random.seed(42)
OUT="/mnt/user-data/outputs/quickfile_demo/"
q=lambda x: D(x).quantize(D("0.01"),ROUND_HALF_UP)
f=lambda d: d.strftime("%d/%m/%Y")
def w(name, hdr, rows):
    with open(OUT+name,"w",newline="",encoding="utf-8") as fh:
        c=csv.writer(fh); c.writerow(hdr); c.writerows(rows)

# ---------- Clients ----------
clients=[
 ("The Copper Kettle Café","14 Market Street","","","Harrogate","HG1 1BB","GB","","CL001","Jess","Moore","jess.moore@example.com","01632 960101"),
 ("Bean & Gone Ltd","Unit 3, Riverside Arcade","Quayside","","Newcastle upon Tyne","NE1 3JE","GB","","CL002","Tom","Ashworth","tom.ashworth@example.com","01632 960102"),
 ("Little Loaf Bakery","22 Church Lane","","","Hebden Bridge","HX7 8AB","GB","","CL003","Priya","Shah","priya.shah@example.com","01632 960103"),
 ("Northern Grind Co-operative","The Old Mill","Mill Road","","Leeds","LS6 2QD","GB","","CL004","Callum","Reid","callum.reid@example.com","01632 960104"),
 ("Station House Deli","Platform 1","Station Approach","","York","YO24 1AB","GB","","CL005","Hannah","Blake","hannah.blake@example.com","01632 960105"),
 ("Moorland Hotel Group Ltd","Moorland House","High Street","Grassington","Skipton","BD23 5AT","GB","","CL006","Martin","Hughes","martin.hughes@example.com","01632 960106"),
 ("Pedal & Pour Cycle Café","8 Bridge End","","","Otley","LS21 1BE","GB","","CL007","Sophie","Turner","sophie.turner@example.com","01632 960107"),
 ("Greenwood Farm Shop","Greenwood Farm","Moor Lane","","Ilkley","LS29 9DP","GB","","CL008","David","Ellis","david.ellis@example.com","01632 960108"),
 ("Campus Coffee Ltd","Student Union Building","University Road","","Sheffield","S10 2TG","GB","","CL009","Amir","Khan","amir.khan@example.com","01632 960109"),
 ("The Reading Room","3 Castle Walk","","","Knaresborough","HG5 8AU","GB","","CL010","Laura","Finch","laura.finch@example.com","01632 960110"),
 ("Brew & Bloom Florist Café","41 Water Street","","","Skipton","BD23 1PB","GB","","CL011","Niamh","Byrne","niamh.byrne@example.com","01632 960111"),
 ("Harbour Lights Restaurant","The Harbour","","","Whitby","YO21 3PU","GB","","CL012","Gareth","Price","gareth.price@example.com","01632 960112"),
]
w("02_clients.csv",["Company Name","Address Line 1","Address Line 2","Address Line 3","Town","Postcode","Country ISO Code","VAT Number","Account Number","Contact first name","Contact surname","Contact email","Contact telephone"],clients)

suppliers=[
 ("Equator Green Bean Imports Ltd","Dock 7, Albert Dock","","","Liverpool","L3 4AA","GB","","SU001","Rosa","Martinez","rosa.martinez@example.com","01632 960201"),
 ("Pennine Packaging Supplies","Unit 12, Calder Trading Estate","","","Huddersfield","HD5 0RL","GB","","SU002","Keith","Barlow","keith.barlow@example.com","01632 960202"),
 ("Oat & Barley Dairy Alternatives Ltd","45 Commerce Way","","","Manchester","M17 1HP","GB","","SU003","Grace","Lin","grace.lin@example.com","01632 960203"),
 ("Yorkshire Property Holdings Ltd","2 Park Square East","","","Leeds","LS1 2NE","GB","","SU004","Robert","Hale","robert.hale@example.com","01632 960204"),
 ("Dales Energy Supply Ltd","Energy House","Kirkstall Road","","Leeds","LS3 1LH","GB","","SU005","Billing","Team","billing@example.com","01632 960205"),
 ("SwiftParcel Couriers","Hub 4, M62 Distribution Park","","","Wakefield","WF2 0XQ","GB","","SU006","Nadia","Clarke","nadia.clarke@example.com","01632 960206"),
 ("Fibrelink Broadband Ltd","100 Network Avenue","","","Bradford","BD1 5PQ","GB","","SU007","Accounts","Dept","accounts@example.com","01632 960207"),
 ("RoastTech Machinery Services","Unit 9, Hope Park","","","Sheffield","S9 1XU","GB","","SU008","Ian","Fletcher","ian.fletcher@example.com","01632 960208"),
 ("Bright Spark Marketing","The Studio, 5 Victoria Road","","","Harrogate","HG1 1EQ","GB","","SU009","Ellie","Watts","ellie.watts@example.com","01632 960209"),
 ("Ledger & Co Accountants","1 Wellington Street","","","Leeds","LS1 4LT","GB","","SU010","Paul","Newman","paul.newman@example.com","01632 960210"),
]
w("03_suppliers.csv",["Company Name","Address Line 1","Address Line 2","Address Line 3","Town","Postcode","Country ISO Code","VAT Number","Account Number","Contact first name","Contact surname","Contact email","Contact telephone"],suppliers)

# ---------- Inventory ----------
items=[ # name, desc, sale price, vat, sales nominal, cost price, purchase nominal, qty on hand
 ("HOUSE-ESP-1KG","House Espresso Blend - roasted whole bean 1kg",D("18.50"),0,4000,D("8.20"),5000,120),
 ("COL-SO-1KG","Colombia Huila Single Origin - roasted whole bean 1kg",D("22.00"),0,4000,D("10.40"),5000,60),
 ("ETH-YIR-1KG","Ethiopia Yirgacheffe Single Origin - roasted whole bean 1kg",D("24.50"),0,4000,D("11.80"),5000,40),
 ("BRA-SAN-1KG","Brazil Santos - roasted whole bean 1kg",D("17.00"),0,4000,D("7.60"),5000,80),
 ("DECAF-1KG","Swiss Water Decaf - roasted whole bean 1kg",D("21.00"),0,4000,D("10.10"),5000,30),
 ("HOUSE-ESP-6KG","House Espresso Blend - bulk bag 6kg",D("99.00"),0,4000,D("46.50"),5000,15),
 ("RETAIL-250G","Retail bag 250g - assorted origins",D("6.25"),0,4000,D("2.70"),5000,200),
 ("OAT-1LX6","Barista oat drink 1L - case of 6",D("13.20"),0,4000,D("9.00"),5000,50),
 ("CUP-8OZ-1000","Compostable paper cups 8oz - box of 1000",D("62.00"),20,4000,D("38.00"),5000,25),
 ("CUP-12OZ-1000","Compostable paper cups 12oz - box of 1000",D("74.00"),20,4000,D("45.00"),5000,25),
 ("LID-1000","Compostable sip lids - box of 1000",D("28.00"),20,4000,D("16.50"),5000,40),
 ("GRINDER-HAND","Ceramic burr hand grinder",D("45.00"),20,4000,D("24.00"),5000,12),
 ("TRAIN-HALF","Barista training - half day on site",D("180.00"),20,4010,D("0.00"),5000,0),
 ("SERVICE-ESP","Espresso machine service & descale",D("95.00"),20,4010,D("0.00"),5000,0),
]
w("06_inventory_items.csv",["Item Name","Description","Unit Price","VAT Rate","Sales Nominal Code","Purchase Price","Purchase Nominal Code","Quantity In Stock"],
  [(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]) for i in items])

# ---------- Sales invoices ----------
TODAY=dt.date(2026,9,29)
sales=[]; inv=1001; sales_summary=[]
start=dt.date(2026,4,2)
for n in range(20):
    d=start+dt.timedelta(days=int(n*178/20)+random.randint(0,2))
    cl=random.choice(clients)
    lines=random.sample(items,random.choice([1,1,2,2]))
    terms=30 if cl[8] not in("CL006","CL009") else 14
    due=d+dt.timedelta(days=terms)
    # paid if due well before today, with a few late/unpaid
    r=random.random()
    paid=None
    if due < TODAY-dt.timedelta(days=5) and r>0.08:
        paid=d+dt.timedelta(days=random.randint(max(3,terms-12),terms+8))
        if paid>=TODAY: paid=None
    elif due>=TODAY-dt.timedelta(days=5) and r<0.3:
        paid=d+dt.timedelta(days=random.randint(3,10))
        if paid>=TODAY: paid=None
    total=D(0)
    for it in lines:
        qty=random.choice([60,80,100,120]) if it[3]==0 else random.choice([1,1,2,3])
        if it[0] in("TRAIN-HALF","SERVICE-ESP","HOUSE-ESP-6KG"): qty=random.choice([1,1,2])
        net=q(it[2]*qty); vat=q(net*it[3]/100); gross=net+vat; total+=gross
        sales.append([f"INV-{inv}",f(d),cl[0],cl[8],f"{it[1]} x {qty} @ £{it[2]}",it[4],it[3],vat,gross,terms,
                      f"PO-{random.randint(2000,9999)}" if cl[8] in("CL006","CL009","CL002") else "",
                      "Thank you for your business" ,f(paid) if paid else "",1200 if paid else ""])
    sales_summary.append((f"INV-{inv}",d,total,paid)); inv+=1
w("04_sales_invoices.csv",["Invoice number","Issue Date","Client name","Account Reference","Description","Sales nominal code","VAT rate","VAT amount","Total gross amount","Term in days","Purchase reference","Notes","Paid date","Paid bank nominal code"],sales)

# ---------- Purchase invoices ----------
purch=[]; ps=[]
def addp(d,sup,ref,lines,terms,paid):
    for desc,nom,rate,net in lines:
        net=q(net); vat=q(net*rate/100)
        purch.append([f(d),sup,ref,desc,nom,rate,vat,net+vat,terms,f(paid) if paid and paid<TODAY else "",1200 if paid and paid<TODAY else ""])
    ps.append((ref,d,sum(q(n)+q(q(n)*r/100) for _,_,r,n in lines),paid))
months=[dt.date(2026,m,1) for m in range(4,10)]
for i,m in enumerate(months):
    mm=m.strftime("%b %Y")
    if i%3==0: addp(m,"Yorkshire Property Holdings Ltd",f"YPH-{2600+i}",[(f"Unit rent - quarter from {mm}",7100,20,2250)],0,m+dt.timedelta(days=1))
    addp(m+dt.timedelta(days=6),"Dales Energy Supply Ltd",f"DES-{88410+i}",[(f"Electricity - {mm}",7200,5,random.randint(240,390)+D("0.45"))],14,m+dt.timedelta(days=20))
    if False: addp(m+dt.timedelta(days=9),"Fibrelink Broadband Ltd",f"FB{530021+i}",[(f"Business broadband & phone - {mm}",7502,20,D("48.00"))],7,m+dt.timedelta(days=16))
    # green beans x2 per month
    for k in range(1):
        d=m+dt.timedelta(days=4)
        kg=random.choice([120,150,180])
        addp(d,"Equator Green Bean Imports Ltd",f"EGB-{7100+i}",
             [(f"Green coffee beans - mixed origins (Brazil, Colombia, Ethiopia) {kg}kg",5000,0,kg*D("5.80"))],30,d+dt.timedelta(days=28))
    d=m+dt.timedelta(days=12)
    if i%3==0: addp(d,"Pennine Packaging Supplies",f"PPS-{41200+i}",
         [("Compostable cups 8oz & 12oz x 10 boxes",5000,20,5*D("38.00")+5*D("45.00")),("Valve bags 1kg kraft x 500",5000,20,D("115.00"))],30,d+dt.timedelta(days=30))
    d=m+dt.timedelta(days=15)
    if i%3==1: addp(d,"SwiftParcel Couriers",f"SPC-{m.month:02d}26",[(f"Courier deliveries - quarter from {mm}",7400,20,random.randint(600,850))],14,d+dt.timedelta(days=12))
    d=m+dt.timedelta(days=18)
    if i%3==0: addp(d,"Oat & Barley Dairy Alternatives Ltd",f"ODA-{3300+i}",[("Barista oat drink 1L cases x 30",5000,0,30*D("9.00"))],30,d+dt.timedelta(days=27))
addp(dt.date(2026,5,20),"RoastTech Machinery Services","RTM-1188",[("Annual roaster service & parts",7800,20,D("640.00"))],30,dt.date(2026,6,18))
if False: addp(dt.date(2026,8,11),"RoastTech Machinery Services","RTM-1302",[("Replacement drum bearing - emergency call out",7800,20,D("385.00"))],30,None)
addp(dt.date(2026,4,28),"Bright Spark Marketing","BSM-077",[("Website refresh & product photography",6201,20,D("1450.00"))],30,dt.date(2026,5,27))
if False: addp(dt.date(2026,9,3),"Bright Spark Marketing","BSM-104",[("Autumn social media campaign",6201,20,D("600.00"))],30,None)
addp(dt.date(2026,6,30),"Ledger & Co Accountants","LCA-2026-061",[("Year-end accounts & corporation tax return FY2025/26",7600,20,D("1150.00"))],30,dt.date(2026,7,28))
purch.sort(key=lambda r: dt.datetime.strptime(r[0],"%d/%m/%Y"))
w("05_purchase_invoices.csv",["Receipt date","Supplier name","Supplier Ref","Description","Purchase nominal code","VAT rate","VAT total","Total gross amount","Term in days","Paid date","Paid account nominal code"],purch)

# ---------- Opening trial balance at 31/03/2026 ----------
tb=[("0020","Plant and Machinery (coffee roaster)",D("18500.00"),0),
    ("0021","Plant and Machinery Depreciation",0,D("4625.00")),
    ("0030","Office Equipment",D("3200.00"),0),
    ("0031","Office Equipment Depreciation",0,D("960.00")),
    ("1001","Stock",D("8450.00"),0),
    ("1100","Trade Debtors",D("6840.00"),0),
    ("1200","Bank Current Account",D("24315.60"),0),
    ("1210","Bank Deposit Account",D("10000.00"),0),
    ("2100","Trade Creditors",0,D("3960.00")),
    ("2200","VAT Liability",0,D("2870.40")),
    ("2210","PAYE and NI",0,D("1450.00")),
    ("2300","Directors Loan Account",0,D("5000.00")),
    ("3000","Ordinary Shares",0,D("100.00"))]
dr=sum(r[2] for r in tb); cr=sum(r[3] for r in tb)
tb.append(("3100","Retained Earnings",0,dr-cr))
w("01_opening_balances.csv",["Nominal Code","Account Name","Debit","Credit"],[(a,b,c or "",d or "") for a,b,c,d in tb])

print("sales invoices",len(sales_summary),"lines",len(sales),"total",sum(s[2] for s in sales_summary),"unpaid",sum(1 for s in sales_summary if not s[3]))
print("purchase invoices",len(ps),"lines",len(purch),"unpaid",sum(1 for p in ps if not p[3] or p[3]>=TODAY))
# Estimated nominal postings (conservative): per line net+VAT, per invoice control a/c, per payment bank+control
def est(rows,paidcol,refcol):
    lines=len(rows); invs={}
    for r in rows: invs[r[refcol]]=bool(r[paidcol])
    return lines*2+len(invs)+2*sum(invs.values())
es=est(sales,12,0); ep=est(purch,9,2)
print("est postings: TB",len(tb),"sales",es,"purchases",ep,"TOTAL",len(tb)+es+ep)
print("TB dr",sum(r[2] or 0 for r in tb),"cr",sum(r[3] or 0 for r in tb))
