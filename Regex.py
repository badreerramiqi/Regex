import re
text = "P1 est un produit composé de P2 et P3 \nP2 est un produit élémentaire \nP5 est un produit composé de P1 et P4 \nP4 est un produit élémentaire \nP9 est un produit composé de P1, P6 et P4 \nP10 est un produit composé de P3 et P5 \nP11 est un produit composé de P5 et P3 "

x = re.findall(r"(P\d+ est un produit élémentaire)" , text)
for i in x :
    print(i)

p = re.findall(r"(P\d+ est un produit composé de P\d+, P\d+ et P\d)" , text)
for i in p :
    print(i)

v = re.findall(r"(P\d+ est un produit composé de P3 et P5)" , text)
v += re.findall(r"(P\d+ est un produit composé de P5 et P3)" , text)
for i in v :
    print(i)

r = re.findall(r"(P\d+ est un produit composé de P[^2])", text)
for i in r :
    print(i)

s = re.findall(r"(P9 est un produit composé de P\d+, P\d+ et P\d)", text)
for i in s :
    print(i)


 