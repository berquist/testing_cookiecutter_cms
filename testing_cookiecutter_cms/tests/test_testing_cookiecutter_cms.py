"""
Unit and regression test for the testing_cookiecutter_cms package.

Adding a string.
"""

# Import package, test suite, and other packages as needed
import testing_cookiecutter_cms
import pytest
import sys

def test_testing_cookiecutter_cms_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "testing_cookiecutter_cms" in sys.modules


def test_add():
    left = 5
    right = 2
    ref = 7
    assert testing_cookiecutter_cms.add(left, right) == ref
