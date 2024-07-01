from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/draft-email', methods=['POST'])
def draft_email():
    data = request.get_json()
    bank = data.get('bank')
    clients = data.get('clients')
    tone = data.get('tone')
    email_content = f"Drafting email for bank: {bank} with tone: {tone}"
    return jsonify({"emailDraft": email_content, "status": "success"})

@app.route('/load-bank-contacts', methods=['POST'])
def load_bank_contacts():
    data = request.get_json()
    file_path = data.get('filePath')
    # Assuming the file is stored on the server
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            contacts = json.load(file)
        return jsonify({"status": "success", "contacts": contacts})
    else:
        return jsonify({"status": "error", "message": "File not found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
