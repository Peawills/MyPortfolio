from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["full_name", "email", "phone", "subject", "message"]
        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "John Doe",
                    "class": "form-input w-full pl-12 pr-4 py-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none transition-all",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "john@example.com",
                    "class": "form-input w-full pl-12 pr-4 py-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none transition-all",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+234 XXX XXX XXXX",
                    "class": "form-input w-full pl-12 pr-4 py-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none transition-all",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "placeholder": "How can I help you?",
                    "class": "form-input w-full pl-12 pr-4 py-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none transition-all",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Tell me about your project...",
                    "rows": 5,
                    "class": "form-input w-full pl-12 pr-4 py-4 border border-gray-300 rounded-xl focus:ring-2 focus:ring-teal-500 focus:border-transparent outline-none transition-all resize-none",
                }
            ),
        }

    def clean_full_name(self):
        name = self.cleaned_data.get("full_name", "").strip()
        if not name:
            raise forms.ValidationError("Please enter your full name.")
        return name
