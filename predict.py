import os
import urllib.request
import pickle
from flask import Flask, request,jsonify
import json

urllib.request.urlretrieve("https://github.com/kurisujhin/CS401-Proj2/raw/master/cntry_ml_model_v0.pickle", filename = "cntry_ml_model_v0.pickle")
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.model=pickle.load(open('cntry_ml_model_v0.pickle','rb'))
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

    # a simple page that says hello
    @app.route('/api/american',methods=['POST'])
    def predict_cntry():
        data = json.loads(request.get_data())
        return jsonify(
            is_american=str(app.model.predict([data['text']])[0]),
            version="kurisu_0.0.2",
            model_data="2022/02/20"
        )

    return app
app=create_app()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')