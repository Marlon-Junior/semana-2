# Semana 2 – Avançando com Python: Listas, Laços e Lógica

## Desafios realizados:

### 1. Lista de Compras Interativa  
O programa solicita que o usuário insira 5 itens para uma lista de compras. Cada item é validado para conter apenas letras. Ao final, o programa exibe:
- A lista completa de compras  
- O primeiro item da lista  
- O último item da lista  
- O total de itens na lista  

---

## Aprendizados da semana:

- Criação e manipulação de **listas** em Python  
- Uso de laços de repetição com `for` e `while`  
- Validação de dados com `try/except` e `raise`  
- Métodos de string como `.isalpha()` para garantir entradas válidas  
- Acesso a elementos da lista por índice (`[0]`, `[-1]`)  
- Uso da função `len()` para contar itens da lista  
- Reforço de operadores lógicos e blocos de controle

---

## Destaque da semana:

### Validação de itens com `.isalpha()`  
Assim como fiz com nomes na Semana 1, agora usei a validação para garantir que cada item da lista de compras contenha apenas letras. Exemplo:

```python
while True:
    item = input("Adicione um item: ")
    if not item.isalpha():
        print("Item inválido. Digite apenas letras.")
        continue
    lista.append(item)
    break
