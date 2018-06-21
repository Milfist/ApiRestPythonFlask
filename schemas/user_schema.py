from crud import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')
