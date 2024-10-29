#!/usr/bin/python3
""" Console Module """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex  # For splitting the line into arguments

class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter for AirBnB clone project"""

    prompt = '(hbnb) '

    classes = {
        'BaseModel': BaseModel, 'User': User, 'State': State,
        'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review
    }

    def do_create(self, arg):
        """Create an instance of a class with attributes"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        # Parse key=value arguments
        kwargs = {}
        for param in args[1:]:
            key, sep, value = param.partition("=")
            if sep == "=":
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1].replace('_', ' ').replace('\\"', '"')
                elif '.' in value:
                    try:
                        value = float(value)
                    except ValueError:
                        continue
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        continue
                kwargs[key] = value

        # Check required attributes for State and City
        if class_name == "State" and "name" not in kwargs:
            print("** missing required attribute 'name' **")
            return
        if class_name == "City" and ("name" not in kwargs or "state_id" not in kwargs):
            print("** missing required attributes 'state_id' and 'name' **")
            return

        new_instance = self.classes[class_name](**kwargs)
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances of a class, or all instances if no class is specified"""
        args = shlex.split(arg)
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        obj_list = []
        for obj in storage.all().values():
            if not args or args[0] == obj.__class__.__name__:
                obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        try:
            attr_value = eval(attr_value)
        except:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
