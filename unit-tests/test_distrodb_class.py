"""
Unit tests for the distrodb class
"""

# Import the DistroDB class for object testing
from distrodb_class import DistroDB

# Global database variable
database = None


def setup_module(module):
    """Setup module runs one time before all tests"""
    global database
    database = DistroDB()
    database.connect("db_data.json")


def teardown_module(module):
    """Teardown module runs one time after all tests"""
    database.disconnect()


def test_ubuntu_data():
    """Test for Ubuntu data"""
    ubuntu_data = database.get_data("ubuntu")
    assert ubuntu_data["name"] == "ubuntu"
    assert ubuntu_data["rank"] == 5


def test_mint_data():
    """Test for Mint data"""
    mint_data = database.get_data("mint")
    assert mint_data["name"] == "mint"
    assert mint_data["rank"] == 3
