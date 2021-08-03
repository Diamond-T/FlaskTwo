from flask import Flask, render_template

app = Flask (__name__)

#the route
@app.route('/')
def index():
    name = "Diamond's"
    title ="Diamonds site"
    return render_template('index.html', name=name, title=title)

@app.route('/diamond')
def info():
    favorites= ['video games', 'Food', 'Reading', 'Watching TV', 'Spending Time with Family']
    return render_template('Favorite_5.html', title='Test Title!', favorites=favorites)


    
