#!/usr/bin/python3

""" Console Module """
import cmd
import shlex  # for splitting arguments
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""
    prompt = '(hbnb) '

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file or DB) and prints the id."""
        args = arg.split(" ")
        if not args:
            print("** class name missing **")
            return
        paremeters = args[1:]
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        kwarg = {}
        for parem in paremeters:
            try:
                key, value = parem.split("=")
                if value.startswith("\"") and value.endswith('\"'):
                    value = value[1:-1].replace('_', ' ')
                    kwarg[key] = value
                elif '.' in value:
                    kwarg[key] = float(value)
                else:
                    kwarg[key] = int(value)
            except:
                continue
        new_instance = HBNBCommand.classes[args[0]](**kwarg)
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
        else:
            storage.delete(storage.all()[key])
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_list = [str(obj) for obj in storage.all().values()]
        elif args[0] in self.classes:
            obj_list = [str(obj) for key, obj in storage.all().items() if key.startswith(args[0])]
        else:
            print("** class doesn't exist **")
            return
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3]

        # Convert attribute value to correct type
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            setattr(obj, attr_name, attr_type(attr_value))
        else:
            setattr(obj, attr_name, attr_value)
        obj.save()

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
