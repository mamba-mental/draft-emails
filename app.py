from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/draft-email', methods=['POST'])
def draft_email():
    data = request.get_json()
    bank = data.get('bank')
    clients = data.get('clients')
    tone = data.get('tone')
    email_content = f"Drafting email for bank: {bank} with tone: {tone}"
    return jsonify({"emailDraft": email_content, "status": "success"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
