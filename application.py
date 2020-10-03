
from operator import itemgetter

from constants import PLAYERS, TEAMS


def experience_modifier(value):
    if value == 'YES':
        return True
    return False


def heights_modifier(heights):
    heights = int(heights.replace(' inches', ''))
    return heights


def data_cleaner():

    clean_data = []

    for PLAYER in PLAYERS:

        name = PLAYER.get('name')

        guardians = PLAYER.get('guardians')

        value = PLAYER.get('experience')
        experience = experience_modifier(value)

        heights = PLAYER.get('height')

        height = heights_modifier(heights)

        clean_data.append({'name': name, 'guardians': guardians, 'experience': experience, 'height': height})

    return clean_data


number_of_teams = len(TEAMS)


def open_roster_list_creator():
    rosters = {team: [] for team in TEAMS}
    return rosters


def sorting_players():
    sorted_players = sorted(clean_data, key=itemgetter('experience'), reverse=True)
    return sorted_players


def team_assigner(rosters, sorted_players):
    for team, player in enumerate(sorted_players):
        rosters[TEAMS[team % len(TEAMS)]].append(player.get('name'))
    return rosters


def start(arg):
        try:
            print("\n\n" + "*" * 10 + "BASKETBALL TEAM STATS TOOL" + "*" * 10)
            print("\n\nMENU:\n\nTo Display Team Stats, Enter [1], to Quit, Enter [2]...\n\n")
            compliance =int(input("Select an option >>>  "))


            if compliance == 1:
                print("")
            elif compliance == 2:
                exit()
    
            else:
                raise ValueError
        except ValueError as err:
            print("\nYour selection was invalid: {} Returning to Main Menu. ".format(err))
            start(arg)
    

def team_option():
    while True:
        try:
            for team, number in enumerate(TEAMS, 1):
                print(team, number)
                print("")
            option =int(input("\nSelect the team you would like to view. \n >>> "))
            print("")
            while True:
                try:
                    if option == 1:
                        names = rosters['Panthers']
                        print("PANTHERS TEAM:\n"
                            "--------------------\n"
                            "Total Players:")
                        print(len(rosters['Panthers']))
                        print("")
                        print(', '.join(names))
                        continue_option = input("\nWould you like to view another team? [Y]es or [N]o?\n ")
                        if continue_option.lower() == "y":
                            team_option()
                        elif continue_option.lower() == "n":
                            exit()
                        else:
                            raise ValueError
        
                    elif option == 2:
                        names = rosters['Bandits']
                        print("BANDITS TEAM:\n"
                            "--------------------\n"
                            "Total Players:")
                        print(len(rosters['Bandits']))
                        print("")
                        print(', '.join(names))
                        continue_option = input("\nWould you like to view another team? [Y]es or [N]o?\n ")
                        if continue_option.lower() == "y":
                            team_option()
                        elif continue_option.lower() == "n":
                            exit()
                        else:
                            raise ValueError
            
                    elif option == 3:
                        names = rosters['Warriors']
                        print("WARRIORS TEAM:\n"
                            "--------------------\n"
                            "Total Players:")
                        print(len(rosters['Warriors']))
                        print("")
                        print(', '.join(names))
                        continue_option = input("\nWould you like to view another team? [Y]es or [N]o?\n ")
                        if continue_option.lower() == "y":
                            team_option()
                        elif continue_option.lower() == "n":
                            exit()
                        else:
                            raise ValueError
                            
                            
                    else:
                        raise ValueError
                        team_option()
                        
                except ValueError:
                    print("\nThat is not a valid option. Please try again.\n ")
                    team_option()

        except ValueError:
            print("\nThat is not a valid option. Please try again.\n ")
    


if __name__ == "__main__":
    clean_data = data_cleaner()
    sorted_players = sorting_players()
    rosters = open_roster_list_creator()
    rosters = team_assigner(rosters, sorted_players)
    start(rosters)
    team_option()
