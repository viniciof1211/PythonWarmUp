import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

# Data Preparation
data = {
    "Task Name": [
        "Membership Launch", "Crowdfunding Planning", "Product Development",
        "Affiliate Partnerships", "Crowdfunding Launch", "Consulting Services Debut",
        "Corporate Sponsorships Secured", "IP Monetization",
        "Cryptocurrency ICO", "Final Revenue Consolidation"
    ],
    "Start Date": [
        "2025-01-15", "2025-01-15", "2025-02-01",
        "2025-02-01", "2025-03-01", "2025-03-01",
        "2025-04-01", "2025-04-01", "2025-05-01",
        "2025-06-01"
    ],
    "End Date": [
        "2025-02-28", "2025-02-28", "2025-03-31",
        "2025-03-31", "2025-04-30", "2025-04-30",
        "2025-05-31", "2025-05-31", "2025-06-30",
        "2025-06-30"
    ],
    "Owner": [
        "Membership Strategist", "Crowdfunding Coordinator", "Product Manager",
        "Affiliate Manager", "Crowdfunding Coordinator", "Consulting Manager",
        "Sponsorship Liaison", "IP Strategist",
        "Blockchain Lead", "Finance Manager"
    ],
    "Status": [
        "Not Started", "Not Started", "Not Started",
        "Not Started", "Not Started", "Not Started",
        "Not Started", "Not Started",
        "Not Started", "Not Started"
    ],
    "Percentage Complete": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Convert dates to datetime
df = pd.DataFrame(data)
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["End Date"] = pd.to_datetime(df["End Date"])

# Plotting Gantt Chart
fig, ax = plt.subplots(figsize=(15, 8))
for i, task in df.iterrows():
    start = date2num(task["Start Date"])
    end = date2num(task["End Date"])
    ax.barh(
        i, end - start, left=start, color='indigo', alpha=0.8, edgecolor='black'
    )
    ax.text(
        start, i, f"{task['Task Name']} ({task['Owner']})",
        va='center', ha='right', fontsize=9, color='white'
    )

# Adding Milestones
milestones = {
    "Funding Goal Reached": "2025-06-30",
    "First Sponsor Secured": "2025-04-15"
}
for milestone, date in milestones.items():
    date = datetime.strptime(date, "%Y-%m-%d")
    ax.scatter(date2num(date), len(df), color='gold', s=150, label=milestone)

# Formatting Chart
ax.set_yticks(range(len(df)))
ax.set_yticklabels(df["Task Name"])
ax.set_xticks(pd.date_range("2025-01-01", "2025-12-31", freq='M'))
ax.xaxis_date()
plt.title("Novum Phase 2 Execution Timeline", fontsize=16, fontweight='bold')
plt.xlabel("Timeline", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# Show Chart
plt.show()
