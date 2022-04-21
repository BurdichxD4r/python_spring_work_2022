#todo: задан словарь

dict_ = { "sdtv_mode":2, "hdmi_drive":2, "hdmi_group":2, "hdmi_mode":16, "overscan_left":20, "overscan_right":12,
          "overscan_top":10 }

# Нужно создать  файл config.txt с содержимым вида:
# sdtv_mode=2
# hdmi_drive=2
# hdmi_group=2
# hdmi_mode=16
# overscan_left=20
# overscan_right=12
# overscan_top=10


config = open('config.txt', "wt")
key_value_list = []
for key, val in dict_.items():
    key_value = str(key) + '=' + str(val) + '\n'
    key_value_list.append(key_value)
config.writelines(key_value_list)
config.close()
