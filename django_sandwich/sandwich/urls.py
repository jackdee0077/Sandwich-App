from django.urls import path
from sandwich.views import sandwichView, IngredientsView, SandwichGeneratorView,MenuView

urlpatterns = [path('',sandwichView.as_view(), name= 'sandwich'),
        path('ingredients/<str:ingredient_type>',IngredientsView.as_view(),name="ingredients_list"),
        path( '',sandwichView.as_view(),name='sandwish_homepage'),
        path('random', SandwichGeneratorView.as_view(), name='sandwich_generator'),
         path('menu', MenuView.as_view(), name='Menu')
        ]
