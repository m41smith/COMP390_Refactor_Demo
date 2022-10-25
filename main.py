import requests
import json
import sqlite3


def issue_get_request(target_url: str):
    """ This function ISSues a GET request to the URL passed as its single parameter.
    A response object is returned
    The status code of the request object is also reported """

    response_obj: requests.Response = requests.get(target_url)
    if response_obj.status_code != 200:
        print(f'The GET request was NOT successful\n{response_obj.status_code} [{response_obj.reason}]')
        return response_obj
    else:
        print(f'the GET request was successful \n{response_obj.status_code} [{response_obj.reason}]')
        return response_obj


def convert_content_to_json(response_obj: requests.Response):
    """ This function accepts a request Response object as its single parameter and tries to
    convert the response content to a json object
    'None' is returned if the conversion was unsuccessful """
    json_data_obj = None
    try:
        json_data_obj = response_obj.json()
        print(f'Response object content converted to JSON object.\n')
    except requests.exceptions.JSONDecodeError as json_decode_error:
        print(f'An error occurred while trying to convert the response content to a json object:\n'
              f'{json_decode_error}')
    finally:
        return json_data_obj


def main():

    target_url_str = 'https://data.nasa.gov/resource/gh4g-9sfh.json'
    response_obj = issue_get_request(target_url_str)

    json_data_obj = convert_content_to_json(response_obj)

    print(json_data_obj)


if __name__ == '__main__':
    main()
