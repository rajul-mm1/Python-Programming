from itertools import permutations

def permutate(G,Y,R):
    balls = 'G'*G + 'R'*R + 'Y'*Y
    unique_arrangement = set(permutations(balls))
    count = 0

    for arrang in unique_arrangement:
        if all(arrang[i] != arrang[i+1] for i in range(len(arrang)-1)):
            count += 1

    return count

G, Y, R = map(int, input().split())
print(permutate(G,Y,R))