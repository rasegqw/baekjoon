sen = input()

word = sen.split(' ')
null_count = 0
for i in word :
    if i =='':
        null_count += 1

for i in range(null_count):
    word.remove('')

print(f'{len(word)}')