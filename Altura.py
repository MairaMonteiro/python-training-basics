c=1.40
cAno = 0.02
j=1.20
jAno=0.03
ano=0

while j <= c :
    c=c + (cAno * ano)
    j=j + (jAno * ano)
    ano+=1
print(f'serão necesários {ano} anos para que eles tenha a mesma altura')