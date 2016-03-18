#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import imghdr
import os

# Iterate through wallpapers, automatically create entries

home_dir = os.path.expanduser("~")
wallpaper_dir = os.path.join(home_dir, "Pictures", "Wallpapers")
gbp_dir = os.path.join(home_dir, ".local", "share", "gnome-background-properties")
outpath = os.path.join(gbp_dir, "personal.xml")

os.makedirs(gbp_dir, exist_ok=True)
with open(outpath, "w") as outfile:
	outfile.write('<?xml version="1.0" encoding="UTF-8"?>')
	outfile.write('<!DOCTYPE wallpapers SYSTEM "gnome-wp-list.dtd">')
	wallpapers = ET.Element("wallpapers")
	tree = ET.ElementTree(wallpapers)
	for root, dirs, images in os.walk(wallpaper_dir):
		for image in images:
			image_path = os.path.join(root, image)
			if imghdr.what(image_path):
				wallpaper = ET.SubElement(wallpapers, "wallpaper")
				wallpaper.set("deleted", "false")
				name = ET.SubElement(wallpaper, "name")
				name.text = os.path.splitext(image)[0]
				filename = ET.SubElement(wallpaper, "filename")
				filename.text = image_path
				options = ET.SubElement(wallpaper, "options")
				options.text = "zoom"
				pcolor = ET.SubElement(wallpaper, "pcolor")
				pcolor.text = "#ffffff"
				scolor = ET.SubElement(wallpaper, "scolor")
				scolor.text = "#000000"
	tree.write(outfile, encoding="unicode")
