Geospotter
==========

![alt tag](https://raw.github.com/achinkulshrestha/geospotter/master/img/main.png)

Many a times it happens during forensic investigations that we face the need to search for illegitimate connections quiickly and triage the source. This tool uses a configuration file to blacklist/Whitelist locations from where traffic can be received. Currently, the tool needs a pcap file but to activate live capture one can use [pypcap](http://code.google.com/pypcap)

Usage:

```
GeoSpotter - A Tool to check Traffic from Blacklisted Locations
usage: PROGRAM [options] <...>
  -v  Verbose logging
  -l log_file Log output to logfile
  -p  Pcap File (Live Capture is not supported currently) 
Copyright (C) 2013 Achin K, mail: achinkul@gmail.com
```

