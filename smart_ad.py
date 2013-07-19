from flask import Flask, jsonify
import urllib2
import simplejson as json
from logix import *

app = Flask(__name__)
app.debug = True


def get_smart_ad(category, price_range):
	if category and price_range:
		data = {}
		arr = []
		data['title'] = "Some detail"
		data['image'] = "http://www.freegreatdesign.com/icon/large-apple-icon-png-2921"
		data['summary'] = "Please buy our product"
		arr.append(data)
		return arr


@app.route('/listing_detail/<listing_id>')
def smart_detail(listing_id):
	url =  'http://api.propertyguru.com.sg/listing/view/%s' % listing_id
	response = urllib2.urlopen(url)
	html = response.read()
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
		## jsut ignore for poc
		print 
	return jsonify(dd)



# print get_price_range(4000)
# print get_price_range(1500)
# print get_price_range(400)

# print get_ad_category(descrip)