lista_compras = []

for i in range(5):
    while True:
        try:
            compras = input("Adicione um item: ")
            if not compras.isalpha():
                raise ValueError("Por favor, digite apenas letras. ")
            lista_compras.append(compras)
            break
        except ValueError as e:
            print(e)

print("\nLista completa de compras:", lista_compras)
print("Primeiro item da lista:", lista_compras[0])
print("Último item da lista:", lista_compras[-1])
print("Total de itens na lista:", len(lista_compras))
