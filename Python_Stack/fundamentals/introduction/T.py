morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
              ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
words = ["gin", "zen", "gig", "msg"]
unique_code = []

for word in words:
    temp_code = ""
    for letter in word:
        temp_code += morse_code[ord(letter) - 97]
    if temp_code not in unique_code:
        unique_code.append(temp_code)

print(len(unique_code))

dic = dict(zip([chr(x) for x in range(97, 97 + 26)],
               [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]))
dic_2 = {}
print(dic)
for word in words:
    trans = ""
    for c in word:
        trans += dic[c]
    dic_2[trans] = 0
    print(dic_2)
