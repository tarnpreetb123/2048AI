output = [5, 6, 9, 8]
largest = max(output)
index = [i for i, j in enumerate(output) if j == largest]
print(index[0])

import math

print(output)

for i in range(len(output)):

    if output[i] != 0:
        output[i] = math.log(output[i], 2)

print(output)
print(max(output))