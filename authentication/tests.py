from django.test import TestCase

from authentication.models import Account

class AccountTest(TestCase):
    def testEmpty(self):
        with self.assertRaises(TypeError):
            Account.objects.create_user()

    def testInvalidEmailUser(self):
        #insufficient arguments
        with self.assertRaises(ValueError):
            Account.objects.create_user('test@test.com')

        #not an email address
        #with self.assertRaises(ValueError):
        #    Account.objects.create_user('test', username='test')

        #not a valid username
        with self.assertRaises(ValueError):
            Account.objects.create_user('test@test.com', username='')

    def testFields(self):
        a = Account.objects.create_user('test@test.com', username='test')

        self.assertEqual(str(a.email), 'test@test.com', 'Emails do not match')
        self.assertEqual(str(a.username), 'test', 'Usernames do not match')

    """
    def testDuplicate(self):
        #duplicate email and username
        with self.assertRaises(ValueError):
            Account.objects.create_user('test@test.com', username='test')
        #duplicate email
        with self.assertRaises(ValueError):
            Account.objects.create_user('test@test.com', username='test1')
        #duplicate username
        with self.assertRaises(ValueError):
            Account.objects.create_user('test1@test.com', username='test')
    """

    def testLatestCreated(self):
        b = Account.objects.create_user('test2@test.com', username='test2')
        self.assertEqual(Account.objects.latest('created_at'),
                         b,
                         'Latest not updating correctly'
        )
