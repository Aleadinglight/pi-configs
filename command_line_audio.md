# Command Line Audio

## Overview
[aplay](https://linux.die.net/man/1/aplay): This is used for `.wav` files.

[mpg321](https://linux.die.net/man/1/mpg321): This is used for `.mp3` files.
  
## aplay 
### Installation
This comes as default in Pi4.

### Usage
Use the following command syntax to play an audio file with aplay:
```shell
aplay <file>
```

## mpg321 
### Installation 
```shell
sudo apt-get -y install mpg321
```

### Usage
Use the following command syntax to play an `mp3` file:

```shell
mpg321 <file>.mp3
```
The volume can be adjusted using the `-g` command line option. In the example below I set the volume to 50% :

```shell
mpg321 -g 50 <file>.mp3
```
