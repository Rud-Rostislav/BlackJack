from Hand import *
from Deck import *

def new_game():
    d = Deck()
    player_hand = Hand("Игрок")
    dealer_hand = Hand("Диллер")

    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())

    dealer_hand.add_card(d.deal_card())
    print(dealer_hand, '|', player_hand)
    in_game = True
    while player_hand.get_value() < 21:
        answear = input("Взять еще карту?(да/нет): ")
        if answear == "да":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("Вы проиграли!")
                in_game = False
        else:
            print("Вы не взяли карту.")
            break
    if in_game:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            if dealer_hand.get_value() > 21:
                print("Вы выиграли!")
                in_game = False
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print("Вы выиграли!")
        elif player_hand.get_value() == 21:
            print("Вы выиграли!")
        elif player_hand.get_value() == 21 and dealer_hand.get_value() == 21:
            print('Ничья!')
        elif player_hand.get_value() == dealer_hand.get_value():
            print('Ничья!')
        else:
            print("Диллер выиграл!")


while True:
    choice = input('Сыграем в блекджек?(да/нет): ')
    if choice == 'да':
        new_game()
    else:
        print('Вы не захотели сыграть!')
        break