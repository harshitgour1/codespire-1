def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_instances(D, P):
    part_size = D // P
    count = 0
    
    for h in range(D):
        equivalent_hours = [(h + i * part_size) % D for i in range(P)]
        if all(is_prime(hour) for hour in equivalent_hours):
            count += 1
            
    return count

# Input reading
D, P = map(int, input().split())
print(count_prime_instances(D, P))
