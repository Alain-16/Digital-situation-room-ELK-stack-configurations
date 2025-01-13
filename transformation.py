import sys
import json

def transform_data(data):
    transformed_data = []
    metadata_keys = ["dataElements", "dataElementGroups", "dataSets", "organisationUnits", "categoryCombos"]

    for key in metadata_keys:
        if key in data:
            for item in data[key]:
                transformed_item = {
                    "type": key,
                    "id": item.get("id", ""),
                    "name": item.get("name", ""),
                    "created": item.get("created", ""),
                    "lastUpdated": item.get("lastUpdated", "")
                }
                if key == "organisationUnits":
                    transformed_item["path"] = item.get("path", "")
                    transformed_item["level"] = item.get("level", "")
                transformed_data.append(transformed_item)
    
    return transformed_data

if __name__ == "__main__":
    try:
        input_data = json.load(sys.stdin)
        processed_output = {
            "data": transform_data(input_data)
        }
        print(json.dumps(processed_output))
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
