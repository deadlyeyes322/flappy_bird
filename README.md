# Flappy bird

## Objective of project

This project I started for the training on practic my OOP knowledge.

## What technologies I will use?

- Standart Python libraries for the game algohrithm and for the load needed files.

```
import random, os, time, sys
```

- Pygame is a main library that we need, It creates screen for the game and updates events on the screen

```
import pygame
```

## Game

Player is controlling Bird, which can only jump. Gamer needed jump over columns and collecting points.

## Algorithm

```
Class Bird:
  pass
```

- Class Bird creates bird texture. We will be capture player inputs and change Bird coordinates.

```
Class Wall:
  pass
```

- Class Wall creates wall texture, which will be obstacle for the player. In this class main task is creating random position for the wall. We can't create static position for obstacle, therefore we need creates any random position with help module Random. 

```
def resource_path(relative_path):
    pass
```

- Function resource_path help us to load needed files for the game.

## Assets

File asset_files.py we needed to save the game assetss.

- Bird assets we will keep in dictionary.

- All the rest we will keep in pygame.image format.
