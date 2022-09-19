from router import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2525)

# 실행 방법 => gunicorn app:app -b 0.0.0.0:2525
