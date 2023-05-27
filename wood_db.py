import requests

properties = [{"name": "Janka", "unit": "N"},
              {"name": "Average Dried Weight", "unit": "kg/m"},
              {"name": "Modulus of Rupture", "unit": "MPa"},
              {"name": "Elastic Modulus", "unit": "GPa"},
              {"name": "Crushing Strength", "unit": "MPa"}]


def extract_property(data, property):
    # Inputs: Data is a string; the entirety of the HTML. Property is a dictionary with name and a unit
    # Outputs: The value of the property
    # Date: October 26, 2019
    # index-of-property is data.index(property[name])
    property_pos = data.index(property["name"])
    unit_pos = property_pos + data[property_pos:].index(property["unit"])
    print(data[property_pos:unit_pos].strip().split(" ")[-1][1:].replace(",", ""))


def get_properties(data, name):
    # Input: Data
    # Output: A dictionary of the entire wood
    output = {"name": name}
    for i in properties:
        output[i["name"]] = extract_property(data, i)
    return output


def link_to_wood_dict(link):
    # Input: A link, a string
    # Output: A dictionary of the wood and save to file
    return get_properties(requests.get(link).text, link.split("/")[-2])


if __name__ == "__main__":
    link_to_wood_dict("https://www.wood-database.com/afzelia-doussie/")
