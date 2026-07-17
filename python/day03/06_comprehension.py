#1
numbers = [1,2,3,4,5]
numbers_cube = [x**3 for x in numbers]
print(numbers_cube)

#2
numbers_thr_times = [x for x in range(1,21) if x%3 == 0]
print(numbers_thr_times)

#3
new_numbers = [-5,3,-2,7,0]
numbers_only_positive = [x if x>=0 else 0 for x in new_numbers]
print(numbers_only_positive)

#4
dict_by_compre = {x: x**3 for x in range(1,6)}
print(dict_by_compre)