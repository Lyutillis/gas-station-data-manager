from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="123safety"
        )
        self.client.force_login(self.admin_user)
        self.manager = get_user_model().objects.create_user(
            username="TestUser",
            email="test@user.com",
            password="123safety",
            first_name="Test",
            last_name="User",
        )

    def test_manager_add_fieldsets_present(self):
        url = reverse("admin:stations_manager_add")
        res = self.client.get(url)
        self.assertContains(res, "First name")
        self.assertContains(res, "Last name")
