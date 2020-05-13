import unicodedata

s = "０６－６７８８－９７４８"
s0 = "06-6788-9748"
print(s)
s2 = unicodedata.normalize("NFKC",s)
print(s2)
print(unicodedata.normalize("NFKC",s0))

t ="　兵庫県尼崎市南初島町10-133"
t0 ="　兵庫県尼崎市南初島町10-133"
t2 = "　　長野森紙業株式会社"
t3 = "　　長野TEST Text　　"

print(t.strip())
print(t0)
print(t2.strip())
print(t3.strip())