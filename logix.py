
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from nltk.classify import PositiveNaiveBayesClassifier
import nltk.data
from nltk.tokenize import *


sent_detector = nltk.data.load('english.pickle')



CATEGORY = {}

CATEGORY['FURN'] = 'Not furnished'
CATEGORY['ELEC'] = 'No aircon'
CATEGORY['FURN'] = 'partially furnished'
CATEGORY['FOOD'] = 'No Cooking'
CATEGORY['WIFI'] = 'No wifi'
CATEGORY['FURN'] = 'Unfurnished'
CATEGORY['WIFI'] = 'NO WIFI'
CATEGORY['MISC'] = 'Spacious'
CATEGORY['ELEC'] = 'without A/C'




PRICE_HIGH = 2000
PRICE_MID = 1000

def get_price_range(price):
	if price >= 2000:
		return "H"
	elif price > 1000 and price < 2000:
		return "M"
	elif price < 1000:
		return "L"


def analyse(description_text):
	various_sentences= regexp_tokenize(description_text, r'[,\.\?!"\n\r]\s*', gaps=True)
	suggested_data = {}

	for sent in various_sentences:
		for valid in CATEGORY.values():
			rate  = fuzz.ratio(valid, sent)
			if rate > 50:
				suggested_data[valid] = rate
	return suggested_data

def get_suggestion(value):
	for k, v in CATEGORY.iteritems():
		if v == value:
			return k

def get_ad_category(description):
	suggested_data = analyse(description)
	value1 = max(suggested_data, key=suggested_data.get)
	cat =  get_suggestion(value1)
	if cat:
		return cat
	else:
		return "MISC"
