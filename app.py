import os
from getdata import get_data

from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.ai.language.questionanswering import models as qna


endpoint = f"{os.environ.get("AZURE_ENDPOINT")}"
credential = AzureKeyCredential(f"{os.environ.get("LANG_RESOURCE_KEY")}")


data_location = "doc"
context = get_data(data_location)

def main():
    client = QuestionAnsweringClient(endpoint, credential)
    with client:
        question="What is the working time?"
        input = qna.AnswersFromTextOptions(
            question=question,
            text_documents=[context]
        )
        output = client.get_answers_from_text(input)

    # best_answer = [a for a in output.answers if a.confidence > 0.9][0]
    best_answer = output.answers[0]
    print(u"Q: {}".format(input.question))
    print(u"A: {}".format(best_answer.answer))
    print("Confidence Score: {}".format(output.answers[0].confidence))
if __name__ == '__main__':
    main()