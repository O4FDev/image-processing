# Image Processing

An image-processing project to group pixels of images and create cool effects!



## Demo

![The rainbow effect shadow mirror demo, please contact me if the image is broken](https://i.imgur.com/CY8dB6a.jpg)

## Authors & Contributors

- [@O4FDev](https://www.github.com/O4FDev) - Creator


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

## Deployment

I am in the process of setting up a [FastAPI for this project]("https://fastapi.tiangolo.com/deployment/").



## Installation

Install ShadowMirror's requirements with pip

```bash
  pip install -r requirements.txt
  python ShadowMirror.py
```
    
## FAQ

#### Curious what frameworks you used?

I used Open-CV for the image processing and Numpy for the array manipulation. 

#### Placeholder question 2 

Placeholder answer 2 
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Support

For support, email luke.lucas@ou.ac.uk or join the NI Tech Slack and post a message in the PyBelfast channel (follow all the rules of the slack please) and I will message you as quickly as possible, please also try to tag me @Luke if you can find me.

## Algorithms 

Here is an overview of the algorithms I have used in this project.

### Calculation of the radius of the circles

The radii of the circles is calculated by the following formula:

```math
average brightness / (sub_group_total*4)
```

### Calculation of the average brightness of the sub groups

The average brightness is the average of the brightness of the pixels in any given sub group of pixels. The sub group size is calculated by the following formula:

```math
y * sub_group_size, x * sub_group_size
```

### Sub group total 

```python
sub_group_size = 10 # Static number, looking into a better way to do this
sub_group_total_y = img.shape[0] // sub_group_size
sub_group_total_x = img.shape[1] // sub_group_size
sub_group_total = sub_group_total_y * sub_group_total_x
```

### Creating the image with the circles

We then loop over a list of the coordinates, radius, etc and create a circle at the centre of each sub group.

### Adding colour 

Almost all of the colour is created in this one line of code: 

```python 
colours.append(
  (x * sub_group_size, y * sub_group_size, brightness))
```

This creates a 3 arguments value for each colour from 0 to 255. Allowing us add the colour to the image using `colours[i]`

### Further reading

If you're interested this far, fair chances you'd be interested in "Halftone Image Processing" there's a great post [here talking about the algorithms.](https://stackoverflow.com/questions/1258047/algorithm-to-make-halftone-images)