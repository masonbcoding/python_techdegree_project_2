#I'm looking to merely pass this one

from operator import itemgetter

from constants import PLAYERS, TEAMS


def experience_modifier(value):
    if value == 'YES':
        return True
    return False


def heights_modifier(heights):
    heights = heights.replace(' inches', '')
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
    print("\n\n" + "*" * 10 + "BASKETBALL TEAM STATS TOOL" + "*" * 10)
    print("\n\nMENU:\n\nTo Display Team Stats, Enter [1], to Quit, Enter [2]...\n\n")
    compliance =int(input("Select an option >>>  "))


    if compliance == 1:
        print("")
    elif compliance == 2:
        exit()
    
    else:
        print("That is not a valid option. Please Enter [1] to Display Teams, or Enter [2] to Quit. ")
        start(arg)

def team_option():
    while True:
        for team, number in enumerate(TEAMS, 1):
            print(team, number)
            print("")
        option =int(input("\nSelect the team you would like to view. \n >>> "))
        print("")
        while True:
            if option == 1:
                print("PANTHERS TEAM:\n"
                    "--------------------\n"
                    "Total Players:")
                print(len(rosters['Panthers']))
                print("")
                print(rosters['Panthers'])
                continue_option = input("Would you like to view another team? [Y]es or [N]o? ")
                if continue_option.lower() == "y":
                    team_option()
                elif continue_option.lower() == "n":
                    exit()
                else:
                    print("That is not a valid selection. Please restart the program and try again.")
                    exit()

            elif option == 2:
                print("BANDITS TEAM:\n"
                    "--------------------\n"
                    "Total Players:")
                print(len(rosters['Bandits']))
                print("")
                print(rosters['Bandits'])
                continue_option = input("Would you like to view another team? [Y]es or [N]o? ")
                if continue_option.lower() == "y":
                    team_option()
                elif continue_option.lower() == "n":
                    exit()
                else:
                    print("That is not a valid selection. Please restart the program and try again.")
                    exit()
    
            elif option == 3:
                print("WARRIORS TEAM:\n"
                    "--------------------\n"
                    "Total Players:")
                print(len(rosters['Warriors']))
                print("")
                print(rosters['Warriors'])
                continue_option = input("Would you like to view another team? [Y]es or [N]o? ")
                if continue_option.lower() == "y":
                    team_option()
                elif continue_option.lower() == "n":
                    exit()
                else:
                    print("That is not a valid selection. Restart the program and try again.")
                    exit()

    else:
        print("That is not a valid option. Please select the team you would like to view using the numerical options provided.")
        exit()
    


if __name__ == "__main__":
    clean_data = data_cleaner()
    sorted_players = sorting_players()
    rosters = open_roster_list_creator()
    rosters = team_assigner(rosters, sorted_players)
    start(rosters)
    team_option()
