from django import forms
from django.core.mail import  EmailMessage

class InquiryForm(forms.Form):
    name=forms.CharField(label='名前',max_length=30)
    email=forms.EmailField(label='メールアドレス')
    title=forms.CharField(label='タイトル',max_length=30)
    message=forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control col-9'
        self.fields['name'].widget.attrs['placeholder']='名前を入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control col-11'
        self.fields['email'].widget.attrs['placeholder'] ='メールアドレスを入力してください。'

        self.fields['title'].widget.attrs['class'] ='form-control col-11'
        self.fields['title'].widget.attrs['placeholder'] ='タイトルを入力してください。'

        self.fields['message'].widget.attrs['class'] ='form-control col-12'
        self.fields['message'].widget.attrs['placeholder'] ='メッセージを入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        name = self.cleaned_data['email']
        name = self.cleaned_data['title']
        name = self.cleaned_data['message']
        subject = '問い合わせ{}'.format(title)
        messege = '送信者名:{0}\nメールアドレス:{1}\nメッセージ:{2}'.format(name,email,message)

        from_,email='admin@example.com'
        to_list=[
            'test@example.com'
        ]
        cc_list=[
            email
        ]

        messege=EmailMessage(subject=subject,body=messege,from_email=from_email,to=to_list,cc=cc_list)
        messege.send()

