import pyotp

@app.route("/2fa", methods=["GET", "POST"])
def two_factor_auth():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            totp = pyotp.TOTP(user.secret_key)
            qr_code = totp.provisioning_uri(name="My App", issuer_name="My Company")
            return render_template("2fa.html", qr_code=qr_code)
    return render_template("login.html")

@app.route("/2fa_verify", methods=["POST"])
def two_factor_auth_verify():
    username = request.form["username"]
    password = request.form["password"]
    token = request.form["token"]
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        totp = pyotp.TOTP(user.secret_key)
        if totp.verify(token):
            session["username"] = username
            return redirect(url_for("protected"))
    return "Invalid token"