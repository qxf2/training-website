"""
The training senior QA web application.

This application serves static pages for trainingseniorqa.com/
"""

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    "The landing page"
    return render_template('index.html', title='Home')

@app.route("/senior-qa-training-approach")
def approach():
    "How we approach training"
    return render_template('senior-qa-training-approach.html',title='Senior QA training approach')

@app.route("/senior-qa-trainees")
def for_whom():
    "Whom is this training program meant for?"
    return render_template('senior-qa-trainees.html',title='Senior QA training audience')

@app.route("/why-join-senior-qa-training")
def why_join():
    "Reasons to join our training program"
    return render_template('why-join-senior-qa-training.html',title='Why join senior QA training')

@app.route("/why-not-join-senior-qa-training")
def why_not_join():
    "Reasons NOT to join our training program"
    return render_template('why-not-join-senior-qa-training.html',title='Why NOT join senior QA training')

@app.route("/before-you-join")
def before_you_join():
    "Read this before you join"
    return render_template('before-you-join.html',title='Senior QA Training: Before you join')

@app.route("/senior-qa-training-benefits")
def benefits():
    "Benefits of joining our training program"
    return render_template('senior-qa-training-benefits.html',title='Senior QA Training Benefits')

@app.route("/senior-qa-training-plan")
def training_plan():
    "The training plan"
    return render_template('senior-qa-training-plan.html',title='Senior QA Training Plan')

@app.route("/senior-qa-training-samples")
def training_samples():
    "Training samples"
    return render_template('senior-qa-training-samples.html',title='Senior QA Training preview')

@app.route("/senior-qa-training-pricing")
def training_pricing():
    "Training pricing"
    return render_template('senior-qa-training-pricing.html',title='Senior QA Training pricing')


#---START OF SCRIPT
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6464, debug= True)