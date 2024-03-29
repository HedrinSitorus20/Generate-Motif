from django .shortcuts import render,redirect
from subprocess import run,PIPE
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages 
from django.core.files.storage import FileSystemStorage
from .models import MotifForm1
from django.contrib.auth.models import User
from .models import Post
from django.contrib.sessions.models import Session
from itertools import zip_longest
import sys, os, re



@login_required(login_url='login')
def image(request):
    user = request.user
    status = user.is_staff
    
    if status == 0:
          status=None
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2 active','nav-link nav-link-3','nav-link nav-link-4']
    return render(request, 'home.html',{"status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def loading(request):
    user = request.user
    status = user.is_superuser

    if status == 1:
          Autentificate = 1
    users = User.objects.all()
    JumlahAkun = User.objects.count()
    
    jumlah_data = Session.objects.count()
    jumlah_Motif = MotifForm1.objects.count()

    return render(request, 'checkLoading.html',{'users':users,'status':Autentificate,'jmlOnline_user':jumlah_data,'jmlMotif':jumlah_Motif,'jmlAkun':JumlahAkun})

@login_required(login_url='login')
def UpdateUser(request, id):
     user = User.objects.get(id = id)

     return render(request, 'UpdateUser.html',{'user':user})

@login_required(login_url='login')
def updaterecord(request, id):
    staff = request.POST['staff']
    active = request.POST['active']
    admin = request.POST['admin']
    member = User.objects.get(id=id)
    member.is_staff = staff
    member.is_active = active
    member.is_superuser = admin
    member.save()
    messages.info(request, 'Data berhasil di ubah')

    return redirect('Monitoring')

@login_required(login_url='login')
def generator(request):
    navlink = ['nav-link nav-link-1 active ','nav-link nav-link-2','nav-link nav-link-3','nav-link nav-link-4']
    return render(request, 'started.html', {'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def external(request):
    jmlBaris = request.POST.get('jmlBaris')
    Baris = "1"
    user = request.user
    username = user.username
    length = len(username)
    # ModeGenerate = request.POST.get('ModeGenerate')
    image=request.FILES['image']
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2 active','nav-link nav-link-3','nav-link nav-link-4']
    path = os.getcwd()
    # print("path now", path)
    # print("image is ", image)
    user = request.user
    status = user.is_staff
    
    if status == 0:
          status=None
    
    fs = FileSystemStorage()
    filename = fs.save(image.name, image)
    fileurl = fs.open(filename)
    templateurl = fs.url(filename)
    # print("file raw url",filename)
    # print("file full url", fileurl)
    # print("template url ", templateurl)

    #Cek format gambar
    formatStatus =run([sys.executable,'utils\\checkformat.py', str(fileurl)],shell=False,stdout=PIPE)
    formatStatus = formatStatus.stdout.strip().decode("utf-8")
    
    if(formatStatus == "0"):
         messages.success(request, "Format file yang diproses hanya menerima jpg")
         return render(request, 'home.html', {"jmlBaris": jmlBaris, "status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

    # check jumlah baris dan inisiasi baris
    rowStatus =run([sys.executable,'utils\\checkrow.py', jmlBaris],shell=False,stdout=PIPE)
    rowStatus = rowStatus.stdout.strip().decode("utf-8")
    # print(rowStatus)
    isOverRow = rowStatus[0]

    if(isOverRow == "0"):
         messages.success(request, "Jumlah baris yang dapat dihasilkan berkisar dari 2 hingga 40")
         return render(request, 'home.html', {"jmlBaris": jmlBaris, "status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

    # check spesifikasi gambar
    status =run([sys.executable,'utils\\check.py', str(fileurl)],shell=False,stdout=PIPE)
    status = status.stdout.strip().decode("utf-8")
    state = status[0]
    imgHeight = status[1:]
    
    
    if state == "0":
        return render(request,'failed.html',{'imgHeight':imgHeight})
    
    status =run([sys.executable,'utils\\checkLidi.py', str(fileurl)],shell=False,stdout=PIPE)
    status = status.stdout.strip().decode("utf-8")
    state = status[0]
    imgWidth = status[1:]
    
    jmlBaris = int(jmlBaris)
    if state == "0":
        return render(request,'failedWidth.html',{'imgWidth':imgWidth})
    else:
        # image =run([sys.executable,'C:\\xampp\\htdocs\\TugasAkhir\\image.py', str(fileurl), str(filename), jmlBaris, Baris, ModeGenerate],shell=False,stdout=PIPE)
        if(jmlBaris %2 == 0):
            jmlBaris = str(jmlBaris)
            image =run([sys.executable,'utils\\CreateimageEven.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
            image2 =run([sys.executable,'utils\\CreateimageEven.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
            image3 =run([sys.executable,'utils\\CreateimageEven.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
            image4 =run([sys.executable,'utils\\CreateimageEven.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
        else:
            jmlBaris = str(jmlBaris)
            image =run([sys.executable,'utils\\CreateimageOdd.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
            image2 =run([sys.executable,'utils\\CreateimageOdd.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
            image3 =run([sys.executable,'utils\\CreateimageOdd.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
            image4 =run([sys.executable,'utils\\CreateimageOdd.py', str(fileurl), str(filename), jmlBaris, Baris, "4", username],shell=False,stdout=PIPE)
        
        image = image.stdout.strip().decode("utf-8")
        image2 = image2.stdout.strip().decode("utf-8")
        image3 = image3.stdout.strip().decode("utf-8")
        image4 = image4.stdout.strip().decode("utf-8")
        

        UrutanLidi = image[(44+length):]
        URLEdit = image[:(44+length)]

        UrutanLidi2 = image2[(44+length):]
        URLEdit2 = image2[:(44+length)]

        UrutanLidi3 = image3[(44+length):]
        URLEdit3 = image3[:(44+length)]

        UrutanLidi4 = image4[(44+length):]
        URLEdit4 = image4[:(44+length)]


        jenisGenerate = ['Tabu Search', 'Greedy Serach', 'Random Search', 'ACO']

        return render(request, 'motif.html',{'user':username,'jmlBaris':jmlBaris, 'raw_url':templateurl, 'edit_url': URLEdit, 'urutan_lidi':UrutanLidi, 'edit_url2': URLEdit2, 'urutan_lidi2':UrutanLidi2, 'edit_url3': URLEdit3, 'urutan_lidi3':UrutanLidi3, 'edit_url4': URLEdit4, 'urutan_lidi4':UrutanLidi4, 'jenis1':jenisGenerate[3], 'jenis2':jenisGenerate[3], 'jenis3':jenisGenerate[3], 'jenis4':jenisGenerate[3],'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def save(request):
    MotifAsal = request.POST.get('image2')
    MotifHasil = request.POST.get('image3')
    Urutan = request.POST.get('urutan')
    Urutan = Urutan[1:-1]
    jenisGenerate = request.POST.get('JenisGenerate')
    jmlBaris = request.POST.get('jmlBaris')
    user = request.POST.get('user')
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2 active','nav-link nav-link-3','nav-link nav-link-4']
    path = os.getcwd()
    # print("path now", path)

    image2 =run([sys.executable,'utils\\saveImagePath.py', str(MotifAsal)],shell=False,stdout=PIPE)
    image3 =run([sys.executable,'utils\\saveImagePath2.py', str(MotifHasil), user],shell=False,stdout=PIPE)

    return render(request, 'download.html',{'user':user,'jmlBaris':jmlBaris,'raw_url1':image2.stdout.strip().decode("utf-8"), 'edit_url1': image3.stdout.strip().decode("utf-8"), 'Urutan':str(Urutan), 'jenis': str(jenisGenerate),'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def PostImage(request):
        if request.method == 'POST':
            if request.POST.get('imgBefore') and request.POST.get('imgAfter') and request.POST.get('urutanLidi') and request.POST.get('jenisGenerate') and request.POST.get('jmlBaris') and request.POST.get('user'):
                    post=MotifForm1()
                    post.imgBefore= request.POST.get('imgBefore')
                    post.imgAfter= request.POST.get('imgAfter')
                    post.urutanLidi = request.POST.get('urutanLidi')
                    post.jenisGenerate = request.POST.get('jenisGenerate')
                    post.jmlBaris = request.POST.get('jmlBaris')
                    post.user = request.POST.get('user')
                    post.save()
                    
                    return render(request, 'success.html')  

            else:
                    return render(request,'success.html')

@login_required(login_url='login')
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'createpost.html')  

        else:
                return render(request,'createpost.html')

def tes(request):
    return render(request, 'createpost.html')

@login_required(login_url='login')
def Search(request):
    filter = request.POST.get('filter')
    f = request.POST.get('SearchMotif')
    user = request.user
    status = user.is_staff
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3 active','nav-link nav-link-4']

    if status == 0:
          status=None
    if filter == "Jumlah Baris":
        motifForm = MotifForm1.objects.all().filter(jmlBaris__iexact=f).values().order_by('time').reverse()
        filter=['Jumlah Baris','Nama','Tanggal']
    elif filter == "Nama":
        motifForm = MotifForm1.objects.all().filter(user__icontains= f).values().order_by('time').reverse()
        filter=['Nama','Jumlah Baris','Tanggal']
    elif filter == "Tanggal":
        motifForm = MotifForm1.objects.all().filter(time__icontains=f).values().order_by('time').reverse()
        filter=['Tanggal','Nama','Jumlah Baris']

    if (motifForm == ""):
         motifForm = None
    
    context = {"motifForm" : motifForm, "typeFilter1": filter[0], "typeFilter2": filter[1], "typeFilter3": filter[2], "valueFilter": f, "status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]}
    if(f == ''):
         return redirect('list1')
    return render(request,"search.html", context)

@login_required(login_url='login')
def show(request):
    user = request.user
    status = user.is_staff
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3 active','nav-link nav-link-4']
    if status == 0:
          status=None
    
    motifForm = MotifForm1.objects.all().values().order_by('time').reverse()
    paginator = Paginator(motifForm, 15)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    totalPage = page.paginator.num_pages

    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(totalPage)
        

    context = {"motifForm":page_obj,'page_range':paginator.get_elided_page_range(page_obj.number,on_each_side=3, on_ends=2), "lastpage": totalPage, "status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]}

    return render(request, "ListMotif.html", context)

@login_required(login_url='login')
def tagName(request, user):
    username = request.user
    status = username.is_staff
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3 active','nav-link nav-link-4']
    if status == 0:
          status=None
    
    motifForm = MotifForm1.objects.all().filter(user__iexact= user).values().order_by('time').reverse()
        

    context = {"motifForm":motifForm,"status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]}

    return render(request, "searchTag.html", context)

@login_required(login_url='login')
def tagJmlBaris(request, jmlBaris):
    username = request.user
    status = username.is_staff
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3 active','nav-link nav-link-4']
    if status == 0:
          status=None
    
    motifForm = MotifForm1.objects.all().filter(jmlBaris__iexact= jmlBaris).values().order_by('time').reverse()
        

    context = {"motifForm":motifForm,"status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]}

    return render(request, "searchTag.html", context)

@login_required(login_url='login')
def tagWaktu(request, time):
    username = request.user
    status = username.is_staff
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3 active','nav-link nav-link-4']
    if status == 0:
          status=None
    time = time[0:10]
    motifForm = MotifForm1.objects.all().filter(time__icontains= time).values().order_by('time').reverse()
        

    context = {"motifForm":motifForm,"status":status,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]}

    return render(request, "searchTag.html", context)

@login_required(login_url='login')
def motif(request, id):
    motif = MotifForm1.objects.get(id = id)
    user = request.user
    status = user.is_superuser
    status1 = user.is_staff
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3 active','nav-link nav-link-4']
    if status1 == 0:
          status1=None
    if status == 0:
          status=None

    if len(motif.imgAfter)>0:
        
        image =run([sys.executable,'utils\\UrutanLidi.py', str(motif.imgBefore)],shell=False,stdout=PIPE)
    #Membuat grid lidi
    image = image.stdout.strip().decode("utf-8")
    UrutanLidi = eval(image)
    UrutanLidi_even = []
    UrutanLidi_odd = []

    for i in range(len(UrutanLidi)):
         if i % 2 == 0:
              UrutanLidi_even.append(UrutanLidi[i])
         else:
              UrutanLidi_odd.append(UrutanLidi[i]) 
    
    image = image[1:-1]
    
    

    Lidi =run([sys.executable,'utils\\GridLidi.py', str(motif.imgBefore)],shell=False,stdout=PIPE)
    Lidi = Lidi.stdout.strip().decode("utf-8")

    Hasil =run([sys.executable,'utils\\GridMotif.py', str(motif.imgAfter)],shell=False,stdout=PIPE)
    Hasil = Hasil.stdout.strip().decode("utf-8")

    RedLine =run([sys.executable,'utils\\redLine.py', Hasil],shell=False,stdout=PIPE)
    RedLine = RedLine.stdout.strip().decode("utf-8")

    Zipfile =run([sys.executable,'utils\\zip.py', str(motif.imgAfter), str(motif.imgBefore)],shell=False,stdout=PIPE)
    Zipfile = Zipfile.stdout.strip().decode("utf-8")

    print(Zipfile)
    Help =run([sys.executable,'utils\\GridHelp.py', str(motif.imgBefore)],shell=False,stdout=PIPE)
    Help = Help.stdout.strip().decode("utf-8")

    print(Help)
    Slice =run([sys.executable,'utils\\Slice.py', Lidi],shell=False,stdout=PIPE)
    Slice = Slice.stdout.strip().decode("utf-8")
    Slice = eval(Slice)

    Slice_even = []
    Slice_odd = []     
    for i in range(len(Slice)):
         if i%2 == 0:
              Slice_even.append(Slice[i])
         else:
              Slice_odd.append(Slice[i])
    
    Slice2 =run([sys.executable,'utils\\Slice.py', RedLine],shell=False,stdout=PIPE)
    Slice2 = Slice2.stdout.strip().decode("utf-8")
    print(Slice2)
    Slice2 = eval(Slice2)

    Slice2_even = []
    Slice2_odd = []

    for i in range(len(Slice2)):
         if i % 2 == 0:
              Slice2_even.append(Slice2[i])
         else:
              Slice2_odd.append(Slice2[i]) 
       
    UrutanMotif = f"[{motif.urutanLidi}]"
    UrutanMotif = eval(UrutanMotif)

    UrutanMotif_even = []
    UrutanMotif_odd = []

    for i in range(len(UrutanMotif)):
         if i % 2 == 0:
              UrutanMotif_even.append(UrutanMotif[i])
         else:
              UrutanMotif_odd.append(UrutanMotif[i]) 
    
    myList = zip_longest(Slice_even, UrutanLidi_even, Slice_odd, UrutanLidi_odd)
    myList2 = zip_longest(Slice2_even, UrutanMotif_even, Slice2_odd, UrutanMotif_odd)

    return render (request, 'lihatMotif.html', {'zip': Zipfile,'GridHelp': Help,'SliceMotif': myList2,'SliceLidi': myList,'UrutanLidi': UrutanLidi,'RedLine': RedLine,'Lidi': Lidi,'urutanAsliLidi': image,'motif': motif, "status":status, 'status1':status1,'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def deleteMotif(request):

    id = request.POST.get('DeleteImage')
    prod = MotifForm1.objects.get(id = id)
    if len(prod.imgAfter)>0:
        
        image1 =run([sys.executable,'utils\\delete.py', str(prod.imgAfter)],shell=False,stdout=PIPE)
        image2 =run([sys.executable,'utils\\delete.py', str(prod.imgBefore)],shell=False,stdout=PIPE)
        
        messages.success(request, "Motif berhasil dihapus")
    prod.delete()
    
    return redirect('list1')

@login_required(login_url='login')    
def showTest(request):
    
    motifForm = Post.objects.all().values()
    context = {"motifForm":motifForm}

    return render(request, "ListMotif.html", context)

@login_required(login_url='login')
def help(request):
    
    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3','nav-link nav-link-4 active']
    return render(request, "help.html", {'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def help_generate(request):

    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3','nav-link nav-link-4 active']
    return render(request, "help-generator.html", {'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def help_lidi(request):

    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3','nav-link nav-link-4 active']
    return render(request, "help-lidi.html", {'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def help_search(request):

    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3','nav-link nav-link-4 active']
    return render(request, "help-search.html", {'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

@login_required(login_url='login')
def help_download(request):

    navlink = ['nav-link nav-link-1 ','nav-link nav-link-2','nav-link nav-link-3','nav-link nav-link-4 active']
    return render(request, "help-download.html", {'navlink1':navlink[0],'navlink2':navlink[1],'navlink3':navlink[2],'navlink4':navlink[3]})

def SignupPage(request):
    if request.user.is_authenticated:
         return redirect('home')
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if not re.match(r"^[a-zA-Z0-9_]+$", uname):
            # username is not valid, return an error response
            messages.info(request, 'Username tidak menerima adanya spasi dan simbol lainnya kecuali tanda "_"')
            return render(request,'signup.html', {'uname': uname,'email': email,'pass1': pass1,'pass2': pass2 })
        
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username sudah pernah digunakan')
                return render(request,'signup.html', {'uname': uname,'email': email,'pass1': pass1,'pass2': pass2 })
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email sudah pernah digunakan')
                return render(request,'signup.html', {'uname': uname,'email': email,'pass1': pass1,'pass2': pass2 })
            elif int(len(pass1)<8):
                 messages.info(request, 'Kata sandi minimal 8 karakter')
                 return render(request, 'signup.html', {'uname': uname,'email': email,'pass1': pass1,'pass2': pass2 })
            else:
                user = User.objects.create_user(username=uname, email=email, password=pass1)
                user.save()
                
                user=authenticate(request,username=uname,password=pass1)
                login(request,user)
                
                messages.success(request, 'Akun Berhasil Dibuat')
                
                return redirect('home')
                    
        else:
            messages.info(request, 'Kata Sandi dan Konfirmasi Kata Sandi yang dimasukkan berbeda')
            return render(request,'signup.html', {'uname': uname,'email': email,'pass1': pass1,'pass2': pass2 })
    else:
        return render(request, 'signup.html')


def LoginPage(request):
    if request.user.is_authenticated:
         return redirect('home')
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request, 'Username atau Kata Sandi Salah', extra_tags='alert')
            return redirect('login')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


