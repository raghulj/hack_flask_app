from flask import Flask, jsonify
import urllib2
import simplejson as json
from logix import *

app = Flask(__name__)
app.debug = True


def get_smart_ad(category, price_range):
		url =  'http://hackapp.raghulj.com/api/get_ad.php?category='+category+'&price_range='+price_range
		html = get_url_response(url)
		return json.loads(html)


def get_url_response(url):
	response = urllib2.urlopen(url)
	html = response.read()
	return html

@app.route('/listing_detail/<listing_id>')
def smart_detail(listing_id):
	url =  'http://api.propertyguru.com.sg/listing/view/%s' % listing_id
	html = get_url_response(url)
	dd = json.loads(html)
	try:
		if dd['price'] and dd['description']:
			price_range = get_price_range(dd['price'])
			category = get_ad_category(dd['description'])
			print price_range + "~~" + category
			ad = get_smart_ad(category, price_range)
			if ad:
				dd['advertisements'] = ad
	except:
		pass
		
	return jsonify(dd)

