data = [387,350,355,361,378,424,323,397,404,373,376,372,364,368,365,326,339,394,391,369,378,358,352,408,332,399]
#dataArray = data.split(" ")

zeroes = 0
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0
sevens = 0
eights = 0
#print (dataArray)
#for element in dataArray:
#    if element == '0':
#        zeroes += 1
#    if element == '1':
#        ones += 1
#    if element == '2':
#        twos += 1
#    if element == '3':
#        threes += 1
#    if element == '4':
#        fours += 1
#    if element == '5':
#        fives += 1
#    if element == '6':
#        sixes += 1
#    if element == '7':
#        sevens += 1
#    if element == '8':
#        eights += 1
#total = zeroes + ones + twos + threes + fours + fives + sixes + sevens + eights
#print("0| " + str(zeroes) + '| rf = '+ str(float(zeroes)/float(total)))
#print("1| " + str(ones)+ '| rf = '+ str(float(ones)/float(total)))
#print("2| " + str(twos)+ '| rf = '+ str(float(twos)/float(total)))
#print("3| " + str(threes)+ '| rf = '+ str(float(threes)/float(total)))
#print("4| " + str(fours)+ '| rf = '+ str(float(fours)/float(total)))
#print("5| " + str(fives)+ '| rf = '+ str(float(fives)/float(total)))
#print("6| " + str(sixes)+ '| rf = '+ str(float(sixes)/float(total)))
#print("7| " + str(sevens)+ '| rf = '+ str(float(sevens)/float(total)))
#print("8| " + str(eights)+ '| rf = '+ str(float(eights)/float(total)))

#print('total|' + str(total) )
data.sort()
for element in data:
    print(element)
    zeroes += 1
print('total numbers: ' + str(zeroes))
