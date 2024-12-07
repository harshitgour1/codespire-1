def treasure_hunt(n, values, T):
    seen = set()
    for value in values:
        complement = T - value
        if complement in seen:
            return "MATCH"
        seen.add(value)
    return "NO MATCH"

# Input reading
n = int(input())
values = list(map(int, input().split()))
T = int(input())

# Output result
print(treasure_hunt(n, values, T))
