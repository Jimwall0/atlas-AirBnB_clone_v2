#!/usr/bin/python3
"""
Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel
import datetime
import os
import json


class test_basemodel(unittest.TestCase):
    """Test the BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initialize the test case"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Setup method"""
        pass

    def tearDown(self):
        """Tear down method"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """Test default instantiation"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Test instantiation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Test instantiation with invalid kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """Test save method"""
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """Test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """Test instantiation with None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """Test instantiation with incomplete kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """Test id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """Test created_at attribute"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        new = self.value()
        initial_updated_at = new.updated_at
        new.save()
        self.assertTrue(new.updated_at > initial_updated_at)
        self.assertFalse(new.created_at == new.updated_at)


if __name__ == "__main__":
    unittest.main()
