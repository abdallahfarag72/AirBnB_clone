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
        if arg is None: 
            arg = ""
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
    
    def do_destroy(self, arg):
        if arg is None:
            arg = ""
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
            del storage.all()[f"{lst[0]}.{lst[1]}"]
            storage.save()
    
    def do_all(self, arg):
        if arg is None:
            arg = ""
        if arg.strip() != "" and arg not in all_classes:
            print("** class doesn't exist **")
        lst = []
        all_objs = storage.all()
        for key, obj in all_objs.items():
            if arg == "" or arg == key.split('.')[0]:
                lst.append(str(obj))
        print(lst)
    
    def do_update(self, arg):
        if arg is None:
            arg = ""
        lst = arg.strip().split()
        if len(lst) < 4:
            if len(lst) == 0:
                print("** class name missing **")
            elif lst[0] not in all_classes:
                print("** class doesn't exist **")
            elif len(lst) == 1:
                print("** instance id missing **")
            elif f"{lst[0]}.{lst[1]}" not in storage.all():
                print("** no instance found **")
            elif len(lst) == 2:
                print("** attribute name missing **")
            elif len(lst) == 3:
                print("** value missing **")
        else:
            cls_name = lst[0]
            obj_id = lst[1]
            att_name = lst[2]
            att_val = lst[3]
            all_objs = storage.all()
            cur_obj = all_objs[f"{cls_name}.{obj_id}"]
            att_type = type(getattr(cur_obj, att_name))
            setattr(cur_obj, att_name, att_type(att_val))
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
