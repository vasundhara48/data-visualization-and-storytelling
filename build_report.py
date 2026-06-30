from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                 PageBreak, Table, TableStyle, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT

CH = "/home/claude/task2_submission/charts/"

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleX", parent=styles["Title"], fontSize=22, spaceAfter=4)
sub_style = ParagraphStyle("SubX", parent=styles["Normal"], fontSize=11, textColor=colors.grey, spaceAfter=18)
h2 = ParagraphStyle("H2", parent=styles["Heading2"], fontSize=14, spaceBefore=14, spaceAfter=6, textColor=colors.HexColor("#1B3B5F"))
body = ParagraphStyle("Body", parent=styles["Normal"], fontSize=10.3, leading=15, alignment=TA_LEFT, spaceAfter=8)
takeaway = ParagraphStyle("Takeaway", parent=styles["Normal"], fontSize=10.3, leading=15,
                           backColor=colors.HexColor("#EAF2F8"), borderPadding=8, spaceAfter=10)

doc = SimpleDocTemplate("/home/claude/task2_submission/Sales_Visual_Story_Report.pdf",
                         pagesize=letter,
                         topMargin=0.6*inch, bottomMargin=0.6*inch,
                         leftMargin=0.7*inch, rightMargin=0.7*inch)

story = []

story.append(Paragraph("Sales Performance: A Visual Story", title_style))
story.append(Paragraph("Data Analyst Internship - Task 2 | Data Visualization &amp; Storytelling", sub_style))
story.append(HRFlowable(width="100%", color=colors.HexColor("#1B3B5F"), thickness=1))
story.append(Spacer(1, 12))

story.append(Paragraph(
    "This report walks through two years (2023-2024) of sales data for a retail business "
    "selling Furniture, Office Supplies, and Technology products across the US. "
    "The goal isn't just to show charts - it's to answer a business question: "
    "<b>where is the company making money, where is it leaking money, and what should "
    "leadership do about it?</b>", body))

story.append(Paragraph(
    "<b>Headline numbers:</b> Total Sales = $1,348,774 | Total Profit = $236,015 "
    "| Overall margin &#8776; 17.5% | About 5.5% of all orders were sold at a loss.", takeaway))

story.append(Spacer(1, 6))

def add_chart_section(title, img_path, insight_text, takeaway_text, img_height=3.1*inch):
    story.append(Paragraph(title, h2))
    story.append(Image(img_path, width=6.4*inch, height=img_height))
    story.append(Spacer(1, 4))
    story.append(Paragraph(insight_text, body))
    story.append(Paragraph("<b>Takeaway:</b> " + takeaway_text, takeaway))

add_chart_section(
    "1. Sales Are Growing, But Not Evenly",
    CH + "01_sales_trend.png",
    "Monthly sales bounce between roughly $40K and $75K, with visible seasonal peaks "
    "rather than a flat, predictable line. This kind of month-over-month swing is normal "
    "for retail, but it matters for inventory and staffing planning.",
    "Use the high months as a forecasting baseline for promotions and stock-up cycles "
    "instead of treating every month the same.",
)
story.append(PageBreak())

add_chart_section(
    "2. Technology Drives Revenue, Office Supplies Barely Registers",
    CH + "02_sales_by_category.png",
    "Technology alone generated $865,617 in sales - nearly two-thirds of total revenue - "
    "while Office Supplies brought in only $100,358. A bar chart was used here instead of "
    "a pie chart because the goal is to compare exact magnitudes across only three "
    "categories, where length is easier to judge accurately than wedge angle.",
    "Technology is the growth engine. Office Supplies may be more of a 'convenience add-on' "
    "category than a category worth heavy marketing investment.",
)

add_chart_section(
    "3. Not Every Profitable Category Has Profitable Sub-Categories",
    CH + "03_profit_by_subcategory.png",
    "Every individual sub-category technically stayed profitable overall, but the gap is "
    "stark: Phones and Accessories each generated over $40K in profit, while Paper, Storage "
    "and Art barely cleared $4-5K. Colour is used here only to flag risk (none currently "
    "fall below zero), not for decoration.",
    "Low-margin sub-categories like Paper and Art are good candidates for bundling or "
    "reduced promotional spend, freeing budget for high performers like Phones.",
    img_height=3.6*inch
)
story.append(PageBreak())

add_chart_section(
    "4. East and West Carry the Business",
    CH + "04_sales_by_region.png",
    "East ($414,718) and West ($409,933) regions together account for roughly 61% of all "
    "sales, while South lags at $224,965 - nearly half of East's total.",
    "South region is underperforming relative to its peers and is worth a closer look: "
    "is it a smaller market, weaker logistics, or under-investment in marketing?",
)

add_chart_section(
    "5. Consumers Are the Core Customer Base",
    CH + "05_segment_share.png",
    "A pie chart is appropriate here because the story is about share of a whole (100%) "
    "across just three segments. Consumer customers make up about 48% of sales, ahead of "
    "Corporate (32%) and Home Office (20%).",
    "Marketing and loyalty programs aimed at individual consumers will likely have the "
    "broadest revenue impact, while Corporate accounts may offer room to grow through "
    "account-based sales outreach.",
    img_height=3.4*inch
)
story.append(PageBreak())

add_chart_section(
    "6. Heavy Discounting Is Where Profit Goes to Die",
    CH + "06_discount_vs_profit.png",
    "Orders placed at a loss carried an average discount rate of about 40%, compared to "
    "just 10% for profitable orders. The scatter plot makes this relationship visible at a "
    "glance: as discount rate climbs past roughly 30%, profit increasingly dips below zero.",
    "Cap discretionary discounts below 25-30% wherever possible, or pair deep discounts "
    "with cost controls (e.g. bundling, reduced shipping tier) so they don't quietly erase "
    "the margin on the sale.",
)

story.append(Paragraph("Summary Storyboard", h2))
data = [
    ["Insight", "What the data shows", "Recommended action"],
    ["Revenue driver", "Technology = 64% of sales", "Protect & expand Technology inventory and marketing"],
    ["Underperformer", "Office Supplies = only 7% of sales", "Reduce SKU range / bundle with other categories"],
    ["Weak region", "South sales trail East/West by ~45%", "Audit pricing, logistics, and local marketing in South"],
    ["Margin leak", "Loss-making orders avg. 40% discount", "Set a discount ceiling and monitor margin in real time"],
    ["Core customer", "Consumer segment = 48% of sales", "Prioritize loyalty/retention programs for consumers"],
]
t = Table(data, colWidths=[1.3*inch, 2.6*inch, 2.5*inch])
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#1B3B5F")),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("FONTSIZE", (0,0), (-1,-1), 8.7),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, colors.HexColor("#F4F7FA")]),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
]))
story.append(t)
story.append(Spacer(1, 14))
story.append(Paragraph(
    "<i>Note: This dataset is a synthetic sample built to mirror the structure of the "
    "classic Superstore dataset (Region, Segment, Category, Discount, Profit, etc.) since "
    "a paid Tableau/Power BI license wasn't available. Charts were built in Python "
    "(pandas + matplotlib) using the same design principles - right chart for the data, "
    "minimal clutter, one colour story per chart, and a takeaway for every chart - that "
    "apply equally in Tableau or Power BI.</i>", body))

doc.build(story)
print("done")
