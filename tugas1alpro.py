"""Nama Kelompok :
1. Zaki Fikri Ardiansyah 23091397149
2. Roland Savitar Herdiansyah 23091397145
3. Nur Fatehah 23091397160
"""

#Daftar Menu

print(
"""ter BBQ : 43_637
    2. Meat Mo
    1. Frankfurnsta : 43_637
    3. Super Supreme : 43_637
    4. Super Supreme Chicken : 43_637
""")

harga_pizza = 0
topping_pizza = int(input("pilih topping pizza: ").lower())
if topping_pizza == 1:
    topping_pizza = "frankfurter"
    harga_pizza = 43_637
elif topping_pizza == 2:
    topping_pizza = "Meat Monsta"
    harga_pizza = 43_637
elif topping_pizza == 3:
    topping_pizza = "Super Supreme"
    harga_pizza = 43_637
elif topping_pizza == 4:
    topping_pizza = "Super Supreme chicken"
    harga_pizza = 43_637

#Crust pizza
print(
"""
    1.Pan : free
