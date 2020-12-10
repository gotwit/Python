features = set()
features.add("server_encryption")
features.add("disk_encryption")
features.add("experience_framework")

for feature in features:
    print(f"{feature}\n")


import re

feature_fmt = "<features>(.*)</features>"
features = ['<features>fspg_backup_and_restore,hsc_backup_and_restore</features>'][0]
tags = re.findall(feature_fmt, features)
print(tags)


print(set(['fspg_backup_and_restore', 'hsc_backup_and_restore']))