import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 5))

# Floor
ax.plot([0, 60], [0, 0], color='black', linewidth=2)

# Step 1
ax.text(2, 5, "Monkey", fontsize=10, color='blue')
ax.add_patch(plt.Rectangle((10, 0), 3, 2, color='brown'))
ax.text(10, 2.5, "Box", fontsize=9)
ax.text(18, 8, "Banana", fontsize=10, color='green')
ax.text(2, -2, "Step 1\nInitial", ha='center')

# Arrow
ax.annotate("", xy=(22, 4), xytext=(19, 4),
            arrowprops=dict(arrowstyle="->", lw=2))

# Step 2
ax.text(25, 5, "Monkey", fontsize=10, color='blue')
ax.add_patch(plt.Rectangle((30, 0), 3, 2, color='brown'))
ax.text(30, 2.5, "Box", fontsize=9)
ax.text(30, -2, "Step 2\nMove to Box", ha='center')

# Arrow
ax.annotate("", xy=(42, 4), xytext=(39, 4),
            arrowprops=dict(arrowstyle="->", lw=2))

# Step 3
ax.add_patch(plt.Rectangle((45, 0), 3, 2, color='brown'))
ax.text(45, 2.5, "Box", fontsize=9)
ax.text(45, 5, "Monkey", fontsize=10, color='blue')
ax.text(46, 8, "Banana", fontsize=10, color='green')
ax.text(46, -2, "Step 3\nPush Box", ha='center')

# Arrow
ax.annotate("", xy=(55, 4), xytext=(52, 4),
            arrowprops=dict(arrowstyle="->", lw=2))

# Step 4
ax.add_patch(plt.Rectangle((57, 0), 3, 2, color='brown'))
ax.text(57, 3.2, "Monkey", fontsize=10, color='blue')
ax.text(58, 8, "Banana", fontsize=10, color='green')
ax.plot([58.5, 58.5], [4.2, 7.5], '--', color='red')
ax.text(58, -2, "Step 4\nClimb & Grab", ha='center')

ax.set_xlim(0, 65)
ax.set_ylim(-4, 10)
ax.set_title("Monkey and Banana Problem - One Frame Visualization")
ax.axis("off")

plt.show()
