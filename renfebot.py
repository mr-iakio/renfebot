#!/usr/bin/env python2.7

import sys
import os
import argparse
import datetime
import mechanize
import logging
import urllib2


###########################################
# Main
###########################################
def main():
    # READ ARGUMENTS
    parser = argparse.ArgumentParser(description=
                                     '''
    Analyse Receiver selection channel tracking in PROSBAS. 
    This means that the satellites tracked by each user, each epoch will be analyzed to assess if they change very often.
    Uses as input the 'RecSatSelection_XXXXX.dat' files in a scenario
    ''')
    # parser.add_argument('scenario', help='PROSBAS Scenario path')
    # parser.add_argument('-t' ,'--timeStep', type=int, default=1, help='Time step to provide statistics (use one data point each "timeStep")')
    args = parser.parse_args()

    logger = logging.getLogger("mechanize.http_responses")
    logger.addHandler(logging.StreamHandler(sys.stdout))
    logger.setLevel(logging.DEBUG)

    response = urllib2.urlopen('http://www.renfe.com/')
    html = response.read()
    print html
    print HOLA
    return

    br = mechanize.Browser()
    br.open("https://www.renfe.com/")
    br.select_form(nr=0)
    br.form['IdOrigen'] = "MADRID (TODAS)"
    br.form['IdDestino'] = "SANTANDER"
    br.form['__fechaIdaVisual'] = "23/12/2017"

    br.find_control("mascota").items[0].selected = False
    br.find_control("atendo").items[0].selected = False

    print br.form

    br.submit()


if __name__ == "__main__":
    main()
