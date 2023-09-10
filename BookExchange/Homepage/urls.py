from django.urls import path
from . import views

urlpatterns = [
    # homepage/
    path('', views.showHomePage, name='homepage'),
    
    # handle book request
    path('getbooks/', views.getBooksRequestHandler, name='getBooksRequestHandle'),

    # homepage/showbook/<id>          
    path('showbook/<int:bookId>/', views.bookDetails, name='book_details'),
    
    # show the from for addBook
    path('addbook/', views.addBook, name='add_book'),
    
    # add the book to the dataBase 
    path('addbook/post/', views.addBookRequestHandle, name='addBookHandle'),  
    
    # show the page for addUser
    path('adduser/', views.addUser, name='add_user'),
    
    # add the user to the DB
    path('adduser/post/', views.addUserRequestHandle, name='addUserHandle'),
    
    #show the login page
    path('login/', views.showLoginPage, name='login'),
    
    #handle the login request
    path('login/post/', views.loginRequestHandle, name='loginHandle'),
    
    
]