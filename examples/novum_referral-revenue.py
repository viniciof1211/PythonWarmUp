import matplotlib.pyplot as plt
import pandas as pd

# Data
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
revenue_generated = [5000, 7000, 9000, 12000, 15000, 18000]  # Revenue from referrals
affiliate_payouts = [1000, 1400, 1800, 2400, 3000, 3600]  # Payouts to affiliates (20% of revenue)

# Create a DataFrame
data = pd.DataFrame({
    "Months": months,
    "Revenue Generated ($)": revenue_generated,
    "Affiliate Payouts ($)": affiliate_payouts
})

# Display the Data Table
print(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(months, revenue_generated, label="Revenue Generated", marker='o', color='blue', linewidth=2)
plt.plot(months, affiliate_payouts, label="Affiliate Payouts", marker='o', color='green', linewidth=2)

# Labels and Title
plt.title("Affiliate Payouts vs Revenue Generated", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Amount ($)", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Show Chart
plt.show()
