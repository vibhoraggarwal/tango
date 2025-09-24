import matplotlib.pyplot as plt
import mpld3

# Define instrument positions based on rhythm/melody and tone range
# (0 = Rhythm, 1 = Melody), (0 = Low Tone, 1 = High Tone)
instruments = {
    "Klavier (Piano)": (0.5, 0.4),
    "Contrabass (Double Bass)": (0.2, 0.1),
    "Geigen (Violin)": (0.8, 0.8),
    "Cello": (0.4, 0.3),
    "Bandonion (Bandoneón)": (0.3, 0.5),
    "Akkordeon (Accordion)": (0.5, 0.6)
}

x = [pos[0] for pos in instruments.values()]
y = [pos[1] for pos in instruments.values()]

plt.figure(figsize=(8, 6))
plt.scatter(x, y, c="crimson", s=100, marker="o", edgecolors="black")

for label, (x_pos, y_pos) in instruments.items():
    plt.text(x_pos + 0.02, y_pos + 0.02, label, fontsize=10)

plt.xlabel("Rhythm  ⟶  Melody", fontsize=12)
plt.ylabel("Low Tone  ⟶  High Tone", fontsize=12)
plt.title("Tango Instruments: Rhythm vs. Melody & Tone Range", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.5)
plt.xlim(0, 1)
plt.ylim(0, 1)

# Save as interactive HTML
html_str = mpld3.fig_to_html(plt.gcf())
with open("diagram.html", "w") as f:
    f.write(html_str)
