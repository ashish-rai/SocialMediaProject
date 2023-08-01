from django import forms
from .models import UserProfile, Post, Comment

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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'cols': 40, 'placeholder': 'Comment on post....'})
        }