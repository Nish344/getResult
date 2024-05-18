from vtu import results
import os
import json

TESTS_DIR = os.path.dirname(os.path.realpath(__file__))

# Helper function to process MBA results
def regular_mba_results(format):
    with open(os.path.join(TESTS_DIR, 'data/regular_mba.html')) as test_file:
        test_content = test_file.read()

    results_processor = results.RegularResultProcessor(usn='1BI23IC033', output_format=format)
    dict_result = results_processor.parse_html_response(test_content)
    return results_processor.formatted_results(dict_result)

# Print MBA result as dictionary
def print_regular_mba_results_as_dict():
    program_result = regular_mba_results(format='dict')
    print("MBA Results as Dict:")
    print(json.dumps(program_result, indent=4))

# Print MBA result as JSON
def print_regular_mba_results_as_json():
    program_result = regular_mba_results(format='json')
    print("MBA Results as JSON:")
    print(program_result)

if __name__ == "__main__":
    print_regular_mba_results_as_dict()
    print_regular_mba_results_as_json()

