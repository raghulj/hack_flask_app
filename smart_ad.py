from flask import Flask, jsonify
import urllib2
import simplejson as json

app = Flask(__name__)
app.debug = True


def get_smart_ad():
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
	print url
	response = urllib2.urlopen(url)
	html = response.read()
	dd = json.loads(html)
	dd['advertisements'] = get_smart_ad()
	return jsonify(dd)
