from django.urls import path
from pages import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('login', views.login, name='login'),
    path('/logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('withdraw', views.withdraw, name='dashboard/withdraw'),
    path('trading', views.trading, name='dashboard/trading'),
    path('fund', views.fund, name='dashboard/fund'),
    path('bitcoin', views.bitcoin, name='coins/bitcoin'),
    path('ethereum', views.ethereum, name='coins/ethereum'),
    path('usdterc20', views.usdterc20, name='coins/usdterc20'),
    path('usdttrc20', views.usdttrc20, name='coins/usdttrc20'),
    path('longtime', views.longtime, name='trades/longtime'),
    path('shorttime', views.shorttime, name='trades/shorttime'),
    path('withdrawal', views.withdrawal, name='dashboard/withdrawal'),

]
