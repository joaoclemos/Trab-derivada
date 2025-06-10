from sympy import symbols, diff, solve
import numpy as np
import matplotlib.pyplot as plt

variavel_x = symbols('x')
funcao = 2*variavel_x**3 + variavel_x**2 - 20*variavel_x + 4
primeira_derivada = diff(funcao, variavel_x)
segunda_derivada = diff(funcao, variavel_x, 2)

pontos_criticos = solve(primeira_derivada, variavel_x)
valores_criticos = [(float(p), float(funcao.subs(variavel_x, p))) for p in pontos_criticos]

pontos_inflexao = solve(segunda_derivada, variavel_x)
valores_inflexao = [(float(p), float(funcao.subs(variavel_x, p))) for p in pontos_inflexao]

intercepto_y = float(funcao.subs(variavel_x, 0))
interceptos_x = solve(funcao, variavel_x)
interceptos_x = [float(x) for x in interceptos_x if x.is_real]

valores_x = np.linspace(-5, 5, 400)
funcao_numerica = lambda t: 2*t**3 + t**2 - 20*t + 4
valores_y = funcao_numerica(valores_x)

plt.plot(valores_x, valores_y, label='f(x)')
for ponto in valores_criticos:
    plt.plot(ponto[0], ponto[1], 'ro', label='Ponto crítico' if ponto == valores_criticos[0] else "")
for ponto in valores_inflexao:
    plt.plot(ponto[0], ponto[1], 'go', label='Ponto de inflexão' if ponto == valores_inflexao[0] else "")
plt.plot(0, intercepto_y, 'bo', label='Intercepto y')
for x_int in interceptos_x:
    plt.plot(x_int, 0, 'bo', label='Intercepto x' if x_int == interceptos_x[0] else "")

plt.axhline(0, color='black', linestyle='--', alpha=0.5)
plt.axvline(0, color='black', linestyle='--', alpha=0.5)
plt.title('Gráfico de f(x) = 2x^3 + x^2 - 20x + 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()