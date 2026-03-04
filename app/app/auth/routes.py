from flask import render_template, request, redirect, url_for, flash
from . import auth


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        # Here would go authentication logic
        if not username:
            flash("Ingrese un nombre de usuario", "error")
            return render_template("auth/login.html")
        return redirect(url_for("main.index"))

    return render_template("auth/login.html", title="Login")
