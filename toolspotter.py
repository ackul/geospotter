#!/usr/bin/env python
"""
GeoSpotter - A Tool to check Traffic from Blacklisted Locations
usage: PROGRAM [options] <...>
  -v  Verbose logging
  -l log_file Log output to logfile
  -p  Pcap File (Live Capture is not supported currently) 
Copyright (C) 2013 Achin K, mail: achinkul@gmail.com
"""

import dpkt
import socket
import os, sys
import logging, getopt
import re

def checkBlacklist(src,dst):
    fp = open('config.txt','r')
    content = fp.readlines()
    print content
    for k in content:
        regex = re.compile(k.strip())
        srcMatches = [string for string in src if re.match(regex, string)]
        dstMatches = [string for string in dst if re.match(regex, string)]
        for i in srcMatches:
            logger.info("Blacklist traffic Alert")
            print "src --> " + i
        for j in dstMatches:
            logger.info("Blacklist traffic Alert")
            print "src --> " + j
                    
                    

def digPcap(pcapfile):
    srcIpList = []
    dstIpList = []
    for(timestamp, packetBuffer) in pcapfile:
        try:
            eth = dpkt.ethernet.Ethernet(packetBuffer)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print '[+] Src: ' +src+' --> Dst: '+dst
            
            srcIpList.append(src)
            dstIpList.append(dst)
        except:
            pass
    checkBlacklist(srcIpList,dstIpList)
            


    
def pcap_reader(pcap_file):
    fp = open(pcap_file, 'rb')
    pcap = dpkt.pcap.Reader(fp)
    print pcap
    digPcap(pcap)
      
if __name__=='__main__':
    
    __usage__ = __doc__.replace("PROGRAM", os.path.basename(sys.argv[0]))
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fileHandler = None
    pcapFile = None
    
    
    
    def die_usage(msg=""):
        sys.stderr.write("%s%s\n" % (__usage__, msg))
        sys.exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvl:p:", ["help", "verbose", "log-file", "pcap-file"])
    except getopt.GetoptError, e:        
        die_usage(str(e))
    for o, a in opts:
        if o in ("-h","--help"): die_usage()
        if o in ("-v", "--verbose"): logger.setLevel(logging.DEBUG)                
        if o in ("-l", "--log-file"): fileHandler = logging.FileHandler(a)
        if o in ("-p", "--pcap-file"): pcapFile = str(a)
            

          
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if (fileHandler is not None):
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
    logger.info("Ready... ")
    if pcapFile == None:
        die_usage("Please enter path to Pcap File (-p option)")
    try:
        pcap_reader(pcapFile)
        
    except Exception as e:
        logger.info(e)
        
        
        
