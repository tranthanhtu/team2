from flask import Flask, render_template

app = Flask(__name__)
class Movie:
    def __init__(self,title,img):
        self.title = title
        self.img = img
movie1 = Movie('The girl next door','https://i.jeded.com/i/the-girl-next-door-2007.31013.jpg')
movie2 = Movie('kungfu panda', 'https://k14.vcmedia.vn/zoom/308_195/QuickNewsK14/4071215/2015/03/img_201503142312165714.jpg')
movies = [movie1,
              movie2,
              Movie('500 days of summer','https://upload.wikimedia.org/wikipedia/en/d/d1/Five_hundred_days_of_summer.jpg')
              ]


@app.route('/')
def hello_world():
    return 'Hello Tu!'

@app.route('/c4e')
def hi_c4e():
    return 'Hello C4E'

@app.route('/c4e/1')
def hi_team1():
    return 'Hello TEam1'

@app.route('/<name>')
def hello(name):
    return 'Hello ' + name

@app.route('/movie')
def get_movie():
    return render_template('movie.html')

@app.route('/movie_2')
def movies__():
    return render_template('movie_2.html',movie_list = movies)


if __name__ == '__main__':
    app.run()
