class Blackboard:
    """Class defining a surface on which to write,
    that can be read and deleted, by a set of methods. The modified attribute
    is "surface" """

    def __init__(self):
        """By default, our surface is empty"""
        self.surface = ""

    def write(self, message_written):
        """Method for writing on the surface of the table.
        If the surface is not empty, we skip a line before adding
        the message to be written"""

        if self.surface != "":
            self.surface += "\n"
        self.surface += message_written

    def read(self):
        """This method is in charge of displaying, thanks to print,
        the surface of the painting"""
        print(self.surface)

    def reset(self):
        """This method allows you to erase the surface of the table"""
        # to be completed


Blackboard.read