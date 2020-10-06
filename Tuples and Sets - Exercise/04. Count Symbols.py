from _collections import defaultdict

text = input()
char_times = defaultdict(int)

for char in text:
    char_times[char] += 1

char_times = sorted(char_times.items(), key=lambda x: x[0])
for k,v in char_times:
    print(f'{k}: {v} time/s')