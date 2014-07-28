Unsplash for Sublime Text
=============================

Use real dummy images instead of placeholders. Unsplash for Sublime Text brings beautiful images from [Unsplash](http://unsplash.com)
to Sublime Text, your favorite code editor.

![Unsplash for Sublime Text](http://labs.urre.me/images/unsplash.jpg)

## Features
* Get random image (or image url) from [Unsplash](http://unsplash.com)
* Insert an `img` tag
* Insert image URL
* Insert Background Image CSS

## How to use

* Launch the Command Palette `Shift`+`Cmd`+ P and search for Unsplash

### Keyboard shortcuts:

* `Alt` + `S` → Insert image tag
* `Alt` + `Shift` + `S` → Insert image URL
* `Cmd` + `Alt` + `Shift` + `S` → Insert Background Image CSS

### Settings

You can specify different images sizes in your `Preferences.sublime-settings`. Tumblr sizes: 1280, 500, 400, 250, 100, 75 pixels. For example:

	{
		"imgWidth": 1280
	}

## Installation

### Package Control

If you have [Package Control](http://wbond.net/sublime_packages/package_control) installed

* Just search for "Unsplash" to install

### Using Git
Go to your Sublime Text Packages directory and clone the repository using:

    git clone https://github.com/urre/Unsplash

### Download Manually

* Download the files using the GitHub .zip download option
* Unzip the files and rename the folder to `Unsplash`
* Copy the folder to your Sublime Text `Packages` directory

## FAQ

#### Which version of Sublime Text does this support?
Both Sublime Text 2 and 3

## Changelog

+ **1.0** Fetch images directly via the Tumblr API. Bug fix: use `background` instead of `background image`. Added settings file for fetching different sizes from Tumblr API.

## Notes

Images from Unsplash is free [do whatever you want](http://creativecommons.org/publicdomain/zero/1.0) (CC0 1.0 Universal (CC0 1.0))

You will find photo credits under each photo on [Unsplash](http://unsplash.com)