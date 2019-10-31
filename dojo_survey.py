from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def form_input():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def form_output():
    name_from_form = request.form['name']
    location_from_form = request.form['dojo']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    contact_from_form = request.form['contact']
    checbox_values_from_form = request.form.getlist('checkbox')

    return render_template('output.html', name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form, comment_on_template=comment_from_form, contact_on_template=contact_from_form, checbox_values_on_template=checbox_values_from_form)

if __name__ == "__main__":
    app.run(debug=True)
