import json
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import *
from datetime import date

"""
what is views ?
    It returns some page when the users request 
    It is a python function that accepts request from the user
    and then provides information
    
"""

# Create your views here.
def showHomePage(request):
    return render(request, 'index.html')

def bookDetails(request, bookId):
    return HttpResponse("<h1>The Id you have entered is: "+str(bookId)+"</h1>")

# show the page to add book
@login_required(login_url='login.html')
def addBook(request):
    return render(request, 'addBook.html')

# handle the jsonRequst of AddBook
def addBookRequestHandle(request):
    if request.method == 'POST': 
        try:
            json_data = json.loads(request.body)
            
            authors = json_data.get("authorsOfBook")
            listOfAuthors = []
            for author in  authors :                
                listOfAuthors.append(
                    Author.objects.create(
                    authorName = author.get("name"),
                    profileUrl = author.get("profileLink")
                ))
                
            new_book = Book.objects.create(
                title = json_data.get("title"), 
                edition = json_data.get("edition"),
                publisher = json_data.get("publisher"), 
                imageUrl = json_data.get("imageUrl"), 
                description = json_data.get("description")
            )
            new_book.authorsOfBook.set(listOfAuthors)
            
            return JsonResponse({'message': 'Book added successfully'}, status = 201)
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        return HttpResponseBadRequest('Only POST requests are allowed')


# show the page for add user
def addUser(request):
    return render(request, 'addUser.html')

# handle the jsonRequest of AddUser
def addUserRequestHandle(request):
    if request.method == 'POST': 
        try:
            json_data = json.loads(request.body)
                
            new_user = CustomUser.objects.create(
                username = json_data.get("username"), 
                password = make_password(json_data.get("passwordHash")),
                institution = json_data.get("institution"), 
                dateOfRes = date.today(), 
                phoneNo = json_data.get("phoneNo"),
                email = json_data.get("email"),
                rating = 0
            )
            
            new_location = PresentAddress.objects.create(
                userId = new_user,
                place = json_data.get("place"),
                upzilla = json_data.get("upzilla"),
                district = json_data.get('district')
            )
            
            
            return JsonResponse({'message': 'User added successfully'}, status = 201)
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        return HttpResponseBadRequest('Only POST requests are allowed')
 
# handle getBooksRequest   
def getBooksRequestHandler(request):
    books = Book.objects.order_by('?')[:2]
    books_json = []
    for book in books:
        book_dict = {
            'title': book.title,
            'edition': book.edition,
            'publisher': book.publisher,
            'imageUrl': book.imageUrl,
            'description': book.description,
        }
        books_json.append(book_dict)
    return JsonResponse(books_json, safe= False)

# show login page
def showLoginPage(request):
    return render(request, 'login.html')

# handle login request
def loginRequestHandle(request):
    if request.method == 'POST': 
        try:
            json_data = json.loads(request.body)
                
            
            username = json_data.get("username") 
            password = json_data.get("passwordHash")
            
            # print(username + " "+ password)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Success")
                return JsonResponse({'message': 'Login successful'}, status=201)
            else:
                print("No success")
                return JsonResponse({'message': 'User not found'}, status=401)
            
        
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        return HttpResponseBadRequest('Only POST requests are allowed')
