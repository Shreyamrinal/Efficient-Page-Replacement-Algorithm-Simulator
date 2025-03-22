import matplotlib.pyplot as plt

with open("results.txt", "r") as file:
    data = file.readlines()

algorithms = []
faults = []
for line in data:
    algo, fault_count = line.split()
    algorithms.append(algo)
    faults.append(int(fault_count))

fig, ax = plt.subplots()
bars = ax.bar(algorithms, faults, color=['orange', 'violet', 'green'])
plt.xlabel("Page Replacement Algorithms")
plt.ylabel("Total Page Faults")
plt.title("Comparison of Page Replacement Algorithms")
annot = ax.annotate("", xy=(0,0), xytext=(10,10), textcoords="offset points",
                    ha="center", va="bottom",
                    bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"),
                    fontsize=10, color="black", weight="bold",
                    arrowprops=dict(arrowstyle="wedge,tail_width=0.5", facecolor="black"))

annot.set_visible(False)  