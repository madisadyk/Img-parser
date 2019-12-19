import requests
from datetime import date, timedelta

draft = "https://edcintl.cr.usgs.gov/downloads/sciweb1/shared/fews/web/asia/centralasia/daily/snowdepth/graphics/sd"
urls = []

sdate = date(2000, 10, 2)   # start date
edate = date(2019, 12, 9)   # end date

delta = edate - sdate       # as timedelta

for i in range(delta.days + 1):
    day = str(sdate + timedelta(days=i))
    temp = draft + day.split('-')[0] + day.split('-')[1] + day.split('-')[2] + '.png'
    urls.append(temp);

def get_file(url):
	r = requests.get(url, stream=True)
	return r

def get_name(url):
	name = url.split('/')[-1]
	return name

def save_image(name, file_object):
	with open(name, 'bw') as f:
		for chunk in file_object.iter_content(2000):
			f.write(chunk)

def main():
	for url in urls:
		save_image(get_name(url), get_file(url))

if __name__ == '__main__':
	main()