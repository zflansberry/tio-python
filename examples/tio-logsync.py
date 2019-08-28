#!/usr/bin/env python3
"""
..
    Copyright: 2017 Twinleaf LLC
    Author: kornack@twinleaf.com

Log data!

"""

import tldevicesync
import argparse

parser = argparse.ArgumentParser(prog='tio_log', 
                                 description='Very simple logging utility.')

parser.add_argument("url", 
                    nargs='?', 
                    default='tcp://localhost/',
                    help='URL: tcp://localhost')
parser.add_argument("logfile", 
                    nargs='?', 
                    default='log.tsv',
                    help='Log filename: log.tsv')
parser.add_argument("--rpc", 
                    action='append', 
                    default=[],
                    type=lambda kv: kv.split(":"), 
                    help='Commands to be run on start; rpc:type:val')
args = parser.parse_args()

tio = tldevicesync.DeviceSync(url=args.url, rpcs=args.rpc)

file = open(args.logfile,'w') 

print(f"Logging to {args.logfile} ...")

streams = []
streams += [tio.vmr0.vector]
streams += [tio.vmr1.vector]
ss = tldevicesync.SyncStream(streams)

#file.write("\t".join(map(str,device.data.stream_columns()))+"\n")

for row in ss.iter():
  # Tab delimited data
  rowstring = "\t".join(map(str,row))+"\n"
  # Write line
  file.write(rowstring)


