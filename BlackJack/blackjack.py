#How to play BlackJack
#1. Create a deck of 52 cards
#2. Shuffle the deck
#3. Ask the players for their bet
#4. Make sure the Player's bet does not exceed their available chips
#5. Deal two cards to the dealer and two to the player
#6. Show only one of the dealers hand, the other remains hidden
#7. Show both of the player's cards
#8. Ask the player if they wish to hit, and take another card
#9. If the player's hand doesn't bust (go over 21), ask if they want to hit again
#10. If the player stands, play the Dealers hand. The dealer will always hit until the dealers value meets or exceeds 17
#11. Determine the winner and adjust the player's chips accordingly
#12. Ask the player if they'd like to play again

#Thought process through this
#There has to be a deck class, card class, and player hand class
#Card class defines the card, so 2 of heart, etc.
#Deck class defines all the cards in a deck (so all 52 cards)
#Players hand defines adding a card to their hand and also adjusting the value for aces
import random

suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')
numbers = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.value = values[number]

    def __str__(self):
        return self.number + " of " + self.suit

class Deck:

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for number in numbers:
                self.all_cards.append(Card(suit, number))

    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()

class PlayerHand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.number]
    
    def adjust_for_ace(self):
        self.value -= 10

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet * 2

    def lose_bet(self):
        self.total -= self.bet


def take_bet(Account):
    print("Enter the amount you want to bet")
    repeat = True

    while repeat:
        try:
            betAmount = int(input(""))
        except:
            print("Please input a number, try again!")
        else:
            if Account.total - betAmount < 0:
                print("You don't have the funds to make this bet, try again")
            else:
                return betAmount 

def hit(deck, hand):
    card = deck.deal_one()

    hand.add_card(card)

def hit_or_stand(deck, hand):
    global playing
    repeat = True

    while repeat:
        userResponse = str(input("Would you like to Hit or Stand?"))
        
        if userResponse[0].lower() == 'h':
            hit(deck, hand)
        elif userResponse[0].lower() == 's':
            print("Dealer is now going to play.")
            playing = False
        else:
            print("Invalid input, please try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" < R E D A C T E D >")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand =", dealer.value)
    print("\nYour Hand:", *player.cards, sep='\n')
    print("Your Hand =", player.value)

def player_busts(player, dealer, chips):
    print("You busted!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("It's a push!")

while True:
    playing = True
    print("BlackJack!")
    print("Info about dealer: They will keep hitting until they reach 17")
    print("Aces count as 1 or 11")

    deck = Deck()
    deck.shuffle()

    playerHand = PlayerHand()
    playerHand.add_card(deck.deal_one())
    playerHand.add_card(deck.deal_one())

    dealerHand = PlayerHand()
    dealerHand.add_card(deck.deal_one())
    dealerHand.add_card(deck.deal_one())

    chips = Chips()

    take_bet(chips)

    show_some(playerHand, dealerHand)

    while playing:
        hit_or_stand(deck,playerHand)

        show_some(playerHand, dealerHand)

        if playerHand.value > 21:
            player_busts(playerHand, dealerHand, chips)
            break
    
    if playerHand.value <= 21:
        while dealerHand.value < 17:
            hit(deck, dealerHand)
        
        show_all(playerHand, dealerHand)

        if dealerHand.value > 21:
            dealer_busts(playerHand, dealerHand, chips)
        
        elif dealerHand.value > playerHand.value:
            dealer_wins(playerHand, dealerHand, chips)

        elif dealerHand.value < playerHand.value:
            player_wins(playerHand, dealerHand, chips)
        
        else: push(playerHand, dealerHand)
    
    print("\nPlayer's chips stand at ", chips.total) 

    new_game = input("Wanna play again? Type 'y' or 'n' ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thanks for playing!")
        False