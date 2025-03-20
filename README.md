# The Johnson project


## Process all lakes in Finland to detect certain shapes of personal interest.


I trained a YOLO v8 computer vision model using sketches (30k images) from the internet. I leveraged OpenStreetMap and Overpass API to get all lakes in Finlands borders exceeding certain area threshold(2,500m^2). Then using OpenCV, I processed the lakes to make them look like my bitmap training data.Then just detect. OSM data doesnt always match with one in f.e. Google Maps and the CNN exhibits "some" overfitting but it has enabled me to do what I set out to do.

### Links
I built this during the 6 week program [Sidequest](https://mysidequest.xyz/s1/projects)


### Images

<p float="left">
  <img src="final\lake_60.032732_24.490773.png" width="325" />
  <img src="final\lake2.png" width="400" />
</p>
<p float="left">
  <img src="final\lake_61.989647_27.664928.png" width="275" />
  <img src="final\lake4.png" width="300" />
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
