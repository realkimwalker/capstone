import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


# Create your tests here.
class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)


    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is <1 day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


    def create_question(question_text, days):
        """
        Create question w/ question_text showing # of days offset to future, or negative for days past
        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)


    class QuestionIndexViewTests(TestCase):
        def test_no_questions(self):
            """
            If no questions exist, an appropriate message is displayed.
            """
            response = self.client.get(reverse("polls:index"))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "No polls are available.")
            self.assertQuerySetEqual(response.context["latest_question_list"], [])


        def test_past_question(self):
            """
            Questions with past pubdate displayed on index page
            """
            question = create_question(question_text="Past question.", days=-30)
            response = self.client.get(reverse("polls:index"))
            self.assertQuerySetEqual(response.context["latest_question_list"], [question])


        def test_future_question(self):
            """
            Questions w pubdate in future aren't displayed on index page
            """
            create_question(question_text="Future question.", days=30)
            response = self.client.get(reverse("polls:index"))
            self.assertQuerySetEqual(respone.context["latest_question_list"],[question])


        def test_two_past_questions(self):
            """
            The questions index page can display multiple questions
            """
            question1 = create_question(question_text="Past question 1.", days=-30)
            question2 = create_question(question_text="Past question 2.", days=-5)
            response = self.client.get(reverse("polls:index"))
            self.assertQuerySetEqual(respone.context[
                "latest_question_list"],
                [question2, question1],
            )


    class QuestionDetailViewTests(TestCase):
        def test_future_question(self):
            """
            Detail view of question w pubdate in future returns 404
            """
            future_question = create_question(question_text="Future question.", days=5)
            url = reverse("polls:detail", args=(future_question.id))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 404)


        def test_past_question(self):
            """
            Detail view of question w pubdate in past displays question text.
            """
            past_question = create_question(question_text="Past question.", days=-5)
            url = reverse("polls:detail", args=(past_question.id))
            response = self.client.get(url)
            self.assertContains(response, past_question.question_text)
