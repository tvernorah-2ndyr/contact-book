import unittest

from contact_book import Contact, ContactBook


class TestContactBook(unittest.TestCase):
    """Test the Contact and ContactBook classes."""

    def setUp(self):
        """Create a fresh contact book for each test."""
        self.book = ContactBook()

        self.amelia = Contact(
            "Amelia Turner",
            "amelia@example.com",
            "+675 7XX XXX XXX"
        )

        self.kofi = Contact(
            "Kofi Mensah",
            "kofi@example.com",
            "+675 7XX XXX XXX"
        )

    def test_add_contact(self):
        """Test that a contact can be added."""
        self.book.add_contact(self.amelia)

        self.assertEqual(len(self.book.contacts), 1)
        self.assertEqual(self.book.contacts[0].name, "Amelia Turner")

    def test_find_contact(self):
        """Test that a contact can be found by name."""
        self.book.add_contact(self.kofi)

        result = self.book.find_contact("Kofi")

        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Kofi Mensah")

    def test_remove_contact(self):
        """Test that a contact can be removed."""
        self.book.add_contact(self.amelia)

        removed = self.book.remove_contact("Amelia Turner")

        self.assertTrue(removed)
        self.assertEqual(len(self.book.contacts), 0)

    def test_masked_view(self):
        """Test that the email address is masked."""
        masked = self.amelia.masked_view()

        self.assertEqual(
            masked,
            "Amelia Turner | a****a@example.com | +675 7XX XXX XXX"
        )


if __name__ == "__main__":
    unittest.main()