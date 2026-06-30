# data-visualization-and-storytelling
Internship: Data Analyst Internship (Elevate Labs)
Task: Task 2 - Data Visualization and Storytelling

## What this task was about

The goal was to take a sales dataset and turn it into a short visual story - not just throw a bunch of charts together, but pick the right chart for each question, cut the clutter, and end with clear business takeaways.

## Tools I used

Tableau/Power BI weren't available to me (no license, and I wanted to avoid the paid-tools issue mentioned in the guidelines), so I rebuilt the same workflow using **Python (pandas + matplotlib)**. The principles are identical to what you'd do in Tableau or Power BI: pick the right chart type, keep one clear colour story per chart, label the takeaway, and avoid 3D/decorative junk.

## Dataset

`data/superstore_sample.csv` - a synthetic sales dataset (1,500 orders, 2023-2024) modeled after the classic Superstore dataset structure: Region, State, Segment, Category, Sub-Category, Ship Mode, Sales, Discount, Profit. I built this myself with `make_data.py` since I didn't have the original Superstore.csv handy, but kept the same columns/logic so the analysis approach transfers directly.

## Files in this repo

```
data/
  superstore_sample.csv        -> the dataset used
charts/
  01_sales_trend.png           -> monthly sales line chart
  02_sales_by_category.png     -> sales by category (bar)
  03_profit_by_subcategory.png -> profit by sub-category (diverging bar)
  04_sales_by_region.png       -> sales by region (bar)
  05_segment_share.png         -> customer segment share (pie)
  06_discount_vs_profit.png    -> discount vs profit (scatter)
make_data.py                   -> script that generates the dataset
make_charts.py                 -> script that generates all 6 charts
build_report.py                -> script that compiles charts + text into the final PDF
Sales_Visual_Story_Report.pdf  -> FINAL DELIVERABLE - the visual report
interview_questions.md         -> my answers to the task's interview questions
```

## How I approached it (following the mini-guide)

1. **Chose the right chart for each question** - bar charts for comparing categories/regions (length is easier to read accurately than pie wedges), a line chart for the trend over time, a pie chart only where it's a true part-of-a-whole story (3-segment split), and a scatter plot to show the discount-vs-profit relationship.
2. **Avoided clutter** - no 3D effects, no rainbow palettes, gridlines kept light, only one accent colour per chart (red used only to flag negative/loss values).
3. **Highlighted key takeaways** - every chart in the report has a one-line "Takeaway" box under it instead of leaving the reader to guess the point.
4. **Added context** - each chart has 2-3 sentences explaining what's actually happening in the numbers, not just a caption.
5. **Focused on business insight, not just visuals** - the report ends with a Summary Storyboard table mapping each insight to a recommended action.
6. **Created a summary storyboard** - last page of the PDF report.

## Key findings (short version)

- Technology drives ~64% of total sales - the clear growth engine.
- Office Supplies is a small slice (~7%) of revenue - not worth heavy investment.
- South region trails East/West by close to 45% - worth investigating.
- Orders with deep discounts (avg ~40%) are where most losses happen; profitable orders average only ~10% discount.
- Consumer segment is the largest customer base (~48% of sales).

See `Sales_Visual_Story_Report.pdf` for the full visual report with charts and write-up.

## How to reproduce

```bash
pip install pandas matplotlib reportlab numpy
python make_data.py      # generates data/superstore_sample.csv
python make_charts.py    # generates the 6 PNG charts in charts/
python build_report.py   # compiles everything into the final PDF
```

## Notes / what I'd do differently with more time

- With real Superstore.csv data (or actual company data) and a live Tableau/Power BI license, I'd build this as an interactive dashboard with filters by Region/Category/Date instead of a static PDF, so a viewer could drill down themselves.
- I'd add a year-over-year comparison once more years of data are available.
