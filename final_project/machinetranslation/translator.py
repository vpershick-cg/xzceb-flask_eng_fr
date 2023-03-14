'''Translator Module'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('k4ENcWWZq4Z1JYYqqw2Q6elpFBwETikeCfPf0Gqtpopx')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

def english_to_french(english_text):
    '''Translate from English to French'''
    french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return french_text

def french_to_english(french_text):
    '''Translate from French to English'''
    english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    return english_text
