clothes = [int(x) for x in input().split(' ')]
capacity = int(input())

racks = 1
racks_capacity = 0

while clothes:
    current_cloth = clothes.pop()
    if racks_capacity + current_cloth <= capacity:
        racks_capacity += current_cloth
    else:
        racks += 1
        racks_capacity = 0
        racks_capacity += current_cloth

print(racks)