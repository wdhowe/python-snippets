"""
Unit tests for the distrodb class
Uses setup and teardown functions to avoid doing something
expensive like initializing a database multiple times.
"""

# Import the DistroDB class for object testing
from distrodb_class import DistroDB

# Import pytest for fixture decorator
import pytest


@pytest.fixture(scope="module")
def database():
    """
    Fixture runs one time setup before all tests and teardown after.
    This is instead of a separate setup and teardown function.
    """
    print("\nSetup running.")
    database = DistroDB()
    database.connect("db_data.json")
    # yield returns the database object and suspends function execution
    # until the end of the test
    yield database
    database.disconnect()


def test_ubuntu_data(database):
    """Test for Ubuntu data"""
    ubuntu_data = database.get_data("ubuntu")
    assert ubuntu_data["name"] == "ubuntu"
    assert ubuntu_data["rank"] == 5


def test_mint_data(database):
    """Test for Mint data"""
    mint_data = database.get_data("mint")
    assert mint_data["name"] == "mint"
    assert mint_data["rank"] == 3
