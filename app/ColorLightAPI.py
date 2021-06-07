import json
import re

import requests
from bs4 import BeautifulSoup
from soup2dict import convert
from nested_lookup import nested_lookup
# from colour import Color
from . import (models,serializers)
class ColorLightAPI():

    def AddToReport(self, payload):
        try:
            print("AddToReport", payload)
            reposrtdata = {
                    "user": payload.get("user"),
                }
            if payload.get("type", None) == 'Single': reposrtdata['message'] = payload.get("singleLineMessage")
            if payload.get("type", None) == 'Multi': reposrtdata['message'] = payload.get("multilineMessage")
            if payload.get("type", None) == 'Image': reposrtdata['message'] = payload.get("imageMessage")
            if payload.get("type", None) == 'Video': reposrtdata['message'] = payload.get("videoMessage")
            if payload.get("VmDSelectionValue", None) == "VMD":
                reposrtdata['VMDS'] = payload.get("vmd_or_Group")
            elif payload.get("VmDSelectionValue", None) == "VMDGroup":
                reposrtdata['VMDGroups'] =payload.get("vmd_or_Group")
            ser = serializers.ReportsSerailizersTemp(data=reposrtdata)
            ser.is_valid(raise_exception=True)
            ser.save()
        except Exception as e:
            print("Exception report function", str(e))

    def getVMDDetail(self, payload):
        try:
            print("payload",payload)
            if payload.get("VmDSelectionValue", None) == "VMD":
                return models.VMDS.objects.filter(id__in=payload.get('vmd_or_Group'))
            elif payload.get("VmDSelectionValue", None) == "VMDGroup":
                vmdList = []
                vmdGroup = models.VMDGroups.objects.filter(id__in=payload.get('vmd_or_Group'))
                for i in vmdGroup:
                    vmdList +=i.VMDS.all()
                    return vmdList
        except Exception as e:
            print("Exception in getVMDDetail", str(e))
            return []

    def ImageMessage(self, payloadFromfront):
        payloadFromfront= dict(payloadFromfront)
        print("payloadFromfront", payloadFromfront)
        try:
            payload = {
                "Programs": {
                    "Program": {
                        "Information": {
                            "Width": payloadFromfront.get("Width"),
                            "Height": payloadFromfront.get("Height")
                        },
                        "Pages": [{
                            "Regions": [
                                {
                                    "Layer": 1,
                                    "Rect": {
                                        "X": payloadFromfront.get("XCoOrdinates"),
                                        "Y": payloadFromfront.get("YCoOrdinates"),
                                        "Width": payloadFromfront.get("Width"),
                                        "Height": payloadFromfront.get("Height")
                                    },
                                    "Items": [{
                                        "Type": "2",
                                        "FileSource": {
                                            "IsRelative": "1",
                                            "FilePath": ".\\two_pics.files\\12638.jpg"
                                        }
                                    }]
                                }
                            ]
                        }]
                    }
                }
            }
            Vmds = self.getVMDDetail(payloadFromfront)
            print("Vmds",Vmds)
            list_of_IPs = []
            resposneData = []
            for i in Vmds:
                print("IP, ", i.VMDIPAddress)
                list_of_IPs.append(i.VMDIPAddress)
            # Send Request
            payload = json.dumps(payload)
            for i in list_of_IPs:
                try:
                    response = requests.post('http://' + i + '/api/program/one_pic.vsn', payload)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": response.status_code,
                            "Response": "Message send successfully to VMD("+i+")" if response.status_code == 200 else response.json()
                        }
                    )
                    self.AddToReport(payloadFromfront)
                except Exception as e:
                    self.AddToReport(payloadFromfront)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": "500",
                            "Response": str(e)
                        }
                    )

            print("Payload:", payload)
            return resposneData
        except Exception as e:
            print("Exception in Image API", str(e))
            pass
    def Message(self, payloadFromfront):
        try:
            Html = None
            type = 4
            if (payloadFromfront.get('type', None) == 'Single'):
                type = 4
                Html = payloadFromfront.get("singleLineMessage")
            elif (payloadFromfront.get('type', None) == 'Multi'):
                type = 4
                Html = payloadFromfront.get("multilineMessage")
            # Parsing Date
            soup = BeautifulSoup(Html, "html.parser")
            # Convert it to a dictionary with convert()
            dict_result = convert(soup)

            all_tags = [tag.name for tag in soup.find_all()]
            print("Message ", Html)
            print("all_tags", all_tags)
            print("dict_result", dict_result)
            LoggFont = {
                "LogFont": {

                }
            }
            TextColor = {

            }
            try:
                color = nested_lookup('@style', dict_result)
                for i in color:
                    try:
                        color_list_ = re.findall('color: rgb\((.*)\)', i)[0].split(',')
                        TextColor["TextColor"] = '0x%02x%02x%02x' % (
                        int(color_list_[0]), int(color_list_[1]), int(color_list_[2]))
                    except: continue
                for i in color:
                    try:
                        font = re.findall('font-size: (\w+px)', i)[0]
                        LoggFont['LogFont']['lfHeight'] = font
                    except: continue
            except Exception as e:print("Error", str(e))


            if "strong" in all_tags:
                LoggFont['LogFont']['lfWeight'] = "700"
            if "em" in all_tags:
                LoggFont['LogFont']['lfItalic'] = "1"
            if "u" in all_tags:
                LoggFont['LogFont']['lfUnderline'] = "1"
            if "s" in all_tags:
                LoggFont['LogFont']['lfStrikeOut'] = "1"

            payload = {
                "Programs": {
                    "Program": {
                        "Information": {
                            "Width": payloadFromfront.get("Width"),
                            "Height": payloadFromfront.get("Height")
                        },
                        "Pages": [{
                            "Regions": [
                                {
                                    "Layer": 1,
                                    "Rect": {
                                        "X": payloadFromfront.get("XCoOrdinates"),
                                        "Y": payloadFromfront.get("YCoOrdinates"),
                                        "Width": payloadFromfront.get("Width"),
                                        "Height": payloadFromfront.get("Height")
                                    },
                                    "Items": [{
                                        "Type": "4",
                                        "Text": soup.get_text(),
                                        "IsScroll": "1",
                                        **LoggFont,
                                        **TextColor
                                    }]
                                }
                            ]
                        }]
                    }
                }
            }
            Vmds = self.getVMDDetail(payloadFromfront)
            list_of_IPs = []
            resposneData = []
            for i in Vmds:
                print("IP, ", i.VMDIPAddress)
                list_of_IPs.append(i.VMDIPAddress)
            # Send Request
            payload = json.dumps(payload)
            for i in list_of_IPs:
                try:
                    response = requests.post('http://' + i + '/api/program/Multi-Line.vsn', payload)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": response.status_code,
                            "Response": "Message send successfully to VMD("+i+")" if response.status_code == 200 else response.json()
                        }
                    )
                    self.AddToReport(payloadFromfront)
                except Exception as e:
                    self.AddToReport(payloadFromfront)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": "500",
                            "Response": str(e)
                        }
                    )

            print("Payload:", payload)
            return resposneData
        except Exception as e:
            print("Exception in singleLineMessage", str(e))

    def WebAppMessage(self, payloadFromfront):
        try:
            Html = None
            if (payloadFromfront.get('type', None) == 'Single'):
                Html = payloadFromfront.get("singleLineMessage")
            elif (payloadFromfront.get('type', None) == 'Multi'):
                Html = payloadFromfront.get("multilineMessage")
            payload = {
                "Programs": {
                    "Program": {
                        "Information": {
                            "Width": payloadFromfront.get("Width"),
                            "Height": payloadFromfront.get("Height")
                        },
                        "Pages": [{
                            "Regions": [
                                {
                                    "Layer": 1,
                                    "Rect": {
                                        "X": payloadFromfront.get("XCoOrdinates"),
                                        "Y": payloadFromfront.get("YCoOrdinates"),
                                        "Width": payloadFromfront.get("Width"),
                                        "Height": payloadFromfront.get("Height")
                                    },
                                    "Items": [{
                                        "Type": "27",

                                    }]
                                }
                            ]
                        }]
                    }
                }
            }
            Vmds = self.getVMDDetail(payloadFromfront)
            list_of_IPs = []
            resposneData = []
            for i in Vmds:
                print("IP, ", i.VMDIPAddress)
                list_of_IPs.append(i.VMDIPAddress)
            # Send Request
            payload = json.dumps(payload)
            for i in list_of_IPs:
                try:
                    response = requests.post('http://' + i + '/api/program/Multi-Line.vsn', payload)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": response.status_code,
                            "Response": "Message send successfully to VMD(" + i + ")" if response.status_code == 200 else response.json()
                        }
                    )
                    self.AddToReport(payloadFromfront)
                except Exception as e:
                    self.AddToReport(payloadFromfront)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": "500",
                            "Response": str(e)
                        }
                    )

            print("Payload:", payload)
            return resposneData
        except Exception as e:
            print("Exception in singleLineMessage", str(e))

