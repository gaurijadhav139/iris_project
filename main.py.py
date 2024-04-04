from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iris.html')


@app.route('/test')
def test():
    return render_template('index.html')

@app.route('/get_data', methods = ['POST'])
def model_prediction():
    data = request.form 
    print(data)

    load_model = pickle.load(open(r'C:\Users\gauri\Documents\flask_model _implementation\model.pkl','rb'))
    print(load_model)

    user_data = [[float(data['x1_sepal_length']),
                  float(data['x2_sepal_width']),
                  float(data['x3_petal_length']),
                  float(data['x4_petal_width'])
                  ]]
    
    print(user_data)


    result = load_model.predict(user_data)

    print(result)

    target = ['setosa', 'versicolor', 'virginica']

    print(f"prediction = {target[result[0]]}")


    return target[result[0]]


if __name__ == "__main__":
    app.run(debug=True)