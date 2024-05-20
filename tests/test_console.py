# tests/test_console.py
import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
from tests.mock_storage import MockStorage

class TestHBNBCommand(unittest.TestCase):


    def setUp(self):
        self.console = HBNBCommand()
        self.console.storage = MockStorage()

    def test_quit(self):
        """Test quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
        output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_EOF(self):
        """Test EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
        output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
        output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create InvalidClass")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create_valid_class(self):
        """Test create with valid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        output = f.getvalue().strip()
        self.assertTrue(len(output) == 36)
        key = f"BaseModel.{output}"
        self.assertIn(key, self.console.storage.all())

    def test_show_missing_class(self):
        """Test show with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class(self):
        """Test show with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
        output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_id(self):
        """Test show with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234")
        output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_show_valid_id(self):
        """Test show with valid class name and id"""
        instance = BaseModel()
        self.console.storage.new(instance)
        key = f"BaseModel.{instance.id}"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {instance.id}")
        output = f.getvalue().strip()
        self.assertEqual(output, str(self.console.storage.all()[key]))

    def test_destroy_missing_class(self):
        """Test destroy with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy InvalidClass")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
        output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_id(self):
        """Test destroy with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234")
        output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_valid_id(self):
        """Test destroy with valid class name and id"""
        instance = BaseModel()
        self.console.storage.new(instance)
        key = f"BaseModel.{instance.id}"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {instance.id}")
        output = f.getvalue().strip()
        self.assertEqual(output, "")
        self.assertNotIn(key, self.console.storage.all())

    def test_all_invalid_class(self):
        """Test all with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all InvalidClass")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_all_valid_class(self):
        """Test all with valid class name"""
        instance = BaseModel()
        self.console.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
        output = f.getvalue().strip()
        self.assertIn(str(instance), output)

    def test_all_no_class(self):
        """Test all with no class name"""
        instance = BaseModel()
        self.console.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all")
        output = f.getvalue().strip()
        self.assertIn(str(instance), output)

    def test_update_missing_class(self):
        """Test update with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class(self):
        """Test update with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update InvalidClass")
        output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
        output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_invalid_id(self):
        """Test update with invalid instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234")
        output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_missing_attribute(self):
        """Test update with missing attribute name"""
        instance = BaseModel()
        self.console.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {instance.id}")
        output = f.getvalue().strip()
        self.assertEqual(output, "** attribute name missing **")

    def test_update_missing_value(self):
        """Test update with missing attribute value"""
        instance = BaseModel()
        self.console.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update BaseModel {instance.id} attr_name")
        output = f.getvalue().strip()
        self.assertEqual(output, "** value missing **")

    def test_update_valid(self):
        """Test update with valid data"""
        instance = BaseModel()
        self.console.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(
                f"update BaseModel {instance.id} name 'New Name'"
                )
        output = f.getvalue().strip()
        self.assertEqual(output, "")
        self.assertEqual(instance.name, 'New Name')


if __name__ == '__main__':
    unittest.main()
