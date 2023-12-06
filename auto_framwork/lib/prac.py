# import re
# # raid_device_info = {}
# raid_details_output= """('', '/dev/md99:\n           Version : 1.2\n     Creation Time : Mon Nov 27 12:04:09 2023\n        Raid Level : raid5\n        Array Size : 585672704 (558.54 GiB 599.73 GB)\n     Used Dev Size : 292836352 (279.27 GiB 299.86 GB)\n      Raid Devices : 3\n     Total Devices : 3\n       Persistence : Superblock is persistent\n\n     Intent Bitmap : Internal\n\n       Update Time : Mon Nov 27 12:04:40 2023\n             State : clean, resyncing \n    Active Devices : 3\n   Working Devices : 3\n    Failed Devices : 0\n     Spare Devices : 0\n\n            Layout : left-symmetric\n        Chunk Size : 512K\n\nConsistency Policy : bitmap\n\n     Resync Status : 0% complete\n\n              Name : winteck-PowerEdge-R720:99  (local to host winteck-PowerEdge-R720)\n              UUID : 0b60080f:826e488f:57fc0cf2:83b80f8f\n            Events : 6\n\n    Number   Major   Minor   RaidDevice State\n       0       8       48        0      active sync   /dev/sdd\n       1       8       64        1      active sync   /dev/sde\n       2       8       80        2      active sync   /dev/sdf\n')"""
# # # matches = re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([a-z]+)\s+(\S+)', x)
# # for match in x:
# #     raid_device_info[int(match[0])] = {'State': match[4], 'Device': match[5]}
# # # return raid_device_info
# #
# # print(raid_device_info)
# for i in
#
#
# # Define the regular expression pattern
# pattern = re.compile(r'\s+(\d+)\s+\d+\s+\d+\s+\d+\s+([a-z]+)\s+(\S+)')
#
# # Find all matches in the raid_details_output
# matches = pattern.findall(raid_details_output)
#
# # Create a dictionary from the matches
# raid_device_info = {f"/dev/{match[2]}": match[1] for match in matches}
#
# print(raid_device_info)
import os.path


#
# import re
#
# # Sample raid_details output
# raid_details_output = """
#     Number   Major   Minor   RaidDevice State
#        0       8       48        0      active sync   /dev/sdd
#        1       8       64        1      active sync   /dev/sde
#        2       8       80        2      active sync   /dev/sdf
# """
#
# # Define the regular expression pattern
# pattern = re.compile(r'\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([a-z]+)\s+(/dev/\w+)')
#
# # Find all matches in the raid_details_output
# matches = pattern.findall(raid_details_output)
#
# # Create a dictionary from the matches
# raid_device_info = {dev: state for _, _, _, _, state, dev in matches}
#
# print(raid_device_info)


# import os
# def mkdir(*folders):
#     for i in folders:
#         if not os.path.exists(i):
#             os.mkdir(i)
#
#
# mkdir("a","b","c")

# def generate_snake_table(n):
#     table = [[0] * n for _ in range(n)]
#
#     current_value = 0
#     for i in range(n):
#         if i % 2 == 0:
#             for j in range(n):
#                 table[i][j] = current_value
#                 current_value += 1
#         else:
#             for j in range(n - 1, -1, -1):
#                 table[i][j] = current_value
#                 current_value += 1
#
#     return table
#
# def display_table(table):
#     for row in table:
#         print(" ".join(map(str, row)))
#
# # Example usage:
# n = 3
# snake_table = generate_snake_table(n)
# display_table(snake_table)


import pkgutil
for module in pkgutil.iter_modules():
    print(module.name)






