# The Johnson project


## Process all lakes in Finland to detect certain shapes of personal interest.


I trained a YOLO v8 computer vision model using sketches (30k images) from the internet. I leveraged OpenStreetMap and Overpass API to get all lakes in Finlands borders exceeding certain area threshold(2,500m^2). Then using OpenCV, I processed the lakes to make them look like my bitmap training data.Then just detect. OSM data doesnt always match with one in f.e. Google Maps and the CNN exhibits "some" overfitting but it has enabled me to do what I set out to do.


![Results](/final/results.png)
*Training graph from one of the previous runs. I halted the training early with the best model so unfortunately i do not have graphs for that*

![Map data](/assets/img/greenmap.jpg)
*Before choosing the OSM API my other option was to scan satellite images using opencv contour detection.*


## Learning
This project interested me because it combines machine learning with very concrete real world data and enabled me to find patterns where no one else has looked and produce some real word results. Training a neural network gave a lot of insight and understanding of how CNNs work. I Also learned of the importance of having high quality data, because the first 16 training runs did not produce sufficient results. I learned about the huge power of opencv with image processing and even data annotating.


### Links
I built this during the 6 week program [Sidequest](https://mysidequest.xyz/s1/projects)

### Data
Thanks to these people for the training data. https://github.com/studiomoniker/Quickdraw-appendix

### Images



<p float="left">
  <img src="final\lake_60.032732_24.490773.png" width="325" />
  <img src="final\lake2.png" width="400" />
</p>
<p float="left">
  <img src="final\lake_61.989647_27.664928.png" width="325" />
  <img src="final\lake4.png" width="275" />
</p>
<p float="left">
  <img src="final\lake_62.760774_24.623631.png" width="325" />
  <img src="final\lake5.png" width="400" />
</p>
<p float="left">
  <img src="final\lake_62.710499_27.962578.png" width="325" />
  <img src="final\lake3.png" width="400" />
</p>
<p float="left">
  <img src="final\lake_63.705917_29.636578.png" width="325" />
  <img src="final\lake1.png" width="300" />
</p>




## License
MIT License - see the [LICENSE.md](LICENSE.md) file for details
