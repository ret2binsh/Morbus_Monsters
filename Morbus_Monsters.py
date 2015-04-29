import os
import sys
from random import choice
from random import randrange

from monsters import *

#To be used for Player stats and save file information
class Player_Info(object):
    pass
  

'''Randomly selects a number to facilitate an accuracy
check. True will result in a hit and False a miss.
'''
def accuracy_check(acc):
    num = randrange(1,100)

    if num <= acc:
        return True
    else:
        return False

'''Randomly selects an attack for the cpu with a higher
weight for using the cure spell when it is low on health.
Does not use option 3 if health is 100.
'''
def cpu_selection(max_health,health):
    if health < max_health:
        if health < max_health * .35:
            attack_option = choice([1,2,3,3])
            return attack_option
        else:
            attack_option = choice([1,1,2,2,3])
            return attack_option
    else:
        attack_option = choice([1,2])
        return attack_option       

'''Sets up the display for the player. An asterisk highlights player1's turn.79
It additionally adjusts the amount of spaces based off of the lenght of the
player's health so both HPs stay under the character name.
'''
def Draw_Player(num):
    print('*' * 31 + 'Morbus Monsters' + '*' * 32 +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + '*' * 78 + '*' +
          '\n' + ' ' * 5 + player1.name + '*' + ' ' * 45 + player2.name +
          '\n' + ' ' * 5 + 'HP:' + str(player1.health) + ' ' * (62 - num) + 'HP:' 
          + str(player2.health) +
          '\n\n*' + '*' * 78 + '*' +
          '\n' + ' ' * 5 + '| 1 - ' + player1.move1[0] + '(' + player1.move1[1]
          + ') | 2 - ' + player1.move2[0] + '(' + player1.move2[1] + ') | 3 - '
          + player1.move3[0] + '(' + player1.move3[1] + ') |' +
          '\n\n*' + '*' * 78 + '*')

'''Same as Draw_Player except for the CPU's turn. Mainly used to alternate
the asterisk next to the character to denote who's turn it is.
'''
def Draw_CPU(num):
    print('*' * 31 + 'Backpack Monsters' + '*' * 32 +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + ' ' * 78 + '*' +
          '\n*' + '*' * 78 + '*' +
          '\n' + ' ' * 5 + player1.name + ' ' * 45 + '*' + player2.name +
          '\n' + ' ' * 5 + 'HP:' + str(player1.health) + ' ' * (62 - num) + 'HP:' 
          + str(player2.health) +
          '\n\n*' + '*' * 78 + '*' +
          '\n' + ' ' * 5 + '| 1 - ' + player1.move1[0] + '(' + player1.move1[1]
          + ') | 2 - ' + player1.move2[0] + '(' + player1.move2[1] + ') | 3 - '
          + player1.move3[0] + '(' + player1.move3[1] + ') |' +
          '\n\n*' + '*' * 78 + '*')

#Function that properly ends the game.
def end_game():

    print('Thanks for playing.')
    os.system('pause')
    
    sys.exit()

'''Checks whether or not the defender is weak or resistant against the attack.
Return a float that will be used to calculate the final attack power.
'''
def Effect(attack_type,weak,strong):
    if attack_type == weak:
        return 1.2
    elif attack_type == strong:
        return .5
    else:
        return 1.0

#Verifies that a proper selection is made to be used for attacks.
def input_request():
    
    player_selection = ''
    while player_selection not in ['1','2','3']:
        player_selection = input('Please select an attack: ')
    
    return player_selection


'''Prompts the user to select from a list of available monsters.
Once one is selected a class is created that replicates the
selected monster from the monsters.py file.
'''
def select_monster():
    
    print('Please Choose a Monster.')

    #Creates the list of selectable monsters
    monsters = []
    for key in available_monsters:
        monsters.append(key.lower())
        print('%s: %dHP' % (key,available_monsters[key].health))

    #Prompts for user input and validates the entry (not case sensitive)
    user_input = ''
    while user_input not in monsters:
        user_input = input('Type the full name: ').lower()

    #Restores proper formatting
    user_input = user_input.title()

    '''Copies the class information provided by the monsters.py from
    the selected monster.
    '''
    class Player_Char(object):
        def __init__(self):
            self.max_health = available_monsters[user_input].max_health
            self.health = available_monsters[user_input].health
            self.acc = available_monsters[user_input].acc
            self.p_type = available_monsters[user_input].p_type
            self.weak = available_monsters[user_input].weak
            self.name = available_monsters[user_input].name
            self.move1 = available_monsters[user_input].move1
            self.move2 = available_monsters[user_input].move2
            self.move3 = available_monsters[user_input].move3
            self.level = available_monsters[user_input].level
            self.exp = available_monsters[user_input].exp
            self.power = available_monsters[user_input].power
            self.defense = available_monsters[user_input].defense

        def __str__(self):
            return ("Name: %s \nLevel: %s \nType: %s \nWeakness: %s\
                    \nHealth: %s \nExp: %s") % (self.name,
                                               self.level,
                                               self.p_type,
                                               self.weak,
                                               self.health,
                                               self.exp)

        def attack_result(self,attack):
            self.health = self.health - attack
            if self.health > 100:
                self.health = 100
                return self.health
            elif self.health < 0:
                print('%s has been eradicated.' % self.name)
                self.health = 0
                return self.health
            else:
                return self.health

        def display_move(self,attack):
            if attack == 1:
                return self.move1
            elif attack == 2:
                return self.move2
            else:
                return self.move3

    return Player_Char()

def cpu_monster():
    
    monsters = []
    for key in available_monsters:
        if available_monsters[key].health == 100:
            monsters.append(key)

    if not monsters:
        end_game()

    monster = choice(monsters)

    class CPU_Char(object):
        def __init__(self):
            self.max_health = available_monsters[monster].max_health
            self.health = available_monsters[monster].health
            self.acc = available_monsters[monster].acc
            self.p_type = available_monsters[monster].p_type
            self.weak = available_monsters[monster].weak
            self.name = available_monsters[monster].name
            self.move1 = available_monsters[monster].move1
            self.move2 = available_monsters[monster].move2
            self.move3 = available_monsters[monster].move3
            self.level = available_monsters[monster].level
            self.exp = available_monsters[monster].exp
            self.power = available_monsters[monster].power
            self.defense = available_monsters[monster].defense

        def __str__(self):
            return ("Name: %s \nLevel: %s \nType: %s \nWeakness: %s\
                    \nHealth: %s \nExp: %s") % (self.name,
                                               self.level,
                                               self.p_type,
                                               self.weak,
                                               self.health,
                                               self.exp)

        def attack_result(self,attack):
            self.health = self.health - attack
            if self.health > 100:
                self.health = 100
                return self.health
            elif self.health < 0:
                print('%s has been eradicated.' % self.name)
                self.health = 0
                return self.health
            else:
                return self.health

        def display_move(self,attack):
            if attack == 1:
                return self.move1
            elif attack == 2:
                return self.move2
            else:
                return self.move3
            

    return CPU_Char()
            

#Main function that handles the Game. 
def main():
	
    #Determines which console commands will be used depending upon OS. 
    clear_console = 'clear' if os.name == 'posix' else 'CLS'
    pause_console = ('read -p "Press any key to continue..."' if 
                     os.name == 'posix' else 'pause')
                     
    os.system(clear_console)

    global player1
    global player2
    player1 = select_monster()
    player2 = cpu_monster()

    os.system(clear_console)
    Draw_Player(len(str(player1.health)))
          
    print()
    print('Player 1 is %s and Player 2 is %s.' % (player1.name,player2.name))
    print()
    print(str(player1))
    print()
    print(str(player2))

    os.system(pause_console)
    os.system(clear_console)

    while player1.health > 0 and player2.health > 0:
    #----------------Player 1's Turn-------------------------------

        Draw_Player(len(str(player1.health)))
        print()
        print('Player 1\'s turn')

        player_selection = input_request()        

        attack_info = player1.display_move(int(player_selection))
        effect = Effect(attack_info[1],player2.weak,player2.p_type)
                                             
        current_attack = Attack(int(player_selection), effect, player1.power,
                                player2.defense)

        miss = accuracy_check(player1.acc)

        if miss == True:
        
            if attack_info[1] == 'Heal':
                print('%s used %s healing himself by %d' % (player1.name,
                                                            attack_info[0],
                                                            abs(current_attack)))
                player1.attack_result(current_attack)
        
            else:
                print('%s used %s for %d damage points' % (player1.name,
                                                           attack_info[0],
                                                           current_attack))
                if effect == 1.2:
                    print('It\'s super effective!')
                elif effect == .5:
                    print('It\'s not very effective')
                
                print('%s\'s health reduced to %d' % (player2.name,
                                                      player2.attack_result(current_attack)))
        else:

            print('%s attempted to use %s but it missed!' % (player1.name,
                                                             attack_info[0]))

        os.system(pause_console)
        os.system(clear_console)
    #---------------Player 2's Turn-------------------------------

        if player2.health <= 0:
            break

        Draw_CPU(len(str(player1.health)))
        
        print('Player 2\'s turn')

        cpu_choice = cpu_selection(player2.max_health,player2.health)
        attack_info = player2.display_move(cpu_choice)
        effect = Effect(attack_info[1],player1.weak,player1.p_type)
        
        current_attack = CPU_Attack(cpu_choice,effect,player2.power,
                                    player1.defense)
        
        if attack_info[1] == 'Heal':
            print('%s used %s healing himself by %d' % (player2.name,
                                                        attack_info[0],
                                                    	abs(current_attack)))
            player2.attack_result(current_attack)
        
        else:
            print('%s used %s for %d damage points' % (player2.name,
                                                       attack_info[0],
                                                       current_attack))
            if effect == 1.2:
                print('It\'s super effective!')
            elif effect == .5:
                print('It\'s not very effective')
                
            print('%s\'s health reduced to %d' % (player1.name,
                                                  player1.attack_result(current_attack)))

        os.system(pause_console)
        os.system(clear_console)

    #Test to see who won the battle
    Draw_Player(len(str(player1.health)))
    if player1.health != 0:
        print('%s wins!' % player1.name)
        player1.exp += 10
    else:
        print('%s wins!' % player2.name)

    repeat = ''

    while repeat not in ['yes','no']:
        repeat = input('Play again? (yes/no): ')
        repeat.lower()

    if repeat == 'yes':
        main()
    else:
        end_game()

if __name__ == '__main__':
    main()
