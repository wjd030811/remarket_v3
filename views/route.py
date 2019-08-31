from flask import Flask


class Route:
    def route(self, app: Flask):
        from views.user import signup, signin, mypage
        app.register_blueprint(signup.api.blueprint)
        app.register_blueprint(signin.api.blueprint)
        app.register_blueprint(mypage.api.blueprint)

        from views.service import list
        app.register_blueprint(list.api.blueprint)
