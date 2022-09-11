"""
nimbbl api testing
"""

import time

import kwargs as kwargs
import mysql.connector
import pytest
import requests
import json
from requests.auth import HTTPBasicAuth
import configparser
from utilities.configuration import *
from utilities.payloads import *
from utilities.resourses import *
from starlette.requests import Request
from starlette.responses import Response
import unittest
import os

os.linesep


class Test_Nimbbl():
	global url, se, payload, head, headersAPI,head1,payload2,payload3
	url = getConfig()['Api']['host']
	se = requests.session()
	payload = "{\n    \"access_key\": \"access_key_BrQv9jPkkn16l3zg\",\n    \"access_secret\": \"access_secret_BrQv9LBGYPmDM7zg\"\n}\n"
	# payload = {
	# 	"access_key":"access_key_BrQv9jPkkn16l3zg",
	# 	"access_secret":"access_secret_BrQv9LBGYPmDM7zg"
	# }
	payload2 = "{\"order_id\" : \"o_NxlAkLbbxVdOYL9Y\"}"
	payload3 = "{\"order_id\":\"o_NxlAkLbbxVdOYL9Y\",\"payment_mode\":\"UPI\",\"upi_id\" : \"politikal919@okhdfcbank\"}"
	
	head = {
		
		'Content-Type': 'application/json',
		'x-nimbbl-key': '168680-2f2ca7557780e0ce59545db6f0c1144',
		'x-nimbbl-user-token': 'user_RqLvaZXP8dpyz3QZ',
		'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMTIxNSwiZXhwIjoxNjYyODE3MTk3LCJ0b2tlbl90eXBlIjoidHJhbnNhY3Rpb24ifQ.CfkWq0srY4asiNXzwOummIdiWVOwoT6-sEcP044zQWo'
		
		
	}
	
	
	def test_get_token(self):
		response = se.post(url + f"/v2/generate-token", data=payload, headers=head)
		print(payload)
		print(response)
		json_response = response.json()
		assert response.status_code == 200
		token = json_response['token'].encode("ascii", "ignore")
		
		id = json_response['auth_principal']['id']
		sub_merchant_id = json_response['auth_principal']['sub_merchant_id']
		assert json_response['auth_principal']['active'] == True
		
		print(json_response)
		print(token)
		global headersAPI
		headersAPI = {
			'accept': 'application/json',
			'Authorization': 'Bearer ' + json_response['token']
		}
		return headersAPI
	
 
	
	def test_create_order(self):
		response = se.post(url + f"/v2/create-order", data=test_order_create(), headers=self.test_get_token())
		print(response)
		j = response.json()
		print(j)
		assert response.status_code == 200 or 201
		assert j['message']== 'Order Created Successfully','order unsuccessful'
		order_id = j['order_id']
		user_id = j['user_id']
		return order_id
	
	def test_fetch_order(self):
		response = se.get(url + f'/v2/get-order/o_NxlAkLbbxVdOYL9Y', headers=self.test_get_token())
		j = response.json()
		assert response.status_code == 200
		print(j)
		
		
	# def test_fetch_payment_modes(self):
	# 	r = se.post(url +f'/v2/payment-modes',data= payload2, headers=head)
	# 	print(r)
		
	def test_upi_collect(self):
		r = se.post(url+f'/v2/initiate-payment',data= payload3,headers=head)
		print(r)