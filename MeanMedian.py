data = []

total = 0
count = 0
data.sort()
    
total = 0
for element in data:
    total += element 
print(data)
mean = (total / len(data))
print (total)
print ("mean: " + str(mean))
# median even
median = (data[int((len(data) / 2))] + data[int((len(data) / 2) - 1)]) /2
# median odd
#median = data[int((len(data) / 2))]

print ("median: " + str(median))

#data.remove(data[0])
#data.remove(data[len(data)-1])

total = 0
#for element in data:
#    total += element

#print (total)
#print ("trimmed mean: " + str(total / len(data)))
#data.sort()
#median = data[int((len(data) / 2)) + 1]

#print ("trimmed median: " + str(median))

print('')
for element in data:
    print('x|' + str(element) + ' x-mean|' + str(element - mean) )
xsum = 0
x2sum = 0

for element in data:
    xsum += element
    x2sum += (element - mean) * (element - mean)
print('x| ' + str(xsum) + ' x2| ' + str(x2sum))
