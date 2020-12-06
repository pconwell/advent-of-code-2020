import csv

# read csv
with open("./input.csv", newline='') as f:
    r = csv.reader(f, delimiter=',')
    d = list(r)

# clean up nested lists to make list flat
have = [int(i[0]) for i in d]

# sort the values (just to make it pretty)
have.sort()

# iterate over the "have" list and create a second
# "need" list with the values needed to make 2020
# for each of the have values
# example: have[0] + need[0] = 2020... have[10] + need[10] = 2020, etc
need = [2020-i for i in have]

# now compare both lists to see what values we *need*
# are in the *have* list. For example, if have[0] = 20 and
# need[0] = 2000, then we check have list for 2000 and vice versa.
answer = (set(have).intersection(need))

print(f"Answer is: {answer} = {list(answer)[0] * list(answer)[1]}")