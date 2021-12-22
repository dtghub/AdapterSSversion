deck = []
for suit in ['H', 'D', 'S', 'C']:
    # deck.append([suit + 'A'])
    for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
        deck.append(suit + value)
print(deck)

