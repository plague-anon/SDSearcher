#!/usr/bin/python3

# TODO:
    # Implement crunch
    # Enable user to enter (at command line) more than one target and subdomain
    # Enable user to upload a file for
        # targets
        # subdomains
    # Enable result output to a file
    # Correct verbose output

# NOTE: This program currently only accepts (at command line): 1 target and 1 subdomain to check


import os, sys, urllib.request, argparse

args=''
target = []
wordlist = []
crunchMin = ''
crunchMax = ''
crunchChars = ''
tOut = 2
verbose = False
version = '0.1.0'
results=[]

def main():
    for targ in target:
        for word in wordlist:
            if verbose:
                print(f'Trying {word}.{targ}')
            try:
                code = urllib.request.urlopen(f'http://{word}.{targ}',timeout=tOut).getcode()
                if code == 200:
                    results.append(f'{word}.{targ} EXISTS[!]')
                    if verbose:
                        print(f'{word}.{targ} FOUND[!]')
                else:
                    if verbose:
                        print(f'No match found for {word}.{target}')
            except Exception as e:
                if verbose:
                    log=[]
                    log.append(f'Error: {e}')
                    print(e)
    if len(results)>=1:
        print("RESULTS")
        print('=======')
        for r in results:
            print(f'{r}\n')
    else:
        print('=====')
        print('No positive results to show')

def setArgs():
    parser = argparse.ArgumentParser(description='Search for active sub Domains on hosts.', usage='./sdsearcher.py -t TARGET -s SUBDOMAIN [-to SECONDS] [-v]')
    parser.add_argument('-t', '--target', help='Target domain (example.com,) to scan for subdomains', action='store')
    parser.add_argument('-s', '--subDomain', help='Sub domain to test', action='store')
    parser.add_argument('-sF', '--subDomain_File', help='File containing list of sub domains to brute', action='store')
    parser.add_argument('-to', '--timeout', help='Request timeout in seconds', action='store')
    parser.add_argument('-v', '--verbose', help='Verbose output mode', action='store_true')
    parser.add_argument('--version', help='Display version information', action='version', version='%(prog)s ' + version)
    global args
    args = parser.parse_args()

def setVars():
    if args.target:
        target.append(args.target) # NOTE: dont forget to sanitise

    if args.subDomain:
        wordlist.append(args.subDomain)
    elif args.subDomain_File:
        domainInputFile = open((args.subDomain_File), 'r')
        for d in domainInputFile:
            wordlist.append(str(d).strip('\n'))
    else:
        crunchMin = input('Enter the minimum length of the wordlist to create: ')
        crunchMax = input('Enter the maximum length of the wordlist to create: ')
        crunchChars = input('Enter the characters crunch should use to make the wordlist: ')


    if args.timeout:
        global timeout
        timeout=args.timeout

    if args.verbose:
        global verbose
        verbose=True

if __name__ == '__main__':
    setArgs()
    setVars()
    main()
