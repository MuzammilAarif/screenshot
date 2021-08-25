# from types import MethodType
# from app import URL1
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
    # URL1 = str(URL)
    # print(URL)
    # print(type(URL))
    # print(type(URL1))
    # URL = 'https://github.com/MuzammilAarif/docker-compose-flask-math'
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get(URL)
    S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
    driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
    driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')
    driver.quit()



    return render_template("screenshot.html")


if __name__ == "__main__":
    app.run(debug=True)
