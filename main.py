from flask import Flask, request
from database import db
from validation import Validation


app = Flask(__name__)

@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    input_fields = data.keys()
    templates = db.all()
    for template in templates:
        template_fields = set(template.keys()) - {'name'}
        if template_fields & input_fields:
            if template_fields.issubset(input_fields):
                return template['name']

    for key in data:
        data[key] = Validation.get_type(data[key])
    return data

if __name__ == '__main__':
    app.run(debug=True)
