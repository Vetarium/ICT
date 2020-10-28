n = int(input())
res = 0
polyheds = {'Tetrahedron': 4,
            'Cube': 6,
            'Octahedron': 8,
            'Dodecahedron': 12,
            'Icosahedron': 20}

for i in range(n):
    res += polyheds[input()]
print(res)