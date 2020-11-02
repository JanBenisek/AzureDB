import os
from flask import Flask, flash, request, redirect, render_template, \
    url_for
import connection_secret
import DB_manager as dm
import random

app = Flask(__name__,
            template_folder="templates",
            static_folder="assets")

app.secret_key = connection_secret.SECRET_KEY

cat_list = ['food', 'technology', 'space', 'history']


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':

        category = request.form['cat_button']

        # If user asks for facts from other users
        if category == 'usr':
            usr_fact = dm.randomFact(conn_str=connection_secret.CONN_STR,
                                     src='usr')

            if usr_fact is None:
                flash('No facts from random users', 'error')
                return redirect(request.url)
            else:
                return render_template("index.html",
                                       randomFact=usr_fact[1],
                                       category=usr_fact[0],
                                       cat_list=cat_list)
        # Facts stored in our DB
        else:
            _, fact = dm.randomFact(conn_str=connection_secret.CONN_STR,
                                    key=category)

            return render_template("index.html",
                                   randomFact=fact,
                                   category=category,
                                   cat_list=cat_list)
    # Otherwise give random fact
    else:
        category, fact = dm.randomFact(conn_str=connection_secret.CONN_STR)

        return render_template("index.html",
                               randomFact=fact,
                               category=category,
                               cat_list=cat_list)


@app.route('/insertFact', methods=['POST'])
def insertFact():

    if request.method == 'POST':

        category = request.form['select_category']
        fact = request.form['input_random_fact']

        # Refuse if no fact was added
        if fact == '':
            flash('Please insert the random fact', 'error')
            return redirect(url_for('index'))

        # Add new fact
        if category != '':

            dm.insertFact(conn_str=connection_secret.CONN_STR,
                          cat=category,
                          fact=fact)

            flash('File successfully uploaded', 'info')

            return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
