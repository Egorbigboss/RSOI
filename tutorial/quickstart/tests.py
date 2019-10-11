from django.test import TestCase
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class SerializerTestCase(TestCase):
    def setUp(self):
        self.serializer_data = {
            'username':'test_user',
            'email':'test_email@mail.com',
            'group':'test_group'
        }


        self.serializer = UserSerializer()

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['username', 'email', 'groups']))
