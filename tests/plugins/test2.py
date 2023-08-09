from flask import Flask, request

class Webhooks:
    app = Flask(__name__)
    requests = request
    payload = None
            
    @app.route('/', method=['POST', 'GET'])
    async def handle_webhook(self):
        self.payload = await request.get_json()
        # 在这里处理接收到的数据
        return 'Webhook received'

    # app.run(host='0.0.0.0',port=3000)
        
