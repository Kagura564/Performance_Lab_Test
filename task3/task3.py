#!/usr/bin/env python
# coding: utf-8

import json
import argparse

def fill_values(tests, values):
    for test in tests:
        test_id = test['id']
        for value in values:
            if value['id'] == test_id:
                test['value'] = value['value']
                break
        if 'values' in test:
            fill_values(test['values'], values)

def main(tests_path, values_path, report_path):
    with open(tests_path, 'r') as f:
        tests = json.load(f)['tests']

    with open(values_path, 'r') as f:
        values = json.load(f)['values']

    fill_values(tests, values)

    with open(report_path, 'w') as f:
        json.dump({"report": tests}, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process test and value data and generate a report.")
    parser.add_argument("tests", help="Path to the tests data file")
    parser.add_argument("values", help="Path to the values data file")
    parser.add_argument("report", help="Path to the report output file")

    args = parser.parse_args()

    main(args.tests, args.values, args.report)





