from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length

app = Flask(__name__)
app.config["SECRET_KEY"] = 'SECRET_KEY'


class NewsForm(FlaskForm):
    title = StringField("Name", validators=[DataRequired(message="Поле не должно быть пустым"),
                                            length(max=255, message="Не должно быть больше 255 символов")])
    text = TextAreaField("Text", validators=[DataRequired(message="Поле не должно быть пустым")])
    submit = SubmitField("Click")


news = [{'title': 'Удивительное событие в школе',
         'text': 'Вчера в местной школе произошло удивительное событие - все '
                 'ученики одновременно зевнули на уроке математики. '
                 'Преподаватель был так поражен этим коллективным зевком, '
                 'что решил отменить контрольную работу.'},
        {'title': 'Случай в зоопарке',
         'text': 'В зоопарке города произошел необычный случай - ленивец '
                 'решил не лениться и взобрался на самое высокое дерево в '
                 'своем вольере. Посетители зоопарка были поражены такой '
                 'активностью и начали снимать ленивца на видео. В итоге он '
                 'получил свой собственный канал на YouTube, где он размещает '
                 'свои приключения.'},
        {'title': 'Самый красивый пёс',
         'text': 'Сегодня в парке прошел необычный конкурс - "Самый красивый '
                 'пёс". Участники конкурса были так красивы, что судьи не '
                 'могли выбрать победителя. В итоге, конкурс был объявлен '
                 'ничейным, а участники получили награды за участие, '
                 'в том числе - пакетики конфет и игрушки в виде косточек. '
                 'Конкурс вызвал большой интерес у посетителей парка, '
                 'и его решили повторить в более масштабном формате.'},
        {'title': 'Штирлиц и чудо света',
         'text': 'Штирлиц упал в глубокую яму и чудом смог из нее выбраться. "Чудес не бывает", - подумал Штирлиц и '
                 'залез обратно'}]


@app.route('/')
def index():
    return render_template('index.html', news=news)


@app.route('/news_detail/<int:id>')
def news_detail(id):
    title = news[id]['title']
    text = news[id]['text']
    return render_template('news_detail.html', title=title, text=text)


@app.route('/add_news', methods=["POST", "GET"])
def addnews():
    form = NewsForm()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        news.append({'title': title, 'text': text})
        return redirect(url_for("index"))
    return render_template('addnews.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
