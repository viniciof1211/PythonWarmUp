import matplotlib.pyplot as plt

# Data
product_types = ['E-Books', 'Courses', 'Apparel', 'Posters']
revenue = [45000, 60000, 25000, 15000]  # Revenue in dollars
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Color palette for the chart

# Plot
plt.figure(figsize=(8, 8))
plt.pie(revenue, labels=product_types, colors=colors, autopct='%1.1f%%', startangle=140, shadow=True, explode=(0.1, 0.1, 0, 0))

# Title
plt.title('Revenue Breakdown by Product Type', fontsize=14, fontweight='bold')
plt.tight_layout()

# Show Chart
plt.show()
