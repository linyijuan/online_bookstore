from django.shortcuts import render
from .models import Book
import MySQLdb

def book_list(request):	
	# Book.objects.create(ISBN = 9780072465631,title ='Database Management Systems',author = 'Raghu Ramakrishnan',publisher ='McGraw-Hill',keywords ='Database',year_of_publication = 2002,price = 47,format ='softcover',copies = 3,subject ='Database');
	# Book.objects.create(ISBN = 9780132943260,title ='Database Systems: A Practical Approach',author = 'Thomas Connolly',publisher ='Pearson',keywords ='Database',price = 61,year_of_publication = 2014,format ='hardcover',copies = 6,subject ='Database');
	# Book.objects.create(ISBN = 9780470624708,title ='Fundamentals of Database Management Systems', author = 'Mark L. Gillenson',publisher ='Wiley',keywords ='Database',year_of_publication = 2011,price =62,format ='hardcover',copies = 5,subject ='Database');
	# Book.objects.create(ISBN = 9780486635446,title ='Probability Theory: A Concise Course', author = 'Y. A. Rozanov',publisher ='Dover Publications',keywords ='Probability', year_of_publication = 2013,price =9,format ='softcover',copies = 25,subject ='Probability');
	# Book.objects.create(ISBN = 9780132569033,title ='Computer Science: An Overview ', author = 'J. Glenn Brookshear',publisher ='Addison-Wesley',keywords ='Computer Science',year_of_publication = 2011,price = 167.46,format ='hardcover',copies = 6,subject ='Computation');
	# Book.objects.create(ISBN = 9780137057382,title ='Curious Folks',author = 'Sherry Seethaler',publisher ='FT Press',keywords ='Curious Folks', year_of_publication = 2010,price = 60,format ='softcover',copies = 10,subject ='Literature'); 
	# Book.objects.create(ISBN = 9780521587020,title ='Frankenstein (Cambridge Literature)',author = 'Mary Shelley',publisher ='Cambridge Press', keywords ='Frankenstein',year_of_publication = 1998,price = 54,format ='hardcover',copies = 2,subject ='Literature');
	# Book.objects.create(ISBN = 9780735611313,title ='Code:The Hidden Language of Computer HW and SW',author = 'Charles Petzold',publisher ='Microsoft Press', keywords ='Code',year_of_publication = 2000,price = 65,format ='hardcover',copies = 8,subject ='Programming');
	# Book.objects.create(ISBN = 9781427798190,title ='Math for Moms and Dads:just for parents',author = 'Kaplan',publisher ='Kaplan Publishing', keywords ='Math',year_of_publication = 2008,price =36,format ='softcover',copies = 5,subject ='Math');
	# Book.objects.create(ISBN = 9781590282410,title ='Python Programming: An Introduction to CS',author = 'John Zelle',publisher ='Franklin Beedle Inc.', keywords ='Python',year_of_publication = 2010,price =18,format ='softcover',copies = 12,subject ='Programming');
	return render(request, 'test.html', {'book_list': Book.objects.all()})

def LoginPage(request):
	return render(request, 'login.html')

def index(request):
	return render(request, 'index.html',{'book_list': Book.objects.all()})

