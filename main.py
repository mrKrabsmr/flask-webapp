from flask import Flask

from config import config
from internal.app.database.models import Base
from internal.app.database import engine
from internal.app.views import login_blueprint, registration_blueprint, profile_blueprint, survey_blueprint

app = Flask(__name__)

app.config.from_object(config)

app.register_blueprint(login_blueprint, url_prefix="/login")
app.register_blueprint(registration_blueprint, url_prefix="/registration")
app.register_blueprint(profile_blueprint, url_prefix="/profile")
app.register_blueprint(survey_blueprint, url_prefix="/survey")


Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True, load_dotenv=True, templates_auto_reload=True)
