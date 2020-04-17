"""
--------------------------------------------------------------------------------------------------
    File Name: hrms/user_management/forms.py
    Description: This module contains all form definitions for the user_management application.
--------------------------------------------------------------------------------------------------
"""
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'employee', 'admin', 'active', 'staff', 'groups')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        password = self.cleaned_data["password1"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    def clean(self):
        data = super(UserAdminCreationForm, self).clean()
        if data.get('admin') is True and 'employee' in self.errors:
            del self.errors['employee']
        return data

    def __init__(self, *args, **kwargs):
        super(UserAdminCreationForm, self).__init__(*args, **kwargs)

        self.fields['employee'].required = True


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'employee', 'password', 'active', 'admin', 'staff', 'groups')

    def clean(self):
        data = super(UserAdminChangeForm, self).clean()
        if data.get('admin') is True and 'employee' in self.errors:
            del self.errors['employee']
        return data

    def __init__(self, *args, **kwargs):
        super(UserAdminChangeForm, self).__init__(*args, **kwargs)

        self.fields['employee'].required = True

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, required=False)

    if password1 is not None and password2 is not None:
        def clean_password2(self):
            # Check that the two password entries match
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            # Save the provided password in hashed format
            user = super(UserAdminChangeForm, self).save(commit=False)
            password = self.cleaned_data["password1"]
            if password:
                user.set_password(password)
            if commit:
                user.save()
            return user
