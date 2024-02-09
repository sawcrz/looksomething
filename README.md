# Looksomething
Are you bored about rendering some 2d widgets? Well, me too.

Basically this is a tiny python program for render a 3d models like a desktop widgets, using SDL ( aka pygame )
as the backend

## Linux usage
copy the repository:
```
git clone 
```

change the current directory:
```
cd looksomething
```

install the dependencies:
```
pip install pyopengl pygame
```

>[!Important]
>
> If you are in debian, you may notice wich 
> pip or python3 package installation may be
> controlled via apt, so, use synaptic or 
> manually install the packages as follows:
> ``` 
> sudo apt install python3-pygame python3-pyopengl
> ```
> otherwise, you must obtain help about your python installation

finally, run it:
```
sudo ./run.sh
```

## Windows usage
copy the repository:
```
git clone https://github.com/SlowArmoredWarrior/looksomething.git
```

change the current directory:
```
cd looksomething
```

run it in git-bash / cmd / powershell:
```
./run.sh
```
or execute it directly 

## Issues
Fell free to present your issues here, i did not found something at the moment to test this

## Future improvements
By the moment, the widget only presents a cube beign illuminated for an implicit light source, the real objective is:

- [ ] Make the window transparent, for only look the widget content without the gray background
- [ ] Add support for materials and textures
- [ ] Add support for models with quad faces

## I want to run it at the init of my OS
Well, it depends of the operating system and i prefer to left it to yourself, basically for delegating the responsability to you over it

## I want to change the model
You can change the 3d model of the widget replacing the kube.obj file in the assets folder for your preferred model with the same file name

>[!Caution]
>
> - The model must have triangular faces
> - Export the model with its correspondient normals
