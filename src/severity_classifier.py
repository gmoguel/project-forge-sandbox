cve_id = input("What is the CVE_ID?\n")
cvss_score = float(input("What is the CVSS Score?\n"))

if cvss_score == 0:
    classification = "None"
elif 0 < cvss_score <= 3.9:
    classification = "Low"
elif 4.0 <= cvss_score <= 6.9:
    classification = "Medium"
elif 7.0 <= cvss_score <= 8.9:
    classification = "High"
elif 9.0 <= cvss_score <= 10.0:
    classification = "Critical"
else:
    0 > cvss_score > 10.00
    classification = "Invalid"

print('''================================
     VULNERABILITY SEVERITY
================================''')

print("CVE: " + cve_id)
print("CVSS: " + str(cvss_score))
print(classification)
print("================================")
