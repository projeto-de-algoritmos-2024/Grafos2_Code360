def supplyWater(n, k, wells, pipes):
	
	floresta = list(range(n+1)) # 

	def find(x):
		if x != floresta[x]:
			floresta[x] = find(floresta[x])

		return floresta[x]
	
	def union(x,y):
		no_1 = find(x)
		no_2 = find(y)

		if no_1 != no_2:
			floresta[no_2] = no_1
			return True
			
		return False

	arestas = []

	for u,v,c in pipes:
		arestas.append((c,u-1,v-1))

	for i,c in enumerate(wells):
		arestas.append((c,i,n))
		
	arestas.sort()
	resposta = 0

	for c,u,v in arestas:
		if union(u,v):
			resposta += c
		
	return resposta

	pass