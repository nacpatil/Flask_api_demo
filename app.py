from flask import Flask, render_template, request
app = Flask(__name__)

data={}
#data['Headings']=
@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      print(result)
      print(result['Name'])
      global data
      print('data before if',data)
      if not (result['Name'] in data.keys()):
         data[result['Name'] ]=result
         print('data',data)
         print("result['Name']",data[result['Name']])
         return render_template("result.html",result = result)
         
      else:
         return render_template("edit.html",result = result, old_result= data[result['Name'] ])
      

@app.route('/update',methods = ['POST', 'GET'])
def update():
      result = request.form
      print('result from updater',result)
      global data
      name_var=result['Name']
      print('name_var',type(name_var),name_var)
      name_var_without_padding=name_var[1:-1]
      data[name_var_without_padding]=result
      print('Final result:::::::',result)
      return render_template('student.html')


@app.route('/fulllist',methods = [ 'GET'])
def fulllist():
      print("Into full list===========")
      global data
      tl=['  Student Name  ','  Physics  ','  Chemistry  ','  Mathematics  ']
      return render_template('print.html',dict=data,headings=tl)



@app.route('/editstudent',methods = [ 'GET'])
def editstudent():
      return render_template('editheader.html')

@app.route('/studenteditlink/<string:iname>',methods = [ 'GET'])
def studenteditlink(iname):
      return render_template('editstudent.html',sname=iname)

if __name__ == '__main__':
   app.run(debug = True)
