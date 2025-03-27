from flask import Flask, render_template, request
import numpy as np
import pickle

diabetes_model = pickle.load(open('models/diabetes.pkl', 'rb'))
heart_model = pickle.load(open('models/heart.pkl', 'rb'))
liver_model = pickle.load(open('models/liver.pkl', 'rb'))
parkinsons_model = pickle.load(open('models/parkinsons.pkl', 'rb'))
##WSGI application helps to communicate between server and application
app = Flask(__name__)
##Decorator has rule==url and option that is methods to be used
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/diabetes", methods=['GET','POST'])
def diabetes():
    return render_template('diabetes.html')

@app.route("/heart", methods=['GET','POST'])
def heart():
    return render_template('heart.html')

@app.route("/parkinsons", methods=['GET','POST'])
def parkinsons():
    return render_template('parkinsons.html')

@app.route("/liver", methods=['GET','POST'])
def liver():
    return render_template('Liver.html')

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        if(len([float(x) for x in request.form.values()])==8):
            preg = int(request.form['pregnancies'])
            glucose = int(request.form['glucose'])
            bp = int(request.form['bloodpressure'])
            st = int(request.form['skinthickness'])
            insulin = int(request.form['insulin'])
            bmi = float(request.form['bmi'])
            dpf = float(request.form['dpf'])
            age = int(request.form['age'])
            
            data = np.array([[preg,glucose, bp, st, insulin, bmi, dpf, age]])
            my_prediction = diabetes_model.predict(data)
            
            return render_template('predict.html', prediction=my_prediction)

        elif(len([float(x) for x in request.form.values()])==13):
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            cp = int(request.form['cp'])
            trestbps = int(request.form['trestbps'])
            chol = int(request.form['chol'])
            fbs = int(request.form['fbs'])
            restecg = int(request.form['restecg'])
            thalach = int(request.form['thalach'])
            exang = int(request.form['exang'])
            oldpeak = float(request.form['oldpeak'])
            slope = int(request.form['slope'])
            ca = int(request.form['ca'])
            thal = int(request.form['thal'])

            data = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
            data1 = np.array(data).reshape(1,-1)
            my_prediction = heart_model.predict(data1)
            return render_template('predict.html', prediction=my_prediction)
        
        elif(len([float(x) for x in request.form.values()])==22):
            MDVP_Fo= float(request.form['MDVP_Fo'])
            MDVP_Fhi= float(request.form['MDVP_Fhi'])
            MDVP_Flo= float(request.form['MDVP_Flo'])
            Jitter= float(request.form['Jitter'])
            Jitter_Abs= float(request.form['Jitter_Abs'])
            MDVP_RAP= float(request.form['MDVP_RAP'])
            MDVP_PPQ= float(request.form['MDVP_PPQ'])
            Jitter_DDP= float(request.form['Jitter_DDP'])
            MDVP_Shimmer= float(request.form['MDVP_Shimmer'])
            MDVP_Shimmer_dB= float(request.form['MDVP_Shimmer_dB'])
            Shimmer_APQ3= float(request.form['Shimmer_APQ3'])
            Shimmer_APQ5= float(request.form['Shimmer_APQ5'])
            MDVP_APQ= float(request.form['MDVP_APQ'])
            Shimmer_DDA= float(request.form['Shimmer_DDA'])
            NHR= float(request.form['NHR'])
            HNR= float(request.form['HNR'])
            RPDE= float(request.form['RPDE'])
            DFA= float(request.form['DFA'])
            spread1= float(request.form['spread1'])
            spread2= float(request.form['spread2'])
            D2= float(request.form['D2'])
            PPE= float(request.form['PPE'])

            data = [MDVP_Fo,MDVP_Fhi,MDVP_Flo,Jitter,Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
            data1 = np.array(data).reshape(1,-1)
            my_prediction = parkinsons_model.predict(data1)
            return render_template('predict.html', prediction=my_prediction)
        
        elif(len([float(x) for x in request.form.values()])==10):
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            tot_bilirubin = float(request.form['tot_bilirubin'])
            direct_bilirubin = float(request.form['direct_bilirubin'])
            tot_proteins = int(request.form['tot_proteins'])
            albumin = int(request.form['albumin'])
            ag_ratio = int(request.form['ag_ratio'])
            sgpt = float(request.form['sgpt'])
            sgot = float(request.form['sgot'])
            alkphos = float(request.form['alkphos'])

            data = [age,gender,tot_bilirubin,direct_bilirubin,tot_proteins,albumin,ag_ratio,sgpt,sgot,alkphos]
            data1 = np.array(data).reshape(1,-1)
            my_prediction = liver_model.predict(data1)
            return render_template('predict.html', prediction=my_prediction)


if __name__ == "__main__":
    app.run(debug=True)