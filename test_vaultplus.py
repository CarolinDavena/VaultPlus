# test_vaultplus.py
"""
Tests for VaultPlus module.
"""

import unittest
from vaultplus import VaultPlus

class TestVaultPlus(unittest.TestCase):
    """Test cases for VaultPlus class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultPlus()
        self.assertIsInstance(instance, VaultPlus)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultPlus()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
