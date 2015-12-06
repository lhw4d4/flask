from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'nickname':'Migual'}
    posts=[
            {'author':{'nickname':'john'},
                'body':'beautiful day in portland!'
            },
            {'author':{'nickname':'susan'},
                'body':'the avengers movie was so cool!'
            }
          ]
    return render_template("index.html",title='Home',user=user,posts=posts)
