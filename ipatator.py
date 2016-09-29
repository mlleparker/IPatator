#!/usr/bin/python
#-*- coding: utf-8 -*-


########################################
## IPatator                           ##
########################################
##
## Author   : Mademoiselle Parker
## Email    : 'Z3dlbm5hZWxsZS5nbG9pcmVAZ21haWwuY29t'.decode('base64')
## Twitter  : 'QE1sbGVQYXJrM3JfZGV2'.decode('base64')
## Github   : 'aHR0cHM6Ly9naXRodWIuY29tL21sbGVwYXJrZXI='.decode('base64')
##
## Version : 0.0.0.3 Alpha
## Code name : Blue ﻿Aluminium Ladybug
##
## Semantic:
##  - Header  : 0.0.5.2
##  - Code    : 0.0.3.0
##  - Artcode :
##
## Licence : Free for all.
##
## Personal message : Peace in your
## hearts, stop war, stop rage, stop
## fighting, the life can be awesome :)
##
## I ᶫᵒᵛᵉᵧₒᵤ . ♥♥♥
##
##
########################################
## Features                           ##
########################################
##
## IPatator is a small library to
##  perform some computation on IP.
##
## IPatator can be useful to generate
##  IP list for scanning network tools
##  and it can obfuscate IPv4 for your
##  hacking tools/attempts.
##
##
########################################
## Divers & Dev notes                 ##
########################################
##
## Many functions are inspired by :
##
##  - https://github.com/bsterne/bsterne-tools/blob/master/cidr/cidr.py
##
## Thanks to Brandon Sterne.
##
##   - https://github.com/bsterne
##
##
## MagicIP() is inspired by :
##
##  - https://github.com/D4Vinci/Cuteit
##
## Thanks to D4Vinci.
##
##  - https://github.com/D4Vinci
##
##
########################################
## Changelog                          ##
########################################
##
## 28/09/2016 0.0.0.3 Alpha
##
##   - Add class MagikIP() for IPv4 obfuscation.
##   - Fix many bugs.
##
##
## 23/08/2016 Major update 0.0.0.2 Alpha
##
##   -> Semantic version updated to 0.0.3.0
##   -> Adding new features :
##
##             - cidr2range()
##             - ip2mask()
##
##
##   -> Refactoring old function :
##
##             - dec2bin()
##
##
########################################
## TODO                               ##
########################################
##
## For version 0.0.0.4 Alpha :
##
##  - Add de-obfuscating features to MagicIP().
##  - Add new obfuscation methods.
##  - Write the wiki (on MDWiki) so... install MDWiki on my blog.
##
##
## For version 0.0.0.3 Alpha :
##
##   - Update FEC  // done.
##   - Erroneous user entry -> crash :  // 4/4 fixed.
##
##        - ip2bin()     // fixed.
##        - ip2mask()    // fixed.
##        - cidr2range() // fixed.
##        - bin2ip()     // fixed.
##
##
########################################
## Bug tracker                        ##
########################################
##
##
##
########################################




 #
 ##
 ### Modules & lib importations
 ########################################

import base64, sys
import re



 #
 ##
 ### Import my pretty libs
 ########################################

#from lib import clistyle



 #
 ##
 ### Core var
 ########################################

__author__ = "Mademoiselle Parker"
__version__ = "0.0.0.3 Alpha"
__codename__= "Blue ﻿Aluminium Ladybug"
__authormail__= 'Z3dlbm5hZWxsZS5nbG9pcmVAZ21haWwuY29t'.decode('base64')
__twitter__ = 'QE1sbGVQYXJrM3I='.decode('base64')
__coredev__ = "Lioness Studios"
__github__ = 'aHR0cHM6Ly9naXRodWIuY29tL21sbGVwYXJrZXI='.decode('base64')
__semantic__ = {'header':{'version':'0.0.5.2'},
                'source':{'version':'0.0.3.0'},
                'artcode':{'name':''},
                }
__libmode__ = None
__nosplash__ = True


def author():
    return __author__


def version():
    return __version__


def codename():
    return __codename__


def authormail():
    return __authormail__


def twitter():
    return __twitter__


def coredev():
    return __coredev__


def github():
    return __github__


def semantic():
    return __semantic__


def libmode():
    return __libmode__


def nosplash():
    return __nosplash__



 #
 ##
 ### External library options & parameters
 ########################################

#clistyle.__printmode__ = "shell"
__skin__ = 'dark'
__skin_color__ = 'whitedark'



def skin():
    return __skin__


def skin_color():
    return __skin_color__


#
# To replace Python prompt.
#
#sys.ps1 = clistyle.loadprompt(skin)
#sys.ps2 = clistyle.loadprompt(skin)

#
# To rotate print mode of CLIStyle.
#
def switchme(mode = None):

    if mode:

        if mode == "irc":

            clistyle.__printmode__ = mode


        elif mode == "shell":

            clistyle.__printmode__ = mode



 #
 ##
 ### Source code
 ########################################

#
# Class MagicIP()
# To obfuscate/encode an IPv4.
#
class MagicIP:


    def __init__(self, ip = None, prefix = None):

        self.ip = ip.replace('http://', '').replace('https://', '').split('/')[0] if self.isip(ip.replace('http://', '').replace('https://', '').split('/')[0]) else None
        self.prefix = prefix if prefix else ''



    #
    # Method isip()
    # To check the IPv4 input validity.
    #
    # Return :
    #
    #  Return True else None.
    #
    def isip(self, ip = None):

        ip_tmp = ip if ip else None if not self.ip else self.ip


        if ip_tmp and len(ip_tmp.split('.')) == 4:


            for x in ip_tmp.split('.'):

                if not x.isdigit():


                    return False


            return True



    #
    # Method ip2hex()
    # To encode an IP in hex.
    #
    # Return :
    #
    #  Return a dict of five elements else None.
    #
    def ip2hex(self):

        if self.ip and self.isip():

            data = self.ip.split("/")[0].split(":")[0].split(".")
            result = {
                      'hex': self.prefix,
                      'hex_obf_1': self.prefix,
                      'hex_obf_2': self.prefix,
                      'hex_obf_3': self.prefix,
                      'hex_obf_4': self.prefix + '0x',
                     }


            for x in data:

                result['hex'] += hex(int(x)) + '.' if x != data[len(data) - 1] else hex(int(x)) + '/' if self.prefix != '' else hex(int(x))
                result['hex_obf_1'] += (hex(int(x)) + '.') if x != data[len(data) - 1] else data[len(data) - 1] + '/' if self.prefix != '' else data[len(data) - 1]
                result['hex_obf_2'] += (hex(int(x)) + '.') if x != data[len(data) - 2] and x != data[len(data) - 1] else (data[len(data) - 2] + '.') if x == data[len(data) - 2] else data[len(data) - 1] + '/' if self.prefix != '' else data[len(data) - 1]
                result['hex_obf_3'] += (hex(int(x)) + '.') if x != data[len(data) - 3] and x != data[len(data) - 2] and x != data[len(data) - 1] else (data[len(data) - 3] + '.') if x == data[len(data) - 3] else (data[len(data) - 2] + '.') if x == data[len(data) - 2] else data[len(data) - 1] + '/' if self.prefix != '' else data[len(data) - 1]
                result['hex_obf_4'] += hex(int(x))[2:]


            result['hex_obf_4'] += '/' if self.prefix != '' else data[len(data) - 1]


            return result



    #
    # Method ip2octal()
    # To encode an IP in octal.
    #
    # Return :
    #
    #  Return a string else None.
    #
    def ip2octal(self):

        if self.ip and self.isip():


            return {
                    'octal': '%s%s%s' % (self.prefix, '.'.join(format(int(x), '04o') for x in self.ip.split('.')), '/' if self.prefix != '' else ''),
                    'octal_obf_1': '%s%s%s' % (self.prefix, '.'.join([format(int(x), '04o') for x in [x for x in self.ip.split('.')[:3]]] + [self.ip.split('.')[3]]), '/' if self.prefix != '' else ''),
                    'octal_obf_2': '%s%s%s' % (self.prefix, '.'.join([format(int(x), '04o') for x in [x for x in self.ip.split('.')[:2]]] + self.ip.split('.')[2:4]), '/' if self.prefix != '' else ''),
                    'octal_obf_3': '%s%s%s' % (self.prefix, '.'.join([format(int(x), '04o') for x in [x for x in self.ip.split('.')[:1]]] + self.ip.split('.')[1:4]), '/' if self.prefix != '' else ''),
                   }



    #
    # Method ip2long()
    # To encode an IP in decimal.
    #
    # Return :
    #
    #  Return a string else None.
    #
    def ip2long(self):

        if self.ip and self.isip():

            ip_tmp = self.ip.split('.')


            return '%s%s%s' % (
                               self.prefix,
                               str(((((int(ip_tmp[0]) * 256 + int(ip_tmp[1])) * 256) + int(ip_tmp[2])) * 256) + int(ip_tmp[3])),
                               '/' if self.prefix != '' else '',
                              )



    #
    # Method ip2url()
    # To 'URL encode' an IP.
    #
    # Return :
    #
    #  Return a string else None.
    #
    def ip2url(self):

        if self.ip and self.isip():


            return '%s%s%s' % (
                               self.prefix,
                               ''.join([hex(ord(x)).replace('0x', '%').upper() for x in self.ip]),
                               '/' if self.prefix != '' else '',
                              )



    #
    # Method ip2all()
    # To get all obfuscated methods in one shot.
    #
    # Var scheme :
    #
    #  scheme is a list who defines all prefix
    #   wanted.
    #
    #     ie : scheme = [
    #                    'http://',
    #                    'http://google.com@',
    #                    'http://www.google.com@search@',
    #                   ]
    #
    # Return :
    #
    #  Return a structured dict.
    #
    def ip2all(self, scheme = None):

        if self.ip and self.isip():

            memo = self.prefix
            self.prefix = ''
            result = {
                      'scheme': {
                                 'long': [],
                                 'octal': [],
                                 'hex': [],
                                 'url_encoded': [],
                                },

                      'raw': {
                              'long': [],
                              'octal': [],
                              'hex': [],
                              'url_encoded': [],
                             }
                     }


            if scheme is None:

                scheme = [
                          'http://',
                          'http://google.com@',
                          'http://www.google.com@search@',
                         ]



            for x in scheme:

                self.prefix = x
                result['scheme']['long'] += [self.ip2long()]
                result['scheme']['url_encoded'] += [self.ip2url()]
                result['scheme']['octal'] += [self.ip2octal()[x] for x in self.ip2octal()]
                result['scheme']['hex'] += [self.ip2hex()[x] for x in self.ip2hex()]


            self.prefix = ''
            result['raw']['long'] += [self.ip2long()]
            result['raw']['url_encoded'] += [self.ip2url()]
            result['raw']['octal'] += [self.ip2octal()[x] for x in self.ip2octal()]
            result['raw']['hex'] += [self.ip2hex()[x] for x in self.ip2hex()]
            self.prefix = memo


            return result



#
# Class IPerator()
# Just an iterator to reduce RAM consumption.
#
class IPerator:


    def iter(self, ipPrefix = None, i = None, subnet = None):

        if ipPrefix and subnet:


            return bin2ip(ipPrefix + dec2bin(i if i else 0, (32 - subnet)) ) if dec2bin(i if i else 0, (32 - subnet)) else bin2ip(ipPrefix)



#
# Function ip2bin()
# To convert IP to binary format.
#
#
# Var scheme :
#
# ip is string who defines the IPv4 address
#  to convert.
# nodot is boolean who defines the format output.
#
#  If set : '00000000000000000000000000000000'
#  If not set : '00000000.00000000.00000000.00000000'
#
#
# Return :
#
#  Return a string like that else None
#
#  '00000000.00000000.00000000.00000000'
#  or
#  '00000000000000000000000000000000'
#
def ip2bin(ip = None, nodot = False):

    if ip and len(ip.split('.')) == 4:

        iplist = [ str(bin(int(x))) for x in ip.split('.') ]
        count = 0


        for x in iplist:

            x = x.replace('0b', '').replace(' ', '0')


            if len(x) < 8:

                x = "0" * (8 - len(x)) + x


            iplist[count] = x
            count += 1


        return "%s.%s.%s.%s" % (iplist[0], iplist[1], iplist[2], iplist[3]) if not nodot else "%s%s%s%s" % (iplist[0], iplist[1], iplist[2], iplist[3])



#
# Function bin2ip()
# Convert a binary string into an IP address.
#
# Var scheme :
#
# binary is string who defines the IP in binary
#  format.
#
#     ie : '10101100.11011001.00010011.10000011'
#          '10101100110110010001001110000011'
#
#
# Return :
#
#  Return a string who contains IP in IPv4 format
#   else None.
#
#    ie : '172.217.19.131'
#
def bin2ip(binary = None):

    if binary:

        binary = binary if '.' not in binary else ''.join(binary.split('.'))
        ip = ""


        for i in range(0, len(binary), 8):

            ip += str(int(binary[i:i + 8], 2)) + "."


        return ip[:-1]



#
# Function dec2bin()
# Convert a decimal number to binary representation.
# If d is specified, left-pad the binary number with 0s to that length.
#
# Return :
#
#  Return a string or None.
#
def dec2bin(number = None, d = None):

    if number or number == 0:

        buff = bin(number)[2:].zfill(8)


        if d is not None:

            while len(buff) < d:

                buff = "0" + buff


        if buff == "":

            buff = "0"


        return buff



#
# Function ip2mask()
# To compute the network mask from an IP given.
#
# Var scheme :
#
#  ip is string who defines IPv4 address.
#
#     ie : 172.217.19.131/12
#
#
# Return :
#
#  Return string else None.
#
#     ie : '255.240.0.0'
#
def ip2mask(ip = None):

    if ip and len(ip.split('/')) > 1:

        ip = ip.split('/')
        mask = '1' * int(ip[1])
        mask = mask.zfill(32)
        mask_out = ''


        for x in range(0, len(mask), 8):

            mask_out += str(int(mask[x:x + 8][::-1], 2)) + "."


        return '.'.join(mask_out[:-1].split('.')[::-1])



#
# Function cidr2range()
# To convert CIDR format to IP range.
# Return all IPs or first & last IP.
#
# Var scheme :
#  cidr is string who defines CIDR block input.
#  start_end is boolean who defines output mode.
#
#   [ Value ]  [ Description                           ]
#     True       Return first & last IP.
#     False      Return all range.
#
#  counter is boolean who enable the IP counter.
#
#   [ start_end ] [ counter ] [ Description            ]
#     False         False       Generate all range. (str)
#     False         True        Return number of IP in CIDR block. (int)
#     True          False       Return first & end IP & number of IP in CIDR block. (dict)
#     True          True        Return first & end IP & number of IP in CIDR block. (dict)
#
#
# Output :
#
#  >>> cidr2range('17.1.1.1/24', False, True)
#  256
#
#  >>> cidr2range('17.1.1.1/24', True, False)
#  {
#   'FisrtIP': '17.1.1.0',
#   'Network': '17.1.1.0',
#   'Mask': '255.255.255.0',
#   'LastIP': '17.1.1.255',
#   'Broadcast': '',
#   'CIDR': '17.1.1.1/24',
#   'MachineNumber': 256,
#  }
#
#  Incorrect values return None.
#
#  >>> cidr2range('oops', 42, False)
#  >>>
#
def cidr2range(cidr = None, start_end = False, counter = False):

    if cidr and len(cidr.split('/')) > 1:

        parts = cidr.split("/")
        baseIP = ip2bin(parts[0], True)
        subnet = int(parts[1])


        if subnet == 32:

            return bin2ip(baseIP)


        #
        # For any other size subnet, print a list of IP addresses by concatenating
        #  the prefix with each of the suffixes in the subnet.
        #
        else:

            ipPrefix = baseIP[:subnet]
            iterum = IPerator()


            if not start_end:
                if not counter:


                    for i in range(2 ** (32 - subnet)):

                        print iterum.iter(ipPrefix, i, subnet)


                else:

                    return 2 ** (32 - subnet)


            else:

                return {
                         'FisrtIP': iterum.iter(ipPrefix, 0, subnet),
                         'LastIP': iterum.iter(ipPrefix, 2 ** (32 - subnet) - 1, subnet),
                         'MachineNumber': 2 ** (32 - subnet),
                         'Broadcast': iterum.iter(ipPrefix, 2 ** (32 - subnet) - 1, subnet),
                         'Network': iterum.iter(ipPrefix, 0, subnet),
                         'Mask': ip2mask(cidr),
                         'CIDR': cidr,
                       }







