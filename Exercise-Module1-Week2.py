#Exercise 1: Finding minimum in the sub_string having k as len
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
result = []
def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        result.append(max(num_list[i:i+k]))
    return result
# print(max_kernel(num_list, k))


#Exercise 2: Counting char in a string
string = 'Happiness'
def char_count(string):
    _dict = {}
    for char in string:
        _dict[char] = _dict.get(char, 0) + 1
    return _dict
# print(char_count('smiles'))

#Exercise 3: 
# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
with open('/content/P1_data.txt', 'r') as file:
  line = file.readlines()
  words = line.split()
  dict = {}
  for word in words:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1


#Exercise 4: Calculating Levenshtein distance
source = 'yu'
target = 'you'
def leven_distance(source, target):
    matrix = [[0 for _ in range(len(target) + 1)] for _ in range(len(source) + 1)]
    for i in range(len(source) + 1):
        matrix[i][0] = i
    for j in range(len(target) + 1):
        matrix[0][j] = j
    for i in range(1,len(source)+1):
        for j in range(1,len(target)+1):
            substring = [matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]]
            if source[i-1] != target[j-1]:
                matrix[i][j] = min(substring)+1
            else:
                matrix[i][j] = min(substring)

    return matrix[len(source)][len(target)]

# print(leven_distance("hola", "hello"))

#Trắc nghiệm:
#Câu 5:
def check_the_number(N):
    list_of_numbers = []
    result = True
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        result = True
    else:
        result = False
    return result
N = 7
# print(check_the_number(7))

#Câu 6:
def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max: 
            result.append(max)
        else:
            result.append(i)
    return result
my_list = [5, 2, 5, 0, 1]
my_list = [5 , 2 , 5 , 0 , 1]
max = 1
min = 0
assert my_function (max = max , min = min , data = my_list ) == [1 , 1 , 1 , 0 , 1]
my_list = [10 , 2 , 5 , 0 , 1]
max = 2
min = 1
#print ( my_function (max = max , min = min , data = my_list ) )

#Câu 7:
def my_function(x, y):
    x.extend(y)
    return x
list_num1 = ['a', 2 , 5]
list_num2 = [1 , 1]
list_num3 = [0 , 0]
#assert my_function ( list_num1 , my_function ( list_num2 , list_num3 ) ) == ['a', 2 , 5 , 1 , 1 ,]
list_num1 = [1 , 2]
list_num2 = [3 , 4]
list_num3 = [0 , 0]
#print ( my_function ( list_num1 , my_function ( list_num2 , list_num3 ) ) )

#Câu 8: 
def my_function(n):
    minimum = min(n)
    return minimum

# Kiểm tra với danh sách đầu tiên
my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100 

# Kiểm tra với danh sách thứ hai
my_list = [1, 2, 3, -1]
#print(my_function(my_list))  

#Câu 10:
def My_function(intergers, number):
    results = []
    for value in intergers:
        if value == number:
            result = True
            results.append(result)
        else:
            result = False
            results.append(result)
    return any(results)
my_list = [1 , 2 , 3 , 4]
#print ( My_function ( my_list , 2) )

#Câu 11:
def my_function_mean(list_nums):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)
#print(my_function_mean([0, 1, 2]))

#Câu 12:
def my_funct_divide3(data):
    var = []
    for i in data:
        if i%3 == 0:
            var.append(i)
    return var
#print(my_funct_divide3([1,2,3,5,6]))

#Câu 13:
def factorial(y):
    if y == 0:
        return 0
    elif y == 1:
        return 1
    elif y >= 1 and type(y) == int:
        for i in range(1, y):
            y = y*i
    else:
        print("Math error")
    return y

#print(factorial(4))
#Câu 14:
def reverse_the_string(x):
    length = len(x) - 1
    reversing = []
    for i in range(length, -1, -1):
        reversing.append(x[i])
    return ''.join(reversing)
#print(reverse_the_string('apricot'))

#Câu 15:
def function_helper(x):
    for value in x:
        if value > 0:
            return 'T'
        else:
            return 'F'
def my_function_helping(data):
    res = [function_helper(x) for x in data]
    return res
data = [2, 3, 5, -1]
print(my_function_helping(data))

#Câu 16:
def helper_function(x, data):
    for i in data:
        if x == i:
            return 0
    return 1
def me_function(data):
    res = []
    for i in data:
        if helper_function(i, res):
            res.append()
    return res
print(me_function([9,9,8,1,1]))

#Exercise 1: Finding minimum in the sub_string having k as len
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
result = []
def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        result.append(max(num_list[i:i+k]))
    return result
# print(max_kernel(num_list, k))


#Exercise 2: Counting char in a string
string = 'Happiness'
def char_count(string):
    _dict = {}
    for char in string:
        _dict[char] = _dict.get(char, 0) + 1
    return _dict
# print(char_count('smiles'))

#Exercise 3: 
# !gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
with open('/content/P1_data.txt', 'r') as file:
  line = file.readlines()
  words = line.split()
  dict = {}
  for word in words:
    if word in dict:
      dict[word] += 1
    else:
      dict[word] = 1


#Exercise 4: Calculating Levenshtein distance
source = 'yu'
target = 'you'
def leven_distance(source, target):
    matrix = [[0 for _ in range(len(target) + 1)] for _ in range(len(source) + 1)]
    for i in range(len(source) + 1):
        matrix[i][0] = i
    for j in range(len(target) + 1):
        matrix[0][j] = j
    for i in range(1,len(source)+1):
        for j in range(1,len(target)+1):
            substring = [matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]]
            if source[i-1] != target[j-1]:
                matrix[i][j] = min(substring)+1
            else:
                matrix[i][j] = min(substring)

    return matrix[len(source)][len(target)]

# print(leven_distance("hola", "hello"))

#Trắc nghiệm:
#Câu 5:
def check_the_number(N):
    list_of_numbers = []
    result = True
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        result = True
    else:
        result = False
    return result
N = 7
# print(check_the_number(7))

#Câu 6:
def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max: 
            result.append(max)
        else:
            result.append(i)
    return result
my_list = [5, 2, 5, 0, 1]
my_list = [5 , 2 , 5 , 0 , 1]
max = 1
min = 0
assert my_function (max = max , min = min , data = my_list ) == [1 , 1 , 1 , 0 , 1]
my_list = [10 , 2 , 5 , 0 , 1]
max = 2
min = 1
#print ( my_function (max = max , min = min , data = my_list ) )

#Câu 7:
def my_function(x, y):
    x.extend(y)
    return x
list_num1 = ['a', 2 , 5]
list_num2 = [1 , 1]
list_num3 = [0 , 0]
#assert my_function ( list_num1 , my_function ( list_num2 , list_num3 ) ) == ['a', 2 , 5 , 1 , 1 ,]
list_num1 = [1 , 2]
list_num2 = [3 , 4]
list_num3 = [0 , 0]
#print ( my_function ( list_num1 , my_function ( list_num2 , list_num3 ) ) )

#Câu 8: 
def my_function(n):
    minimum = min(n)
    return minimum

# Kiểm tra với danh sách đầu tiên
my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100 

# Kiểm tra với danh sách thứ hai
my_list = [1, 2, 3, -1]
#print(my_function(my_list))  

#Câu 10:
def My_function(intergers, number):
    results = []
    for value in intergers:
        if value == number:
            result = True
            results.append(result)
        else:
            result = False
            results.append(result)
    return any(results)
my_list = [1 , 2 , 3 , 4]
#print ( My_function ( my_list , 2) )

#Câu 11:
def my_function_mean(list_nums):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)
#print(my_function_mean([0, 1, 2]))

#Câu 12:
def my_funct_divide3(data):
    var = []
    for i in data:
        if i%3 == 0:
            var.append(i)
    return var
#print(my_funct_divide3([1,2,3,5,6]))

#Câu 13:
def factorial(y):
    if y == 0:
        return 0
    elif y == 1:
        return 1
    elif y >= 1 and type(y) == int:
        for i in range(1, y):
            y = y*i
    else:
        print("Math error")
    return y

#print(factorial(4))
#Câu 14:
def reverse_the_string(x):
    length = len(x) - 1
    reversing = []
    for i in range(length, -1, -1):
        reversing.append(x[i])
    return ''.join(reversing)
#print(reverse_the_string('apricot'))

#Câu 15:
def function_helper(x):
    for value in x:
        if value > 0:
            return 'T'
        else:
            return 'F'
def my_function_helping(data):
    res = [function_helper(x) for x in data]
    return res
data = [2, 3, 5, -1]
print(my_function_helping(data))

#Câu 16:
def helper_function(x, data):
    for i in data:
        if x == i:
            return 0
    return 1
def me_function(data):
    res = []
    for i in data:
        if helper_function(i, res):
            res.append()
    return res
print(me_function([9,9,8,1,1]))
















    
    


