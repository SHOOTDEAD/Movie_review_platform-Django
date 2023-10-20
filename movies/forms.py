from django import forms


class ReviewForm(forms.Form):
    review = forms.CharField(
        label="",
        max_length=100,
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "#Write your review here", "class": "reviews-data"}
        ),
    )
    review_type = forms.BooleanField(label="Do you like this movie", required=False)
