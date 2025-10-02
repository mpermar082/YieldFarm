# test_yieldfarm.py
"""
Tests for YieldFarm module.
"""

import unittest
from yieldfarm import YieldFarm

class TestYieldFarm(unittest.TestCase):
    """Test cases for YieldFarm class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = YieldFarm()
        self.assertIsInstance(instance, YieldFarm)
        
    def test_run_method(self):
        """Test the run method."""
        instance = YieldFarm()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
