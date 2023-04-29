""" This module creates functions to translate text from English to French 
and vice versa, using IBM Watson Language Translator Service """

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# Set up authentication and create an instance of the service
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set the service URL
translator.set_service_url(url)

def englishToFrench(english_text):
    """
    Translate the English text to French
    """
    french_text = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """
    Translate the French text to English
    """
    english_text = translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()['translations'][0]['translation']
    
    return english_text
