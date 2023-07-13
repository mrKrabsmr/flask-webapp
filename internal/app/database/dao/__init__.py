from internal.app.database import session
from internal.app.database.dao.user import UserDAO
from internal.app.database.dao.survey.question import QuestionDAO
from internal.app.database.dao.survey.result import ResultDAO
from internal.app.database.dao.survey.survey import SurveyDAO

user_dao = UserDAO(session)

survey_dao = SurveyDAO(session)
question_dao = QuestionDAO(session)
result_dao = ResultDAO(session)


