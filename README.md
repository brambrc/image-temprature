# image-temprature
This project are for early assessment with Ubersnap.

The apps is to be considered early assessment to make or enhance the image to warmer or colder temperature. This program created using python and pillow plugins.


# Instructions
To run the apps you need to follow the instructions:

- make sure you have installed python and pip installed

- clone this project using the following command

```
git clone https://github.com/brambrc/image-temprature.git
```

- after cloning the project, then open the project using the terminal, and install pillow plugin

```
pip install Pillow
```

- In the project already provided example .jpg image "input.jpg" to start with. If you want to make the temprature of the image warmer just simply use the following command:

```
python temp.py [input.filename] [output.filename] [value temprature]
```

For warmer use the following command
```
python temp.py input.jpg output.jpg 60
```

For colder use the following command

```
python temp.py input.jpg output.jpg -60
```




