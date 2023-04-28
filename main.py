print("Оттачиваю git навык")


while True:

    question = input("Оттачиваешь навык? - ")

    if question == "Да":
        print("Тогда я создам словарь. Зачем? Потому что!")
        dictionary = {"Рик":"Гениальный ученый", "Морти":"Ссыкливый внук"}
        print(dictionary)
        break
    elif question == "Нет":
        print("Ну и дурак")
        break
    else:
        print("Либо Да либо Нет")

