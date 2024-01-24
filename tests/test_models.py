from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuTest(TestCase):
    def setUp(self) -> None:
        self.item1 = Menu.objects.create(
            title = 'Pizza',
            price = 12.99,
            inventory = 10
        )

    def test_create_menu_item(self) -> None:
        item2 = Menu.objects.create(
            title = 'Burger',
            price = 17.99,
            inventory = 5
        )
        self.assertEqual(Menu.objects.count(), 2)
        self.assertEqual(item2.title, 'Burger')
        self.assertEqual(item2.price, Decimal(17.99))
        self.assertEqual(item2.inventory, 5)

    def test_get_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        self.assertEqual(item.title, 'Pizza')
        self.assertEqual(item.price, Decimal(12.99).quantize(Decimal("0.00")))
        self.assertEqual(item.inventory, 10)

    def test_delete_menu_item(self) -> None:
        item = Menu.objects.get(id = self.item1.id)
        item.delete()
        self.assertEqual(Menu.objects.count(), 0)