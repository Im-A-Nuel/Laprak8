data1='text1.txt'
handle1=open(data1, 'r')
data2='text2.txt'
handle2=open(data2, 'r')

new=''
for baris in handle1:
    for kata in baris:
        if kata.isalpha():
            new+=kata
        elif kata.isspace():
            new+=' '
    new=new.split()

newe=''
for word in handle2:
    for abjak in word:
        if abjak.isalpha():
            newe+=abjak
        elif abjak.isspace():
            newe+=' '
    newe=newe.split()
kosong=''
beda=''
for cas in new :
    if cas in newe:
        kosong=kosong+cas+' '
    elif cas not in newe:
        beda=beda+cas+' '

print(f'Sama : {kosong}')
print(f'Beda : {beda}')




handle1.close()
handle2.close()
