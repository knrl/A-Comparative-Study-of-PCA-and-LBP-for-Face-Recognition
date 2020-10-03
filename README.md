<h1 align="center"> A Comparative Study of PCA and LBP for Face Recognition Under Illumination Variations </h1>

<br/>
<br/>
<p align="center">
  <img width="500"  src="images/yale-face-1.png">
</p>

<p align="center">Fig 1. Yale Face Database</p>
<br/>

<div class='text-justify'><p>
The purpose of this study is to compare the facial recognition performance of PCA and LBP models, which have two different approaches. For this, the cropped Extended Yale Face Database B database was used and on this database, their performances in face recognition were compared on face images illuminated from 4 different angles [1]. Sample images are shown in Figure 1. A total of 2432 face images, including 64 different facial images of 38 subjects, were studied. In the training data, there are a total of 1440 face images from 48 images, 12 for each different lighting from 30 subjects. In the test data, there are 16 visuals for each 30 subjects in the training data with different illumination equally and 16 visuals from 8 subjects separated from the training data in the same way, a total of 608 visuals. The images were grayscale before being processed by the models. Roc Curve (Roc Curve) for evaluating the models and quantifying the quality of the estimates, as a performance criterion in correct definition; precision, precision and F1 measurement were used.
</p></div><br/>

<h2>How does PCA work?</h2>
<p>
  <strong>We can divide the PCA process into 5 main steps;</strong>

1- Standardizing the Data: As PCA chooses key components based on the variances of the data, the data is scaled. To standardize the data, we subtract the mean value from each and divide it by the standard deviation.
</p>
<p align="center">
  <img height="150"  src="http://marunreview.com/wp-content/uploads/2020/09/Screen-Shot-2020-09-25-at-13.51.57-300x167.png">
</p>
<p>
2- Covariance Matrix Calculation: It is the matrix that gives the covariance (relationship) of each variable in the data set with other variables.</p>
<p align="center">
  <img height="150"  src="http://marunreview.com/wp-content/uploads/2020/09/Screen-Shot-2020-09-25-at-14.01.10-1024x266.png">
</p>
<p>
3- Calculating Eigenvectors and Eigenfaces: Some vectors can change direction when multiplied by another matrix [2]. These special vectors that can remain in the same direction as a result of this product are called "eigenvectors". The values of the product of an eigenvector by a matrix that are equal to one lambda multiple of the eigenvector are called "eigenvalues" [2]. Eigenvalues and eigenvectors help us choose basic components. </p>
<p align="center">
  <img height="150"  src="http://marunreview.com/wp-content/uploads/2020/09/Screen-Shot-2020-09-25-at-14.05.01-768x297.png">
</p>
<p>
4- Eigenvector Selection: As we mentioned before, we are looking for the most meaningful dimensions that will work for us. In the beginning, there were M variables, the choice is made according to the eigenvalues of K eigenvectors such that M> K The selected eigenvectors are chosen according to their eigenvalues in descending order.</p>

<p>
5- Finalizing the Data: After its basic components are obtained, the existing data are positioned according to the new subspace. The existing space consists of data that we initially scaled, with the (W) matrix consisting of K fundamental components that we obtained to transform the space according to the fundamental components, the dot product is made with the transpose of each row of the existing space.</p>


<br/><br/>
<h2>Sources</h2>
<ul>
  <li><a href="https://scikit-learn.org/">scikit-learn</a></li>
  <li><a href="https://opencv.org/">OpenCV</a></li>
  <li><a href="http://cvc.cs.yale.edu/cvc/projects/yalefacesB/yalefacesB.html">The Extended Yale Face Database</a></li>
</ul>  

<br/>

[1] Lee, K. C., Ho, J., Kriegman, D. J., “Acquiring linear subspaces for face recognition under variable lighting,” IEEE Transactions on pattern analysis and machine intelligence, vol. 27, no. 5, pp. 684-698, 2005.
[2] Özdeğerler-Özvektörler: http://kisi.deu.edu.tr//kemal.sehirli/%c3%96zde%c4%9ferler.pdf


