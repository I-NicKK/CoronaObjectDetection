# Final project CS583
This is the final project for CS583 class, in this project I created a web based application using python and flask that takes in an image as an input from the user, performs image recognition to find the name of the object if it belongs to these classes:
Pan
<ul>
<li>Shipping Box</li>
<li>Soda Can</li>
<li>Table</li>
<li>Paper</li>
<li>Glass</li>
<li>backpack</li>
</ul>
Then outputs how long can coronavirus last on these surfaces.

## Dependencies
1. The data is included with the project inside tf_files/objects/ directory
2. Python
3. Tensorflow
4. Anaconda would be preferable as it comes with most of the libraries installed but project will work without it
5. Flask
6. Libraries like Numpy, Scipy etc.

## Working
1. In the same directory, run "python server.py" This will start the flask server
2. Open the browser and goto "localhost:5000"
3. There the webpage will ask you to upload an image
4. After uploading the image hit submit
5. You'll get result on how long can coronavirus last on that surface

## Results
<img src = "https://ibb.co/yhtGv5y">
