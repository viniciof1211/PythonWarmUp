import matplotlib.pyplot as plt

# Data
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
agreements = {
    "Agreement 1": [5000, 10000, 15000, 20000, 25000, 30000],
    "Agreement 2": [4000, 8000, 12000, 16000, 20000, 24000],
    "Agreement 3": [3000, 6000, 9000, 12000, 15000, 18000],
    "Agreement 4": [2000, 4000, 6000, 8000, 10000, 12000],
    "Agreement 5": [1000, 2000, 3000, 4000, 5000, 6000],
}

# Plot
plt.figure(figsize=(12, 6))
for agreement, revenue in agreements.items():
    plt.plot(months, revenue, marker='o', label=agreement)

# Labels and Title
plt.title('Incremental IP Revenue Growth (5 Agreements)', fontsize=14, fontweight='bold')
plt.xlabel('Months', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Show Chart
plt.show()
