import csv
import xml.etree.ElementTree as ET


def process_child(child, keys):
    d = child.attrib
    return [d.get(k) for k in keys]


def convert(path_to_xml, path_to_csv):
    tree = ET.parse(path_to_xml)
    root = tree.getroot()

    with open(path_to_csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        keys = next(root.iter(tag='row')).keys()
        csvwriter.writerow(keys)
        csvwriter.writerows(
            process_child(child, keys=keys) for child in root.iter(tag='row'))
