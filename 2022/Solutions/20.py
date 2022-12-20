input = [(int(num), i) for i, num in enumerate(open("2022/Input/20.txt").readlines())]
n = len(input)
print("len input/number distinct", n, len(set(input)))
print(input)
# is_at = list(range(n))

def mix(order, numbers):
    k, i = next((k, i) for i,k in enumerate(numbers) if k[1] == order)
    
    return numbers[:(i + k[0] + 1) % n] + [k] + numbers[i + k[0] % n:]
    
    
    print(k, i)


for i in range(n):
    mix(i, input)
    


