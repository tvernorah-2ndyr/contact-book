class Contact:
    """Represent a person's contact information."""

    def __init__(self, name, email, phone):
        """Initialize a contact with a name, email, and phone number."""
        self.name = name
        self.email = email
        self.phone = phone

    def masked_view(self):
        """Return the contact with the email address partially masked."""
        local_part, domain = self.email.split("@", 1)

        if len(local_part) <= 2:
            masked_local = "*" * len(local_part)
        else:
            masked_local = (
                local_part[0]
                + "*" * (len(local_part) - 2)
                + local_part[-1]
            )

        # Keep the domain visible while protecting the email's local part.
        masked_email = masked_local + "@" + domain

        return f"{self.name} | {masked_email} | {self.phone}"


class ContactBook:
    """Manage a collection of contacts."""

    def __init__(self):
        """Initialize an empty contact book."""
        self.contacts = []

    def add_contact(self, contact):
        """Add a contact to the contact book."""
        self.contacts.append(contact)

    def remove_contact(self, name):
        """Remove a contact by name.

        Returns:
            bool: True if a contact was removed, otherwise False.
        """
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return True

        return False

    def find_contact(self, name):
        """Find a contact by a name or part of a name.

        Returns:
            Contact or None: The matching contact if found.
        """
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                return contact

        return None


# Create a contact book.
book = ContactBook()

# Add sample contacts.
amelia = Contact(
    "Amelia Turner",
    "amelia@example.com",
    "+675 7XX XXX XXX"
)

kofi = Contact(
    "Kofi Mensah",
    "kofi@example.com",
    "+675 7XX XXX XXX"
)

book.add_contact(amelia)
book.add_contact(kofi)

print("Added contact:", amelia.name)
print("Added contact:", kofi.name)

print("Masked view:", amelia.masked_view())

result = book.find_contact("Kofi")

if result:
    print("Search result for 'Kofi':", result.masked_view())
else:
    print("Contact not found.")