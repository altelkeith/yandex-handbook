text = []
for i in range(3):
    text.append(str(input()))

text_str_min = ""

for i in range(3):
    if "зайка" in text[i]:
        text_str_min = text[i]
        break

for i in range(3):
    if "зайка" in text[i] and text[i] < text_str_min:
        text_str_min = text[i]

print(text_str_min, len(text_str_min))