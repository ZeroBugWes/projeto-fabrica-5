pais_a = 80000
taxa_a= 3/100

pais_b = 200000
taxa_b= 1.5/100

anos = 0

while pais_a < pais_b:
    pais_a = pais_a *  (1 + taxa_a )
    pais_b = pais_b *  (1 + taxa_b )
    anos = anos + 1

print(f"Serâo nescessarios {anos} para que o Pais A passe ou iguale a o Pais B")
print(f"Populaçao final do Pais A: {round(pais_a)} habitantes")
print(f"Populaçao final do Pais B: {round(pais_b)} habitantes")