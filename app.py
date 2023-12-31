from flask import Flask,render_template,jsonify

app = Flask(__name__)




JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bangalore, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'Mumbai, India',
        'salary': 'Rs. 14,00,000'
    },
    {
        'id': 5,
        'title': 'UX/UI Designer',
        'location': 'Hyderabad, India',
        'salary': 'Rs. 11,00,000'
    }
]


@app.route("/")
def home():
    return render_template('home.html' , 
                           jobs=JOBS,
                           company_name='Jovian')


@app.route("/api/jobs")
def list():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run()