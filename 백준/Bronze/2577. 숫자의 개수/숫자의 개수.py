#2577

sum = 1

for i in range(3):
    a = int(input())
    sum*= a

string_sum = str(sum)
string_sum = list(map(int,string_sum))
#print(string_sum)

for i in range(10):
    print(string_sum.count(i))
