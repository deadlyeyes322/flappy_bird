# Flappy bird

## Objective of project

This project I started for training on practic my knowledge in OOP.

## What technologies I will use?

- Standart Python libraries for game algohrithm and for needed files upload.

```
import random, os, time, sys
```

- Pygame is main library that we need, It created screen for game and updated events on this screen

```
import pygame
```

## Game

Player controlling Bird, which can only jump. Gamer need jump over columns and collecting points.

## Algorithm

```
Class Bird:
  pass
```

- Class Bird created bird texture and in this class we will be follow player input and change Bird position in space.

```
Class Wall:
  pass
```

- Class Wall created wall texture, which will be obstacle for the player. In this class our main task is create random position for the wall. We can't create static position for obstacle and therefore we need with help module random create some random position. And this is a place, which posed great difficulties for me.

```
def resource_path(relative_path):
    pass
```

- Function resource_path help us to upload needed files for game.

## Assets

File asset_files.py we needed to save pictures game assets

- Bird assets we will be keep in dictionary

- All the rest we will keep in pygame.image format
