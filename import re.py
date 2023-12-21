import re
text = "P1 est un produit composé de P2 et P3 \nP2 est un produit élémentaire \nP5 est un produit composé de P1 et P4 \nP4 est un produit élémentaire \nP9 est un produit composé de P1, P6 et P4 \nP10 est un produit composé de P3 et P5 \nP11 est un produit composé de P5 et P3 "

x = re.findall(r"(P\d+ est un produit élémentaire)", text)
print(x)

p = re.findall(r"(P\d+ est un produit composé de P\d+, P\d+ et P\d)", text)
print(p)

v = re.findall(r"(P\d+ est un produit composé de P3 et P5)", text)
v += re.findall(r"(P\d+ est un produit composé de P5 et P3)", text)
print(v)

r = re.findall(r"(P\d+ est un produit composé de P[^2])", text)
print(r)

s = re.findall(r"(P9 est un produit composé de P\d+, P\d+ et P\d)", text)
print(s)