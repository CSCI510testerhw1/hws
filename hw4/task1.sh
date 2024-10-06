#!/bin/bash
kill $(ps aux | grep infinite.sh | gawk '{ if($11 == "bash") {print $2}}')