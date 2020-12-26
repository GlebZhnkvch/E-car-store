from django import forms
from ads.models import Ad


class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        exclude = [
            'available',
            'author',
            'created_at',
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows': '3'}),
        }

        labels = {
            'brand': 'Марка',
            'car_model': 'Модель',
            'capacity': 'Емкость батареи (кВт•ч)',
            'year': 'Год выпуска',
            'equipment': 'Комплектация',
            'mileage': 'Пробег (км)',
            'price': 'Цена (USD)',
            'description': 'Описание',
            'phone_number_ad': 'Номер телефона',
            'author_ad': 'Ваше имя',
            'image': 'Выберите фото',
        }
