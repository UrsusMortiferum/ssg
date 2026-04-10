import unittest
from generate_webpages import extract_title


class TextExtractTitle(unittest.TestCase):
    def test_eq(self):
        out = extract_title("# Test title")
        self.assertEqual(out, "Test title")

    def test_eq_double_title(self):
        out = extract_title("""
# Hey from test title

# Hey from definitely not a title thingy
""")
        self.assertEqual(out, "Hey from test title")

    def test_eq_late_title(self):
        out = extract_title("""


# This is definitely a late title, why do you need those empty lines
""")
        self.assertEqual(
            out, "This is definitely a late title, why do you need those empty lines"
        )

    def test_no_title(self):
        try:
            extract_title("definitely not a title")
            self.fail("Where's my exception babe?")
        except Exception as e:
            pass


if __name__ == "__main__":
    unittest.main()
