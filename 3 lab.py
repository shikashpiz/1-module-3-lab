# TODO  Напишите функцию count_letters
def count_letters(main_str):
    main_str = main_str.lower()
    clovar = {}
    for simvol in main_str:
        if simvol.isalpha():
            clovar[simvol] = clovar.get(simvol,0) + 1
    return clovar

# TODO Напишите функцию calculate_frequency
def calculate_frequency(clovar):
    vse_bukv = sum(clovar.values())
    chastota_clovar = {}
    for bukv, count in clovar.items():
        chastota_clovar[bukv] = count / vse_bukv

    return chastota_clovar


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
def ctolb_chastot(chastot):
    for bukv, chastota in chastot.items():
        print(f"{bukv}: {chastota:.2f}")

kolvo_bukv = count_letters(main_str)
chastot = calculate_frequency(kolvo_bukv)
ctolb_chastot(chastot)
