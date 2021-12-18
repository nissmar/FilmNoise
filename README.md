# FilmNoise
Analog grain simulation on grayscale images, inspired by http://www.ipol.im/pub/art/2017/192/
# Why analog grain

Here is a comparison of different noises.

## Gaussian noise, std=30

  <img src="film_grains/white.jpg" width="800"/>

## Bernouilli (0 or 1)
 
 <img src="film_grains/bernouilli.jpg" width="800"/>


## Ours 
  <img src="film_grains/our_noise.jpg" width="800"/>

# Examples

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



<p float="left">
  <img src="example_images/pixabay_zebra.jpeg" width="400"/>
  <img src="example_outputs/zebra1.jpg" width="400"/>
</p>


# Code

Run `noise_image.py`. The mix parameter allows the user to control the intensity of the grain.
