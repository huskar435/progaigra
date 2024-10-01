input_data = open('input.txt','r')
data = input_data.read()
k = int(data)
a = 9
b = 9-k
j = str(k) + str(9) + str(b)
output_data = open('output.txt','w') 
output_data.write(j)
output_data.close()
input_data.close()