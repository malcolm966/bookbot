SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.suit_index = SUITS.index(suit)

    def __eq__(self, other):
        return (
            self.rank_index == other.rank_index and self.suit_index == other.suit_index
        )

    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.rank_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Round:
    def resolve_round(self):
        raise NotImplementedError("Subclasses must implement resolve_round()")


# Don't touch above this line


class HighCardRound(Round):
    def __init__(self, card1:Card, card2:Card) -> None:
        super().__init__()
        self.card1 = card1
        self.card2 = card2
    def resolve_round(self):
        if self.card1 > self.card2:
            return 1
        elif self.card1 < self.card2:
            return 2
        else:
            return 0


class LowCardRound(Round):
    def __init__(self, card1:Card, card2:Card) -> None:
        super().__init__()
        self.card1 = card1
        self.card2 = card2
    
    def resolve_round(self):
        if self.card1 > self.card2:
            return 2
        elif self.card1 < self.card2:
            return 1
        else:
            return 0





run_cases = [
    (Card("Ace", "Spades"), Card("2", "Clubs"), 1, 2),
    (Card("Queen", "Hearts"), Card("Queen", "Diamonds"), 1, 2),
]

submit_cases = run_cases + [
    (Card("10", "Clubs"), Card("10", "Spades"), 2, 1),
    (Card("King", "Hearts"), Card("Queen", "Spades"), 1, 2),
    (Card("2", "Diamonds"), Card("2", "Diamonds"), 0, 0),
    (Card("5", "Clubs"), Card("10", "Hearts"), 2, 1),
    (Card("Jack", "Spades"), Card("2", "Spades"), 1, 2),
]


def result_to_card(card1, card2, placement):
    if placement == 1:
        return card1
    elif placement == 2:
        return card2
    else:
        return "Tie"


def test(card1, card2, expected_high_winner, expected_low_winner):
    try:
        print("---------------------------------")
        print(f"Inputs:")
        print(f" * card1: {card1}")
        print(f" * card2: {card2}")

        print("\nTesting HighCardRound:")
        high_round = HighCardRound(card1, card2)
        high_result = high_round.resolve_round()
        expected_winner = result_to_card(card1, card2, expected_high_winner)
        actual_winner = result_to_card(card1, card2, high_result)
        print(f"Expected winner: {expected_winner}")
        print(f"Actual winner:   {actual_winner}")
        high_correct = high_result == expected_high_winner

        print("\nTesting LowCardRound:")
        low_round = LowCardRound(card1, card2)
        low_result = low_round.resolve_round()
        expected_winner = result_to_card(card1, card2, expected_low_winner)
        actual_winner = result_to_card(card1, card2, low_result)
        print(f"Expected winner: {expected_winner}")
        print(f"Actual winner:   {actual_winner}")
        low_correct = low_result == expected_low_winner

        if high_correct and low_correct:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
