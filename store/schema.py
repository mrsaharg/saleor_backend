import graphene
from graphene_django.types import DjangoObjectType
from .models import Product

# product type
class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("name", "type", "sku", "quantity")  # Ensure all fields are included

# mutation: add
class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        type = graphene.String(required=True)
        sku = graphene.String(required=True)
        quantity = graphene.Int(required=True)

    product = graphene.Field(ProductType)

    def mutate(self, info, name, type, sku, quantity):
        if Product.objects.filter(sku=sku).exists():
            raise Exception(f"Product with SKU '{sku}' already exists.")

        product = Product(name=name, type=type, sku=sku, quantity=quantity)
        product.save()
        return CreateProduct(product=product)

# mutation: update
class UpdateProduct(graphene.Mutation):
    class Arguments:
        sku = graphene.String(required=True)
        name = graphene.String()
        type = graphene.String()
        quantity = graphene.Int()

    product = graphene.Field(ProductType)

    def mutate(self, info, sku, name=None, type=None, quantity=None):
        product = Product.objects.filter(sku=sku).first()
        if not product:
            raise Exception(f"Product with SKU '{sku}' not found.")
        if name:
            product.name = name
        if type:
            product.type = type
        if quantity is not None:
            product.quantity = quantity

        product.save()
        return UpdateProduct(product=product)

# mutation: delete
class DeleteProduct(graphene.Mutation):
    class Arguments:
        sku = graphene.String(required=True)

    success = graphene.Boolean()
    message = graphene.String()

    def mutate(self, info, sku):
        product = Product.objects.filter(sku=sku).first()
        if not product:
            return DeleteProduct(success=False, message=f"Product with SKU '{sku}' not found.")

        product.delete()
        return DeleteProduct(success=True, message="Product deleted successfully.")

# fetch and filter
class Query(graphene.ObjectType):
    all_products = graphene.List(
        ProductType, 
        type=graphene.String(),
        search=graphene.String()
    )

    def resolve_all_products(self, info, type=None, search=None):
        #start
        products = Product.objects.all()

        #filter by type
        if type:
            products = products.filter(type__icontains=type)

        #search
        if search:
            products = products.filter(name__icontains=search) | products.filter(sku__icontains=search)

        return products

class Mutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    delete_product = DeleteProduct.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
