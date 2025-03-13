import csv
import xml.etree.ElementTree as ET
import xml.dom.minidom
import sys
import os

def convert_csv_to_city_xml(csv_file, xml_file):
    print(f"🔍 Debug: Script started!")

    if not os.path.exists(csv_file):
        print(f"❌ Error: CSV file '{csv_file}' not found.")
        return

    print(f"📂 Reading CSV from: {csv_file}")
    print(f"📝 Saving XML to: {xml_file}")

    root = ET.Element("odoo")
    data_element = ET.SubElement(root, "data")

    classification_mapping = {
        "MUNICIPALITY": "Municipality",
        "CITY": "City"
    }

    try:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

            if not rows:
                print("⚠️ Warning: CSV file is empty!")
                return

            required_columns = {"code_correspondence", "name", "city_code", "classification",
                                "old_name", "city_class", "income_classification",
                                "province_code", "province_correspondence", "province_id"}

            if not required_columns.issubset(reader.fieldnames):
                print(f"❌ Error: CSV file is missing required columns: {required_columns - set(reader.fieldnames)}")
                return

            for row in rows[:5]:  # Print first 5 rows for debugging
                print(f"🔹 Processing: {row}")

            for row in rows:
                record = ET.SubElement(data_element, "record", attrib={
                    "id": row["id"].strip(),
                    "model": "psgc.city"
                })

                for key, value in row.items():
                    value = value.strip() if value else ""

                    if key == "id":  # Skip adding "id" as a field
                        continue

                    if key == "classification" and value:
                        value = classification_mapping.get(value.upper(), value)

                    if key == "province_id" and value:  # Use "ref" for province_id only if not empty
                        ET.SubElement(record, "field", attrib={"name": key, "ref": value})
                    else:
                        field_element = ET.SubElement(record, "field", attrib={"name": key})
                        field_element.text = value

        # Convert to a string and beautify it
        raw_xml = ET.tostring(root, encoding="utf-8")
        pretty_xml = xml.dom.minidom.parseString(raw_xml).toprettyxml(indent="    ")

        # Write beautified XML to file
        with open(xml_file, "w", encoding="utf-8") as f:
            f.write(pretty_xml)

        print(f"✅ Beautified XML file successfully created: {xml_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Usage: python3 convert_csv_to_city_xml.py input.csv output.xml")
    else:
        convert_csv_to_city_xml(sys.argv[1], sys.argv[2])