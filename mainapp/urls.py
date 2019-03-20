from django.urls import path,include
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/profile/', views.profile_menu,name="profilemenu"),
    path('accounts/addinvoice/', views.add_invoice,name="addinvoice"),
    path('accounts/invoicedetail/<no>/', views.invoice_detail,name="invoicedetail"),
    path('accounts/editinvoice/<pk>/', views.edit_invoice,name="editinvoice"),
    path('accounts/viewinvoice/', views.view_invoice,name="viewinvoice"),
    path('accounts/searchinvoice/', views.search_invoice,name="searchinvoice"),
    path('accounts/searchbyno/', views.searchbyno,name="searchbyno"),
    path('accounts/printinvcc/<invoice_no>/', views.print_inv_cc,name="printinvcc"),
    path('accounts/printinvhc/<invoice_no>/', views.print_inv_hc,name="printinvhc"),
    path('accounts/makeduesbill/', views.make_duesbill,name="makeduesbill"),
    path('accounts/makemoneyreciept/', views.make_moneyreciept,name="makemoneyreciept"),
    path('accounts/imageview/', views.image_view,name="imageview"),
]
