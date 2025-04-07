total_score = [1,22222,3,5,8,99,30,10,25,34,57,8,90,100,77,29,64,101,200]
print(max(total_score))
# find the highest number in the list
max_score = 0
for score in total_score:
    if max_score < score:
        max_score = score
# do the same thing
print(max_score)