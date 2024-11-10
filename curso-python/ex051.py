primeiro = int(input("primeiro termo"))
rz = int(input("digite a Razão :"))
decimo = primeiro + (10 - 1) * rz
for rz in range(primeiro, decimo + rz, rz):
  print("{}".format(rz), end=" > ")
print("Fim")