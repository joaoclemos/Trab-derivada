from sympy import symbols, solve

variavel_x = symbols('x')
funcao = 2*variavel_x**3 + variavel_x**2 - 20*variavel_x + 4

intercepto_y = funcao.subs(variavel_x, 0)

interceptos_x = solve(funcao, variavel_x)

print("Intercepto com o eixo y:", (0, intercepto_y))
print("Interceptos com o eixo x:", [(x_val, 0) for x_val in interceptos_x])