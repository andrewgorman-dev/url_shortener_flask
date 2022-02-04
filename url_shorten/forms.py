
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, Length


class UrlForm(FlaskForm):
    long_url = StringField('Long Url (to be shortened)',
                           validators=[DataRequired(),
                                       Length(min=20, max=200)])
    name = StringField('Name (reference required)', validators=[DataRequired()])
    expiry_date_time = DateTimeField('(Optional) I would like my link to expire at exactly:', format='%Y-%m-%d %H:%M:%S')
    submit = SubmitField('Generate shorter url')

