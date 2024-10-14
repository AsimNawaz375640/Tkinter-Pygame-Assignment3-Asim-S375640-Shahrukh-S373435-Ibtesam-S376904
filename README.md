# Assignment 03 - Tkinter and Pygame Projects

This repository contains two projects:

1. **AI Image Classifier** using Tkinter and TensorFlow.
2. **Side-Scrolling 2D Game** built with Pygame.

## Table of Contents
- [AI Image Classifier](#ai-image-classifier)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Requirements](#requirements)
- [Side-Scrolling 2D Game](#side-scrolling-2d-game)
  - [Overview](#overview-1)
  - [Features](#features-1)
  - [Installation](#installation-1)
  - [Gameplay](#gameplay)
  - [Controls](#controls)
  - [Game Screens](#game-screens)

---
## Names and Student IDs

- **Asim Nawaz** - S375640
- **Shah Rukh** - S373435
- **Ibtesam Ahmad Dar** - S376904

---

# AI Image Classifier

## Overview

This project is a desktop AI image classification application built using **Tkinter** for the GUI and **TensorFlow** with **MobileNetV2** for the image classification model. The user can upload an image, and the app will use the model to predict the top categories of objects in the image.

## Features

- **Upload Image**: The user can upload an image file (JPEG, PNG, etc.).
- **AI Prediction**: Uses the **MobileNetV2** model for image classification.
- **Results Display**: Shows top predictions and their confidence scores.
- **Simple GUI**: Built using Tkinter with a modern design.

## Installation

### 1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Ensure the following packages are installed:

- **TensorFlow**
- **Pillow**
- **NumPy**

## Usage

1. Run the application using the following command:

   ```bash
   python main.py
   ```

2. Upload an image and press **Predict** to classify the image.

## Requirements

- **Python 3.x**
- **TensorFlow 2.x**
- **Pillow 9.x**
- **NumPy 1.23.x**

---

# Side-Scrolling 2D Game

## Overview

This is a side-scrolling 2D game built with Python and Pygame. In the game, the player controls a character to run, jump, and shoot projectiles. The player must defeat enemies, collect items, and progress through levels. The game includes a dynamic health and score system, splash screens, and game over and victory screens.

## Features

- **Player Movement**: Run, jump, and shoot.
- **Enemies**: Increase in size and difficulty as levels progress.
- **Collectibles**: Health boosts and extra lives.
- **Dynamic Health Bar**: Tracks player's health.
- **Multiple Levels**: 3 levels with increasing difficulty.
- **Game Over and Victory Screens**.

## Installation

### 1. Clone the repository or download the project files.
### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the game:
```bash
python main.py
```

## Gameplay

The game involves controlling a character through levels by avoiding enemies, collecting health boosts, and shooting enemies.

### Controls

- **Arrow Keys**: Move left or right.
- **Spacebar**: Jump.
- **Z**: Shoot.
- **Enter**: Start the game.
- **R**: Restart the game.

## Game Screens

- **Splash Screen**: Press Enter to start.
- **Game Over Screen**: Press R to restart after losing.
- **Victory Screen**: Press R to restart after completing all levels.
