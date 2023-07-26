from django import forms
from .models import UserProfile, Post

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = [
#             "profile_pic",
#             "gender",
#             "bio",
#         ]   
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic', 'locations', 'gender']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']