def pattern(n=5):
    count=1
    for i in range(65,65+n):
        print(chr(i)*count)
        count+=1
pattern()
