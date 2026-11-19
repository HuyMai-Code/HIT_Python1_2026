def rank_students(score_by_name):
    return sorted(score_by_name.items(), key = lambda i : (-i[1],i[0]))

score_by_name = {"Minh": 9, "Lan": 7, "An": 9, "Vy": 5}
print("Bài 3:")
print(dict(rank_students(score_by_name)))
print("___________________________________")