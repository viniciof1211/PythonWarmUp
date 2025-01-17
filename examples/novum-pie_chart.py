import matplotlib.pyplot as plt

# Data
labels = ['Small Donations', 'Medium-Tier Perks', 'High-Tier Sponsorships']
sizes = [40, 35, 25]  # Percentages
colors = ['#ff9999', '#66b3ff', '#99ff99']  # Color palette
explode = (0.1, 0.1, 0)  # Highlighting small and medium tiers

# Plot
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)

# Title
plt.title('Crowdfunding Revenue Streams', fontsize=14, fontweight='bold')
plt.tight_layout()

# Show Chart
plt.show()
