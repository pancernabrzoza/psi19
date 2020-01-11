def funkcja(stopnie,temperature_type):
    if temperature_type == 'f':
        f=(stopnie*1.8)+32
        odp=("fahrenheity = {}").format(f)
    elif temperature_type == 'r':
        r = (stopnie + 273.15) * 1.8
        odp = ("rakine = {}").format(r)
    elif temperature_type == 'k':
        k = stopnie + 273.15
        odp = ("kelviny = {}").format(k)
    print(odp)
funkcja(1,"k")

