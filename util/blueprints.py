import routes


def register_blueprint(app):
    app.register_blueprint(routes.team)
    app.register_blueprint(routes.player)
    app.register_blueprint(routes.division)
    app.register_blueprint(routes.auth)
    app.register_blueprint(routes.coach) 
    app.register_blueprint(routes.user)
    app.register_blueprint(routes.stadium) 

    