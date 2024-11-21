from app import create_app
from views.DepartmentView import departament_blueprint
from views.UserView import user_blueprint


app = create_app()
app.register_blueprint(departament_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)