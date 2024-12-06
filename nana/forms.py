from django import forms
from .models import Essay





class EssayForm(forms.ModelForm):
    class Meta:
        model = Essay
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'cols': 100,  # Sets the column size (width in characters)
                'style': 'width: 100%;',  # Ensures the textarea takes 100% of the available width
                         'placeholder': 'Write no more than 500 words'
            })
        }
