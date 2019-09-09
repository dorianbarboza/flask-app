from flask_restful import Resource, request
from wtforms import Form, validators, StringField, PasswordField

class NewUserForm(Form):
    phone = StringField('User Phone Number', [validators.DataRequired()])
    password = PasswordField('User Password', [validators.DataRequired()])

class NewUser(Resource):
    def post(self):
        form = NewUserForm(request.form)
        if not form.validate():
            return 'ko', 400
        return 'ok', 200

class ViewUsers(Resource):
    def get(self):
        return {'user':'phone'}
