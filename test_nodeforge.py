# test_nodeforge.py
"""
Tests for NodeForge module.
"""

import unittest
from nodeforge import NodeForge

class TestNodeForge(unittest.TestCase):
    """Test cases for NodeForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodeForge()
        self.assertIsInstance(instance, NodeForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodeForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
