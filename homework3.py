list_bukvy = {1:"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т",
                2:"D, G, Д, К, Л, М, П, У",
                3:"B, C, M, P, Б, Г, Ё, Ь, Я",
                4:"F, H, V, W, Y, Й, Ы",
                5:"K, Ж, З, Х, Ц, Ч",
                8:"J, X, Ш, Э, Ю",
                10:"Q, Z, Ф, Щ, Ъ"}

word = input("Введите слово: ").upper()
summ = 0
for i in word:
    for k, v in list_bukvy.items():
        if i in v:
            summ += k
print(f"Стоимость слова: {summ}")