import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            command = 'python -m scripts.label_image \
       --graph=tf_files/retrained_graph.pb  \
    --image=static/images/' + filename
            comm = os.popen(command).read()
            object = comm[36:100]
            for i,j in enumerate(object):
                if j==' ':
                    object_name = object[0:i]
                    break
            url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            if object_name == 'backpack':
                object_name = 'Backpack'
                object_class = 'Plastics'
                d_min = '2'
                d_max = '3 days'
                other_objects = 'Milk containers, Detergent bottles, Subway, Bus seats, Elevator buttons'
            
            elif object_name == 'shipping_box':
                object_name = 'Shipping Box'
                object_class = 'Cardboard'
                d_min = '0'
                d_max = '1 day'
                other_objects = 'Any cardboard related material'  
                
            elif object_name == 'pan':
                object_name = 'Pan'
                object_class = 'Copper'
                d_min = '0'
                d_max = '4 hours'
                other_objects = 'Pennies, Teakettles, Cookware'   
            
            elif object_name == 'soda_can':
                object_name = 'Soda Can'
                object_class = 'Aluminium'
                d_min = '2'
                d_max = '8 hours'
                other_objects = 'tinfoil, water bottles'   
            
            elif object_name == 'glass':
                object_name = 'Glass Cup'
                object_class = 'Glass'
                d_min = '0'
                d_max = '5 days'
                other_objects = 'Drinking glasses, Measuring cups, Mirrors, Windows' 
            
            elif object_name == 'paper':
                object_name = 'Page'
                object_class = 'Paper'
                d_min = '0'
                d_max = '5 days'
                other_objects = 'mail, newspaper'   
            
            elif object_name == 'table':
                object_name = 'Table'
                object_class = 'Wood'
                d_min = '0'
                d_max = '4 days'
                other_objects = 'Furniture, Decking'   
            
            
            
            
            
            
            return render_template('hello2.html', url = url, object = object_name, surface = object_class, time1 = d_min, time2 = d_max, items = other_objects)
    return render_template('hello.html')


                               
if __name__ == '__main__':
   app.run(debug = True)