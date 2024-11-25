
# Make sure the test finds the application code
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
    
import unittest
from app import string_utils

class TestStringDistance(unittest.TestCase):
        
    def test_similar_text(self):
        score:float = string_utils.calcualte_text_distance("Software engineering is the cornerstone of a successful software project.","Building engineering is the cornerstone of a successful building project.")
        self.assertGreater(score, 0.7)
        self.assertLess(score,0.8)
        
    def test_non_similar_text(self):
        score:float = string_utils.calcualte_text_distance("Requirements are a first level entity in Agile development","Microservices have helped address scalibility issues in today's cloud environments.")
        self.assertGreater(score, 0.3)
        self.assertLess(score,0.4)

if __name__ == "__main__":
    unittest.main()