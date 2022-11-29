from email import message
from http.client import CONTINUE
from pyexpat.errors import messages
from tkinter import messagebox
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse,StreamingHttpResponse
from datetime import datetime
from django.contrib import auth
from myapp import models
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
from myapp import models


import cv2
import threading
import json
import os
import smtplib
from django.http import StreamingHttpResponse
from django.contrib.auth.forms import UserCreationForm

import myproject

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = '/index/' #reverse_lazy('users-home')

    '''
    template_name='users/password-change.html'
    success_url=reverse_lazy('users:password-change-done-view')'''

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name='users/password-reset-done.html'


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

'''
def captcha():
  hashkey = CaptchaStore.generate_key() # 驗證碼答案
  image_url = captcha_image_url(hashkey) # 驗證碼地址
  captcha = {'hashkey': hashkey,'image_url': image_url}
  return captcha
#重新整理驗證碼
def refresh_captcha(request):
  return HttpResponse(json.dumps(captcha()),content_type='application/json')
 
# 驗證驗證碼
def jarge_captcha(captchaStr,captchaHashkey):
  if captchaStr and captchaHashkey:
    try:
      # 獲取根據hashkey獲取<a href="https://www.796t.com/category.php?cid=15">資料庫</a>中的response值
      get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
      if get_captcha.response == captchaStr.lower(): # 如果驗證碼匹配
        return True
    except:
      return False
  else:
    return False
 

class IndexView(View):
  def get(self,request):
    hashkey = CaptchaStore.generate_key() # 驗證碼答案
    image_url = captcha_image_url(hashkey) # 驗證碼地址
    print(hashkey,image_url)
    captcha = {'hashkey': hashkey,'image_url': image_url}
    return render(request,"login.html",locals())
 
  def post(self,request):
    capt = request.POST.get("captcha",None) # 使用者提交的驗證碼
    key = request.POST.get("hashkey",None) # 驗證碼答案
    if jarge_captcha(capt,key):
      return HttpResponse("驗證碼正確")
    else:
      return HttpResponse("驗證碼錯誤")'''

def hello2(request,name):
    return HttpResponse("Hello! "+name)
def hello3(request,name):
    now=datetime.now()
    return render(request,"hello3.html",locals())
def index(request):
    return render(request, 'index.html')
def news(request):
    news = models.News.objects.all().order_by('id')
    return render(request,'news.html', locals())
def messageboard(request):
    msboard = models.Messageboard.objects.all().order_by('-id') #order_by('-欄位')，「-」號→降冪排序 (未打「-」號→升冪排序)
    return render(request, 'messageboard.html', locals()) #讀取表單資料要加locals()

def messageboardpost(request):
    if request.method == "POST":
        msboardname = request.POST.get('msboardname')
        msboardcontent = request.POST.get('msboardcontent')
        if not(len(msboardcontent)>0):
            #message='請輸入內容!!!!!'
            messagebox.showinfo(title='留言板',message='請輸入內容!!!!!')
        else:
            datetime = request.POST.get('datetime')
            unit = models.Messageboard.objects.create(msboardname=msboardname, msboardcontent=msboardcontent, datetime=datetime)
            unit.save()
            return redirect('/messageboard/')
    return render(request, 'messageboardpost.html')

def messageboardedit(request,id=None,mode=None):
    if mode=="load":
        unit=models.Messageboard.objects.get(id=id)
        return render(request,'messageboardedit.html',locals())
    elif mode=="save":
        unit=models.Messageboard.objects.get(id=id)
        unit.msboardcontent=request.POST.get('msboardcontent')
        if not(len(unit.msboardcontent)>0):
            messagebox.showinfo(title='留言板',message='請輸入內容!!!!!')
        else:
            unit.save()
        return redirect('/messageboard/')

def messageboarddelete(request,id=None):
    if id!=None:
        if request.method=="POST":
            id=request.POST.get('id')

        try:
            unit=models.Messageboard.objects.get(id=id)
            unit.delete()
            return redirect('/messageboard/')
        except:
            messagebox.showinfo(title='留言版',message='錯誤!')
    
    return render(request,'messageboard.html',locals())
    
def sendfeedback(request):
    if request.method == "POST":
        feedbacktype = request.POST.get('feedbacktype')
        detail = request.POST.get('detail')
        if not(len(detail)>0):
            #message='請輸入內容!!!!!'
            messagebox.showinfo(title='留言板',message='請輸入內容!!!!!')
        else:
            feedbackemail = request.POST.get('feedbackemail')
            datetime = request.POST.get('datetime')
            unit = models.SendFeedback.objects.create(feedbacktype=feedbacktype,detail=detail,feedbackemail=feedbackemail,datetime=datetime)
            unit.save()

            # 電子郵件內容樣板
            email_template = render_to_string(
                'accounts/sandfeedback_email.html',
                {
                    'feedbacktype': request.POST.get('feedbacktype'),
                    'detail': request.POST.get('detail')
                }
            )
            email = EmailMessage(
                '問題反映已傳送通知信 <Smarter 智慧化影音創作系統>',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                [feedbackemail]  # 收件者
            )
            email.fail_silently = False
            email.send()

            return redirect('/sendfeedback_successful/')
    return render(request,'sendfeedback.html')
def sendfeedback_successful(request):
    return render(request,'sendfeedback_successful.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/index/')
    else:
        return render(request, 'login.html', locals())

        
def logout(request):
    auth.logout(request)
    return redirect('/index/')

def sign_up(request):
    form =  RegisterForm()

    if request.method == "POST":
        user_email=request.POST.get('email')
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # 電子郵件內容樣板
            email_template = render_to_string(
                'accounts/signup_success_email.html',
                {'username': request.POST.get('username')}
            )
            email = EmailMessage(
                '註冊成功通知信 <Smarter 智慧化影音創作系統>',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                [user_email]  # 收件者
            )
            email.fail_silently = False
            email.send()


            return redirect('/accounts/login/')  #重新導向到登入畫面


    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)

    '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'sign_up.html', locals())'''


    '''
    if request.method == "POST":
        userid = request.POST.get('userid')
        pos = userid.find('@') #宣告變數pos，判斷使用者輸入之userid內是否包含'@' (此段「str.find('')」可找出'@'在userid的第幾位數)
        if pos>0: #輸入之userid包含'@'，pos會計算出'@'在第幾位數 (若不包含'@'，pos=-1)
            if not(len(userid)>pos and userid.find('.',pos)>0): 
                #判斷: NOT相反值[輸入之userid的長度是否大於pos('@'在第幾位數)，即'@'後面要有內容<布林值>  AND  從pos('@'位於第幾位數)所在位數後面開始尋找'.'，找出'.'位於第幾位數，若無則回傳-1<布林值>]
                #( )內判斷式為成功註冊帳號的條件 --即成功寫入資料庫-- ，要轉成未成功條件，使用NOT()
                messagebox.showinfo(title='註冊帳號',message='請填寫正確Email格式!')
            else:
                password = request.POST.get('password')
                username = request.POST.get('username')
                unit = Userinfo.objects.create(userid=userid, password=password, username=username)
                unit.save()
            

                return redirect('/index/')
                '''
            
    return render(request, "sign_up.html", locals())

def userinfoedit(request):
    return render(request, 'userinfoedit.html', locals())
def userinfo(request):
    return render(request, 'userinfo.html', locals())
def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "upload-file.html", context = {
        "files": documents
    })



    return FileResponse(model.image.open(), as_attachment=True, filename=filename_with_extension)
'''
def deleteFile(request,id): 

        dir = 'file_path' 
        Id = id 
        deletefile = models.Document.objects.filter(id = Id) 
        #不可以直接写成  os.remove(dir+'{}'.format(deletefile.name))
        for i in deletefile: 
            os.remove(dir+'{}'.format(i.name))

        models.Document.objects.filter(id = Id).delete()
        return render(request,"upload-file.html")'''
                
def makevideo(request):
    return render(request, 'makevideo.html', locals())

def smartrecord(request):
    cap = cv2.VideoCapture(0)                         # 讀取電腦攝影機鏡頭影像。
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 取得影像寬度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 取得影像高度
    fourcc = cv2.VideoWriter_fourcc('M','P','G','4')          # 設定影片的格式為 MPG4
    out = cv2.VideoWriter('output3.mp4', fourcc, 20.0, (width,  height))  # 產生空的影片
    if not cap.isOpened():
        messagebox.showinfo("error","Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            messagebox.showinfo("error","Cannot receive frame")
            break
        out.write(frame)       # 將取得的每一幀圖像寫入空的影片
        cv2.imshow('recording video', frame)
        if cv2.waitKey(1) == ord('q'):
            break             # 按下 q 鍵停止

    cap.release()
    out.release()      # 釋放資源
    cv2.destroyAllWindows()
    return render(request, 'index.html', locals())


def recordingvideo(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request,'recordingvideo.html')


def ytcomments(request):
    return render(request, 'ytcomments.html', locals())