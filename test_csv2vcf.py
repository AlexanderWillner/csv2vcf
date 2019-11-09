import unittest
import json
import csv2vcf
from io import StringIO

class test_convert_to_vcard(unittest.TestCase):

    def test_all(self):
        output = StringIO()
        csv2vcf.convert_to_vcard("test_csv2vcf.csv", 1, json.loads('{"given":1, "surname":2, "maiden":3, "note":4, "bday":5, "zip":6, "city":7, "street":8, "country":9, "email":10, "tel":11, "mobile":12}'), output)
        self.assertIn("First", output.getvalue(), "first name missing")
        self.assertIn("Last", output.getvalue(), "last name missing")
        self.assertIn("Maiden", output.getvalue(), "maiden name missing")
        self.assertIn("Note", output.getvalue(), "note missing")
        self.assertIn("2000", output.getvalue(), "birthday missing")
        self.assertIn("12345", output.getvalue(), "city code missing")
        self.assertIn("City", output.getvalue(), "city missing")
        self.assertIn("Street 1", output.getvalue(), "street missing")
        self.assertIn("Country", output.getvalue(), "country missing")
        self.assertIn("mail@example.org", output.getvalue(), "mail missing")
        self.assertIn("+155512345", output.getvalue(), "phone missing")
        self.assertIn("+995551234567", output.getvalue(), "mobile missing")

if __name__ == '__main__':
    unittest.main()
