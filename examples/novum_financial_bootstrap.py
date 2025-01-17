# Python code to generate the chart for revenue projection

import matplotlib.pyplot as plt

# Data
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
members = [100, 100, 100, 150, 175, 200]
revenue = [25000, 25000, 25000, 37500, 43750, 50000]
scaling_trendline = [50000, 50000, 50000, 75000, 87500, 100000]

# Plot
plt.figure(figsize=(10, 6))
plt.plot(months, revenue, label="Revenue (100 Members)", marker='o', color='blue', linewidth=2)
plt.plot(months, scaling_trendline, label="Scaling Trendline (200 Members)", linestyle='--', color='green', linewidth=2)

# Labels and Title
plt.title("Revenue Projection for Membership Strategy", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Show Chart
plt.show()
