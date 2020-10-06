import re
from _collections import defaultdict

with open(r'C:\Users\zdravkob\Desktop\08-File-Handling-Lab-Resources\Words Count\words.txt', 'r') as words_input:
    words = words_input.read().split()
#print(words)

with open(r'C:\Users\zdravkob\Desktop\08-File-Handling-Lab-Resources\Words Count\text.txt', 'r') as text_input:
    text = text_input.read()

#print(text)

occurrence = (defaultdict(str))

for word in words:
    pattern = f'[\s|-]({word})[\s|.|,]'
    matches = re.findall(pattern, text, re.IGNORECASE)
    occurrence[word] = len(matches)

occurrence = dict(sorted(occurrence.items(), key=lambda x: x[1], reverse=True))

for key, value in occurrence.items():
    print(f'{key} - {value}')