#Longoria Bunoust Giovanni Javier    Grupo: 3CV4

def ruta_costo_minimo(cost, M, N):
    # Crear matriz dp
    dp = [[float('inf')] * (N+1) for _ in range(M+1)]
    dp[0][0] = cost[0][0]
    
    # Rellenar dp de forma iterativa
    for i in range(1, M+1):
        for j in range(1, N+1):
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + cost[i][j]
    
    return dp[M][N]

# Ejemplo de uso
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]

M = 2
N = 2

costo_minimo = ruta_costo_minimo(cost, M, N)
print("Costo mínimo de la ruta:", costo_minimo)
