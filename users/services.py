import stripe
from rest_framework.reverse import reverse_lazy

from config.settings import STRIPE_KEY

stripe.api_key = STRIPE_KEY


def create_product(name):
    """ Create Stripe product """
    return stripe.Product.create(name=name)


def create_price(amount, product):
    """ Create Stripe price """
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product.get('id')
    )


def create_session(price):
    """ Create Stripe session """

    success_url = f"http://localhost:8000/{reverse_lazy('payments')}"
    session = stripe.checkout.Session.create(
        success_url=success_url,
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
