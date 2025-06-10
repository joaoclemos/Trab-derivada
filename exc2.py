from sympy import symbols, diff, solve, S
import numpy as np
import matplotlib.pyplot as plt

variavel_x = symbols('x')
funcao = 2*variavel_x**3 + variavel_x**2 - 20*variavel_x + 4
primeira_derivada = diff(funcao, variavel_x)

pontos_criticos = solve(primeira_derivada, variavel_x)
pontos_criticos = [float(p) for p in pontos_criticos]
pontos_criticos.sort()

intervalos = [(-float('inf'), pontos_criticos[0]), 
              (pontos_criticos[0], pontos_criticos[1]), 
              (pontos_criticos[1], float('inf'))]
pontos_teste = [-5, (pontos_criticos[0] + pontos_criticos[1]) / 2, 5]

print("Análise dos intervalos:")
for i, intervalo in enumerate(intervalos):
    ponto_teste = pontos_teste[i]
    sinal = float(primeira_derivada.subs(variavel_x, ponto_teste))
    print(f"Intervalo {intervalo}: f'({ponto_teste}) = {sinal}")
    if sinal > 0:
        print(f"f é crescente em {intervalo}")
    elif sinal < 0:
        print(f"f é decrescente em {intervalo}")

valores_x = np.linspace(-5, 5, 400)
funcao_primeira_derivada = lambda t: 6*t**2 + 2*t - 20
valores_y = funcao_primeira_derivada(valores_x)

plt.plot(valores_x, valores_y, label="f'(x)")
plt.axhline(0, color='black', linestyle='--')
for ponto in pontos_criticos:
    plt.axvline(ponto, color='red', linestyle='--', alpha=0.5)
plt.title("Gráfico da primeira derivada")
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.grid(True)
plt.legend()
plt.show()