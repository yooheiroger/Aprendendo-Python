print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     //    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    // " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    "/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/

''')

print('Welcome to Treasure Hunt')
direction = input('You are at cross road. Where do you want to go? Type "Left" or "Right"')
direction_upper = direction.upper()
if direction_upper == 'LEFT':
    print('You were hit by a car. You die. GAME OVER')
else:
    print('Good, right now you are getting close to an island. You follow the map through the jungle and reach the river')
    river = input('What are you going to do? Swimming across the river or use a vine to cross it? Type "Swimming" or "Vine"')
    river_choice = river.upper()
    if river_choice == 'SWIMMING':
        print('There are a bunch of crocodiles in the river and they eat you. You Die. GAME OVER')
    else:
        print('Great, you used the vine to cross the river safety.')
        door = input('you reach the old hut with 3 doors. Type "Yellow, "Red", "Blue" ')
        blue_door = door.upper()
        if blue_door == 'YELLOW':
            print('When you open the door, you get hit by an arrow...GAME OVER')
        elif blue_door == 'RED':
            print('You open slowly but a mechanism behind it activate a bomb... GAME OVER')
        elif blue_door == 'BLUE':
            print('Right door. You see a hole in the ground leading to a secret passage')
            print('you founded the treasure Congrats!')
            print('''
                     __________________
                    .-'  \ _.-''-._ /  '-.
                  .-/\   .'.      .'.   /\-.
                 _'/  \.'   '.  .'   './  _
                :======:======::======:======:  
                 '. '.  \     ''     /  .' .'
                   '. .  \   :  :   /  . .'
                     '.'  \  '  '  /  '.'
                       ':  \:    :/  :'
                         '. \    / .'
                           '.\  /.'    miK
                             '\/'

            ''')
        else:
            print('Invalid Type')


