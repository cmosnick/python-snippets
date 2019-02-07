# Script to pretty print a timestamp

import sys
import datetime

def main(timestamp):
  dateandtime = datetime.datetime.utcfromtimestamp(float(timestamp)/1000)
  print(dateandtime.strftime('%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    main(sys.argv[1])