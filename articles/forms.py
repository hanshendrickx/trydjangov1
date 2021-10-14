from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data
        print("cleande_data", cleaned_data)
        title = cleaned_data.get("title")
        if title.lower().strip() == "the office":
            raise forms.ValidationError('This title is taken.')
        print("title", title)
        return title

    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)    
        return cleaned_data