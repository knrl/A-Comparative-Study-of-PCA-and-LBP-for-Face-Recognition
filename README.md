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

<p>
PCA sürecini 5 ana adıma ayırabiliriz;

1- Veriyi Standardize Etmek: PCA verilerin varyanslarına bağlı olarak temel bileşenleri seçtiğinden veriler ölçeklendirilir. Veriyi standardize etmek için her birinden ortalama değeri çıkarıp, standart sapmaya bölüyoruz.
</p>
<p align="center">
  <img width="500"  src="http://marunreview.com/wp-content/uploads/2020/09/Screen-Shot-2020-09-25-at-13.51.57-300x167.png">
</p>
<br/><p>
2- Kovaryans Matris Hesaplaması: Veri setindeki her değişkenin diğer değişkenler ile olan kovaryansını (ilişkisini) veren matristir (2).</p>
<p align="center">
  <img width="500"  src="http://marunreview.com/wp-content/uploads/2020/09/Screen-Shot-2020-09-25-at-14.01.10-1024x266.png">
</p>
<br/><p>
3- Özvektörlerin ve Özyüzlerin Hesaplanması: Bazı vektörler bir başka matris ile çarpıldığında yön değiştirebilir (4). Bu çarpım sonucunda yine aynı yönde kalabilen bu özel vektörlere “özvektörler” denir. Bir özvektörün bir matris ile çarpımının, özvektörün bir lambda katına eşit olan değerlerine de “özdeğerler” denir (4). Özdeğerler ve özvektörler temel bileşenleri seçmemiz için bize yardımcı olur. </p>
<p align="center">
  <img width="500"  src="http://marunreview.com/wp-content/uploads/2020/09/Screen-Shot-2020-09-25-at-14.05.01-768x297.png">
</p>
<br/><p>
4- Özvektör Seçimi: Daha önce bahsettiğimiz gibi işimize yarayacak en anlamlı boyutları arıyoruz. Başlangıçta M tane değişken vardı, M>K olacak şekilde K tane özvektörün özdeğerlerine göre seçim yapılır. Seçilen özvektörleri özdeğerlerine göre büyükten küçüğe doğru seçilir. Bu matrise W diyelim.</p>

<br/><p>
5- Verilerin Son Halini Alması: Temel bileşenleri elde ettiğimize göre mevcut verileri yeni alt uzaya göre konumlandıralım. Mevcut uzay başlangıçta ölçeklendirdiğimiz verilerden oluşuyor, temel bileşenlere göre uzay dönüşümü yapmak için elde ettiğimiz K tane temel bileşinden oluşan (W) matrisle mevcut uzayın her satırının transpozesiyle nokta çarpımı yapılır.</p>


<br/><br/>
<h2>Sources</h2>
<ul>
  <li><a href="https://scikit-learn.org/">scikit-learn</a></li>
  <li><a href="https://opencv.org/">OpenCV</a></li>
  <li><a href="http://cvc.cs.yale.edu/cvc/projects/yalefacesB/yalefacesB.html">The Extended Yale Face Database</a></li>
</ul>  

<br/>

[1] Lee, K. C., Ho, J., Kriegman, D. J., “Acquiring linear subspaces for face recognition under variable lighting,” IEEE Transactions on pattern analysis and machine intelligence, vol. 27, no. 5, pp. 684-698, 2005.


