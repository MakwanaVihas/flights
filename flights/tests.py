from django.test import TestCase,Client
from .models import Airport ,Flight
# Create your tests here.
class ModelsTestCase(TestCase):
    def setUp(self):
        a1 = Airport.objects.create(code="AAA",city="aaa")
        a2=Airport.objects.create(code="BBB",city="bbb")

        Flight.objects.create(origin=a1,destination=a2,duration=100)
        Flight.objects.create(origin=a1,destination=a2,duration=200)
        Flight.objects.create(origin=a1,destination=a1,duration=-300)
    def test_departure_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),3)
    def test_index(self):
       c=Client()
       response=c.get("/")
       self.assertEqual(response.status_code,200)
       self.assertEqual(response.context["flights"].count(),3)
