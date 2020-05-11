from django import forms
from django.core import validators

# def starts(value):
#     if value[0]!='d':
#         raise forms.ValidationError('Name Should start with d')

class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()

    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(10)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)



    def clean(self):
        print('Total form validation')
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        inputrollno=total_cleaned_data['rollno']
        bot_handler_value=total_cleaned_data['bot_handler']
        if len(inputname)<4:
            raise forms.ValidationError('Name is too short')
        if len(inputname)>10:
            raise forms.ValidationError('Name is too long')
        if inputrollno<=2:
            raise forms.ValidationError('Roll No should be greater than 2 digits')
        if len(bot_handler_value)>=0:
            raise forms.ValidationError('Request from bot handler')


class SignupForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        total_cleaned_data=super().clean()
        pswd=total_cleaned_data['password']
        rpswd=total_cleaned_data['rpassword']
        if pswd!=rpswd:
            raise forms.ValidationError('Passwords did not match')


    # def clean_name(self):
    #     print('validating name')
    #     inputname=self.cleaned_data['name']
    #     if len(inputname)<4:
    #         raise forms.ValidationError('Name is too short')
    #     return inputname
