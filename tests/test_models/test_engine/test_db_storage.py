import unittest
from os import environ, remove
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb


@unittest.skipIf(environ.get('HBNB_TYPE_STORAGE') != 'db',
                 "Test just in case DBStorage")

class TestDBStorage(unittest.TestCase):
    """All test for the Data Base"""

    @classmethod
    def setUpClass(cls):
        """Obj for testing"""

        cls.user = User()
        cls.user.first_name = "Miguel"
        cls.user.last_name = "Colmenares"
        cls.user.email = "5693@holbertonstudents.com"
        cls.storage = FileStorage()


    @classmethod
    def teardown(cls):
        """delete obj after test"""
        del cls.user
        remove("file.json")

    def test_module_doc(self):
        """ test module docstring """

        self.assertIsNotNone(tests.test_models.test_engine.
                             test_db_storage.__doc__)
        self.assertNotIn(" ", tests.test_models.test_engine.
                         test_db_storage.__doc__)

    def test_all_method(self):
        """test for all method"""

        # Test all method docstring
        self.assertIsNotNone(models.engine.db_storage.all.__doc__)
        self.assertNotIn(" ", models.engine.db_storage.all.__doc__)

        # Test all method output

        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

if __name__ == "__main__":
    unittest.main()
