from django import forms

from .models import Comment



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name":"Your Name",
            "comment_text": "Your Feedback"
        }
        error_messages={
            "user_name":{
                "required": "Your name must not be empty!",
                "max_length": "Please, enter the maximum of 100 characters"
            },
            "comment_text":{
                "required": "Your text must not be empty!"
            }
        }




