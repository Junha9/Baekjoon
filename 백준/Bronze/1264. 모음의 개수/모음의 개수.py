while True:
    line = input()
    if line == '#':
        break
    count = 0
    for vowel in 'aeiouAEIOU':
        count += line.count(vowel)
    print(count)