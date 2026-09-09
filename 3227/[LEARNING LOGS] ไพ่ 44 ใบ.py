"""ไพ่ 44 ใบ"""

def main():
    """main"""
    card = input().upper()

    rank = card[:-1]
    suit = card[-1]

    if rank == "A":
        rank = "ace"
    elif rank == "J":
        rank = "jack"
    elif rank == "Q":
        rank = "queen"
    elif rank == "K":
        rank = "king"

    if suit == "D":
        suit = "diamonds"
    elif suit == "H":
        suit = "hearts"
    elif suit == "S":
        suit = "spades"
    elif suit == "C":
        suit = "clubs"

    print(rank, "of", suit)

main()
