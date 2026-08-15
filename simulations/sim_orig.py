import random

original_deck = [0,
        1,
        2,2,
        3,3,3,
        4,4,4,4,
        5,5,5,5,5,
        6,6,6,6,6,6,
        7,7,7,7,7,7,7,
        8,8,8,8,8,8,8,8,
        9,9,9,9,9,9,9,9,9,
        10,10,10,10,10,10,10,10,10,10,
        11,11,11,11,11,11,11,11,11,11,11,
        12,12,12,12,12,12,12,12,12,12,12,
        'freeze', 'freeze', 'freeze',
        '2nd chance', '2nd chance', '2nd chance',
        'flip 3', 'flip 3', 'flip 3',
        '+2','+4','+6','+8','+10','x2']

class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.round_score = 0
        self.hand = []
        self.active = True
        self.busted = False
        self.got_flip7 = False
        
    def reset(self):
        self.round_score = 0
        self.hand = []
        self.active = True
        self.busted = False
        self.got_flip7 = False
        
    def draw(self, deck): # remove a random card and return its value
        i = random.randint(0, len(deck)-1)
        card = deck[i]
        deck.pop(i)
        return card
    
    def bust(self):
        self.round_score = 0
        self.active = False
        self.busted = True
        
    def freeze(self):
        self.active = False
        
    def flip7(self, player, opponent): # change to return true or false
        count = 0
        #for i in range(len(self.hand)):
            #if isinstance(self.hand[i], int):
                #count += 1
        for i in range(0, 13):
            if i in self.hand:
                count += 1
        if count >= 7:
            player.active = False
            opponent.active = False
            player.got_flip7 = True
            
    def score(self):
        self.round_score = 0
        if self.busted == False:
            for i in range(len(self.hand)):
                if isinstance(self.hand[i], int):
                    self.round_score += self.hand[i]
            if 'x2' in self.hand:
                    self.round_score *= 2
            for i in range(len(self.hand)):
                if isinstance(self.hand[i], str) and self.hand[i][0] == '+':
                    self.round_score += int(self.hand[i][1:])
            if self.got_flip7:
                self.round_score += 15
        else:
            self.round_score = 0
        return self.round_score

baseline = Player('baseline')
variant = Player('variant')

def handle_int(card, player):
    if isinstance(card, int):
        if card in player.hand:
            if '2nd chance' in player.hand:
                player.hand.remove('2nd chance')
                player.hand.remove(card)
            else:
                player.bust()

def handle_action(card, deck, player, opponent):
    if card == 'freeze':
        if opponent.active:
            opponent.freeze()
        else:
            player.freeze()
            
    if card == '2nd chance':
        if '2nd chance' in player.hand[:-1]:
            player.hand.remove('2nd chance')
            if '2nd chance' not in opponent.hand:
                opponent.hand.append('2nd chance')
            
    if card == 'flip 3':
        flip3_cards = []
        
        i = random.randint(0,1)
        if i == 0:
            if player.active:
                target = player
            else:
                target = opponent
        if i == 1:
            if opponent.active:
                target = opponent
            else:
                target = player
            
        i = 1
        while i <= 3 and target.active:
            new_card = target.draw(deck)
            handle_int(new_card, target)
            target.hand.append(new_card)
            flip3_cards.append(new_card)
            # check if reached 7 cards during flip 3
            if target == player:
                player.flip7(player, opponent)
            else:
                opponent.flip7(opponent, player)
            i += 1
            
        for drawn_card in flip3_cards: # resolve potential action cards drawn during filp 3
            if target.active:
                if target == player:
                    handle_action(drawn_card, deck, player, opponent)
                if target == opponent:
                    handle_action(drawn_card, deck, opponent, player)
                    
baseline_wins = 0
variant_wins = 0
ties = 0

with open('results_orig.csv', 'w') as myfile:
    myfile.write('Game,Baseline score,Variant score,Winner\n')
    
    for i in range(1000):
        baseline.total_score = 0
        variant.total_score = 0
        
        while baseline.total_score < 200 and variant.total_score < 200:
    
            baseline.reset()
            variant.reset()
            deck = original_deck.copy()
            
            while baseline.active or variant.active:
                
                if baseline.active:
                    # baseline's turn
                    if len(baseline.hand) > 4:
                        baseline.active = False
                        
                    else:
                        card = baseline.draw(deck)
                        handle_int(card, baseline)
                        baseline.hand.append(card)
                        handle_action(card, deck, baseline, variant)
                        if baseline.busted == False:
                            baseline.flip7(baseline, variant)
                        
                if variant.active:
                    # variant's turn
                    if len(variant.hand) > 4:
                        variant.active = False
                        
                    else:
                        card = variant.draw(deck)
                        handle_int(card, variant)
                        variant.hand.append(card)
                        handle_action(card, deck, variant, baseline)
                        if variant.busted == False:
                            variant.flip7(variant, baseline)
            
            baseline.round_score = baseline.score()
            variant.round_score = variant.score()
            baseline.total_score += baseline.round_score
            variant.total_score += variant.round_score
            
        winner = ''
        if baseline.total_score > variant.total_score:
            winner = 'baseline'
            baseline_wins += 1
        elif variant.total_score > baseline.total_score:
            winner = 'variant'
            variant_wins += 1
        else:
            winner = 'tie'
            ties += 1
            
        myfile.write(f'{i+1},{baseline.total_score},{variant.total_score},{winner}\n')
    myfile.write('\n')
    myfile.write(f'Baseline wins:,{baseline_wins},Variant wins:,{variant_wins},Ties:,{ties}')
    
