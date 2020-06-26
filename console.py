#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel


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

    def do_create(self, args):
        if not args:
            print("** class name missing **")
        elif not args == "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)

    def do_show(self, args):


if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()
