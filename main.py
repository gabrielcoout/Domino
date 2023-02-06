import numpy as np

def check_invalid_hand(hands, N):
    for player in hands:
        count = 0
        for index in range(7):
            if hands[player][index][0]==hands[player][index][1]:
                count += 1
            if count == 4:
                return False
            else:
                pass
    return True

def shuffle_tiles(N):
    tiles = [[i,j] for i in range(N+1) for j in range(N+1) if i<=j]
    np.random.shuffle(tiles)
    initial_state = dict()
    initial_state['p1'] = tiles[0:7]
    initial_state['p2'] = tiles[7:14]
    initial_state['p3'] = tiles[14:21]
    initial_state['p4'] = tiles[21:28]
    return initial_state

def legal_play(player, edge):
    legal_actions = []
    if len(edge)==0:
        legal_actions = player
    else:
        for i in player:
            if i[0] == edge[0] or i[0] == edge[1]:
                legal_actions.append(list(i))
                continue
            if i[1] == edge[0] or i[1] == edge[1]:
                legal_actions.append(list(i))
                continue
    return legal_actions

def is_doublet(tile):
    try:
        if tile[0] == tile[1]:
            return True
        else:
            return False
    except IndexError:
        print('The input is\'nt a valid form of tile.')

def action(legal_actions, player, edge):
    print(f'As pontas são {edge}')
    if len(legal_actions) != 0:
        if len(edge)!=0:
            
            choice_1 = True
            while choice_1:
                try:
                    tile = input(f'Escolha uma das pedras para jogar \n{legal_actions} \n')
                    tile = list(int(tile) for tile in tile.split(","))
                    if tile in legal_actions:
                        choice_1 = False
                    else:
                        print('Input inválido')
                except ValueError:
                    print('Input inválido')
                    continue

            if (tile == edge or tile == edge[::-1]) and (not(is_doublet(tile) or is_doublet(edge))) :
                
                choice_2 = True
                while choice_2:
                    try:
                        position = int(input('Escolha a ponta que você quer jogar (0 ou 1)\n'))
                        if position == 0 or position == 1:
                            choice_2 = False
                        else:
                            print('Input inválido')
                    except ValueError:
                        print('Input inválido')
                        continue
            else:    
                for i in tile:
                    if i == edge[0]:
                        position = 0
                    elif i == edge[1]:
                        position = 1
                    else: 
                        continue

            if tile[0] == edge[position]:
                edge[position] = tile[1] 
                player.remove(tile)
                return edge
                
            if tile[1] == edge[position]:
                edge[position] = tile[0] 
                player.remove(tile)
                return edge
                
        else:
            choice_3 = True
            while choice_3:
                try:
                    tile = input(f'Escolha uma das pedras para jogar \n{legal_actions} \n')
                    tile = list(int(tile) for tile in tile.split(","))
                    if tile in legal_actions:
                        choice_3 = False
                        edge = tile
                        player.remove(tile)
                        return edge
                    else:
                        print('Input inválido')
                except ValueError:
                        print('Input inválido')
                        continue
    else:
        print('Nenhuma jogada legal disponível')
        return edge

def main():    
    N = 6
    keep_playing = True
    edge = []

    while keep_playing:
        hand = shuffle_tiles(N)
        if check_invalid_hand(hand, N):
            break
        else:
            continue
    
    
    while keep_playing:
        player_order_list = ['p1','p2','p3','p4']
        
        for player in player_order_list:
            active_player_hand = hand[player]
            print(f'{player}\'s turn \n{player}\'s hand: {active_player_hand}')
            
            
            legal_action = legal_play(active_player_hand, edge)
            
            edge = action(legal_action, active_player_hand, edge)
            
            if len(active_player_hand)==0:
                keep_playing = False
                print(f'{player} won the game')
            
            hand[player] = active_player_hand
            print('\n')
            
if __name__ == "__main__":
    main()