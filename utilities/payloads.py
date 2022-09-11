"""

"""
import random
import pytest
import os
def test_randomid():
	ranom_id = random.randint(1,24000)
	return ranom_id
def test_order_create():
	payload="{\"amount_before_tax\": 24,\"currency\":\"INR\",\"invoice_id\":\"Dpt9\",\"device_user_agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36\",\"order_from_ip\": \"x.x.x.x\",\"tax\": 0,\"user\": {\"mobile_number\":\"9999999999\",\"email\":\"dth993178@kmail.com\",\"first_name\":\"sp\",\"last_name\":\"th\"    },\"shipping_address\": {\"address_1\":\"Some address\",\"street\":\"Your street\",\"landmark\":\"My landmark\",\"area\":\"My area\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"pincode\":\"400018\",\"address_type\":\"residential\"},\"total_amount\": 24,\"order_line_items\": [{\"referrer_platform_sku_id\":\"sku1\",\"title\":\"Designer Triangles\",\"description\":\"Wallpaper by  chenspec from Pixabay\",\"quantity\": 1,\"rate\": 24,\"amount\": 24,\"total_amount\": 24,\"image_url\":\"https:\/\/cdn.pixabay.com\/photo\/2021\/02\/15\/15\/25\/rhomboid-6018215_960_720.jpg\"}]}"
	return payload
def test_token():
	token=  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTIxNSwiZXhwIjoxNjYyODEwNzQzLCJ0b2tlbl90eXBlIjoidHJhbnNhY3Rpb24ifQ.Oy77Ei-cbXSoeF46rj5JgiXN0PeCB8ZtFOixHQhWdcE'
	return token
def test_md5():
	md5 = '4b7ee15ac9c6bb38d2bb509c7389bbfa'
	return md5