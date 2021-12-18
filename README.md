# FilmNoise

Analog grain simulation on grayscale images, inspired by http://www.ipol.im/pub/art/2017/192/

# Why analog grain

Although the dynamic range of analog film cannot be matched, its texure can be mimicked in post-production. However the usual noise distributions don't render film noise (grain) convincingly:  

## Gaussian noise, std=30

  <img src="film_grains/white.jpg" width="800"/>

## Bernouilli (0 or 1)
 
 <img src="film_grains/bernouilli.jpg" width="800"/>

## Ours 

We add white circles to fixed-size black patches, preserving the mean of the pixel of the original image: 
  <img src="film_grains/our_noise.jpg" width="800"/>

# Examples

<p float="left">
  <img src="example_images/pixabay_zebra.jpeg" width="400"/>
  <img src="example_outputs/zebra1.jpg" width="400"/>
</p>

<p float="left">
  <img src="example_outputs/zebra_eye.jpg" width="805"/>
</p>


<p float="left">
  <img src="example_images/pixabay_japan.jpeg" width="400"/>
  <img src="example_outputs/japan0.5.jpg" width="400"/>
</p>

<p float="left">
  <img src="example_images/pixabay_man.jpeg" width="400"/>
  <img src="example_outputs/man0.2.jpg" width="400"/>
</p>


<p float="left">
  <img src="example_images/rodin.jpeg" width="400"/>
  <img src="example_outputs/rodin1.jpg" width="400"/>
</p>

<p float="left">
  <img src="example_images/venus.jpeg" width="400"/>
  <img src="example_outputs/venus0.5.jpg" width="400"/>
</p>





# Code

The code can be ran `noise_image.py`. The mix parameter allows the user to control the intensity of the grain, there is a live preview in the notebook.
The whole process takes about 30s.
