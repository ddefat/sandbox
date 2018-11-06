import factory

from factory import DjangoModelFactory


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = "caesar.Product"

    name = factory.Sequence(lambda n: 'Product %d' % n)
    reference = factory.Faker('text', max_nb_chars=25)
    price = factory.Faker('random_number', digits=5)
    created_date = factory.Faker('date_time_this_year')