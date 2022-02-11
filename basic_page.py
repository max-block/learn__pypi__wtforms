from wtforms import Form, IntegerField, StringField


class BasicForm(Form):
    name = StringField()
    age = IntegerField()
