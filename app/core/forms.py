from django import forms


class SignInForm(forms.Form):
    email = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label='Lembre-se de mim da próxima vez')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if field == 'remember_me':
                self.fields[field].widget.attrs.update({
                    'class': 'form-check-input',
                    'checked': True})
                continue

            if field == 'email':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com o seu e-mail'})

            if field == 'password':
                self.fields[field].widget.attrs.update({
                    'placeholder': 'Entre com a sua senha'})

            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-lg'})

