# ==========================
# Practice Day 03
# ==========================

# 1. 학생 이름 리스트
students = ["Kim", "Lee", "Park", "Choi", "Kim"]

print("학생 목록")
print(students)
print()


# 2. Set으로 중복 제거
unique_students = set(students)

print("중복 제거된 학생 목록")
print(unique_students)
print()


# 3. Dictionary로 학생 점수 저장
scores = {
    "Kim": 95,
    "Lee": 88,
    "Park": 76,
    "Choi": 91
}

print("학생 점수")
for name, score in scores.items():
    print(f"{name}: {score}")
print()


# 4. 모든 학생에게 5점 추가
bonus_scores = {
    name: score + 5
    for name, score in scores.items()
}

print("보너스 적용 점수")
print(bonus_scores)
print()


# 5. 90점 이상인 학생 찾기
passed_students = [
    name
    for name, score in bonus_scores.items()
    if score >= 90
]

print("90점 이상인 학생")
print(passed_students)
print()


# 6. 최고 점수 찾기
best_score = max(bonus_scores.values())

print("최고 점수")
print(best_score)
print()


# 7. 최고 득점자 모두 찾기
best_students = [
    name
    for name, score in bonus_scores.items()
    if score == best_score
]

print("최고 득점자")
print(best_students)
print()


# 8. 최고 득점자의 정보를 튜플 리스트로 저장
best_student_info = [
    (name, best_score)
    for name in best_students
]

print("최고 득점자 정보")
print(best_student_info)
print()


# 튜플 언패킹
for name, score in best_student_info:
    print(f"{name}: {score}")