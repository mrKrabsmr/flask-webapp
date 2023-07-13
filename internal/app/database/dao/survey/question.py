from sqlalchemy.orm import Session

from internal.app.database.models import Question


class QuestionDAO:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session.query(Question).all()

    def get_question_by_sid(self, sid, start):
        return self.session.query(Question).filter_by(survey_id=sid).offset(start).first()

    def get_one(self, qid):
        return self.session.query(Question).filter_by(id=qid).first()

    def create(self, data):
        question = Question(**data)
        self.session.add(question)
        self.session.commit()

    def update(self, qid, data):
        question = self.get_one(qid)
        if "question" in data:
            question.body = data.get("question")
        question.save()
        self.session.commit()

    def delete(self, qid):
        question = self.get_one(qid)
        self.session.delete(question)
        self.session.commit()
