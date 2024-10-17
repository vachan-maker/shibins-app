from flask import Flask, request, render_template
import requests
app = Flask(__name__)

@app.route('/movie', methods=['GET'])
def movie():

    inputYear = request.args.get('year')
    inputTitle = request.args.get('title')
    response = requests.get(f'https://www.omdbapi.com/?t={inputTitle}&y={inputYear}&plot=full&apikey=f072924a')
    data = response.json()
    print(data['Title'])
    title = data['Title']
    year = data['Year']
    genre = data['Genre']
    plot = data['Plot']
    poster = data['Poster']
    return render_template('index.html', title=title, year=year, genre=genre,poster =poster, plot=plot)

@app.route('/')
def form():
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)
