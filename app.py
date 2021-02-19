import flask
from flask import request, url_for, render_template, redirect


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = 'pk.eyJ1Ijoiam9obmVtbWFudWVsIiwiYSI6ImNrbGJ5MzUyNTAzaXAycXA3cmJyOGpsZHcifQ.SlunA1xGHP9g_Phyqgi5nw'

  return render_template('index.html',
        mapbox_access_token=mapbox_access_token)

if __name__ == '__main__':
    app.run(debug=True)