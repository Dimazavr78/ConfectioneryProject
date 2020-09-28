'''
from django import forms
from django.contrib.auth import get_user_model


class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def save(self, *args, **kwargs):
        user = super(ClientCreationForm, self).save(*args, **kwargs)
        user.set_password(self.cleaned_data['password'])
        user.save()


class ClientChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']
'''