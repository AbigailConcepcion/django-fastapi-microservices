from apps.products.models import Product

class ProductRepository:

    @staticmethod
    def list():
        return Product.objects.all()

    @staticmethod
    def get(product_id: int):
        return Product.objects.filter(id=product_id).first()

    @staticmethod
    def create(**data):
        return Product.objects.create(**data)
