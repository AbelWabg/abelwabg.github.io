from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, static_url_path='/static', static_folder='static')

# 首頁路由，返回 index.html
@app.route('/')
def index():
    return render_template('index.html')

# 支付批准路由，處理 Pi Network 的支付批准請求
@app.route('/payment/approve', methods=['POST'])
def approve():
    try:
        paymentId = request.json.get('paymentId')
        if not paymentId:
            return jsonify({"error": "paymentId is required"}), 400

        approve_url = f"https://api.minepi.com/v2/payments/{paymentId}/approve"
        response = requests.post(approve_url, headers={"Authorization": f"Key {gvmivpxg7uo2wvo774q2jtlwlkbojxybevlv7fjt7sapmhsxeryrlmf5jjewdkru}"})
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to approve payment", "details": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 支付完成路由，處理 Pi Network 的支付完成請求
@app.route('/payment/complete', methods=['POST'])
def complete():
    try:
        paymentId = request.json.get('paymentId')
        txid = request.json.get('txid')
        if not paymentId or not txid:
            return jsonify({"error": "paymentId and txid are required"}), 400

        complete_url = f"https://api.minepi.com/v2/payments/{paymentId}/complete"
        response = requests.post(complete_url, headers={"Authorization": f"Key {gvmivpxg7uo2wvo774q2jtlwlkbojxybevlv7fjt7sapmhsxeryrlmf5jjewdkru}"}, json={"txid": txid})
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to complete payment", "details": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 支付取消路由，處理 Pi Network 的支付取消請求
@app.route('/payment/cancel', methods=['POST'])
def cancel():
    try:
        paymentId = request.json.get('paymentId')
        if not paymentId:
            return jsonify({"error": "paymentId is required"}), 400

        cancel_url = f"https://api.minepi.com/v2/payments/{paymentId}/cancel"
        response = requests.post(cancel_url, headers={"Authorization": f"Key {gvmivpxg7uo2wvo774q2jtlwlkbojxybevlv7fjt7sapmhsxeryrlmf5jjewdkru}"})
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to cancel payment", "details": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 支付錯誤路由，處理 Pi Network 的支付錯誤請求
@app.route('/payment/error', methods=['POST'])
def error():
    try:
        paymentId = request.json.get('paymentId')
        if not paymentId:
            return jsonify({"error": "paymentId is required"}), 400

        cancel_url = f"https://api.minepi.com/v2/payments/{paymentId}/cancel"
        response = requests.post(cancel_url, headers={"Authorization": f"Key {gvmivpxg7uo2wvo774q2jtlwlkbojxybevlv7fjt7sapmhsxeryrlmf5jjewdkru}"})
        
        if response.status_code == 200:
            return jsonify(response.json()), 200
        else:
            return jsonify({"error": "Failed to handle payment error", "details": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 獲取用戶信息路由，處理 Pi Network 的用戶信息請求
@app.route('/me', methods=['POST'])
def getme():
    try:
        accessToken = request.json.get('accessToken')
        if not accessToken:
            return jsonify({"error": "accessToken is required"}), 400

        user_url = "https://api.minepi.com/v2/me"
        response = requests.get(user_url, headers={"Authorization": f"Bearer {accessToken}"})
        
        if response.status_code == 200:
            user_data = response.json()
            return jsonify({"username": user_data.get("username")}), 200
        else:
            return jsonify({"error": "Failed to get user info", "details": response.text}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 啟動 Flask 應用
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)