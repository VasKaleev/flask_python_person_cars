from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, NumberRange

""" class ProfileForm(FlaskForm):
   way = SelectField(
      'Выберите сторону света, в которую желаете отправиться',
      coerce = int,
      choices=[
         (0, 'Север'),
         (1, 'Восток'),
         (2, 'Юг'),
         (3, 'Запад'),
      ],
      render_kw={
         'class': 'form-control'
      },
   )
   number_steps = IntegerField(
    'Как далеко планируется продвинуться?',
    validators = [NumberRange(min=1), DataRequired()],
    default=1,
    render_kw = {
      'class':'form-control' 
    },
   )
   submit = SubmitField('В путь!') """
class ProfileFormPerson(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    age = IntegerField('Age:', validators=[DataRequired()])
    submit = SubmitField('Submit')
class ProfileFormCar(FlaskForm):
    brand = StringField('Brand:', validators=[DataRequired()])
    model = StringField('Model:', validators=[DataRequired()])
    av = SelectField(
      'Выберите автовлвдельца',
      coerce = int,
      choices=[
         (1, 'Ekaterina'),
         (2, 'Andreew'),
         (3, 'Vasily'),
         (4, 'Evgeniy'),
      ],
      render_kw={
         'class': 'form-control'
      },
   )
    submit = SubmitField('Submit')