data=[12,34,56,22,13,18,11,45]
temp=data[0]
for d in data:
    if(d>temp):
        temp=d
print("Biggest = ",temp)
