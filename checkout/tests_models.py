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


# class TestCheckoutOrderLineItem(TestCase):

#     def test_check_order_exists(self):
#         order_number = Order(id=1, order_total=699.00)
#         order_number.save()
#         service_detail = Service(name="Test service")
#         service_detail.save()
#         orderLineItem = OrderLineItem(service='service.name',
#                                       select_date='25-Jan-2021 23:00',
#                                       quantity=1, lineitem_total=699.00,
#                                       order=order_number)

#         orderLineItem.save()
#         self.assertEqual(orderLineItem.service, 'service.name')
#         self.assertEqual(orderLineItem.select_date, '25-Jan-2021 23:00')
#         self.assertEqual(orderLineItem.quantity, 1)
#         self.assertEqual(orderLineItem.lineitem_total, 699.00)

    # def test_price_by_quantiy(self):
    #     order_number = Order(id=1, order_total=49.00)
    #     order_number.save()
    #     lineitem_total = OrderLineItem(quantity=2,
    #                                    order=order_number)
    #     lineitem_total.save()
    #     self.assertEqual(lineitem_total.self.price * lineitem_total.quantity, 98.00)
