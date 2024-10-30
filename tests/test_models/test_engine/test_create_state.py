import unittest
from models.base_model import BaseModel
from console import HBNBCommand
from models import storage

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up a new instance of HBNBCommand for testing."""
        self.command = HBNBCommand()
        storage.all().clear()  # Clear existing storage before each test

    def test_create_instance_success(self):
        """Test creating a new instance successfully."""
        self.command.do_create("BaseModel name='Test' age=25")
        all_objects = storage.all()
        self.assertEqual(len(all_objects), 1)
        self.assertTrue(any(obj.name == 'Test' for obj in all_objects.values()))
        self.assertTrue(any(obj.age == 25 for obj in all_objects.values()))

    def test_create_class_missing(self):
        """Test class name missing."""
        with self.assertLogs('console', level='ERROR') as log:
            self.command.do_create("")
        self.assertIn("** class name missing **", log.output)

    def test_create_class_does_not_exist(self):
        """Test non-existing class."""
        with self.assertLogs('console', level='ERROR') as log:
            self.command.do_create("NonExistentClass name='Test'")
        self.assertIn("** class doesn't exist **", log.output)

    def test_create_with_invalid_parameter(self):
        """Test creating with an invalid parameter."""
        self.command.do_create("BaseModel invalid_param")
        all_objects = storage.all()
        self.assertEqual(len(all_objects), 0)  # No new instance should be created

    def tearDown(self):
        """Clean up any remaining objects after each test."""
        storage.all().clear()

if __name__ == '__main__':
    unittest.main()
