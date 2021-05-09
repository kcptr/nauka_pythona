samoloty = ['boeing', 'airbus']

print(samoloty[0])
print(samoloty[1])

for samolot in samoloty:
    print(samolot)

for idx in range( len(samoloty) ) :
    print('idx: ' + str(idx) + ' : ' + samoloty[idx])
