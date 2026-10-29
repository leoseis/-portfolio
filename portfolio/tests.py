from django.test import SimpleTestCase
from django.urls import reverse, resolve


class PortfolioTests(SimpleTestCase):

    def test_url_configuration_loads(self):
        """
        Check that Django's URL configuration can be loaded.
        """
        from django.urls import get_resolver

        resolver = get_resolver()
        self.assertIsNotNone(resolver)

    def test_admin_url_resolves(self):
        """
        Check that Django recognises the admin URL.
        """
        match = resolve("/admin/")
        self.assertEqual(match.url_name, "index")


