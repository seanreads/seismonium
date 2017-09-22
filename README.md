SEISMONIUM (aka Earth Chimes submission to Currents 2016: http://currentsnewmedia.org/festivals/currents-2016/)
==========

TODO:
* define translation between magnitude scale and note pitch
* sketch out user-interface

Description
===========

Earth Chimes translates seismographic data describing our constantly vibrating planet into animated shapes and sounds. 
A 10 foot by 8 foot, video projection displays an increasing number of colored circles, all varying size, onto a empty background. As each circle appears, a musical note is heard, which corresponds in loudness and pitch to the size and intensity of the circle. Over a period of minutes, the black background fades away, revealing underneath a map of a familiar territory. The shapes and sounds overlaid on the map are visualized/sonified information extracted from U.S. Geological Survey Earthquake Data (USGS) (http://earthquake.usgs.gov). The size of each circle represents quake magnitude, as does the loudness of each accompanying note. The pitch of each note indicates the depth (kilometers) of the quake’s epicenter below the Earth’s surface.
The process repeats for one hour -- revealing additional geographic locations behind the visual/sonic signatures of their specific place on the vibrating Earth.

Data Translation
================

Publicly available data feeds from the U.S. Geological Survey provide data point that translate to visual and audible corollaries. The data format is detailed on the USGS website at http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php.

The data translation is as follows:

* Quake Depth → Note Pitch
* Quake Magnitude → Circle Size and Sound Volume

The data contains earthquake events spanning 14+ years. The video of Earth Chimes plays back the events over the course of 5 minutes per geographic location.

Technologies
============

* Apple Quicktime
* Google Maps
* MIDI.js
* Python/Django
