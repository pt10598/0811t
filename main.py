from flask import Flask, request, render_template, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
app = Flask(__name__)

@app.route('/')
def formPage():
    return render_template('page.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        tte = request.form['user2']
        tte2 = request.form['user3']
        chrome_options=Options()
        chrome_options.add_argument("--headless")
        driver=webdriver.Chrome(options=chrome_options)
        driver.get("https://ppstrq.nat.gov.tw/pps/pubQuery/PropertyQuery/propertyQuery.do")
        return redirect(url_for('success', name=user,serc6=tte,serc9=tte2))

@app.route('/success/<name>/<serc6>/<serc9>/')
def success(name,serc6,serc9):
    return f"<h2>{name}</h2>"\
           f"<h2>{serc6}</h2>"\
           f"<h2>{serc9}</h2>"\
           "<h2><input type='button' value='返回首頁' onclick='history.back()' style='width:90px;height:40px;'/></h2>"\


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
