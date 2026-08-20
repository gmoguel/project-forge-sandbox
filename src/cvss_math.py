cve_id = input("what is the CVE ID?")
cvss_score = float(input("What is the CVSS Score?"))
assets = int(input("How many affected assets?"))
age = int(input("How long has the vulnerability been present in days?"))

print("================================")
print("    VULNERABILITY PROFILE       ")
print("============================+===")

risk_points = float(cvss_score * assets)
print("CVE: " + cve_id)
print("CVSS Score: ",  cvss_score)
print("Affected Assets: ",  assets)
print("Age: " + str(age) + " days")
print(" ")
print("Risk Points",  risk_points)

print("============================+===")

