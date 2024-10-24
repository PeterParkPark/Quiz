import flask

app=flask.Flask(__name__)

app.secret_key = 'secretkey'

questions = [
    {"id":1, "question": "상식문제 1: 서울은 현재 9월 11일 오전 4시이다. 이 시각 영국에서는 어느 날짜의 어느 시각일까? ","answer": "9월 10일 오후 7시", "score": 30},
    {"id":2, "question": "코딩문제 1: Python에서 리스트의 마지막 요소를 어떻게 가져오나요?", "answer": "[-1]", "score": 30},
    {"id":3, "question": "상식문제 2: 대한민국 수도? ", "answer": "서울", "score": 20},
    {"id":4, "question": "코딩문제 2: Python에서 주석을 다는 방법은?", "answer": "#", "score": 10},
    {"id":5, "question": "상식문제 3: 세계에서 가장 큰 나라는?", "answer": "러시아", "score": 10}
]

@app.route('/')
def index():
    flask.session['current_question']=0
    flask.session['score']=0

    return flask.redirect(flask.url_for('question'))
@app.route('/question')
def question():
    current_question = flask.session.get('current_question',0)

    if current_question >= len(questions):
        return flask.redirect(flask.url_for('result'))
    

    question = questions[current_question]

    return flask.render_template('quiz.html',question=question)

if __name__=="__main__":
    app.run(debug=True)