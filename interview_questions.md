# Interview Questions - My Answers

**1. What is the importance of data visualization?**
Raw numbers in a spreadsheet don't tell a story on their own - most people can't spot a trend by scanning 1,500 rows of numbers. Visualization turns that data into a shape the brain can process instantly: a line going up or down, a bar that's clearly taller than the rest. It speeds up decision-making and makes it much easier to spot outliers, trends, and relationships that would otherwise be buried.

**2. When do you use a pie chart vs bar chart?**
I use a pie chart only when I'm showing how a *whole* breaks into a small number of parts (ideally 5 or fewer) and the percentages are the actual point - like "what share of sales comes from each customer segment." Bar charts are better almost everywhere else, especially when there are more categories, when I want the reader to compare exact values rather than guess at angles, or when I'm ranking things (best to worst). In this task, I used a bar chart for Region and Category comparisons, and a pie chart only for the 3-way Segment split.

**3. How do you make visualizations more engaging?**
Give every chart a clear, specific title that states the insight (not just "Sales by Region" but something closer to "East and West Carry the Business"), use colour with intention rather than decoration (e.g. red only for losses), add direct data labels so the reader doesn't have to estimate, and keep one chart focused on one idea instead of cramming multiple messages into it.

**4. What is data storytelling?**
It's the practice of connecting data, visuals, and narrative together so a viewer doesn't just see numbers - they understand what happened, why it matters, and what to do next. A good data story has a clear beginning (context), middle (the finding, shown visually), and end (the recommended action), the same way the Summary Storyboard table at the end of my report ties every chart back to a business decision.

**5. How do you avoid misleading visualizations?**
Always start bar chart axes at zero so bar heights are proportional to the real values, avoid 3D effects that distort perception of size, label what's actually being measured (sum vs. average vs. count), use consistent scales when comparing charts, and don't cherry-pick a date range that exaggerates a trend. I also try to make sure the chart type itself doesn't oversell a difference - e.g. not zooming into a tiny y-axis range to make a small change look dramatic.

**6. What are best practices in dashboard design?**
Put the most important KPI/number top-left since that's where the eye lands first, group related charts together, keep a consistent colour palette across the whole dashboard (not different palettes per chart), limit the number of charts on one screen so it doesn't feel overwhelming, and always allow filtering/drill-down so different users can ask their own follow-up questions of the same dashboard.

**7. What tools have you used for visualization?**
For this task I used Python (pandas for data prep, matplotlib for the charts) and reportlab to assemble everything into a PDF report, since I didn't have a Tableau/Power BI license available. I'm familiar with the core concepts of Tableau and Power BI as well (drag-and-drop chart building, calculated fields, dashboard filters) and the design principles I followed here - right chart type, minimal clutter, clear takeaways - apply the same way in either tool.
