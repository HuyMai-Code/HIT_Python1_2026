def average_score(scores):
    sum = 0
    for i in scores:
        sum += i
    return sum / len(scores)

def count_passed(scores, threshold = 5):
    cnt = 0
    for i in scores:
        if i >= threshold:
            cnt+=1
    return cnt

a = [8, 4, 9, 5]
print("Bài 2:")
print(f"Trung bình: {average_score(a):.2f}")
print(f"Số lượng với ngưỡng mặc định: {count_passed(a)}")
print(f"Số lượng với ngưỡng 8: {count_passed(a, 8)}")
print("___________________________________")