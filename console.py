#!/usr/bin/python3
"""The entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Implementing the command interpreter functionality"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exits the program"""
        return True

    def do_EOF(self, arg):
        """Implements EOF functionality"""
        print("")
        return True

    def do_help(self, arg):
        """Outputs the help document"""
        super().do_help(arg)

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
