while True:
    data = input().split()
    name = data[0]
    age = int(data[1])
    weight = int(data[2])
    
    if name == "#" and age == 0 and weight == 0:
        break
    
    if age > 17 or weight >= 80:
        print(f"{name} Senior")
    else:
        print(f"{name} Junior")
