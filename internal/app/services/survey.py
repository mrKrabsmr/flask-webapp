import datetime

from internal.app.database.dao import user_dao, survey_dao, question_dao


class SurveyService:
    items_per_page = 20

    def get_survey_list_data(self, page):
        start = (page - 1) * self.items_per_page

        data = survey_dao.get_paginated_data(start, self.items_per_page)

        total_pages = len(data) // self.items_per_page + (
            1 if len(data) % self.items_per_page > 0 else 0
        )

        return data, total_pages

    @staticmethod
    def get_survey(sid):
        survey = survey_dao.get_one(sid)
        if not survey:
            return False
        return True

    @staticmethod
    def get_question(sid, page):
        question = question_dao.get_question_by_sid(sid, page)
        if not question:
            return False
        return question

    def check_answer(self, sid, page, answer):
        question = self.get_question(sid, page)
        return question.true_option == answer

    def create_survey(self, uid, data):
        data = {
            "user_id": uid,
            "title": data.get("title"),
            "created_at": datetime.datetime.now()
        }
        survey_dao.create(data)

        self.create_questions(data)

    @staticmethod
    def create_questions(data):
        questions = [key for key in data if key.startswith("question")]
        t_counter, f_counter = 1, 1
        for question in questions:
            data = {
                "body": data[question],
                "true_option": data[f"answer_option_{t_counter}"],
                "false_option_1": data[f"answer_option_{f_counter}"],
                "false_option_2": data[f"answer_option_{f_counter + 1}"],
                "false_option_3": data[f"answer_option_{f_counter + 2}"],
            }
            question_dao.create(data)
            t_counter += 1
            f_counter += 3


