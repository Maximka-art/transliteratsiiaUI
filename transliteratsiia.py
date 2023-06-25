Fio = input("Введите ФИО на русском языке: ").lower()
finish = ""
slovar = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e", "ё": "e", "ж": "zh", "з": "z", "и": "i", "й": "i",
          "к": "k", "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ф": "f",
          "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ь": "", "ы": "y", "ъ": "ie", "э": "e", "ю": "iu",
          "я": "ia"}
for i in range(len(Fio)):
    if Fio[i] in slovar:
        finish += slovar[Fio[i]]
    else:
        finish += Fio[i]
print(finish.upper())
