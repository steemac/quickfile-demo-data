# QuickFile demo data – Harbour Lane Coffee Roasters Ltd (fictional)

A fictional Yorkshire wholesale coffee roaster. Opening balances at **31/03/2026**, trading **April–September 2026**. All names, contacts and addresses are made up (emails use example.com, phones use the Ofcom 01632 960xxx drama range).

## Import order
1. **01_opening_balances.csv** – Trial balance (Debit/Credit, balances at 71,305.60). Import via *Trial Balance import*, choose "Other" as source, date 31/03/2026, then check the "Map to" nominal for each line.
2. **02_clients.csv** – 12 clients (Data Import Wizard > Clients).
3. **03_suppliers.csv** – 10 suppliers (Data Import Wizard > Suppliers).
4. **04_sales_invoices.csv** – 20 invoices / 30 lines. Multi-line invoices repeat the invoice number. Mix of 0% (coffee, oat drink) and 20% (cups, grinders, training, servicing) VAT. 4 unpaid, including some overdue.
5. **05_purchase_invoices.csv** – 23 invoices / 25 lines (quarterly rent, monthly electricity at 5% VAT and green beans, plus occasional packaging, courier, oat drink, marketing, accountancy and roaster service). 1 unpaid.
6. **06_inventory_items.csv** – 14 reusable inventory items.

## Notes
- **Nominal postings:** sized to stay well within QuickFile's free 1,000-posting allowance. A cautious estimate is about 245 postings in total: 14 from the trial balance, about 110 from sales and about 120 from purchases. That counts a net and a VAT posting for every line, one control-account posting per invoice and two postings per payment, so the real figure should be lower (for example, 0% lines may not post VAT). This leaves room to demo bank entries, journals and new invoices.
- Dates are DD/MM/YYYY; VAT rates are whole numbers (20, 5, 0) as QuickFile requires.
- Header names match QuickFile's field names so columns auto-map; paid invoices use bank nominal 1200.
- Sales use nominal 4000 (goods) and 4010 (services); purchases use 5000, 6201, 7100, 7200, 7400, 7600, 7800. Check these against your chart of accounts.
- Sales imports are within QuickFile's 250-invoices-per-upload limit.
- The opening Trade Debtors (6,840) and Trade Creditors (3,960) are balances only, with no matching individual invoices.
- QuickFile doesn't document a CSV import format for inventory items, so the column layout in file 06 is a best guess. If there's no import for it, use it as a reference list for adding items by hand.
- `generate_demo_data.py` rebuilds every file (fixed random seed) if you want to change volumes or dates.
