from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=10, error_messages={
        "max_length":"Entered Value is tool long keep it under 10 char"
    })






