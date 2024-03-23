
all_codes = [14, 15, 16, 17, 18, 19, 20]

print("All codes (Normal list):", all_codes)

total_codes = sum(all_codes)
print("Total codes (Comprehensive list):", total_codes)

odd_tracked_codes = [code for code in all_codes if code % 2 != 0]
print("Codes tracked by odd numbers (Comprehensive list):", odd_tracked_codes)

codes_set = set(all_codes)
print("Set of codes:", codes_set)
