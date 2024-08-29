from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=10, error_messages={
        "max_length":"Entered Value is tool long keep it under 10 char"
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=150)
    rating = forms.IntegerField(label= "Your Rating", min_value=1, max_value=5)





