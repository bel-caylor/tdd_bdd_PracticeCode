"""
Test Cases TestAccountModel
"""
import json
from unittest import TestCase
from models import db
from models.account import Account

ACCOUNT_DATA = {}

class TestAccountModel(TestCase):
    """Test Account Model"""

    @classmethod
    def setUpClass(cls):
        """ Connect and load data needed by tests """
        db.create_all()
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnect from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        for data in ACCOUNT_DATA:
            Account(**data).create()

    def tearDown(self):
        """Remove the session"""
        db.session.query(Account).delete()
        db.session.commit()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_all(self):
        """Test return all() rows"""
        self.assertEqual(len(Account.all()), len(ACCOUNT_DATA))

    
    def test_repr(self):
        """Test self"""
        account = Account(name="Test Account")
        expected_repr = '<Account \'Test Account\'>'  # Escape the single quote

        self.assertEqual(repr(account), expected_repr)
