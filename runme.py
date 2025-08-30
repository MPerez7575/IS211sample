class SoccerPlayer:
    def __init__(self, name, team):
        """
        Constructor of a SoccerPlayer class
        :param name: The name of the player
        :param team: The team of the player
        """
        self.name = name
        self.team = team


    def display(self):
        """Display the Soccer Player's name and team"""
        print (f"I am {self.name} and I play for {self.team}")


if __name__ == "__main__":
    p1 = SoccerPlayer("Leo Messi", "Barcelona")
    p2 = SoccerPlayer("Cristiano Ronaldo", "Real Madrid")

    p1.display()
    p2.display()

    """ print("This is a assignment 1 part 2")"""
    """ added this line"""