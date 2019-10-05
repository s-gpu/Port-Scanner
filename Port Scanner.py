#!/usr/bin/python3

'''
 ' Port Scanner in Python 3
 ' Author: Sanjan Geet Singh <>
'''

from datetime import datetime
from socket import socket

def now():
      return datetime.now()

def error(msg):
      print("Error:", msg)
      exit(-1)

def scan(addr, time_limit):
      try:
            sock = socket()
            sock.settimeout(time_limit)
            code = sock.connect_ex(addr)
            sock.close()
            return code
      except:
            error("Please check the IP address/Hostname/Internet Connection.")

def main():
      host = input("Enter Target IP or Hostname: ")
      if host == '':
            error("Please input the Target IP Address or Hostname.")

      minp = input("Enter lower port range (default: 1): ")
      if minp == '':
            minp = 1
      else:
            minp = int(minp)
            if minp < 1 or minp > 65535:
                  error("Lower port range cannot be lower than 1 and more than 65535.")

      maxp = input("Enter upper port range (default: 65535): ")
      if maxp == '':
            maxp = 65535
      else:
            maxp = int(maxp)
            if maxp < minp:
                  error("Upper port range should be greater than lower port range.")
            if maxp > 65535:
                  error("Upper port range cannot be more than 65535.")

      time_limit = input("Enter time limit to scan each port (default: 0.5): ")
      if time_limit == '':
            time_limit = 0.5
      else:
            time_limit = float(time_limit)
            if time_limit <= 0:
                  error("Time limit should be greater than 0.")

      print("\nStarting Scan...")
      start_time = now()

      for port in range(minp, maxp+1):
            if scan((host, port), time_limit) == 0:
                  print("Port {}: Open".format(port))

      print("Scan Finished")
      stop_time = now()

      print("Time Elapsed: {}".format(stop_time-start_time))

if __name__ == '__main__':
      main()
