from flask import Flask, request

app = Flask(__name__)
list_of_messages = list()


@app.route('/')
def start():
    return 'Messanger Flask server is running! ' \
            '<br> <a href="/status">Check status</a>'


@app.route('/status')
def status():
    return {
        'message count': len(list_of_messages)
    }


# отправка сообщений
@app.route('/api/Messanger', methods=['POST'])
def send_message():
    msg = request.json
    print(msg)
    list_of_messages.append(msg)
    msg_text = f'{msg["UserName"]} <{msg["TimeStamp"]}>: {msg["MessageText"]}'
    print(f'Всего сообщений: {len(list_of_messages)}, посланное сообщение: {msg_text}')
    return f'Сообщение отослано успешно. Всего сообщений: {len(list_of_messages)}', 200


# получение сообщений
@app.route('/api/Messanger/<int:id>')
def get_message(id):
    print(id)
    if 0 <= id < len(list_of_messages):
        print(list_of_messages[id])
        return list_of_messages[id], 200
    else:
        return 'Not found', 400



if __name__ == '__main__':
    app.run()
