from sqlalchemy import desc

from internal.app.database.models import Survey


class SurveyDAO:
    def __init__(self, session):
        self.session = session

    def get_(self):
        return self.session.query(Survey)

    def get_all(self):
        return self.session.query(Survey).all()

    def get_paginated_data(self, start, ipp):
        return self.session.query(Survey).order_by(desc("created_at")).offset(start).limit(ipp).all()

    def get_one(self, sid):
        return self.session.query(Survey).filter_by(id=sid).first()

    def create(self, data):
        survey = Survey(**data)
        self.session.add(survey)
        self.session.commit()

    def update(self, sid, data):
        survey = self.get_one(sid)
        if "title" in data:
            survey.title = data.get("title")
        survey.save()
        self.session.commit()

    def delete(self, sid):
        survey = self.get_one(sid)
        self.session.delete(survey)
        self.session.commit()
