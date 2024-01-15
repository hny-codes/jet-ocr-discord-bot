# Jet - OCR Discord Bot

![](/screenshots/jet-bg.png)

Found yourself in quick need to extract text from an image in Discord? Meet Jet, a discord bot that aims to extract text from any image attachment you feed it!

Powered by [Python-tesseract](https://pypi.org/project/pytesseract/)

**See blog post here:** [Jet - OCR Funsies on Discord](https://hny-blogs.vercel.app/posts/jet-discord-ocr)

## Table of Contents

- [Purpose](#purpose)
  - [The Problem](#the-problem)
  - [The Solution](#the-solution)
- [Setup](#setup)
- [How It Works](#how-it-works)
  - [Language Detection](#language-detection)
  - [Grabbing Text](#grabbing-text)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Disclaimer](#disclaimer)
- [Current Issues](#current-issues)
- [References](#references)

## Purpose

The purpose of this project is to create a discord bot where as a user, I would type a command along with an attachment that has text and in return, the bot would return the user the text within the image through **optical character recognition** (OCR).

### The Problem

During the years of 2022, I became quite interested in Japanese culture and the likes through games (ex. gacha games) and media (variety shows).

This interest led me to taking an interest in picking up Japanese as a language to learn. However, one problem arises during my own self-studies:

> If I wanted to learn Japanese, I would need to learn the Japanese characters and invest time into learning the various kanji that represent the fundamentals of the Japanese language, but I don't exactly have a Japanese keyboard nor know the characters in the first place. How would I be able grab each individual (or set of) Japanese kanji in the first place?

![](</screenshots/GnT%20(2012-08-26)%20_231119%20(Raw)%20-%20Kiki%20Mizu%20Yokan.jpg>)
_Gaki No Tsukai 2012 - Kiki Mizu Yokan episode_

### The Solution

Through my development journey, I came across the concept of OCR and how it works. This gave me the idea where if I were to utilize the power of OCR to **grab text from images** that I provide, I would be able to **easily retrieve various kanji** to use them for my self-studies.

## Setup

**Python version: 3.8.10**

1. Clone this repository
2. Using Python, install the necessary packages within `requirements.txt`

Example:

```bash
pip install -r requirements.txt
```

3. Within the root project folder, create a `.env` file. This will store your Discord token. Your directory should look something like this:

```
OCR-BOT/
├── tests/
├── image_util.py
├── main.py
├── ocr_reader.py
├── .env          <--- your newly created .env file!
└── ...
```

4. Inside your `.env` file, add your Discord token with the following:

```
DISCORD_TOKEN='YOUR TOKEN HERE'
```

5. Run `main.py` and you should be good to go!

Example:

```
python main.py
```

## How it Works

While online, the bot will listen to the `$text` command. This command must include an image attachment that is meant to read. If successful, **the bot will respond a message to confirm the attachment**.

### Language Detection

When the attachment is read, Pytesseract's `image_to_osd()` function is called to collect information about the attachment. This information includes:

- Page Orientation (Degrees)
- Page Rotation
- **Script/Language detection**

### Grabbing Text

Pytesseract's `image_to_string()` function is then called utilizing the detected language.

- If an image that contains English is detected, then `Latin` (English) will be passed to the `image_to_string()` function as the primary language
- If an image that contains Japanese is detected, then `Japanese` or `Katakana` will be passed to the `image_to_string()` function instead

Once the text has been returned, **the bot edits their confirmation message and replace it with the acquired text.**

**Note:** Images are parse as-is without any preprocessing (OpenCV). Expect inaccurate outputs.

## Usage

All commands are prepended with the `$` symbol.

- `$text` - Extracts text from an image while providing accuracy on how well the extraction performed.

- `$text jpn` - this command can be used for better accuracy for images that contain Japanese text if the automatic language is inaccurate.

## Screenshots

![](/screenshots/screenshot-examples.png)

## Disclaimer

At the end of the day, this is simply a hobby project that I made for myself and a couple of other friends within my Discord circle of friends that can make use of it.

Although I am quite interested in OCR and it's ability, I have little knowledge of the matter.

Jet **will** throw wacky outputs if users feed images that contain verbose backgrounds or include different symbols/icons (that isn't just text).

**Even though the bot isn't perfect, it suit my use cases completely.**

## Current Issues

Nothing concretely planned to be fixed here, however here are some issues that arose from usage:

- Detected languages from `image_to_osd()` can be quite inaccurate.
  - `Hebrew` or `Han` can be detected from attaching an image with Japanese
  - `Cyrillic` can sometimes be detected from attaching an image with English
- Inaccurate results despite having little background noise.

![](/screenshots/screenshot-oops.png)

## References

- [Discord.py](https://discordpy.readthedocs.io/en/latest/index.html)
- [Pytesseract PyPi Page](https://pypi.org/project/pytesseract/)
- [Python Exception Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [pyimagesearch article on psm modes](https://pyimagesearch.com/2021/11/15/tesseract-page-segmentation-modes-psms-explained-how-to-improve-your-ocr-accuracy/)
