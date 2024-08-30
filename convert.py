# Programmer: maxhaase@gmail.com

import csv

def csv_to_ldif(csv_file, ldif_file):
    with open(csv_file, 'r') as csvfile, open(ldif_file, 'w') as ldiffile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ldiffile.write(f"dn: {row['dn']}\n")
            for key, value in row.items():
                if key != 'dn' and value:
                    ldiffile.write(f"{key}: {value}\n")
            ldiffile.write("\n")  # Blank line separates LDAP entries

# Example usage
csv_to_ldif('input.csv', 'output.ldif')
