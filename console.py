#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd

from models.base_model import BaseModel
from models import storage

all_classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """Implementing the command interpreter functionality"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Implements EOF functionality"""
        return True

    def do_help(self, arg):
        """Outputs the help document"""
        super().do_help(arg)

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Create instance of specific class
        """
        if arg is None or arg.strip() == "":
            print("** class name missing **")
        elif arg not in all_classes.keys():
            print("** class doesn't exist **")
        else:
            obj = all_classes[arg]()
            obj.save()
            print(obj.id)
    
    def do_show(self, arg):
        """Show object info given its class and id
        """
        lst = arg.strip().split()
        if len(lst) == 0:
            print("** class name missing **")
        elif lst[0] not in all_classes.keys():
            print("** class doesn't exist **")
        elif len(lst) == 1:
            print("** instance id missing **")
        elif f"{lst[0]}.{lst[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{lst[0]}.{lst[1]}"])



if __name__ == "__main__":
    HBNBCommand().cmdloop()
