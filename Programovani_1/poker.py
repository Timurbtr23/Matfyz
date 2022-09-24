# Poker
# Timur Badretdinov
# Winter semester 2021/22

import random
from termcolor import cprint


class Card:
    """
    Class which implement structure of game cards
        self.name - name of card (6, J, 10, A), type str
        self.number - strength of card (2-10, J=11, Q=12, K=13, A=14), type int
        self.suit - suit of card ("♥", "♣", "♠", "♦"), type str
    """
    def __init__(self, name, number, suit):
        self.name = name
        self.number = number
        self.suit = suit


class Game:
    """
    Class of the game engine
        self.deck_of_cards - all cards in the game, type list
        self.players - all players in the game, type list
        self.active_players - all players in the active game, type list
        self.table - all cards on the table, type list
        self.bank - money on the table of the active game, type int
    """
    def __init__(self):
        self.deck_of_cards = []
        self.players = []
        self.active_players = []
        self.table = []
        self.bank = 0

    def print_the_table(self):
        """Function that prints cards on the table"""
        cprint("Table is ", end="", color="magenta")
        for i in range(len(self.table)):
            cprint(f"{game.table[i].name}{game.table[i].suit} ", end="", color="magenta")
        print()

    def show_cards_of_all_players(self):
        """Function that prints cards of the players"""
        for player in self.active_players:
            player.print_cards()

    def show_status_of_all_players(self):
        """Function that prints status of the players"""
        for player in self.active_players:
            player.print_status()

    def add_players(self, player):
        """Function that add players to the game"""
        self.players.append(player)

    def make_cards(self):
        """Function that makes deck of Cards"""
        names = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["♥", "♣", "♠", "♦"]

        number = 2
        for name in names:
            for suit in suits:
                self.deck_of_cards.append(Card(name=name, number=number, suit=suit))
            number += 1

    def shuffle_the_deck(self):
        """Function that shuffles the deck before the game"""
        random.shuffle(self.deck_of_cards)

    def distribution_of_cards(self):
        """Function that distributes cards to the players, 2 cards for each player"""
        count = 0
        while count != len(self.players) * 2:
            for player in self.players:
                player.cards.append(self.deck_of_cards[0])
                del self.deck_of_cards[0]
                count += 1

    # Poker has 3 part of the game: the Flop, the Turn and the River
    # Before the flop players do first bets
    def first_bets(self):
        for player in self.players:
            player.money -= 10
            self.bank += 10
        print("First bets")

    def the_flop(self):
        # Part of the game when 3 cards on the table
        for j in range(3):
            self.table.append(self.deck_of_cards[0])
            del self.deck_of_cards[0]
        del self.deck_of_cards[0]
        self.print_the_table()

    def the_turn(self):
        # Part of the game after the Flop. To table appends 1 more card from the deck
        self.table.append(self.deck_of_cards[0])
        del self.deck_of_cards[0]
        del self.deck_of_cards[0]
        self.print_the_table()

    def the_river(self):
        # Part of the game after the Turn. To table appends 1 more card from the deck
        self.table.append(self.deck_of_cards[0])
        self.print_the_table()

    def mix_cards_and_table(self):
        """Help function that mixes cards of the players with cards on the table to easy get a combination and status"""
        for player in self.active_players:
            player.cards_n_table = player.cards + self.table

    def sort_cards_n_table(self):
        """Function that sorts list cards of the table and of the player"""
        # Sorting method - insert sort
        for player in self.active_players:
            for i in range(1, len(player.cards_n_table)):
                x = player.cards_n_table[i]
                j = i - 1
                while j >= 0 and x.number < player.cards_n_table[j].number:
                    player.cards_n_table[j + 1] = player.cards_n_table[j]
                    j -= 1
                player.cards_n_table[j + 1] = x
            player.cards_n_table = list(reversed(player.cards_n_table))

    def check_status_of_players(self):
        # Checking all of the possible combinations while get first True from any of them
        for player in self.active_players:
            if player.check_flush_royal():
                pass
            elif player.check_straight_flush():
                pass
            elif player.check_four_of_kind():
                pass
            elif player.check_full_house():
                pass
            elif player.check_flush():
                pass
            elif player.check_straight():
                pass
            elif player.check_three_of_kind():
                pass
            elif player.check_double_pair():
                pass
            elif player.check_pair():
                pass
            elif player.check_highest_card():
                pass

    def who_is_win(self, players):
        """Function that calculate who wins, depends on the status of players"""
        status_of_winner = 0
        winner_list = []
        for player in range(len(players)):
            if players[player].status > status_of_winner:
                status_of_winner = players[player].status
                winner_list = [player]
                continue
            # if we have a few players with the same score
            if players[player].status == status_of_winner:
                winner_list.append(player)
        return winner_list

    def reset_cards(self):
        """After game we should get the cards back and reset current stage of the game's data"""
        for player in self.players:
            player.cards = []
            player.cards_n_table = []
            player.status = 0
        self.deck_of_cards = []
        self.table = []
        self.bank = 0


class Player:
    """
    Class that implements Players
        self.cards - cards of the player, type list
        self.name - name of the player, type str
        self.cards_n_table - help list which is mix of table cards and own cards, type list
        self.status - status of the Player, the higher combination - the higher status - the higher chances to win, int
        self.status_name - name of the combination which the player has, type str
        self.money - money of the player, starts from 1000, type int
    """
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.cards_n_table = []
        self.status = 0
        self.status_name = ""
        self.money = 1000

    def __str__(self):
        print(f"Name of player - {self.name}")

    def print_cards(self):
        """Function that print cards of the player"""
        cprint(f"{self.name} cards are ", end="", color="red")
        for card in self.cards:
            cprint(f"{card.name}{card.suit} ", end="", color="red")
        print()

    def print_status(self):
        """Function that print status of the player"""
        print(f"{self.name} status is {self.status_name}")

    def how_much_money(self):
        """Function that print money of the player"""
        cprint(f"{self.name} has {self.money}$", color="green")

    # Next possible combinations of the cards
    def check_highest_card(self):
        """
            Check the highest card.
            The score ranges from 2 to 14 according to the value of the card.
        """
        self.status = self.cards_n_table[0].number
        self.status_name = "High Card"
        return True

    def check_pair(self):
        """
            Check if there are Pair (ex. K and K)
            the score ranges from 15 to 27 according to the value of the card
        """
        for j in range(len(self.cards_n_table)-1):
            if self.cards_n_table[j].number == self.cards_n_table[j+1].number:
                self.status = 13 + self.cards_n_table[j].number
                self.status_name = "Pair"
                return True
        return False

    def check_double_pair(self):
        """
            Check if there are Double Pair (ex, Q, Q, 3, 4, 3)
            The score ranges from 28 to 39 according to the value of the cards
        """
        count = 0
        x = []
        for j in range(len(self.cards_n_table)-1):
            if (self.cards_n_table[j].number == self.cards_n_table[j+1].number) \
                                                                        and (self.cards_n_table[j+1].number not in x):
                x.append(self.cards_n_table[j+1])
                count += 1
                if count == 2:
                    self.status = 25 + x[0].number
                    self.status_name = "Double pair"
                    return True
        return False

    def check_three_of_kind(self):
        """
            Check if there are Three of Kind (3 same cards, ex. 5, 5, 5, 6, 7)
            The score ranges from 40 to 52 according to the value of the cards
        """
        for j in range(len(self.cards_n_table)-2):
            if self.cards_n_table[j].number == self.cards_n_table[j + 1].number == self.cards_n_table[j + 2].number:
                self.status = 38 + self.cards_n_table[j].number
                self.status_name = "Three of kind"
                return True
        return False

    def check_straight(self):
        """
            Check if there are Straight (sequence of 5 cards, ex. 5, 6, 7, 9, 8)
            The score ranges from 53 to 62 according to the value of the cards
        """
        arr = []
        for card in self.cards_n_table:
            arr.append(card.number)
        arr = list(set(arr))

        if len(arr) > 4:
            count = 0
            maximum = 0
            for i in range(len(arr) - 1):
                if arr[i]+1 == arr[i+1]:
                    count += 1
                    maximum = arr[i+1]
                else:
                    count = 0
            if count >= 4:
                self.status = 51 + maximum-4
                self.status_name = "Straight"
                return True
        else:
            return False

    def check_flush(self):
        """
            Check if there are Flush (5 same suits)
            The score ranges from 63 to 71 according to the value of the cards
        """
        arr = []
        suits = ["♥", "♣", "♠", "♦"]
        for card in self.cards_n_table:
            arr.append(card.suit)
        for suit in suits:
            if arr.count(suit) == 5:
                maximum = 0
                for card in self.cards_n_table:
                    if card.suit == suit and card.number > maximum:
                        maximum = card.number
                self.status = 63 + maximum-6
                self.status_name = "Flush"
                return True
        return False

    def check_full_house(self):
        """
            Check if there are Full House (Three of Kind + Pair, ex. 5, 6, 5, 6, 5)
            The score ranges from 72 to 84 according to the value of the cards
        """
        help_arr = []
        count = 0
        maxim = 0
        for card in self.cards_n_table:
            help_arr.append(card)
        for j in range(len(help_arr)-2):
            if help_arr[j].number == help_arr[j + 1].number == help_arr[j + 2].number:
                maxim = help_arr[j].number
                del help_arr[j]
                del help_arr[j]
                del help_arr[j]
                count += 1
                break
        for j in range(len(help_arr)-1):
            if help_arr[j].number == help_arr[j+1].number and count == 1:
                self.status = 70 + maxim
                self.status_name = "Full House"
                return True
        return False

    def check_four_of_kind(self):
        """
            Check if there are Four of Kind (4 same cards, ex, J, J, J, Q, J)
            The score ranges from 85 to 97 according to the value of the cards
        """
        for j in range(len(self.cards_n_table)-3):
            if self.cards_n_table[j].number == self.cards_n_table[j + 1].number\
                    == self.cards_n_table[j + 2].number == self.cards_n_table[j + 3].number:
                self.status = 83 + self.cards_n_table[j].number
                self.status_name = "Four of Kind"
                return True
        return False

    def check_straight_flush(self):
        """
            Check if there are Straight + Flush.
            The score ranges from 98 to 105 according to the value of the cards
        """
        suit_arr = []
        help_arr = []
        suits = ["♥", "♣", "♠", "♦"]
        for card in self.cards_n_table:
            suit_arr.append(card.suit)
        for suit in suits:
            if suit_arr.count(suit) == 5:
                main_suit = suit
                for card in self.cards_n_table:
                    if card.suit == main_suit:
                        help_arr.append(card)
                if len(help_arr) != 5:
                    return False
                count = 0
                maximum = 0
                # check straight part
                for i in range(len(help_arr) - 1):
                    if help_arr[i].number - 1 == help_arr[i + 1].number:
                        count += 1
                        maximum = help_arr[i + 1].number
                    else:
                        count = 0
                        maximum = 0
                if count >= 4:
                    self.status = 96 + maximum - 4
                    self.status_name = "Straight Flush"
                    return True
            else:
                return False

    def check_flush_royal(self):
        """
            Check if there are Flush Royal (10, J, Q, K, A with the same suit).
            The max score - 106
        """
        suit_arr = []
        help_arr = []
        suits = ["♥", "♣", "♠", "♦"]
        for card in self.cards_n_table:
            suit_arr.append(card.suit)
        for suit in suits:
            if suit_arr.count(suit) == 5:
                main_suit = suit
                for card in self.cards_n_table:
                    if card.suit == main_suit:
                        help_arr.append(card)
                if len(help_arr) != 5:
                    return False
                summ = 0
                for card in help_arr:
                    summ += card.number
                if summ == 60:
                    self.status = 106
                    self.status_name = "Flash Royale"
                    return True
            else:
                return False


class Bot(Player):
    # Computer player
    def __init__(self, name):
        super().__init__(name)


class User(Player):
    # User player
    def __init__(self, name):
        super().__init__(name)

    def bet(self):
        """Func that does bets"""
        self.print_cards()
        self.how_much_money()
        if self.money <= 0:
            return -1
        else:
            print("0 is fold, 1 is check, 2 is bet")
            while True:
                try:
                    print("Your move -  ", end="")
                    choice = int(input())
                    if choice > 2 or choice < 0:
                        print('0 is fold, 1 is check, 2 is bet')
                        continue
                except ValueError:
                    print('Write a number please')
                else:
                    break

            if choice == 0:
                return 0

            elif choice == 1:
                return -1

            elif choice == 2:
                while True:
                    try:
                        print("How much money will you bet? - ", end="")
                        how_much = int(input())
                        if how_much > self.money:
                            print('Not enough money')
                            continue
                        if how_much < 0:
                            print('Please bet a positive number (>0)')
                            continue
                    except ValueError:
                        print('Write a number please')
                    else:
                        break
                self.money -= how_much
                return how_much


# Driver Code
if __name__ == "__main__":
    game = Game()  # create game
    print("Welcome to Poker! There are rules of the game - https://bicyclecards.com/how-to-play/basics-of-poker/")

    user = User(input("Enter your name - "))  # create user
    game.add_players(user)  # add user to the game

    # adding computer players with wrong input control
    count_of_bots = 0  # count of computer players
    while True:
        try:
            print("How many bots do you want to play with? (from 1 to 5) - ", end="")
            bots = int(input())
            if bots > 5 or bots < 1:
                print('So much bots. Write down from 1 to 5')
                continue
        except ValueError:
            print('Write a number please')
        else:
            count_of_bots = bots
            break

    for bot in range(count_of_bots):
        game.add_players(Bot(f"Computer {bot+1}"))

    # game engine
    while True:
        # making, shuffle and distribution of cards
        game.make_cards()
        game.shuffle_the_deck()
        game.distribution_of_cards()

        # data of the user: cards and money
        user.print_cards()
        user.how_much_money()

        # game use that list to save active players in the game. Player could have 0 money or do fold
        game.active_players = []
        for player in game.players:
            game.active_players.append(player)

        # implementing of first bets with control if user do fold
        break_it = False
        game.first_bets()
        user_move = user.bet()
        if user_move == 0:
            del game.active_players[0]
            break_it = True
        elif user_move > 0:
            game.bank += user_move * len(game.players)

        # 3 main stages of the game
        moment = 0
        for _ in range(3):
            print()
            if moment == 0:
                game.the_flop()
            elif moment == 1:
                game.the_turn()
            elif moment == 2:
                game.the_river()

            # bets on the stages
            print()
            if not break_it:
                user_move = user.bet()
                if user_move == 0:
                    del game.active_players[0]
                    break_it = True
                elif user_move > 0:
                    game.bank += user_move * len(game.players)
            moment += 1

        # calculating of the statuses and winners
        game.mix_cards_and_table()
        game.sort_cards_n_table()

        print()
        game.check_status_of_players()
        game.print_the_table()
        game.show_cards_of_all_players()
        game.show_status_of_all_players()

        winners = game.who_is_win(game.active_players)
        if len(winners) == 1:
            print(f"Winner is {game.active_players[winners[0]].name}")
            game.active_players[winners[0]].money += game.bank
        elif len(winners) > 1:
            for k in winners:
                print(f"Winner is {game.active_players[k].name}")
                game.active_players[k].money += game.bank // len(game.active_players)

        # asking to continue, controlling money and preparing to the next game
        print()
        if user.money == 0:
            print("Game Over. You have no money :(")
            print("Thank you for the game.")
            exit()
        else:
            while True:
                game_continue = input("Do you want to continue? y/n - ")
                if game_continue == "y":
                    game.reset_cards()  # preparing
                    print("=========================")
                    break
                elif game_continue == "n":
                    print("=========================")
                    if user.money > 1000:
                        print("Conratulations! You made {}$".format(user.money - 1000))
                    else:
                        print("Unfortunately you lose {}$".format(1000 - user.money))
                    print("Thank you for the game. We will wait for you visit again.")
                    exit()
                else:

                    continue

