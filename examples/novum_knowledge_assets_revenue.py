import matplotlib.pyplot as plt

# Data
months = ["January", "February", "March", "April", "May", "June"]
subscription_revenue = [1200, 1500, 1800, 2000, 2500, 3000]  # Revenue for each month in dollars

# Plot
plt.figure(figsize=(10, 6))
plt.bar(months, subscription_revenue, color='skyblue', edgecolor='black')

# Customization
plt.title("Monthly Subscription Revenue from Knowledge Assets", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Show Chart
plt.show()
