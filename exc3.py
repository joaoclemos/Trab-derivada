from sympy import symbols, diff, solve, S
import numpy as np
import matplotlib.pyplot as plt

variavel_x = symbols('x')
funcao = 2*variavel_x**3 + variavel_x**2 - 20*variavel_x + 4
segunda_derivada = diff(funcao, variavel_x, 2)

pontos_inflexao = solve(segunda_derivada, variavel_x)
pontos_inflexao = [float(p) for p in pontos_inflexao]

intervalos = [(-float('inf'), pontos_inflexao[0]), 
              (pontos_inflexao[0], float('inf'))]

print("Análise da concavidade:")
for intervalo in intervalos:
    ponto_teste = (intervalo[0] + intervalo[1]) / 2
    sinal = segunda_derivada.subs(variavel_x, ponto_teste)
    print(f"Intervalo {intervalo}: f''({ponto_teste}) = {sinal}")
    if sinal > 0:
        print(f"f é côncava para cima em {intervalo}")
    elif sinal < 0:
        print(f"f é côncava para baixo em {intervalo}")

print("\nPontos de inflexão:")
for ponto in pontos_inflexao:
    valor = funcao.subs(variavel_x, ponto)
    print(f"Ponto de inflexão em x = {ponto}, f({ponto}) = {valor}")

valores_x = np.linspace(-5, 5, 400)
funcao_segunda_derivada = lambda t: 12*t + 2
valores_y = funcao_segunda_derivada(valores_x)

plt.plot(valores_x, valores_y, label="f''(x)")
plt.axhline(0, color='black', linestyle='--')
for ponto in pontos_inflexao:
    plt.axvline(ponto, color='red', linestyle='--', alpha=0.5)
plt.title("Gráfico da segunda derivada")
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.grid(True)
plt.legend()
plt.show()