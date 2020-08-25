from flask import Flask
from summarizer import Summarizer

app = Flask(__name__)

@app.route('/')
def hello_world():
	body = 'When troubleshooting Cloud Run, your first step should always be to confirm that you can run your container image locally. If your container image is not running locally, the root cause of the problem is not coming from Cloud Run. You need to diagnose and fix the issue locally first.'
	model = Summarizer()
	summary = model(body)
	return summary


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
