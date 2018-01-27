# The Standard Problem in simple writing goes like this:
#
#
# * You are given 2 eggs.
# * You have access to a 100-storey building.
# * Eggs can be very hard or very fragile means it may break if dropped from the first floor or may not even break if dropped from 100 th floor.Both eggs are identical.
# * You need to figure out the highest floor of a 100-storey building an egg can be dropped without breaking.
# * Now the question is how many drops you need to make. You are allowed to break 2 eggs in the process

N = 100
# the element of result is a tuple
# first elem of the tuple is the mininum number needed
# second elem of the tuple is the firs position to throw the egg
results = [(0, 0), (1, 1)]
for i in range(2, N + 1):
    minNum, minPos = N + 1, -1
    for j in range(1, i + 1):
        temp = 1 + max(j - 1, results[i - j][0])
        if temp < minNum:
            minNum, minPos = temp, j
    results.append((minNum, minPos))

for result in results:
    print (result)
