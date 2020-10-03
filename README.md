<h1 align="center"> A Comparative Study of PCA and LBP for Face Recognition Under Illumination Variations </h1>

<br/><br/>
<!-- ABOUT THE PROJECT -->
## About The Study
<br/>
<div class='text-justify'><p>
The purpose of this study is to compare the facial recognition performance of PCA and LBP models, which have two different approaches. For this, the cropped Extended Yale Face Database B database was used and on this database, their performances in face recognition were compared on face images illuminated from 4 different angles [1]. Sample images are shown in Figure 1. A total of 2432 face images, including 64 different facial images of 38 subjects, were studied. In the training data, there are a total of 1440 face images from 48 images, 12 for each different lighting from 30 subjects. In the test data, there are 16 visuals for each 30 subjects in the training data with different illumination equally and 16 visuals from 8 subjects separated from the training data in the same way, a total of 608 visuals. The images were grayscale before being processed by the models. Roc Curve (Roc Curve) for evaluating the models and quantifying the quality of the estimates, as a performance criterion in correct definition; precision, precision and F1 measurement were used.
</p></div>

<p align="center">
  <img width="500" height="320" src="images/yale-face-1.png">
</p>

<p align="center">Fig 1. Yale Face Database</p>
<br/><br/>

<h2>Sources</h2>
<ul>
  <li><a href="https://scikit-learn.org/">scikit-learn</a></li>
  <li><a href="https://opencv.org/">OpenCV</a></li>
  <li><a href="http://cvc.cs.yale.edu/cvc/projects/yalefacesB/yalefacesB.html">The Extended Yale Face Database</a></li>
</ul>  

<br/>

[1] Lee, K. C., Ho, J., Kriegman, D. J., “Acquiring linear subspaces for face recognition under variable lighting,” IEEE Transactions on pattern analysis and machine intelligence, vol. 27, no. 5, pp. 684-698, 2005.


