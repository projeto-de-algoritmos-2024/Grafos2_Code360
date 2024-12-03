class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges = [(ai, bi, weight, i) for i, (ai, bi, weight) in enumerate(edges)]

        def prim_force_edge(force_edge=None, exclude_edge=None):
            grafo = defaultdict(list)
            for ai, bi, weight, i in edges:
                if exclude_edge is not None and i == exclude_edge:
                    continue
                grafo[ai].append((weight, bi, i))
                grafo[bi].append((weight, ai, i))
            
            mst_weight = 0
            visited = set()
            min_heap = []

            if force_edge:
                mst_weight += force_edge[2]
                visited.add(force_edge[0])
                visited.add(force_edge[1])
                for neighbor in grafo[force_edge[0]]:
                    if neighbor[1] not in visited:
                        heappush(min_heap, neighbor)
                for neighbor in grafo[force_edge[1]]:
                    if neighbor[1] not in visited:
                        heappush(min_heap, neighbor)
            else:
                visited.add(0)
                for neighbor in grafo[0]:
                    heappush(min_heap, neighbor)

            while min_heap and len(visited) < n:
                weight, node, edge_i = heappop(min_heap)
                if node in visited:
                    continue
                visited.add(node)
                mst_weight += weight
                for neighbor in grafo[node]:
                    if neighbor[1] not in visited:
                        heappush(min_heap, neighbor)

            return mst_weight if len(visited) == n else float('inf')

        # mst peso original
        original_mst_weight = prim_force_edge()

        critica, pseudo_critica = [], []
        for ai, bi, weight, i in edges:
            # critica
            if prim_force_edge(exclude_edge=i) > original_mst_weight:
                critica.append(i)
            # pseudo-critica
            elif prim_force_edge(force_edge=(ai, bi, weight)) == original_mst_weight:
                pseudo_critica.append(i)

        return [critica, pseudo_critica]