from django import forms
from . models import Review

# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=10, error_messages={
#         "max_length":"Entered Value is tool long keep it under 10 char"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=150)
#     rating = forms.IntegerField(label= "Your Rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        #fields = ['user_name', 'review_text', 'rating']
        fields = '__all__'
        #exclude = ['review_text']
        labels = {"user_name":"username",
                 "review_text": "Your Feedback",
                 "rating": "Your Rating"}
        error_messages = {
            "user_name":{
                "required":"Your Name Must Not be Empty",
                "max_length":"Entered Value is tool long keep it under 10 char"
                }
            }
        

            




