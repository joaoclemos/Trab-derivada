from sympy import symbols, diff, solve

variavel_x = symbols('x')
funcao = 2*variavel_x**3 + variavel_x**2 - 20*variavel_x + 4

primeira_derivada = diff(funcao, variavel_x)

pontos_criticos = solve(primeira_derivada, variavel_x)

valores_criticos = [(ponto, funcao.subs(variavel_x, ponto)) for ponto in pontos_criticos]

print("Primeira derivada:", primeira_derivada)
print("Pontos críticos (x):", pontos_criticos)
print("Valores de f nos pontos críticos:", valores_criticos)