i=int(input())
gohyaku = i // 500
go = (i % 500) // 5
print(int(gohyaku*1000+go*5))