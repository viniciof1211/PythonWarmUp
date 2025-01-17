import matplotlib.pyplot as plt
import numpy as np

# Data
sponsors = ['Sponsor A', 'Sponsor B', 'Sponsor C', 'Sponsor D', 'Sponsor E']
current_revenue = [10000, 10000, 10000, 10000, 10000]
projected_revenue = [20000, 20000, 20000, 20000, 20000]  # Projections for repeat contributions

x = np.arange(len(sponsors))  # Positions for the bars

# Plot
plt.figure(figsize=(10, 6))
bar_width = 0.35
plt.bar(x - bar_width / 2, current_revenue, width=bar_width, label='Current Contribution', color='blue')
plt.bar(x + bar_width / 2, projected_revenue, width=bar_width, label='Projected Contribution', color='green')

# Labels and Title
plt.xticks(x, sponsors)
plt.title('Corporate Sponsor Revenue Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Corporate Sponsors', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show Chart
plt.tight_layout()
plt.show()
