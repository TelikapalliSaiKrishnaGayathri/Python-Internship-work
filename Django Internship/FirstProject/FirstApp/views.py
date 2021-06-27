from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hello Good Evening All...")

def htmltag(y):
	return HttpResponse("<h2>Hi Welcome to APSSDC</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:red'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:grey;padding:26px'>Hi User <span style='color:green'>{}</span> and your age is: <span style='color:blue'>{}</span></h3>".format(un,ag))


def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert<h3>('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is:{}</h3>".format(ename,ename,eage,eid))


def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailID':email}
		return render(req,'html/display.html',data)
	

	return render(req,'html/myform.html')


def register(request):
	if request.method=="POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST.get('email')
		address = request.POST['address']
		phonenumber = request.POST.get('phonenumber')
		gender = request.POST['gender']
		lang = request.POST.getlist('lang')
		d = {'firstname':firstname,'lastname':lastname,'email':email,'address':address,'phonenumber':phonenumber,'gender':gender,'lang':lang}
		return render(request,'html/show.html',d)

	return render(request,'html/registerboot.html')

def loginpage(request):
	if request.method=="POST":
		usrname = request.POST.get('usrname')
		pwd = request.POST.get('pwd')
		d1 = {'usrname':usrname,'pwd':pwd}
		return render(request,'html/disp.html')
	
	return render(request,'html/login.html')


def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def btregi(request):
	return render(request,'html/btregst.html')


def register1(request):
	#name = "Krishna"
	#email = "krishna26@gmail.com"
	reg = Register(name = "Krishna",email = "Krishna26@gmail.com")
	reg.save()
	return HttpResponse("record entered successfully!")

def register2(request):
	if request.method=="POST":
		name = request.POST['name']
		email = request.POST.get('email')
		reg = Register(name = name, email = email)
		reg.save()
		return HttpResponse("Record entered successfully!")

	return render(request,'html/register2.html')


def disp(request):
	data = Register.objects.all()
	return render(request,'html/disp1.html',{'data':data})


def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("Your Name is: {} and your email ID is: {}".format(w.name,w.email))


def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/disp')
	return render(request,'html/supdate.html',{'p':t})


def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/disp')
	return render(request,'html/sndlt.html',{'z':b})

