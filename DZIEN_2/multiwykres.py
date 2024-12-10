import numpy as np
import matplotlib.pyplot as plt

#przygotowanie danych
osoby = ("Anna","Piotr","Olga","Roman")
informacje = {
    'wiek':(34,56,23,45),
    'waga':(56.8,89.6,60.3,105.6),
    'wzrost':(162,178,170,189)
}

x = np.arange(len(osoby))
width = 0.25
multiplier = 0

fig,ax = plt.subplots(constrained_layout=True)
for attribute,measurement in informacje.items():
    offset = width*multiplier
    rects = ax.bar(x+offset,measurement,width,label=attribute)
    ax.bar_label(rects,padding=5)
    multiplier += 1

ax.set_ylabel("cecha")
ax.set_title("wybrane informacje na temat osób...")
ax.set_xticks(x+width,osoby)
ax.legend(loc='upper left',ncols=3)
ax.set_ylim(0,200)
plt.savefig("wykresmulti.png",dpi=300)

plt.show()

