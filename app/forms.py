from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(Form):
    id = StringField('id', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])

    #first_name = StringField('First_name', validators=[DataRequired()])
    # def validate(self):
    #     return True
    #
    # def validate(self):
    #     valid = Form.validate(self)
    #     if not valid:
    #         return False
    #
    #     user = User.query.filter_by(id=self.id.data)
    #     if user is not None:
    #         if user.first_name==self.first_name.data and user.last_name==self.last_name.data:
    #             if user.voted=='No':
    #                 return True;
    #             return 'The user already voted'
    #         return 'Wrong data entered. Please choose another one.'
    #     return 'user not recognized in database. Please choose another one.'
