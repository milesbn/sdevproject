from django import template
from products.models import Product

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def cart_total(cart):
    total = 0
    for id, item in cart.items():
        total += float(item['price']) * item['quantity']
    return total

@register.filter(name='mul') 
def mul(value, arg):
    return float(value) * arg