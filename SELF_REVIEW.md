# Self-Review

## Code Review Checklist

1. Check correctness of the code.
2. Check readability and clear naming.
3. Check that appropriate tests are included.
4. Check that functions have accurate documentation.
5. Check that errors are handled appropriately.
6. Check that privacy and security considerations are addressed.

## Review Findings

The contact book was reviewed against the checklist.

- The contact and contact book functions work correctly.
- Class and method names are clear and descriptive.
- Unit tests cover adding, finding, removing, and masking contacts.
- Docstrings are included for classes and methods.
- Email addresses are masked in displayed contact information.
- The remove_contact method was improved to handle extra spaces and ignore letter case when matching names.

## Improvement Made

The `remove_contact()` method was updated to use `strip()` and `lower()` when comparing names. This makes name matching more reliable when a user enters a name with extra spaces or different capitalization.

The updated code was tested after the improvement, and all 4 unit tests passed.