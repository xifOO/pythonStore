from config.settings import CART_SESSION_ID
from products.models import Product


class Cart(object):
    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """Перебор товаров в корзине и получение товаров из базы данных"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, product, quantity, update_quantity=False):
        """Добавить или обновить количество товара в корзине"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"price": str(product.price), "quantity": 0}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        """Удалить товар из корзины"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        """Сохранение сессии корзины"""
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def get_total_price(self):
        """Получение общей суммы корзины"""
        return sum(int(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Удаляем сессию корзины"""
        del self.session[CART_SESSION_ID]
        self.session.modified = True