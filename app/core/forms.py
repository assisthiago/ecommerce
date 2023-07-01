from django import forms
from django.contrib.auth.password_validation import validate_password


class BaseForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        validators=[validate_password],
    help_text=[
            'Sua senha não pode ser muito parecida com o resto das suas informações pessoais.',
            'Sua senha precisa conter pelo menos 8 caracteres.',
            'Sua senha não pode ser uma senha comumente utilizada.',
            'Sua senha não pode ser inteiramente numérica.'])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'email':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com o seu e-mail'})

            if field == 'password':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com a sua senha'})

            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-lg'})


class SignInForm(BaseForm):
    remember_me = forms.BooleanField(
        label='Lembre-se de mim da próxima vez', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['remember_me'].widget.attrs.update({
            'class': 'form-check-input',
            'checked': True})


class SignUpForm(BaseForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='Sobrenome')
    password_confirm = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm:
            if password != password_confirm:
                self.add_error('password_confirm', 'As senhas são diferentes.')

        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'first_name':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com o seu nome'})

            if field == 'last_name':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com o sobrenome'})

            if field == 'password_confirm':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Confirme a sua senha'})

            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-lg'})


class RecoverPasswordForm(SignUpForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'password':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com a sua nova senha'})

            if field == 'password_confirm':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Confirme a sua nova senha'})
