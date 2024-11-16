from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        "caption": 'А.С. Пушкин о Крыме',
        "poem": ["Прекрасны вы, брега Тавриды:",
                 "когда вас видишь с корабля",
                 "при свете утренней Киприды,",
                 "как вас впервой увидел я;",
                 "вы мне предстали в блеске брачном:",
                 "на небе синем и прозрачном сияли груды ваших гор -",
                 "долин, деревьев, сел узор",
                 "разостлан был передо мною."
                 ]
    }
    return render_template('home.html',  **context)

@app.route('/about')
def about():
    context = {
        "image_link": "static/images/crimea_2.jpg"  # Размещаем фото Крыма
    }
    return render_template('about.html', **context)

if __name__ == '__main__':
    app.run(debug=True)