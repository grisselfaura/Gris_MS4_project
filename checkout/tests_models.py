from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Service


class TestCheckoutOrderModel(TestCase):

    def test_billing_address(self):
        billing_address = Order(full_name='Test Billing Name',
                                street_address1='Test Address1',
                                street_address2='Test Address2',
                                town_or_city='Test City',
                                postcode='Test Postcode',
                                country='Test Country')

        self.assertEqual(billing_address.full_name, 'Test Billing Name')
        self.assertEqual(billing_address.street_address1, 'Test Address1')
        self.assertEqual(billing_address.street_address2, 'Test Address2')
        self.assertEqual(billing_address.town_or_city, 'Test City')
        self.assertEqual(billing_address.postcode, 'Test Postcode')
        self.assertEqual(billing_address.country, 'Test Country')

    def test_request_order(self):
        order = Order(order_total=999.00, email='testmode@gmail.com')
        order.save()
        self.assertEqual(order.order_total, 999.00)
        self.assertEqual(order.email, 'testmode@gmail.com')


class TestCheckoutOrderLineItem(TestCase):

    def test_check_order_exists(self):
        order_number = Order(id=1, order_total=699.00)
        order_number.save()
        service_detail = Service(name="Test service", price=699.00)
        service_detail.save()
        orderLineItem = OrderLineItem(service=service_detail,
                                      select_date='2021-12-10 22:00',
                                      quantity=1, order=order_number)

        orderLineItem.save()
        self.assertEqual(orderLineItem.service, service_detail)
        self.assertEqual(orderLineItem.select_date, '2021-12-10 22:00')
        self.assertEqual(orderLineItem.quantity, 1)
        self.assertEqual(orderLineItem.lineitem_total, 699.00)
