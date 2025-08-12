from flask import Flask, request, jsonify

app = Flask(name)

@app.get("/healthz")
def healthz(): return jsonify({"ok": True})

if name == "main":
app.run(host="0.0.0.0", port=5000)
