#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ The console """

    prompt = "(hbnb)"

    def do_quit(self, args):
        """ Quit command to exit the program """

        return(True)

    def do_EOF(self, args):
        """ EOF to exit the program """

        return(True)

    def emptyline(self):
        """an empty line executes anything"""

        pass
if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
