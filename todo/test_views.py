from django.test import TestCase

# Create your tests here.

class TestDjango(TestCase):
    def test_this_thing_works(self):
        self.assertEqual(1, 1) # pass
    
    def test_this_thing_works2(self):
        self.assertEqual(0, 1) # fail

    def test_this_thing_works3(self):
        self.assertEqual(0, ) # syntax error

    def test_this_thing_works4(self):
        self.assertEqual(0, 4) # fail