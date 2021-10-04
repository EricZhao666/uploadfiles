from django.http import HttpResponse
from django.shortcuts import render,redirect
def index(request):
    return render(request,'upload/m1.html')

def success(request):
    return render(request,'upload/success.html')

# 存储文件
def upload(request):
    file=request.FILES.get('upload_file')
    with open(f'load/{file.name}','wb') as f:
        f.write(file.read())
    return redirect('/success/')
def upload_multiple(request):
    files=request.FILES.getlist('upload_file')
    for rec_file in files:
        with open(f'load/{rec_file.name}', 'wb') as f:
            f.write(rec_file.read())
    return redirect('/upload/')