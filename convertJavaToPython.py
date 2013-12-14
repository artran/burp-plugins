import argparse
import re
from os import listdir
from os.path import isfile, join


interface_re = re.compile(r'public interface (?P<class_name>\w+)')
constants_re = re.compile(r'(?:public\s*)?(?:static\s*)?(?:final\s*)?(?:[\w<>\[\]]+)\s+(?P<name>[\w]+)\s*=\s*(?P<value>[\w\d]+)')
function_re = re.compile(r'(?:private|public)?\s+(?:[\w<,>\[\]]+)\s+(?P<method_name>\w+)\((?P<args>[\w\s,\[\]]*)\)', flags=re.MULTILINE)
coalesce_whitespace_re = re.compile(r'\s+')
params_re = re.compile(r'(\s?)[\w\[\]<>]+\s(\w+)\s?')


def read_whole_file(interfaceFile):
    file_str = ''
    for line in interfaceFile:
        file_str += line
    return file_str


def output_class_definition(file_str, output_file):
    match = interface_re.search(file_str)
    output_file.write('class %s:\n' % match.group('class_name'))


def output_constant_definitions(file_str, output_file):
    matches = constants_re.finditer(file_str)
    constants_found = False
    for match in matches:
        constants_found = True
        output_file.write('    %s = %s\n' % (match.group('name'), match.group('value')))

    if constants_found:
        output_file.write('\n')


def fixup_reserved_words(python_args):
    python_args = python_args.replace('from', 'frm')
    python_args = python_args.replace('type', 'typ')
    python_args = python_args.replace('buffer', 'buf')
    return python_args


def put_all_args_on_one_line(method_args):
    python_args = method_args.replace('\r', '').replace('\n', '')
    return python_args


def remove_type_definitions(python_args):
    python_args = re.sub(params_re, r'\1\2', python_args)
    return python_args


def fixup_args(method_args):
    python_args = put_all_args_on_one_line(method_args)
    python_args = remove_type_definitions(python_args)
    python_args = fixup_reserved_words(python_args)
    prefix = ', ' if python_args else ''
    python_args = prefix + python_args
    python_args = re.sub(coalesce_whitespace_re, ' ', python_args)
    return python_args


def output_function_definitions(file_str, output_file):
    matches = function_re.finditer(file_str)
    for match in matches:
        python_args = fixup_args(match.group('args'))
        output_file.write('    def %s(self%s):\n        pass\n\n' % (match.group('method_name'), python_args))


def convert_one_interface(interfaceFile, output_file):
    file_str = read_whole_file(interfaceFile)
    output_class_definition(file_str, output_file)
    output_constant_definitions(file_str, output_file)
    output_function_definitions(file_str, output_file)
    output_file.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('indir')
    parser.add_argument('outdir')
    args = parser.parse_args()

    output_file = open(join(args.outdir, 'burp.py'), 'w')

    filesInIndir = [f for f in listdir(args.indir) if isfile(join(args.indir, f)) and f.endswith('.java')]

    for f in filesInIndir:
        with open(join(args.indir, f), 'r') as interface_file:
            convert_one_interface(interface_file, output_file)

    output_file.flush()
    output_file.close()