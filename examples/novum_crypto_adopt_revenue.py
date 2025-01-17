import matplotlib.pyplot as plt

# Data
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
adoption_rates = [5, 10, 20, 35, 50, 70]  # Percentage of adoption rate
ico_revenue = [10000, 20000, 35000, 55000, 80000, 110000]  # Revenue from ICOs in dollars

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(adoption_rates, ico_revenue, color='purple', edgecolor='black', s=100)

# Customization
for i, month in enumerate(months):
    plt.text(adoption_rates[i] + 1, ico_revenue[i] + 1000, month, fontsize=9)

plt.title("Cryptocurrency Adoption Rates vs. ICO Revenue", fontsize=14, fontweight='bold')
plt.xlabel("Adoption Rate (%)", fontsize=12)
plt.ylabel("ICO Revenue ($)", fontsize=12)
plt.grid(alpha=0.3)

# Show Chart
plt.tight_layout()
plt.show()
