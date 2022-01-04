num = 1
count=0
while num != 0 :
    num = int(input('digite um número'))
    if 100 <= num <= 200 :
         count+=1
print(f'Um número entre 100 e 200 foi digitado {count} vezes')