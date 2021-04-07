with open('file1.txt', 'r+') as f:
    lines = f.read()
    words = lines.split()
    print('No of words is', len(words))
