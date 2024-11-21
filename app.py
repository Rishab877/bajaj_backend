from flask import Flask, request, jsonify
import base64
import math

app = Flask(__name__)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        data = request.json.get("data", [])
        file_b64 = request.json.get("file_b64", "")

        numbers = [int(x) for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        lowercase_alphabets = [x for x in data if x.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
        is_prime_found = any(is_prime(int(x)) for x in numbers)

        file_valid = False
        file_mime_type = None
        file_size_kb = None

        if file_b64:
            try:
                file_data = base64.b64decode(file_b64, validate=True)
                file_size_kb = len(file_data) / 1024
                file_mime_type = "unknown"
                file_valid = True
            except Exception:
                file_valid = False

        response = {
            "is_success": True,
            "user_id": "your_name_ddmmyyyy",
            "email": "your_email@example.com",
            "roll_number": "your_roll_number",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
            "is_prime_found": is_prime_found,
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
