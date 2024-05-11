peso = float(input("Digite o peso da pesca em Kg:"))

exesso = peso - 50

multa =exesso * 4

print(f"Foram{exesso:.2f}Kg em exesso, logo, a multa é de R${multa:.2f}")