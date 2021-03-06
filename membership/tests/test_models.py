from django.test import TestCase
import datetime

from membership.models import User, Customer, Class


class UserTestCase(TestCase):
    # Create your tests here.

    def __init__(self, *args, **kwargs):
        self.today = datetime.date.today()

        super(UserTestCase, self).__init__(*args, **kwargs)
        self.username1 = "test_1"
        self.firstname1 = "first_name_1"
        self.lastname1 = "last_name_1"
        self.email1 = "email1@hotmail.com"
        self.age = 40
        self.date_of_birth1 = "{}-{}-{}".format(
            self.today.year - 40, self.today.month, self.today.day)
        self.address1 = "1/1 north pole"
        self.telephone1 = "0812345678"

        self.male = "male"
        self.wrong_gender = "wrong"

    def setUp(self):
        from allauth.account.models import EmailAddress
        self.user1 = User.objects.create(username=self.username1,
                                         first_name=self.firstname1,
                                         last_name=self.lastname1,
                                         date_of_birth=self.date_of_birth1,
                                         address=self.address1,
                                         telephone=self.telephone1,
                                         gender=self.male)
        # create email for user 1
        EmailAddress.objects.create(
            user_id=self.user1.id, email=self.email1, primary=True)

        self.user2 = User.objects.create(username="test_name_2",
                                         first_name="first_name_2",
                                         last_name="last_name_2",
                                         gender=self.wrong_gender)
        # create email for user 1
        EmailAddress.objects.create(
            user_id=self.user2.id, email="email2-1@hotmail.com", primary=True)
        EmailAddress.objects.create(
            user_id=self.user2.id, email="email2-2@hotmail.com", primary=False)
        EmailAddress.objects.create(
            user_id=self.user2.id, email="email2-3@hotmail.com", primary=False)

    def test_default_telephone(self):
        """test if telephone didn't given"""
        self.assertEqual("0XX-XXX-XXXX", self.user2.telephone)

    def test_default_address(self):
        """test if address didn't given"""
        self.assertEqual("unknown", self.user2.address)

    def test_gender_validation(self):
        """test default gender"""
        self.assertEqual("unknown", self.user2.gender)

    def test_email_exist(self):
        """test get_email method"""
        self.assertEqual(self.email1, self.user1.get_email().email)

    def test_multiple_email_size(self):
        """test get_emails method"""
        self.assertEqual(3, len(self.user2.get_emails()))

    # TODO: move this to customer model testing
    # for customer
    # def test_default_class(self):
    #     """test if class didn't given"""
    #     user2 = User.objects.get(username="test_name_2")
    #     self.assertEqual("None", user2.classes.name)

    def test_correctly_firstname(self):
        """test firstname in database"""
        self.assertEqual(self.firstname1, self.user1.first_name)

    def test_correctly_age(self):
        """test calculate age in database"""
        self.assertEqual(self.age, self.user1.get_age())

    def test_correctly_birthday(self):
        """test is birthday save correctly"""
        from django.utils.dateparse import parse_date
        self.assertEqual(parse_date(self.date_of_birth1),
                         self.user1.date_of_birth)
