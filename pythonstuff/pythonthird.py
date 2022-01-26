import carandhuman

conk = carandhuman.Audi(58.4, 140.6)
print(conk)
conk.accelerate(48)
print(conk)
print(f"{conk:km}")
conk.cartype = "yonk"
print(conk)
if conk.canMassage:
    print("your vehicle can massage you")
print(conk.canMassage)
