from django.test import TestCase
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class SerializerTestCase(TestCase):
    def setUp(self):
        self.serializer_data = {
            'username':'test_user',
            'email':'test_email@mail.com',
            'groups':'test_group'
        }
        self.serializer = UserSerializer()


    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['username', 'email', 'groups']))

    def test_color_must_be_in_choices(self):
        serializer = UserSerializer(data=self.serializer_data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.data, {'username' : 'test_user', 'email' : 'test_email@mail.com','groups' : 'test_group'})
