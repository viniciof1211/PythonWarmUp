import matplotlib.pyplot as plt

# Data
ventures = ['Venture 1', 'Venture 2', 'Venture 3', 'Venture 4', 'Venture 5']
investment = [10000, 10000, 10000, 10000, 10000]  # $50,000 equally divided
average_return_rate = 0.4  # 40% average return
projected_returns = [amount + (amount * average_return_rate) for amount in investment]

# Plot
plt.figure(figsize=(10, 6))
x = range(len(ventures))

# Bar Chart
plt.bar(x, investment, width=0.4, label='Original Investment', color='blue', align='center')
plt.bar(x, projected_returns, width=0.4, label='Projected Returns', color='green', align='edge')

# Customization
plt.xticks(x, ventures)
plt.xlabel("Ventures", fontsize=12)
plt.ylabel("Amount ($)", fontsize=12)
plt.title("Projected ROI for Diversified Ventures", fontsize=14, fontweight='bold')
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Show Chart
plt.tight_layout()
plt.show()
