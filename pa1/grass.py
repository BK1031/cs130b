"""
n sprinklers are installed in a horizontal strip of grass l meters long and w meters wide.
Each sprinkler is installed at the horizontal center line of the strip. For each sprinkler
we are given its position as the distance from the left end of the center line and its
radius of operation.

What is the minimum number of sprinklers to turn on in order to water the entire strip of grass?

Input
Input consists of at most 35 cases. The first line for each case contains integer numbers n, l,
and w with 1 <= n <= 10000, 1 <= l <= 10^7, and 1 <= w <= 100. The next n lines contain two
integers giving the position x (0 <= x <= l) and radius of operation r (1 <= r <= 1000) of a sprinkler.

The picture above illustrates the first case from the sample input.

Output
For each test case output the minimum number of sprinklers needed to water the entire strip of grass.
If it is impossible to water the entire strip output -1.
"""

def check_gaps(chosen, l):
    grass = {}
    for i in range (0, l):
        grass[i] = False
    
    for i in range(len(chosen)):
        for j in range(chosen[i][0] - chosen[i][1], chosen[i][0] + chosen[i][1]):
            if j < 0 or j > l:
                continue
            else:
                grass[j] = True

    # print(grass)
    for i in range(0, l):
        if not grass[i]:
            return False
    
    return True

def check_overlap(chosen):
    for i in range(len(chosen) - 1):
        right = chosen[i][0] + chosen[i][1]
        left = chosen[i + 1][0] - chosen[i + 1][1]
        if right <= left:
            return False
    return True

def solve(n, l, w):
    sprinklers = []
    cursor = 0
    chosen = []

    for _ in range(n):
        x, r = map(int, input().split())
        sprinklers.append((x, r))

    sprinklers.sort(key=lambda x: x[0])
    # print(sprinklers)

    for i in range(n):
        if sprinklers[i][1] < w / 2:
            continue
        
        if sprinklers[i][0] - sprinklers[i][1] <= cursor and sprinklers[i][0] + sprinklers[i][1] > cursor:
            # check if this sprinkler is better than the last one
            if len(chosen) > 0 and chosen[-1][0] - chosen[-1][1] > sprinklers[i][0] - sprinklers[i][1]:
                chosen.pop()

            if len(chosen) > 1 and chosen[-2][0] + chosen[-2][1] > sprinklers[i][0] - sprinklers[i][1]:
                chosen.pop()

            chosen.append(sprinklers[i])
            cursor = sprinklers[i][0] + sprinklers[i][1]
    
    # print(f"cursor: {cursor}")
    # print(f"chosen: {chosen}")
    if cursor < l:
        print(-1)
    elif not check_overlap(chosen):
        print(-1)
    else:        
        print(len(chosen))

for _ in range(3):
    n, l, w = map(int, input().split())
    solve(n, l, w)
