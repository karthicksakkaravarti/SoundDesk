from rest_framework import status
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        try:
            fields = {
                         "VMDName": "VMD Name",
                         "VMDLocation": "VMD Location",
                         "VMDLatitude": "VMD Latitude",
                         "VMDLongitude": "VMD Longitude",
                         "VMDIPAddress": "VMD IP Address",
                         "VMDPort": "VMD Port",
                         "VMDResolutionHeight": "VMD Resolution Height",
                         "VMDResolutionwidth": "VMD Resolution width",
                         "VMDStatus": "VMD Status",
                         "VMDBrightness": "VMD Brightness",
                         "AssigneUser": "Assigne User",
                         "VMDS": "VMD",
                     }
            if (response.status_code == 400):
                for i, j in exc.detail.items():
                    response.data['Error'] = fields.get(str(i), i) +" : "+"-".join(j)
        except Exception as e:
            print("Exception in Custome handler", str(e))
            pass



    return response