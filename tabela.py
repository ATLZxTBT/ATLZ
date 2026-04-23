import matplotlib.pyplot as plt
ano = ["Jan","Fev","Mar","Abr","Mai","Jun","Jul","Ago","Set","Out","Nov","Dez"]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
y = []
total = 0
for i in range(12):
    package = int(input(f"Entregas realizadas no mês de \033[1;32m{ano[i]}: \033[0m"))
    total += package
    y.append(package)
media = total / 12

plt.title("|| VENDAS DE 2026 ||")
plt.bar(ano, y)
plt.show()