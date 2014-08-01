#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2014-07-30.
Copyright (c) 2014 __MyCompanyName__. All rights reserved.
"""

import sys
import os


def main():
	
	tables = {}
	
	tables["Small Launch Vehicles (5,000 lbs. or less to LEO)"] = (
		("Vehicle name","Athena 2","Cosmos","Pegasus XL","Rockot","Shtil","START","Taurus"),
		("Country/Region of origin","USA","Russia","USA","Russia","Russia","Russia","USA"),
		("LEO capacity lb (kg)","4,520 (2,065)","3,300 (1,500)","976 (443)","4,075 (1,850)","947 (430)","1,392 (632)","3,036 (1,380)"),
		("Reference LEO altitude mi (km)","115 (185)","249 (400)","115 (185)","186 (300)","124 (200)","124 (200)","115 (185)"),
		("GTO capacity lb (kg)","1,301 (590)","0","0","0","0","0","988 (448)"),
		("Reference site and inclination","CCAFS 28.5 deg.","Plesetsk 62.7 deg.","CCAFS 28.5 deg.","Plesetsk 62.7 deg.","Barents Sea 77-88 deg.","Svobodny 51.8 deg.","CCAFS 28.5 deg."),
		("Estimated launch price (2000 US$)","$24,000,000","$13,000,000","$13,500,000","$13,500,000","$200,000*","$7,500,000","$19,000,000"),
		("Estimated LEO payload cost per lb (kg)","$5,310 ($11,622)","$3,939 ($8,667)","$13,832 ($30,474)","$3,313 ($7,297)","$211 ($465)","$5,388 ($11,687)","$6,258 ($13,768)"),
		("Estimated GTO payload cost per lb (kg)","$18,448 ($40,678)","N/A","N/A","N/A","N/A","N/A","$19,234 ($42,411)")
	)
	
	
	labels = {}
	
	labels["Question"] = {
		"What is the current cost of space travel?",
		"How do you define cost?",
		"How do you define travel to space?"
	}
	
	labels["Answer"] = {
		"the average cost of a LEO, Small launch vehicle can on average range anywhere from $8,445 to $3,208 per pound depending on the vehicles country of origin in 2002.",
		"the cost of a vehicle launch can be greatly influenced by government subsidies, e.g. the minimum cost of a LEO small launch vehicle was  the Russia Shtil rocket at a cost of $211 per pound or the Russia Rockot rocket at a cost of $3,313 depending on whether you count Russian government subsidies. "
	}
	
	labels["Citation"] = {
		"Corporation2002"
	}
	
	labels["Resource Text"] = {
		"the 'price per pound to orbit' metric was developed to compare vehicles for their cost effectiveness, mostly in the comparison of vehicles in the design phase. Price per pound offers a simple way to normalize launch costs, permitting more meaningful comparisons among vehicles of different capabilities. This metric has gained wide acceptance, with almost every proposed new launch vehicle since the Space Shuttle using some type of price-per-pound target.",
		"Shtil launch costs partially subsidized by the Russian Navy as part of missile launch exercises",
		"Average Price Per Pound for Western and Non-Western Launch Vehicles...LEO...SMALL: Western = $8,445,Non-Western=$3,208 * (The Zenit 3SL is considered a non-Western launch vehicle because of its Ukrainian and Russian heritage)"
	}
	labels["Resource Table"] = {
		"Small Launch Vehicles (5,000 lbs. or less to LEO)"
	}
	
	graph = {}
	
	graph["What is the current cost of space travel?"]	= {
		"How do you define cost?",
		"How do you define travel to space?",
		"In 2002, the average cost of a LEO, Small launch vehicle can on average range anywhere from $8,445 to $3,208 per pound depending on the vehicles country of origin.",
		"the cost of a vehicle launch can be greatly influenced by government subsidies, e.g. the minimum cost of a LEO small launch vehicle was  the Russia Shtil rocket at a cost of $211 per pound or the Russia Rockot rocket at a cost of $3,313 depending on whether you count Russian government subsidies. "
	}
	
	graph["How do you define cost?"]	= {
		"the 'price per pound to orbit' metric was developed to compare vehicles for their cost effectiveness, mostly in the comparison of vehicles in the design phase. Price per pound offers a simple way to normalize launch costs, permitting more meaningful comparisons among vehicles of different capabilities. This metric has gained wide acceptance, with almost every proposed new launch vehicle since the Space Shuttle using some type of price-per-pound target."
	}
	
	graph["the 'price per pound to orbit' metric was developed to compare vehicles for their cost effectiveness, mostly in the comparison of vehicles in the design phase. Price per pound offers a simple way to normalize launch costs, permitting more meaningful comparisons among vehicles of different capabilities. This metric has gained wide acceptance, with almost every proposed new launch vehicle since the Space Shuttle using some type of price-per-pound target."] = {
		"Corporation2002"
	}
	
	graph["How do you define travel to space?"] = {
		"non-geosynchronous orbit (NGSO) - which includes low Earth orbit (LEO), medium Earth orbit, and highly elliptical orbits - and geosynchronous orbit (GSO) launches."
	}
	
	graph["non-geosynchronous orbit (NGSO) - which includes low Earth orbit (LEO), medium Earth orbit, and highly elliptical orbits - and geosynchronous orbit (GSO) launches."] = {
		"Corporation2002"
	}
	
	graph["Shtil launch costs partially subsidized by the Russian Navy as part of missile launch exercises"] = {
		"Corporation2002"
	}
	
	graph["Small Launch Vehicles (5,000 lbs. or less to LEO)"] = {
		"Corporation2002",
		"Shtil launch costs partially subsidized by the Russian Navy as part of missile launch exercises",
	}
	
	graph["Average Price Per Pound for Western and Non-Western Launch Vehicles...LEO...SMALL: Western = $8,445,Non-Western=$3,208 * (The Zenit 3SL is considered a non-Western launch vehicle because of its Ukrainian and Russian heritage)"] = {
		"In 2002, the average cost of a LEO, Small launch vehicle can on average range anywhere from $8,445 to $3,208 per pound depending on the vehicles country of origin.",
		"Corporation2002"
	}

	
	print "Tables:	"
	print tables
	print "Labels:	"
	print labels
	print "Graph:	"
	print graph

if __name__ == '__main__':
	main()

