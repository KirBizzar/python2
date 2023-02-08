print('Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")

print('Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")

print ('Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.')
print('Введите число')
n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')


print ('1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')
print ('2. Реализуйте алгоритм перемешивания списка')
n = int(input("Введите число"))
file_path = "file.txt"
with open(file_path,"w")as write_file:
    for i in range(randint(1,n)):
        write_file.write(f"{randint(0,n-1)}\n")
        
nums=[]3
for i in range(n):
    nums.append(randint(-n,n))
    
with open(file_path) as read_file:
    positions = read_file.read().split("\n")
    
prod_nums = 0
for index in positions:
    prod_nums *=nums[index]
    print(prod_nums)
    
def give_randint(min_num,max_num):
    difference = max_num - min_num
    seed = datetime.today().microsecond/(10**6)
    return min_num+int(difference*seed)

def fisher_yates_shuffle_algorithm(numvers:list):
    end = len(numbers)-1
    start = -1
    for i in range(end,start,-1):
        j=give_randint(0,i+1)
        numbers[i],numbers[j] = numbers[j],numbers[i]
        return numbers