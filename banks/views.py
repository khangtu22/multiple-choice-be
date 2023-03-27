from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
from choices.models import ChoiceModel
from questions.models import QuestionModel


class ImportAPIView(APIView):
    def get(self, request, pk=None, format=None):
        df = pd.read_excel('/Users/tranvankhang/psmi/psmi/media/bank.xlsx')

        for index, row in df.iterrows():
            self.splitRow(row)

        return Response("Import success!")

    def splitRow(self, row):
        question = QuestionModel()
        question.question = row['Question']
        question.answer = row["Answer"]
        question.explain = row["Explanation"]
        is_equal = str(row['Type']).lower().strip() == 'multi-select'
        question.isMultipleChoice = is_equal
        question.save()

        num_of_choice = 0
        for i in range(7):
            if i == 0:
                continue
            if (str(row['Answer Option ' + str(i)]).lower() == 'nan'):
                continue

            choice = ChoiceModel()
            choice.isRightChoice = str(i) in str(row['Answer'])
            choice.content = str(i) + ". " + str(row['Answer Option ' + str(i)])
            choice.question = question
            choice.save()
            num_of_choice = num_of_choice + 1

        question.numOfChoice = num_of_choice

        question.save()
