import requests

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
    def singleLineMessage(self, payloadFromfront):
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
                                        "Type": "4",
                                        "Text": payloadFromfront.get("singleLineMessage"),
                                        "IsScroll": "1"
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
            for i in list_of_IPs:
                try:
                    response = requests.post('http://' + i + '/api/program/Multi-Line.vsn', payload)
                    resposneData.append(
                        {
                            "IP": i,
                            "StatusCode": response.status_code,
                            "Response": response.json()
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

            print("Payload value in fun", payload)
            return resposneData
        except Exception as e:
            print("Exception in singleLineMessage", str(e))

