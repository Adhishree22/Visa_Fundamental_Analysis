# Visa Fundamental Analysis — Three-Statement Financial Model & Investment Framework

A production-grade equity research and valuation project on Visa Inc. (NYSE: V) built entirely in Python with a modular financial modeling architecture.

The project integrates historical financial data (2022–2025), driver-based forecasting (2026–2030), fully linked three-statement modeling, ratio analysis, multi-method valuation, quality/risk/growth scoring, and Tableau-based visualization into a complete institutional-style investment framework.

**Recommendation:** BUY
**Market Price:** $339.30
**Target Price:** $460
**Implied Upside:** +35%
**Conviction:** MEDIUM CONVICTION (68.93%)

---

## Live Dashboard
Tableau Dashboard: [Insert Tableau Public Link]

---


## Project Structure

```
financial-model/
│
├── README.md                          # This file
│
├── main_model.ipynb                   # (Google Colab compatible)                                
│
├── data/
│   ├── data_loader.py                 # Load & Parse Financial Data (Historical Data From Yfinance)
│   ├── data_processing.py             # Historical Financial Dataframe Construction
│   └── export_tableau.py              # Exports Clean Csvs For Tableau 
│
├── models/
│   ├── forecast.py                # Revenue & Driver Forecasting
│   ├── schedules/
│   │   ├── debt.py                # Debt schedule builder
│   │   ├── equity.py              # Equity schedule builder
│   │   ├── ppe.py                 # PPE depreciation schedule
│   │   └── working_capital.py     # Working capital schedule
│   │
│   └── statements/
│       ├── income_statement.py    # P&L construction
│       ├── balance_sheet.py       # Balance sheet + reconciliation
│       ├── cashflow_operating.py  # Operating cash flow
│       ├── cashflow_investing.py  # Investing cash flow
│       ├── cashflow_financing.py  # Financing cash flow
│       └── cash_balance.py        # Cash reconciliation
│   
├── analysis/
│   ├── eps.py                     # EPS Calculations
│   ├── driver_scenarios.py        # Driver Scenarios
│   ├── ratios/
│   │   ├── growth_ratios.py
│   │   ├── profitability_ratios.py
│   │   ├── liquidity_ratios.py
│   │   ├── leverage_ratios.py
│   │   ├── efficiency_ratios.py
│   │   ├── cashflow_ratios.py
│   │   ├── capital_ratios.py
│   │   └── risk_industry_ratios.py
│   │
│   ├── valuation/
│   │   ├── dcf_valuation.py       # DCF intrinsic value
│   │   ├── dcf_summary.py         # DCF Summary
│   │   ├── sensitivity.py         # Sensitivity analysis
│   │   ├── core.py                # Valuation function
│   │   ├── equity.py              # P/E, P/S, P/B multiples
│   │   ├── enterprise.py          # EV/EBITDA, EV/Revenue, EV/EBIT
│   │   ├── fcf_yield.py           # FCF yield approach
│   │   ├── dividend_yield.py      # Dividend yield approach
│   │   ├── diagnostics.py         # Multiples Diagnosis
│   │   └── aggregator.py          # Blended valuation
│   │
│   ├── scoring/
│   │   ├── utils.py               # Normalization function
│   │   ├── quality.py             # Quality scoring system
│   │   ├── risk.py                # Risk scoring system
│   │   ├── growth.py              # Growth scoring system
│   │   └── composite.py           # Composite scoring
│   │
│   └── decision/
│       ├── investment.py          # Investment decision logic
│       └── narrative.py           # Thesis generation
│
└── dashboard/                     # CSVs and Tableau Workbook
```

---

## Data Flow

```
yfinance (2022-2025 Actuals)
        ↓
Data Loader & Processor
        ↓
Historical DataFrame 
        ↓
Revenue Forecast (Payment Volume × Take Rate)
        ↓
Income Statement → Balance Sheet → Cash Flow Statements
        ↓
Supporting Schedules (Debt, Equity, PPE, WC)
        ↓
Ratio Analysis (Growth, Profitability, Liquidity, Leverage, Efficiency, Cash Flow, Capital, Risk/Industry)
        ↓
DCF Valuation + Multiples + Yield Approaches
        ↓
Quality, Risk, Growth Scoring
        ↓
Blended Price Target & Investment Recommendation
        ↓
Tableau Dashboard Visualization
```

---

## Data Sources
- yfinance — Income Statement, Balance Sheet, Cash Flow Statement, Beta, Market Data
- Coverage Period: FY2022–FY2025 historicals
- Forecast Period: FY2026–FY2030

---

## Financial Model Overview
### Historical & Forecast Coverage
| # | Category | Coverage |
|---|-----------|------------|
| 1 |Historical Period | 2022–2025 |
| 2 |Forecast Period | 2026–2030 |
| 3 |Financial Metrics | 75 |
| 4 |Ratios & KPIs | 70+ |
| 5 |Statements | Income Statement, Balance Sheet, Cash Flow |
| 6 |Schedules | Debt, Equity, PPE, Working Capital |
| 7 |Valuation | Equity Multiples, Enterprise Multiples, Yield Multiples, DCF  |
| 8 |Reconciliation | Fully linked and balanced |

---

## Revenue Forecast Framework

Visa's revenue model is driven through a simplified transaction-economics framework:
```
Revenue = Payment Volume × Take Rate
```

| # | Driver | 2025 | 2030 |
|---|-----------|------------|------------|
| 1 |Payment Volume Growth | 5.64% | 4.94% | 
| 2 |Take Rate | 0.28% | 0.33% |
| 3 |Revenue CAGR | — | 8.02% |

### Forecast Outputs
| # | Metric | 2025 | 2030 |
|---|-----------|------------|------------|
| 1 |Revenue | $39.96B | $60.79B | 
| 2 |Net Income | $20.04B | $31.77B | 
| 3 |Free Cash Flow | $21.58B | $37.89B | 
| 4 |Operating Margin | 66.39% | 67.06% | 
| 5 |Net Margin | 50.14% | 52.27% | 

---

## Key Deliverables

### **Three-Statement Integrated Financial Model** 
Complete, reconciled financials for 9 years (2022–2030):

**Income Statement** (all years, all line items):
- Revenue → COGS → Gross Profit → OpEx → Operating Income → Other Expense → Interest → EBT → Taxes → Net Income
- 2030 Revenue: $60.79B | 2030 Net Income: $31.77B
- Stable operating margin: 66.39% (2025) → 67.06% (2030)
- Stable net margin: 50.14% (2025) → 52.27% (2030)

**Cash Flow Statement** (9 years, fully linked):
- Operating Cash Flow: $23.06B (2025) → $39.99B (2030), +10% CAGR
- Capex: $1.48B (2025) → $2.09B (2030), 3% of revenue
- Free Cash Flow: $21.58B (2025) → $37.89B (2030), 62% margin by 2030
- Financing: Dividends + Buybacks = $22.95B (2025) → $32.71B (2030)
- Cash Balance: $24.99B (2025) → $40.98B (2030)

**Balance Sheet** (fully reconciled, Assets = Liabilities + Equity):
- Total Assets: $99.63B (2025) → $132.61B (2030)
- Goodwill & Intangibles: $47.53B (2025) → $47.10B (2030)
- Total Liabilities: $61.72B (2025) → $86.91B (2030)
- Total Equity: $37.91B (2025) → $45.60B (2030)
- Balance Sheet Check: **0.0** across all 9 years 

### **Supporting Schedules** (modular, linked)
- **Debt Schedule:** TotalDebt, LongTermDebt, ShortTermDebt, Interest, Debt Issued, Debt Repayment
- **Equity Schedule:** NetIncome, Dividends, Buybacks, Share Issuance, SBC, Common Stock Equity, Preferred Stock Equity
- **PPE Schedule:** Depreciation, Capex, Net PPE
- **Working Capital Schedule:** Receivables, Payables, Current Assets/Liabilities, NWC changes

### **Comprehensive Ratio Analysis** (70+ ratios) 

**Profitability:**
- Net Margin: 50.14% (2025) → 52.27% (2030)
- Operating Margin: 66.39% (2025) → 67.06% (2030)
- Gross Margin: 80.36% (2025) → 81.17% (2030)
- ROE: 52.91% (2025) → 69.68% (2030)
- ROA: 20.13% (2025) → 23.96% (2030)

**Growth:**
- Revenue Growth: 11.34% (2025) → 8.02% (2030)
- EPS Growth: 4.83% (2025) → 7.47% (2030)
- FCF Growth: 15.43% (2025) → 10.01% (2030)
- Earnings Growth: 1.59% (2025) → 7.99% (2030)

**Liquidity & Leverage:**
- Current Ratio: 1.08x (2025) → 1.35x (2030)
- Debt-to-EBITDA: 0.97x (2025) → 0.82x (2030)
- Interest Coverage: 45.09x (2025) → 45.55x (2030)
- Net Debt-to-EBITDA: 0.31x (2025) → 0.13x (2030)

**Cash Quality:**
- FCF-to-Revenue: 54% (2025) → 62% (2030)
- OCF-to-NetIncome: 1.15x (2025) → 1.26x (2030)
- FCF Conversion: 1.08x (2025) → 1.19x (2030), >100% conversion
- FCF per Share: $11.16 (2025) → $19.18 (2030)

---

## Multi-Method Valuation Framework

| # | Valuation Method          | Fair Value Range | Implied Upside   | Key Assumption                 |
|---| ------------------------- | ---------------- | ---------------- | ------------------------------ |
| 1 | **P/E Approach**          | $351 – $451      | +3% to +33%      | 28–32x earnings multiple       |
| 2 | **EV-Based Methods**      | $336 – $468      | Flat to +38%     | EBITDA / Revenue / EBIT comps  |
| 3 | **DCF Valuation**         | $375 – $683      | +10% to +101%    | WACC 7.32%, Terminal Growth 4% |
| 4 | **FCF Yield Method**      | $338 – $541      | +0% to +59%      | 3% steady-state FCF yield      |
| 5 | **Blended Target Price**  | **$460 – $470**  | **+35% to +38%** | Weighted valuation consensus   |

---

## DCF Assumptions & Sensitivity
### Core Assumptions
| # | Assumption  | Value
|---| --------------------- | ------------|
| 1 | WACC  | 7.32%  | 
| 2 | Risk Free Rate  | 0.07  | 
| 3 | Market Premium  | 0.05  | 
| 4 | Terminal Growth Rate  | 4.00%  | 


## DCF Scenario Outputs
| # |Scenario  | Enterprise Value  | Equity Value  | Implied Price  | Terminal Value Weight  | 
|---|-------------------| ---------------- | ---------------- | ----------------| ---------------- |
| 1 |Low Case  | $747.4B  | $741.8B  | $375.42  | 83%  | 
| 2 |Base Case  | $960.0B  | $954.5B  | $483.04  | 87%  | 
| 3 |High Case  | $1.36T  | $1.35T  | $683.26  | 91%  | 

---

## Scoring Framework
### Quality Score

Measures:
-Profitability
-Capital efficiency
-Cash flow quality
-Balance sheet strength

Year	Score
2025	51.92
2030	90.20


### Risk Score

Measures:
-Leverage
-Coverage
-Liquidity
-Cash flow stress
-Operating risk
-Volatility risk

Year	Score
2025	54.39
2030	26.41


###Growth Score

Measures:
-Revenue growth
-Earnings growth
-Cash flow growth
-Operating growth
-Reinvestment growth

Year	Score
2025	45.05
2030	31.43

---

## Tableau Story — 6 Dashboards
| # | Dashboard | Key Charts |
|---|-----------|------------|
| 1 |**Executive Summary** | KPIs, Recommendation card, Valuation Summary, Capital Return Metrics, Revenue & EPS Trends | 
| 2 |**Income Statement Analysis | Income Statement Structure, Margin Trends, YoY growth | 
| 3 |**Balance Sheet Analysis | Assets Composition, Liabilities Equity Structure, Debt Maturity, Balance Sheet Ratios| 
| 4 |**Cash Flow Analysis | Cash Flow Structure, FCF Vs Cash Balance, Cash Flow ratios | 
| 5 |**Valuation & Multiples | Multiples Heatmap, DCF Sensitivity, Price Targets, Expected Returns | 
| 6 |**Investment Framework | Quality Components, Risk Intelligence Heatmap, Factor Score trends, Returns Trends, Operating Summary, Investment Thesis Summary | 

---

## Key Findings

### Financial Forecasts (2026–2030)

| Metric | 2030 | CAGR (2025–2030) |
|--------|------|------------------|
| **Revenue** | $60.79B | +8.02% |
| **Operating Income** | $40.67B | +8.01% |
| **Net Income** | $31.77B | +7.99% |
| **EPS** | $15.83 | +7.47% |
| **Operating Cash Flow** | $39.99B | +9.91% |
| **Free Cash Flow** | $37.89B | +10.01% |
| **Operating Margin** | 67.06% | Stable |
| **Net Profit Margin** | 52.27% | Stable |
| **ROE** | 69.68% | Expanding |
| **ROIC** | ~25% | Stable |

---

## Investment Thesis

### Key Upside Catalysts ⬆️
▲ Strong valuation upside (~35.5% to target)
▲ Improving business quality trajectory (51.9 → 90.2)
▼ Declining risk profile over forecast period (54.4 → 26.4)
■ Valuation multiple expansion potential (PE: 31.6x → 27x)

### Key Downside Risks ⬇️
■ Moderate current business quality profile (51.9/100)
▼ Suboptimal long-term growth trajectory (6–9% CAGR)
▲ Elevated near-term risk levels (54/100)
▲ High dependence on terminal value assumptions

---

## Tools & Technologies

| Tool | Usage |
|------|-------|
| Python (Pandas, NumPy) | Data engineering, ratio calculation, EDA, comps, risk scoring |
| yfinance | Financial statement data retrieval |
| Modular Python scripts | Clean separation across pipeline, ratios, EDA, comps, risk, export |
| Jupyter Notebook | Orchestration and documentation |
| Tableau Public | Interactive 6-dashboard story with global filters |

---
## How to Run

```bash
# Clone repository
git clone 
cd financial-model

# Install dependencies
pip install pandas numpy yfinance

# Run the model
notebook main_model.ipynb
```
---

## Known Assumptions & Limitations
-Forecasts assume stable macroeconomic conditions
-Terminal growth capped at 4%
-DCF highly sensitive to WACC assumptions
-Multiples valuation depends on market sentiment
-Historical financial data sourced through yfinance
-Forecasts rely partially on historical trend continuation

---
