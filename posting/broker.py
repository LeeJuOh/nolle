from .TextClassifier.Bi_LSTM.Classifier import init
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'posting'


    def ready(self):
        # TODO: Write your codes to run on startup
        print('init')
        init()