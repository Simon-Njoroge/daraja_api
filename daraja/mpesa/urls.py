from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('stk_push/',views.stk_push, name='stk_push'),
    path('thankyou/',views.thank_you,name='thank_you')
]
