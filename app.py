# from values.py import the function values
from values import values, category_id, category_table

# import Flask
from flask import Flask, render_template, request, redirect

# create app passing the __name__
app = Flask(__name__)

# HOME PAGE
# define what to do when the user hits the "/"
@app.route("/")
def index():
    cat_id = request.args.get('cat_id')
    print (f"Hello all {cat_id}")
    if not cat_id or "all" == cat_id:
        # 
        # the left variable is what is used on the html page
        return render_template("index.html", yt_data=values(), cat_table= category_table())

    else:
        print(f"Hello category {cat_id}")
        return render_template("index.html", yt_data=category_id(cat_id), cat_table= category_table())


@app.route('/table')
def tables():
    return render_template('tables.html')


if __name__=='__main__':
    app.run(debug=True)