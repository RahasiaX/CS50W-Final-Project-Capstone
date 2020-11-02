from .models import Shoe, ShoeSize
import django_filters
from django import forms

BRAND_CHOICES = (
    ('Nike', 'Nike'),
    ('Air Jordan', 'Air Jordan'),
    ('adidas', 'adidas'),
    ('A Bathing Ape', 'A Bathing Ape'),
)

SIZES_CHOICES = (
    ('5', '5'),
    ('5.5', '5.5'),
    ('6', '6'),
    ('6.5', '6.5'),
    ('7', '7'),
    ('7.5', '7.5'),
    ('8', '8'),
    ('8.5', '8.5'),
    ('9', '9'),
    ('9.5', '9.5'),
    ('10', '10'),
    ('10.5', '10.5'),
    ('11', '11'),
    ('11.5', '11.5'),
    ('12', '12'),
    ('12.5', '12.5'),
    ('13', '13'),
    ('13.5', '13.5'),
    ('14', '14'),
    ('14.5', '14.5'),
)

COLLAB_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

COLOR_CHOICES = (
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Brown', 'Brown'),
    ('Green', 'Green'),
    ('Grey', 'Grey'),
    ('Orange', 'Orange'),
    ('Pink', 'Pink'),
    ('Purple', 'Purple'),
    ('Red', 'Red'),
    ('White', 'White'),
    ('Yellow', 'Yellow'),
    ('Multicolor', 'Multicolor'),
    ('Other', 'Other')
)

ORDER_CHOICES = (
    ('price_asc', 'Price ascending'),
    ('price_desc', 'Price descending'),
    ('latest', 'Latest'),
    ('model_asc', 'A-Z'),
    ('model_desc', 'Z-A'),
)

class ShoeFilter(django_filters.FilterSet):
    brand = django_filters.MultipleChoiceFilter(choices=BRAND_CHOICES, widget=forms.CheckboxSelectMultiple)
    shoesize__size = django_filters.MultipleChoiceFilter(label='Sizes', choices=SIZES_CHOICES, widget=forms.CheckboxSelectMultiple, field_name='shoesize__size')
    collaboration = django_filters.MultipleChoiceFilter(choices=COLLAB_CHOICES, widget=forms.CheckboxSelectMultiple)
    shoecolor__color = django_filters.MultipleChoiceFilter(label='Color', choices=COLOR_CHOICES, widget=forms.CheckboxSelectMultiple, field_name='shoecolor__color')
    shoesize__price = django_filters.NumberFilter()
    shoesize__price__gt = django_filters.NumberFilter(label='From', field_name='shoesize__price', lookup_expr='gt')
    shoesize__price__lt = django_filters.NumberFilter(label='To', field_name='shoesize__price', lookup_expr='lt')
    ordering = django_filters.ChoiceFilter(label='Sort By', choices=ORDER_CHOICES, method='filter_by_order', field_name='ordering')

    class Meta:
        model = Shoe
        fields = ['brand', 'collaboration', 'shoesize__size', 'shoecolor__color', 'shoesize__price', 'ordering']

    def filter_by_order(self, queryset, name, value):
        if value == 'price_asc':
            expression = 'shoesize__price'
        elif value == 'price_desc':
            expression = '-shoesize__price'
        elif value == 'latest':
            expression = '-id'
        elif value == 'model_asc':
            expression = 'model'
        elif value == 'model_desc':
            expression = '-model'
        return queryset.order_by(expression)