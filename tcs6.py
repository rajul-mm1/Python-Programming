time = int(input())
entry = list(map(int, input().split()))
leaving = list(map(int, input().split()))

current_guests = 0
max_guests = 0

for i in range(time):
    current_guests += entry[i] - leaving[i]
    max_guests = max(max_guests, current_guests)

print(max_guests)
