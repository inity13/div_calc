amount_in_wallet = float(input("""Kokonaissumma?
"""))
a_divs = float((amount_in_wallet / 10) * 2)

#print("DEBUG:A divs" + str(a_divs))

j_divs = float((amount_in_wallet / 10) * 4)
k_divs = float((amount_in_wallet / 10) * 4)
print("*********************************")
print("A osuus: " + str(a_divs))
print("J osuus: " + str(j_divs))
print("K osuus: " + str( k_divs))
print("*********************************")
print("*********************************")
print("Ilmoitettu maara: " + str(amount_in_wallet))
print("Osinkojen summa: " + str(a_divs + j_divs + k_divs))
