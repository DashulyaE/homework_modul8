import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(pay):
    """Создает продукт в страйпе"""

    title_product = f"{pay.paid_course}" if pay.paid_course else f"{pay.paid_lesson}"
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get("id")


def create_stripe_price(stripe_product_id, amount):
    """Создаём цену в страйпе"""

    return stripe.Price.create(
        currency="rub",
        unit_amount=int(amount * 100),
        product=stripe_product_id,
    )


def create_stripe_session(price):
    """Создаём сессию в страйпе"""
    try:
        session = stripe.checkout.Session.create(
            success_url="http://127.0.0.1:8000/users/payment/create/",
            line_items=[{"price": price.get("id"), "quantity": 1}],
            mode="payment",
        )
        print(session)  # Для отладки
        return session.id, session.url
    except Exception as e:
        print(f"Stripe error: {e}")
        return None, None
