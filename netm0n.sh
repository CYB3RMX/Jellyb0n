#!/bin/bash

# Arguments
iface=$1
xterm -e "sudo tcpdump -i $iface"
