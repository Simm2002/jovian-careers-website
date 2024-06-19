from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
  'id':1,
  'title':'Data Analyst',
'location':'delhi, inida',
'salary':'Rs, 100000'},
   {
    'id':2,
    'title':'Data Scientist',
  'location':'Uk, London',
  'salary':'£ 120000'},
   {
    'id':1,
    'title':'Data Enginer',
  'location':'USA, inida',
  'salary':'$ 70000'}
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

print(__name__)
if __name__ == "__main__":
 app.run(host='0.0.0.0',debug=True)