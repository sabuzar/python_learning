max = 0
min = 100
grade_9=[50,49,40,39,30,29,0,19,10,9]
total_score = 0
for score in grade_9:
    total_score=score + total_score
    if  score < min:
        min = score
    if score > max:
        max = score
avg = total_score/len(grade_9)
print(avg)
print(max)
print(min)
