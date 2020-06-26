#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


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
            new.save()
            print(new.id)

    def do_show(self, args):
        """ """
        if not args:
            print("** class name missing **")
        else:
            list_arg = args.split()
            if not list_arg[0] == "BaseModel":
                print("** class doesn't exist **")
            elif len(list_arg) == 1:
                print("** instance id missing **")
            else:
                dic_obj = storage.all()
                id_found = list_arg[0] + "." + list_arg[1]
                if id_found in dic_obj:
                    obj = dic_obj[id_found]
                    print(obj)
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ """
        if not args:
            print("** class name missing **")
        else:
            list_arg = args.split()
            if not list_arg[0] == "BaseModel":
                print("** class doesn't exist **")
            elif len(list_arg) == 1:
                print("** instance id missing **")
            else:
                dic_obj = storage.all()
                id_found = list_arg[0] + "." + list_arg[1]
                if id_found in dic_obj:
                    del dic_obj[id_found]
                    storage.save()
                else:
                    print("** no instance found **")
    def do_all(self, args):
        """ """
        if not args == "BaseModel" and len(args) > 0:
            print("** class doesn't exist **")
        else:
            obj_all = storage.all()
            list_all = []
            for value in obj_all.values():
                list_all.append(str(value))
            print(list_all)

if __name__ == '__main__':
    console = HBNBCommand()
    console.cmdloop()