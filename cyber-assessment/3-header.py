#!/usr/bin/python3

import sys
import urllib.request
def main():
	if len(sys.argv) < 2:
		print("Usage: python script.py <url>")
		sys.exit(1)

	url = sys.argv[1]

	try:
		with urllib.request.urlopen(url) as response:
			x_request_id = response.getheader("X-Request-Id")
			if x_request_id:
				print(x_request_id)
			else:
				print("X-Request-Id header not found")
	except Exception as e:
		print(f"Error: {e}")
if __name__ == "__main__":
	main()
