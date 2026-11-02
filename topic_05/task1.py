import random

choices = ["stone", "scissor", "paper"]
while True:
    
    user_choices = input("Введіть значення (stone, scissor, paper) або 'exit' для виходу: ").lower()

    if user_choices == 'exit':
        print("Гру завершено!")
        break

    if user_choices not in choices:
        print("Помилка: введено неправильне значення.")
        continue
    
    computer_choice = random.choice(choices)
    print(f"Вибір комп'ютера: {computer_choice}")

    if user_choices == computer_choice:
        print("Нічия!")
    elif (user_choices == "stone" and computer_choice == "scissor") or \
    (user_choices == "scissor" and computer_choice == "stone") or \
    (user_choices == "paper" and computer_choice == "stone"):
        print("Ви перемогли!")
    else:
        print("Комп'ютер переміг!")
    
    print("-" * 20)
