#!/usr/bin/python3
""" Console Module """
import cmd
import sys
import shlex  # For splitting arguments while handling quotes
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console """

    # Determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    # Available classes in the console
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }

    # Commands that can be used with dot notation (e.g., User.all())
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    # Types for the Place attributes
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def do_create(self, arg):
        """Creates a new instance of a class, saves it (to the JSON file),
        and prints the id. Example usage:
        create <Class name> <param 1> <param 2> ...
        Parameters must be in the form key=value.
        Strings must be enclosed in double quotes.
        Spaces are replaced with underscores in the input.
        Example:
        create State name="California"
        """
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args[0]]()
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """ Shows an individual object """
        from models import storage
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = class_name + "." + args[1]
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Destroys a specified object """
        from models import storage
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = class_name + "." + args[1]
        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """ Shows all objects, or all objects of a class"""
        from models import storage
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.all()
        elif args[0] in HBNBCommand.classes:
            obj_dict = storage.all(HBNBCommand.classes[args[0]])
        else:
            print("** class doesn't exist **")
            return
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print(obj_list)

    def do_update(self, arg):
        """ Updates a certain object with new information """
        from models import storage
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = class_name + "." + args[1]
        try:
            obj = storage.all()[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
