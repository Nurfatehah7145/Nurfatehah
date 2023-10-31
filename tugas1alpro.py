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
    2.StuffedCrust Cheese : 11_818
    3.StuffedCrust sausage : 9_091
    4.Cheesy Bites : 13_636
    5.Crown Crust : 11_818
""")

harga_crust = 0
crust_pizza = int(input("pilih crust"). lower())
if crust_pizza == 1:
    crust_pizza = "pan"
    harga_crust = 0
elif crust_pizza == 2:
    crust_pizza = "StuffedCrust Cheese"
    harga_crust= 11_818
elif crust_pizza == 3:
    crust_pizza = "StuffedCrust Sausage"
    harga_crust = 9_091
elif crust_pizza == 4:
    crust_pizza = "Cheesy Bites"
    harga_crust = 13_636
elif crust_pizza == 5:
    crust_pizza = "Crown Crust"
    harga_crust = 11_818

#Ukuran pizza
print(
"""
    1.Personal : free
    2.Regular : 57_273
    3.Large : 89_728
""")
harga_ukuran = 0
ukuran_pizza =int(input("pilih ukuran pizza"). lower())
if ukuran_pizza == 1:
    harga_ukuran = 0
elif ukuran_pizza == 2:
    harga_ukuran =57_273
elif ukuran_pizza == 3:
    harga_ukuran = 89_728

#Tambahan cheese
harga_keju = 0
print("harga keju : 13_636")
tambahan_keju = input("tambahan keju (y/n): ")
if tambahan_keju == "y":
    harga_keju = 13_636
    tambahan_keju = True
elif tambahan_keju  == "n":
    tambahan_keju = False

#total harga
total_harga = (harga_pizza + harga_crust + harga_ukuran + harga_keju)
print("total yang harus dibayar adalah Rp" + str(total_harga))

print("Terima Kasih telah membeli Pizza di Pizza Hut")
print(f"Pesanan Anda Pizza dengan Topping {topping_pizza}")
print(f"Crust/Pinggiran {crust_pizza} dan")
print(f"ukuran pizza {ukuran_pizza}")
print(f"{'dengan' if tambahan_keju else 'tanpa'} Tambahan Keju")
print(f"Total Harga: Rp {total_harga}")
