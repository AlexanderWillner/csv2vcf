#!/usr/bin/env python

"""
    Author : Mridul Ahuja (original author)
    Author : Alexander Willner (updates, refactoring)
    Github : https://github.com/AlexanderWillner/csv2vcf
    Description : A small command line tool to convert CSV files to VCard files

"""

import os
import sys
import csv
import json


def convert_to_vcard(input_file, single_output, input_file_format):

    FN = input_file_format['name']-1 if 'name' in input_file_format else None
    GIVEN = input_file_format['given']-1 if 'given' in input_file_format else None
    SURNAME = input_file_format['surname']-1 if 'surname' in input_file_format else None
    NICKNAME = input_file_format['nickname']-1 if 'nickname' in input_file_format else None
    ORG = input_file_format['org']-1 if 'org' in input_file_format else None
    TEL = input_file_format['tel']-1 if 'tel' in input_file_format else None
    URL = input_file_format['url']-1 if 'url' in input_file_format else None
    BDAY = input_file_format['bday']-1 if 'bday' in input_file_format else None
    ROLE = input_file_format['role']-1 if 'role' in input_file_format else None
    EMAIL = input_file_format['email']-1 if 'email' in input_file_format else None
    NOTE = input_file_format['note']-1 if 'note' in input_file_format else None

    i = 0

    with open(input_file, 'r') as source_file:
        reader = csv.reader(source_file)
        if single_output:  # if single output option is selected
            vcf = open('csv2vcf/all_contacts.vcf', 'w')

        for row in reader:
            N_VAL = row[SURNAME] if SURNAME is not None else ''
            N_VAL = N_VAL + ";" + row[GIVEN] if GIVEN is not None else ''
            FN_VAL = row[FN] if FN is not None else row[GIVEN] + " " + row[SURNAME]
            NICKNAME_VAL = row[NICKNAME] if NICKNAME is not None else ''
            ORG_VAL = row[ORG] if ORG is not None else ''
            TEL_VAL = row[TEL] if TEL is not None else ''
            URL_VAL = row[URL] if URL is not None else ''
            BDAY_VAL = row[BDAY] if BDAY is not None else ''
            ROLE_VAL = row[ROLE] if ROLE is not None else ''
            EMAIL_VAL = row[EMAIL] if EMAIL is not None else ''
            NOTE_VAL = row[NOTE] if NOTE is not None else ''

            print 'BEGIN:VCARD'
            print 'VERSION:3.0'
            print 'N:' + N_VAL
            print 'FN:' + FN_VAL
            print 'NICKNAME:' + NICKNAME_VAL
            print 'TEL;HOME;VOICE:' + TEL_VAL
            print 'EMAIL:' + EMAIL_VAL
            print 'BDAY:' + BDAY_VAL
            print 'ORG:' + ORG_VAL
            print 'ROLE:' + ROLE_VAL
            print 'URL:' + URL_VAL
            print 'NOTE:' + NOTE_VAL
            print 'END:VCARD'
            print '----------------------'

            if not single_output:  # default ( multi-file output )
                vcf = open('csv2vcf/' + FN_VAL + '_' + TEL_VAL + ".vcf", 'w')

            # write the file
            vcf.write('BEGIN:VCARD' + "\n")
            vcf.write('VERSION:3.0' + "\n")
            vcf.write('N:' + N_VAL + ';' + "\n")
            vcf.write('FN:' + FN_VAL + "\n")
            vcf.write('NICKNAME:' + NICKNAME_VAL + "\n")
            vcf.write('TEL;HOME;VOICE:' + TEL_VAL + "\n")
            vcf.write('EMAIL:' + EMAIL_VAL + "\n")
            vcf.write('BDAY:' + BDAY_VAL + "\n")
            vcf.write('ORG:' + ORG_VAL + "\n")
            vcf.write('ROLE:' + ROLE_VAL + "\n")
            vcf.write('URL:' + URL_VAL + "\n")
            vcf.write('NOTE:' + NOTE_VAL + "\n")
            vcf.write('END:VCARD' + "\n")
            vcf.write("\n")

            if not single_output:  # default ( multi-file output )
                vcf.close()
            i += 1

    vcf.close()
    print str(i) + " VCARDS written"
    print '----------------------'


def main(args):
    args_len = len(args)

    if args_len < 3 or args_len > 4:
        print("Usage:")
        print(args[0] + " CSV_FILE_NAME [ -s | --single ] INPUT_FILE_FORMAT")
        sys.exit()

    if args_len == 3:
        input_file = args[1]

        try:
            input_file_format = json.loads(args[2])
        except Exception:
            print '\033[91m'+"ERROR : json could not be parsed"+'\033[0m'
            sys.exit()

        single_output = 0
    elif args_len == 4:
        input_file = args[1]

        if args[2] == '-s' or args[2] == '--single':
            single_output = 1
        else:
            print '\033[91m'+"ERROR : invalid argument `" + args[2] + "`"+'\033[0m'
            sys.exit()

        try:
            input_file_format = json.loads(args[3])
        except Exception:
            print '\033[91m'+"ERROR : json could not be parsed"+'\033[0m'
            sys.exit()

    if not os.path.exists(input_file):
        print '\033[91m'+"ERROR : file `" + input_file + "` not found"+'\033[0m'
        sys.exit()

    if not os.path.exists('csv2vcf'):
        os.makedirs('csv2vcf')

    convert_to_vcard(input_file, single_output, input_file_format)


if __name__ == '__main__':
    main(sys.argv)
