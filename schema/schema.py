from graphene_django import DjangoObjectType
import graphene

from products.models import Category, Products


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class ProductsType(DjangoObjectType):
    class Meta:
        model = Products


class Query(graphene.ObjectType):
    category = graphene.List(CategoryType)
    product = graphene.List(ProductsType)

    def resolve_category(self, info):
        return Category.objects.all()

    def resolve_product(self, info):
        return Products.objects.all()


schema = graphene.Schema(query=Query)
