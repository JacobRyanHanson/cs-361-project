import sys
from TA_Scheduling_App.classes.user import User
import unittest

class TestSetFirstName(unittest.TestCase):
    def setUp(self):
        self.user = User(userID=1, userType='TA', firstName='Jane', lastName='Doe', email='jane.doe@example.com',
                          phoneNumber='555-123-4567', address='1234 Elm St', birthDate='1995-08-30')
    def test_setFirstName_valid(self):
        self.assertTrue(self.user.setFirstName("John"))

    def test_setFirstName_valid_with_spaces(self):
        self.assertTrue(self.user.setFirstName("John Smith"))

    def test_setFirstName_valid_with_hyphen(self):
        self.assertTrue(self.user.setFirstName("John-Smith"))

    def test_setFirstName_valid_with_apostrophe(self):
        self.assertTrue(self.user.setFirstName("John's"))

    def test_setFirstName_invalid_empty_string(self):
        self.assertFalse(self.user.setFirstName(""))

    def test_setFirstName_invalid_whitespace(self):
        self.assertFalse(self.user.setFirstName("   "))

    def test_setFirstName_invalid_special_characters(self):
        self.assertFalse(self.user.setFirstName("#$%@"))

    def test_setFirstName_invalid_numbers(self):
        self.assertFalse(self.user.setFirstName("1234"))

    def test_setFirstName_invalid_combination(self):
        self.assertFalse(self.user.setFirstName("John1234"))

    def test_setFirstName_valid_unicode(self):
        self.assertTrue(self.user.setFirstName("Élodie"))

    def test_setFirstName_valid_mixed_case(self):
        self.assertTrue(self.user.setFirstName("jOhN"))

    def test_setFirstName_valid_spaces_before_after(self):
        self.assertTrue(self.user.setFirstName("  John  "))

    def test_setFirstName_invalid_only_numbers(self):
        self.assertFalse(self.user.setFirstName("1234"))

    def test_setFirstName_invalid_long_string(self):
        self.assertFalse(self.user.setFirstName("a" * 256))

    def test_setFirstName_valid_one_letter(self):
        self.assertTrue(self.user.setFirstName("J"))

class TestSetLastName(unittest.TestCase):
    def setUp(self):
        self.user = User(userID=1, userType='TA', firstName='Jane', lastName='Doe', email='jane.doe@example.com',
                          phoneNumber='555-123-4567', address='1234 Elm St', birthDate='1995-08-30')

    def test_setLastName_valid(self):
        self.assertTrue(self.user.setLastName("Smith"))

    def test_setLastName_valid_with_spaces(self):
        self.assertTrue(self.user.setLastName("Smith Johnson"))

    def test_setLastName_valid_with_hyphen(self):
        self.assertTrue(self.user.setLastName("Smith-Johnson"))

    def test_setLastName_valid_with_apostrophe(self):
        self.assertTrue(self.user.setLastName("O'Connor"))

    def test_setLastName_invalid_empty_string(self):
        self.assertFalse(self.user.setLastName(""))

    def test_setLastName_invalid_whitespace(self):
        self.assertFalse(self.user.setLastName("   "))

    def test_setLastName_invalid_special_characters(self):
        self.assertFalse(self.user.setLastName("#$%@"))

    def test_setLastName_invalid_numbers(self):
        self.assertFalse(self.user.setLastName("1234"))

    def test_setLastName_invalid_combination(self):
        self.assertFalse(self.user.setLastName("Smith1234"))

    def test_setLastName_valid_unicode(self):
        self.assertTrue(self.user.setLastName("Åström"))

    def test_setLastName_valid_mixed_case(self):
        self.assertTrue(self.user.setLastName("sMitH"))

    def test_setLastName_valid_spaces_before_after(self):
        self.assertTrue(self.user.setLastName("  Smith  "))

    def test_setLastName_invalid_only_numbers(self):
        self.assertFalse(self.user.setLastName("1234"))

    def test_setLastName_invalid_long_string(self):
        self.assertFalse(self.user.setLastName("a" * 256))

    def test_setLastName_valid_one_letter(self):
        self.assertTrue(self.user.setLastName("S"))

class TestSetEmail(unittest.TestCase):
    def setUp(self):
        self.user = User(userID=1, userType='TA', firstName='Jane', lastName='Doe', email='jane.doe@example.com',
                          phoneNumber='555-123-4567', address='1234 Elm St', birthDate='1995-08-30')

    def test_setEmail_valid(self):
        self.assertTrue(self.user.setEmail("john.smith@example.com"))

    def test_setEmail_invalid_empty_string(self):
        self.assertFalse(self.user.setEmail(""))

    def test_setEmail_invalid_no_at_symbol(self):
        self.assertFalse(self.user.setEmail("john.smithexample.com"))

    def test_setEmail_invalid_no_domain(self):
        self.assertFalse(self.user.setEmail("john.smith@"))

    def test_setEmail_invalid_no_username(self):
        self.assertFalse(self.user.setEmail("@example.com"))

    def test_setEmail_invalid_multiple_at_symbols(self):
        self.assertFalse(self.user.setEmail("john@smith@example.com"))

    def test_setEmail_invalid_whitespace(self):
        self.assertFalse(self.user.setEmail("john.smith @example.com"))

    def test_setEmail_invalid_missing_tld(self):
        self.assertFalse(self.user.setEmail("john.smith@example"))

    def test_setEmail_invalid_domain_start_with_period(self):
        self.assertFalse(self.user.setEmail("john.smith@.example.com"))

    def test_setEmail_invalid_domain_end_with_period(self):
        self.assertFalse(self.user.setEmail("john.smith@example.com."))

    def test_setEmail_invalid_domain_multiple_periods(self):
        self.assertFalse(self.user.setEmail("john.smith@example..com"))

    def test_setEmail_valid_mixed_case(self):
        self.assertTrue(self.user.setEmail("JOHN.Smith@example.com"))

    def test_setEmail_valid_unicode(self):
        self.assertTrue(self.user.setEmail("jane.åström@example.com"))

    def test_setEmail_valid_subdomain(self):
        self.assertTrue(self.user.setEmail("jane.doe@subdomain.example.com"))

    def test_setEmail_invalid_long_string(self):
        self.assertFalse(self.user.setEmail("a" * 256 + "@example.com"))

    def test_setEmail_valid_underscore(self):
        self.assertTrue(self.user.setEmail("john_smith@example.com"))

    def test_setEmail_valid_dash(self):
        self.assertTrue(self.user.setEmail("john-smith@example.com"))

    def test_setEmail_invalid_username_start_with_period(self):
        self.assertFalse(self.user.setEmail(".john.smith@example.com"))


