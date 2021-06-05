from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.core.exceptions import ValidationError

from comments.models import Comment
from products.models import Product


class BuynowForm(forms.Form):
    amount = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        try:
            self.available_amount = kwargs.pop('amount')
        except:
            self.available_amount = 1
        super(BuynowForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget = forms.NumberInput(attrs={'min': 1,
                                                                'max': self.available_amount,
                                                                'step': 1,
                                                                'value': 1})

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if type(amount) != int:
            raise ValidationError('Wrong amount!')
        return amount


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'amount', 'description',
                  'product_model', 'manufacturer', 'publicly_listed', 'category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Edit product'))


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'stars',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add Comment'))
