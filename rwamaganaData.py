import json
import requests
from Dhis_Endpoints import RWAMAGANA_URL, AUTH_HEADER

def process_data_from_api():
    headers = {
        'Authorization': AUTH_HEADER
    }

    response = requests.get(RWAMAGANA_URL, headers=headers)
    data = response.json()

    headers = data['headers']
    metaData = data['metaData']
    rows = data['rows']

    processed_data = []

    for row in rows:
        data_element_id = row[0]
        value = float(row[1])
        period_id = metaData['dimensions']['pe'][0]
        org_unit_id = metaData['dimensions']['ou'][0]

        data_element_name = metaData['items'][data_element_id]['name']
        period_name = metaData['items'][period_id]['name']
        org_unit_name = metaData['items'][org_unit_id]['name']

        entry = {
            "dataElement": data_element_name,
            "value": value,
            "period": period_name,
            "orgUnit": org_unit_name
        }

        processed_data.append(entry)

    return processed_data

if __name__ == "__main__":
    processed_data = process_data_from_api()
    # Output as a JSON array
    print(json.dumps(processed_data, indent=4))

