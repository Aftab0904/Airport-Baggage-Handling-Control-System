import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# Create assets directory
os.makedirs('assets', exist_ok=True)

# Professional Industrial Theme
plt.style.use('dark_background')
sns.set_palette("viridis")

# 1. GENERATE MOCK DATA: 24-Hour Throughput (Bags Per Hour)
np.random.seed(42)
hours = np.arange(24)
# Simulating peaks for morning/evening flight clusters
throughput = 1500 + 1000 * np.sin(np.pi * hours / 6) + np.random.normal(0, 200, 24)
throughput = np.clip(throughput, 500, 3000)

# Calculate Trendline (Polynomial Fit)
z = np.polyfit(hours, throughput, 3)
p = np.poly1d(z)
trendline = p(hours)

# 2. GENERATE MOCK DATA: Fault Distribution
fault_types = ['Diverter Jam', 'Sensor Blockage', 'Node Timeout', 'E-Stop Trigger']
fault_counts = [45, 25, 15, 5]

# 3. PLOTTING THE DASHBOARD
fig = plt.figure(figsize=(16, 10))
grid = plt.GridSpec(2, 2, wspace=0.3, hspace=0.4)

# Plot 1: Throughput Analysis with Trendline
ax1 = fig.add_subplot(grid[0, :])
sns.lineplot(x=hours, y=throughput, ax=ax1, color='#00d1ff', linewidth=3, label='Real-time Throughput (BPH)')
ax1.plot(hours, trendline, "r--", alpha=0.8, linewidth=2, label='Polynomial Trendline')
ax1.fill_between(hours, throughput, 0, color='#00d1ff', alpha=0.1)
ax1.set_title('System Throughput Dynamics: 24-Hour Cycle Analysis', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Hour of Day', fontsize=12)
ax1.set_ylabel('Bags Per Hour (BPH)', fontsize=12)
ax1.set_xticks(hours)
ax1.grid(True, linestyle='--', alpha=0.3)
ax1.legend(loc='upper right')

# Plot 2: Fault Distribution (Donut Chart)
ax2 = fig.add_subplot(grid[1, 0])
colors = ['#ff4b2b', '#ff9068', '#fbc531', '#4cd137']
wedges, texts, autotexts = ax2.pie(fault_counts, labels=fault_types, autopct='%1.1f%%', 
                                  colors=colors, startangle=140, pctdistance=0.85, 
                                  wedgeprops=dict(width=0.4, edgecolor='w'))
ax2.set_title('Failure Mode Distribution', fontsize=14, fontweight='bold')

# Plot 3: System Efficiency (Cumulative Success vs. Goal)
ax3 = fig.add_subplot(grid[1, 1])
goals = np.full(24, 2500)
sns.barplot(x=hours[::2], y=throughput[::2], ax=ax3, color='#4cd137', alpha=0.7, label='Actual Performance')
ax3.axhline(2500, color='red', linestyle='--', label='Target Efficiency Goal')
ax3.set_title('Operational Efficiency vs. Target Benchmarks', fontsize=14, fontweight='bold')
ax3.set_ylabel('Bags Per Hour')
ax3.set_xlabel('Sampled Hours')
ax3.legend(loc='lower right')

plt.suptitle('Airport Baggage Handling Control System: Advanced Analytics Dashboard', fontsize=22, fontweight='bold', y=0.98)
plt.savefig('assets/system_analytics_dashboard.png', dpi=300, bbox_inches='tight', facecolor='#121212')
print("Advanced analytics dashboard generated successfully at assets/system_analytics_dashboard.png")
