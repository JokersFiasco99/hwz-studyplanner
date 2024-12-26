from .models import Category

def create_default_categories():
    default_categories = ['Studium', 'Arbeit', 'Sport', 'Familie', 'Freizeit']
    for cat_name in default_categories:
        Category.objects.get_or_create(name=cat_name)
