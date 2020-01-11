def funkcja(data_text):
    print({"length":len(data_text),"letters":list(data_text),"big_letters":data_text.upper(),
           "small_letters":data_text.lower()})
funkcja("zdaniedosprawdzenia")