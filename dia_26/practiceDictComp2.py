'''
new_dict = {new_key:new_value for (key,value) in dict.items()}
'''

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# (temp_c * 9/5) + 32 = temp_f para pasar a farenheit
weather_f = {d:(wc * 9 / 5) + 32 for (d,wc) in weather_c.items()}

print(weather_f)