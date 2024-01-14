#!/usr/bin/python3
"""Test for console."""

import unittest
import test
import console
from console import HBNBCommand


class Test_console_documentation(unittest.TestCase):
    """Test module, classes and methods documentation"""

    def test_module_doc(self):
        """Test module docstring"""
        self.assertIsNotNone(console.__doc__)

    @classmethod
    def setup_class(self):
        """Set up class for test"""
        self.console_obj = HBNBCommand()

    def test_classes_doc(self):
        """Test all classes docstring"""
        self.assertIsNotNone(HBNBCommand.__doc__)
        self.assertNotEqual(HBNBCommand.__doc__, " ",
                            msg="docstring can't be a whitespace")

    def test_methods_doc(self):
        """Test methods docstring"""
        self.assertIsNotNone(HBNBCommand.preloop.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.precmd.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.postcmd.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_create.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_create.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_show.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_show.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_destroy.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_all.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_all.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_count.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_count.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.do_update.__doc__,
                             msg="This method doesn't have docstring")
        self.assertIsNotNone(HBNBCommand.help_update.__doc__,
                             msg="This method doesn't have docstring")

        # Make sure docstring is not an empty space

        self.assertNotEqual(HBNBCommand.preloop.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.precmd.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.postcmd.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_quit.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_quit.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_EOF.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.emptyline.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_create.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_create.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_show.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_show.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_destroy.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_destroy.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_all.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_all.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_count.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_count.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.do_update.__doc__, " ",
                            msg="docstring can't be a whitespace")
        self.assertNotEqual(HBNBCommand.help_update.__doc__, " ",
                            msg="docstring can't be a whitespace")

    def test_class_instance(self):
        """Test class is created corretly"""

        test_obj1 = HBNBCommand()
        test_obj2 = test_obj1
        self.assertIsInstance(test_obj1, HBNBCommand)
        self.assertIs(test_obj1, test_obj2)

    def test_class_attr(self):
        "Test attributes of class"
        test_obj1 = HBNBCommand()
        self.assertTrue(test_obj1.classes)
        self.assertIsNotNone(test_obj1.classes)
        self.assertIsInstance(test_obj1.classes, dict)
        self.assertIn('BaseModel', test_obj1.classes)
        self.assertTrue(test_obj1.dot_cmds)
        self.assertIsNotNone(test_obj1.dot_cmds)
        self.assertIsInstance(test_obj1.dot_cmds, list)
        self.assertIn('create', test_obj1.dot_cmds)
        self.assertTrue(test_obj1.types)
        self.assertIsNotNone(test_obj1.types)
        self.assertIsInstance(test_obj1.types, dict)
        self.assertIn('latitude', test_obj1.types)


if __name__ == '__main__':
    unittest.main()
