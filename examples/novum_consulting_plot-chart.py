import matplotlib.pyplot as plt
import pandas as pd

# Data
months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
new_clients = [5, 8, 12, 16, 20, 25]  # Number of new clients each month
revenue = [clients * 1000 for clients in new_clients]  # Revenue at $1,000 per client

# Create a DataFrame
data = pd.DataFrame({
    "Months": months,
    "New Clients": new_clients,
    "Revenue ($)": revenue
})

# Display the Data Table
print(data)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(months, new_clients, label="New Clients", marker='o', color='blue', linewidth=2)
plt.plot(months, revenue, label="Revenue ($)", marker='o', color='green', linewidth=2)

# Labels and Title
plt.title("Consultancy Revenue Growth", fontsize=14, fontweight='bold')
plt.xlabel("Months", fontsize=12)
plt.ylabel("Counts / Revenue ($)", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Show Chart
plt.show()
