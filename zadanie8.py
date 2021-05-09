samochody = ['syrena', 'polonez']

print(samochody[0])
print(samochody[1])

for samochod in samochody:
    print(samochod)

for idx in range( len(samochody) ) :
    print('idx: ' + str(idx) + ' : ' + samochody[idx])
