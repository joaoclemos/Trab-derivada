from sympy import symbols, diff, solve, limit, oo
import numpy as np
import matplotlib.pyplot as plt

variavel_x = symbols('x')
funcao = (2*variavel_x - 5) / (variavel_x + 3)

dominio_excecao = solve(variavel_x + 3, variavel_x)
print("a) Domínio: Todos os reais exceto x =", dominio_excecao)

primeira_derivada = diff(funcao, variavel_x)
pontos_criticos = solve(primeira_derivada, variavel_x)
valores_criticos = [(float(p), float(funcao.subs(variavel_x, p))) for p in pontos_criticos if p.is_real]
print("b) Pontos críticos:", valores_criticos)

intervalos = [(-float('inf'), -3), (-3, float('inf'))]
pontos_teste = [-5, 5]
print("c) Análise de crescimento/decrescimento:")
for i, intervalo in enumerate(intervalos):
    ponto_teste = pontos_teste[i]
    sinal = float(primeira_derivada.subs(variavel_x, ponto_teste))
    print(f"Intervalo {intervalo}: f'({ponto_teste}) = {sinal}")
    if sinal > 0:
        print(f"f é crescente em {intervalo}")
    elif sinal < 0:
        print(f"f é decrescente em {intervalo}")

print("d) Máximos e mínimos locais:", "Nenhum, pois f'(x) nunca é zero" if not valores_criticos else valores_criticos)

segunda_derivada = diff(funcao, variavel_x, 2)
pontos_inflexao = solve(segunda_derivada, variavel_x)
print("e) Análise da concavidade:")
for i, intervalo in enumerate(intervalos):
    ponto_teste = pontos_teste[i]
    sinal = float(segunda_derivada.subs(variavel_x, ponto_teste))
    print(f"Intervalo {intervalo}: f''({ponto_teste}) = {sinal}")
    if sinal > 0:
        print(f"f é côncava para cima em {intervalo}")
    elif sinal < 0:
        print(f"f é côncava para baixo em {intervalo}")
print("Pontos de inflexão:", "Nenhum, pois f''(x) nunca é zero" if not pontos_inflexao else pontos_inflexao)

assintota_vertical = dominio_excecao[0]
limite_positivo = limit(funcao, variavel_x, oo)
limite_negativo = limit(funcao, variavel_x, -oo)
assintota_horizontal = limite_positivo if limite_positivo == limite_negativo else None
print("f) Assíntotas:")
print(f"Assíntota vertical: x = {assintota_vertical}")
print(f"Assíntota horizontal: y = {assintota_horizontal}")

intercepto_y = funcao.subs(variavel_x, 0)
interceptos_x = solve(funcao, variavel_x)
print("g) Interceptos:")
print(f"Intercepto y: (0, {intercepto_y})")
print(f"Interceptos x: {[(x_val, 0) for x_val in interceptos_x]}")

valores_x = np.concatenate([np.linspace(-10, -3.1, 200), np.linspace(-2.9, 10, 200)])
funcao_numerica = lambda t: (2*t - 5) / (t + 3)
valores_y = funcao_numerica(valores_x)

plt.plot(valores_x, valores_y, label='f(x)')
plt.axvline(float(assintota_vertical), color='red', linestyle='--', alpha=0.5, label='Assíntota vertical')
plt.axhline(float(assintota_horizontal), color='green', linestyle='--', alpha=0.5, label='Assíntota horizontal')
plt.plot(0, float(intercepto_y), 'bo', label='Intercepto y')
for x_int in interceptos_x:
    plt.plot(float(x_int), 0, 'bo', label='Intercepto x' if x_int == interceptos_x[0] else "")

plt.title('Gráfico de f(x) = (2x - 5)/(x + 3)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.ylim(-10, 10)
plt.show()