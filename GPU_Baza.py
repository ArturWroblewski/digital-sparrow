import jsonlines
import json

#opendata-2019-03-08-062818+0000.jsonl - Orginal
#opendata-2019-03-06-062740+0002.jsonl - test
with jsonlines.open('opendata-2019-03-08-062818+0000.jsonl') as f:
    for item in f:

        if item['_source']['data']['scene']['stats']['result']==str('OK'):
            try:
                print(item['_source']['data']['device_info']['compute_devices'][0]['name']+' | '+item['_source']['data']['device_info']['compute_devices'][0]['type']+' | '+ str(item['_source']['data']['scene']['stats']['total_render_time'])+' | '+item['_source']['data']['system_info']['system']+' | '+item['_source']['data']['scene']['name'])
            except:
                print("Błąd")


        if item['_source']['data']['scene']['stats']['result']==str('OK2'):
            print('-----------------New----------------------')
            print(item['_source']['data']['device_info']['compute_devices'][0]['name']+' | '+item['_source']['data']['device_info']['compute_devices'][0]['type']+' | '+ str(item['_source']['data']['scene']['stats']['total_render_time'])+' | '+item['_source']['data']['system_info']['system'])

            print(item['_source']['data']['scene']['stats']['result'])
            print(item['_source']['data']['device_info']['compute_devices'])
            print(item['_source']['data']['scene']['name'])
            print(item['_source']['data']['scene']['stats']['total_render_time'])
            print(item['_source']['data']['system_info']['system'])
            print(item['_source']['data']['device_info']['compute_devices'][0]['name'])





            print('-----------------tmp----------------------')



            print(item['_source']['date_created'])
            print(item['_index'] + ' ' + item['_source']['date_created'])

            print('-----------------List Subfolders system_info ----------------------')
            for subitem in item['_source']['data']['system_info']:
                print(subitem)