s = input('введите текст ').split()
count = 0
for i in s:
    if i == 'python':
        count += 1
print(count)  