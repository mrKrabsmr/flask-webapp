from internal.app.database.models import Result


class ResultDAO:
    def __init__(self, session):
        self.session = session

    def get_(self):
        return self.session.query(Result)

    def get_all(self):
        return self.session.query(Result).all()

    def get_one(self, rid):
        return self.session.query(Result).filter_by(id=rid).first()

    def create(self, data):
        result = Result(**data)
        self.session.add(result)
        self.session.commit()

    def update(self, rid, data):
        result = self.get_one(rid)
        if "result" in data:
            result.body = data.get("result")
        result.save()
        self.session.commit()

    def delete(self, rid):
        result = self.get_one(rid)
        self.session.delete(result)
        self.session.commit()
