from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email

class RegisterForm(FlaskForm):
    email=StringField(label='Email:', validators=[DataRequired(),Email()], render_kw={"placeholder":"example@gmail.com"})
    password=PasswordField(label='Password:', validators=[DataRequired()])
    name=StringField(label='Name:',validators=[DataRequired()])
    submit=SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField(label='Email:', validators=[DataRequired(),Email()],render_kw={"placeholder":"example@gmail.com"})
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField('Log me in')
