from django.shortcuts import render,redirect
from . credentials import MpesaAccessToken, MpesaPassword
import requests
# Create your views here.
def index(request):
    return render(request,'index.html')

def stk_push(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        amount = request.POST.get('amount')

        access_token = MpesaAccessToken.validated_token

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

        headers = {"Authorization": "Bearer %s" % access_token}
        payload={    
           "BusinessShortCode": MpesaPassword.shortcode,    
           "Password": MpesaPassword.decoded_password,    
           "Timestamp":MpesaPassword.timestamp,    
           "TransactionType": "CustomerPayBillOnline",    
           "Amount": amount,    
           "PartyA":phone_number,    
           "PartyB":MpesaPassword.shortcode,    
           "PhoneNumber":phone_number,    
           "CallBackURL": "https://mydomain.com/pat",    
           "AccountReference":"Test",    
           "TransactionDesc":"Test"
}
        response = requests.post(api_url, json=payload, headers=headers)
        return redirect('/thankyou/')
def thank_you(request):
    return render(request,'thankyou.html')