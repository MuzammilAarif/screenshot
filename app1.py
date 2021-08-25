from flask import Flask, request, render_template
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)

@app.route("/")
def fond():

    return render_template("screenshot.html")

@app.route("/up", methods=["POST", "GET"])
def find():
    
    URL = request.form.get('search')
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.get(URL)
    
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height'))
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
    driver.quit()

    return render_template("screenshot.html")

if __name__ == "__main__":
    app.run(debug=True)
