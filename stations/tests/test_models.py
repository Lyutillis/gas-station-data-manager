import os

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from stations.models import Manager, Fuel, Station, Discount, Transaction
from config.settings import MEDIA_ROOT


class ModelsTests(TestCase):
    def test_create_manager(self):
        username="TestUser"
        email="test@user.com"
        password="123safety"
        first_name="Test"
        last_name="User"
        manager = Manager.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        self.assertEqual(manager.username, username)
        self.assertEqual(manager.email, email)
        self.assertEqual(manager.first_name, first_name)
        self.assertEqual(manager.last_name, last_name)
        self.assertTrue(manager.check_password(password))

    def test_manager_str(self):
        manager = Manager.objects.create_user(
            username="TestUser",
            email="test@user.com",
            password="123safety",
            first_name="Test",
            last_name="User",
        )
        self.assertEqual(str(manager), f"{manager.username} ({manager.first_name} {manager.last_name})")

    def test_fuel_str(self):
        fuel = Fuel.objects.create(
            name="Diesel",
            price=100
        )
        
        self.assertEqual(str(fuel), f"{fuel.name}: {fuel.price}$\litre")
    
    def test_station_str(self):
        manager = Manager.objects.create_user(
            username="TestUser",
            email="test@user.com",
            password="123safety",
            first_name="Test",
            last_name="User",
        )
        station = Station.objects.create(
            address="address",
            image=None,
        )
        station.managers.add(manager.pk)
        self.assertEqual(str(station), f"{station.address}")

    def test_station_image_upload(self):
        manager = Manager.objects.create_user(
            username="TestUser",
            email="test@user.com",
            password="123safety",
            first_name="Test",
            last_name="User",
        )
        station = Station.objects.create(
            address="address",
            image=None,
        )
        station.managers.add(manager.pk)

        station.image = SimpleUploadedFile(name='test_image.jpg', content=open(os.path.join(MEDIA_ROOT, "test_image.jpg"), 'rb').read(), content_type='image/jpeg')
        station.save()

        self.assertTrue(station.image.url)
        self.assertNotEqual(station.image.url, os.path.join(MEDIA_ROOT, "test_image.jpg"))

    def test_discount_str(self):
        discount = Discount.objects.create(
            description="Test discount",
            discount=10,
            is_active=True,
        )

        self.assertEqual(str(discount), f"{discount.discount}%: {discount.description}")

    def test_transaction_str(self):
        discount = Discount.objects.create(
            description="Test discount",
            discount=10,
            is_active=True,
        )
        fuel = Fuel.objects.create(
            name="Diesel",
            price=100
        )
        manager = Manager.objects.create_user(
            username="TestUser",
            email="test@user.com",
            password="123safety",
            first_name="Test",
            last_name="User",
        )
        station = Station.objects.create(
            address="address",
            image=None,
        )
        station.managers.add(manager.pk)

        transaction = Transaction.objects.create(
            fuel=fuel,
            amount=5,
            station=station,
            discount=discount,
        )

        self.assertEqual(str(transaction), f"{transaction.date}: total {transaction.total}$|{transaction.fuel.name}")
    
    def test_transaction_total_values(self):
        discount_active = Discount.objects.create(
            description="Test discount",
            discount=10,
            is_active=True,
        )
        discount_not_active = Discount.objects.create(
            description="Test discount",
            discount=10,
            is_active=False,
        )
        fuel = Fuel.objects.create(
            name="Diesel",
            price=100
        )
        manager = Manager.objects.create_user(
            username="TestUser",
            email="test@user.com",
            password="123safety",
            first_name="Test",
            last_name="User",
        )
        station = Station.objects.create(
            address="address",
            image=None,
        )
        station.managers.add(manager.pk)

        transaction = Transaction.objects.create(
            fuel=fuel,
            amount=5,
            station=station,
            discount=discount_not_active,
        )

        expected_total = transaction.amount * transaction.fuel.price
        self.assertEqual(transaction.total, expected_total)
        self.assertEqual(transaction.discount_total, 0)

        transaction = Transaction.objects.create(
            fuel=fuel,
            amount=5,
            station=station,
            discount=discount_active,
        )

        expected_total = transaction.amount * transaction.fuel.price
        discount_total_expected = expected_total * (transaction.discount.discount / 100)
        self.assertEqual(transaction.discount_total, discount_total_expected)
        self.assertEqual(transaction.total, expected_total - discount_total_expected)
