#!/usr/bin/env python3
from tkinter import *
import requests
import sys
import time
exec(open(r"variables").read())
import datetime
from urllib.request import urlopen
from json import loads

# this is where the display is being created
class ETHTicker:
	def __init__(self, master):
		self.master = master
		self.close_button = Button(image=ethlogo, command=self.close)
		self.close_button.grid(row=0, column=0)
		self.label = Label(master, text=("ETH Dashboard"), font=('Helvetica',32, 'bold'), width=17, anchor='center', fg='black', bg = 'white')
		self.label.grid(row=0, column=1)

	def labels():
		hwg()
		internet_on()
		title = "Market Data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=2, column=1, sticky=W)

		if priceeth1hrchange *100 > price1hrchangediff:
				color = "lightgreen"
		elif priceeth1hrchange * 100 < price1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"
		percentage = "{:,.1%}".format(priceeth1hrchange)
		percentage2 = "{:,.1%}".format(priceeth24hrchange)
		currency = "{:,.2f}".format(priceeth)
		text1 = "ETH Price: " + str(currency) + "   (" + str(percentage) + " / " + str(percentage2) + ")"
		down_label = Label(text=(text1),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = color)
		down_label.grid(row=3, column=1, sticky=W)

		if priceyfi1hrchange * 100 > price1hrchangediff:
				color = "lightgreen"
		elif priceyfi1hrchange * 100 < price1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"		
		percentage = "{:,.1%}".format(priceyfi1hrchange)
		percentage2 = "{:,.1%}".format(priceyfi24hrchange)
		currency = "${:,.0f}".format(priceyfi)
		text13 = "YFI Price: " + str(currency) + " (" + str(percentage) + " / " + str(percentage2) + ")  "
		down_label = Label(text=(text13),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg=color)
		down_label.grid(row=4, column=1, sticky=W)

		if priceuni1hrchange * 100 > price1hrchangediff:
				color = "lightgreen"
		elif priceuni1hrchange * 100 < price1hrchangediff * -1:
				color = "lightcoral"
		else:
				color = "white"		
		currency = "${:,.2f}".format(priceuni)
		percentage = "{:,.1%}".format(priceuni1hrchange)
		percentage2 = "{:,.1%}".format(priceuni24hrchange)
		text14 = "UNI Price: " + str(currency) + "  (" + str(percentage) + " / " + str(percentage2) + ")  "
		down_label = Label(text=(text14),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg=color)
		down_label.grid(row=5, column=1, sticky=W)

		currency = "{:,.2%}".format(market_dominance_percentage)
		text3 = "ETH Dominance: " + str(currency)
		down_label = Label(text=(text3),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		down_label.grid(row=6, column=1, sticky=W)

		currency = "{:,.0f}".format(marketcapeth)
		text4 = "ETH Marketcap: $" + str(currency)
		down_label = Label(text=(text4 + '\n' text4a),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		down_label.grid(row=7, column=1, sticky=W)

		title = "Blockchain Data"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=9, column=1, sticky=W)

		currency = "{:,.0f}".format(average_gasfee)
		text5 = "Average Gas: " + str(currency) + " gwei  "
		date_time_obj = "{:,.1f}".format(average_wait_time)
		text5b = "Avg Wait time: " + str(date_time_obj) + " min  "
		down_label = Label(text=(text5 + '\n' + text5b),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=10, column=1, sticky=W)

		date_time_obj =  "{:,.2f}".format(average_block_time)
		text5a = "Avg Block time: " + str(date_time_obj) + " sec  "
		down_label = Label(text=(text5a + '\n'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=11, column=1, sticky=W)

		title = "DeFi"
		down_label = Label(text=(title),anchor=NW, justify=LEFT,font=('Helvetica', 28, 'bold'), bg='black', fg='gold')
		down_label.grid(row=12, column=1, sticky=W)

		currency = "${:,.1f}".format(defilockedusd)
		text10 = "Value locked: " + str(currency) + " B  "
		currency = "${:,.1f}".format(dominance_valueusd)  + " B  "
		text11 = str(dominance_name) + " locked: " + str(currency)
		down_label = Label(text=(text10 + '\n' + text11),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=13, column=1, sticky=W)

		currency = "{:,.0f}".format(TVLBTC)
		text12 = "BTC locked: " + str(currency) + u'\u20bf'
		currency = "{:,.0f}".format(LNDBTC)
		text12a = "Lightning volume: " + str(currency) + u'\u20bf'
		down_label = Label(text=(text12 + '\n' + text12a + '\n'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg='white')
		down_label.grid(row=14, column=1, sticky=W)
					
		text98 = str(errormessage)
		down_label = Label(text=(text98),anchor=NW, justify=LEFT,font=('Helvetica',14), bg='black', fg='red')
		down_label.grid(row=17, column=1, sticky=W)
	
		now = datetime.datetime.now()
		text99 = "Current time: " + str(now)
		down_label = Label(text=(text99),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='black', fg='white')
		down_label.grid(row=18, column=1, sticky=W)
	
# This is where you set the update time. 290000 is about 5 minutes	
		down_label.after(290000,ETHTicker.labels)

	def close(self):
		root.destroy()

def hwg():
	global priceeth
	global priceeth1hrchange
	global priceeth24hrchange
	global priceyfi24hrchange
	global priceuni24hrchange
	global marketcapeth
	global marketcap24h
	global priceyfi
	global priceuni
	global market_dominance_percentage
	global average_gasfee
	global defilockedusd
	global dominance_name
	global dominance_valueusd
	global errormessage
	global TVLBTC
	global LNDBTC
	global status
	global average_block_time
	global average_wait_time
	global priceyfi1hrchange
	global priceuni1hrchange
	global defi_market_cap

	defi_market_cap = 0
	priceeth = 0
	priceeth1hrchange = 0
	priceeth24hrchange = 0
	marketcapeth = 0
	marketcap24h = 0
	market_dominance_percentage = 0
	average_gasfee = 0

	try:
#	get the defipulse Project data 
		defi_pulse_url = 'https://data-api.defipulse.com/api/v1/defipulse/api/GetProjects?api-key='+ defipulseApikey
		urltest = requests.get(defi_pulse_url)
		status = urltest.status_code
		if status == 429:
			print("Error DefiPulse. Wrong or expired API key")
			errormessage = "Error DefiPulse. Wrong or expired API key"
			raise
		elif status == 200:
			total_value_locked = requests.get(defi_pulse_url)
			json_obj = total_value_locked.json()

			for project in json_obj:
				name = project.get("name")
				if name == 'WBTC':
					WBTC = project['value']['tvl']['BTC'].get("value")
				elif name == 'RenVM':
					RENBTC = project['value']['tvl']['BTC'].get("value")
				elif name == 'Lightning Network':
					LNDBTC = project['value']['tvl']['BTC'].get("value")
			TVLBTC = WBTC + RENBTC + LNDBTC
		else:
			print("Error reading DeFiPulse. Error-code: " + str(status))
			errormessage = "Unknown error reading DeFiPulse Project"
	except:
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	get the defipulse Marketdata 
		defi_pulse_url = 'https://data-api.defipulse.com/api/v1/defipulse/api/MarketData?api-key='+ defipulseApikey
		urltest = requests.get(defi_pulse_url)
		status = urltest.status_code
		if status == 429:
			print("Error DefiPulse. Wrong or expired API key")
			raise
		elif status == 200:
			marketdata=requests.get(defi_pulse_url).json()
			defilockedusd=marketdata['All']['total']
			dominance_valueusd = marketdata['All']['dominance_value']
			dominance_name = str(marketdata['All']['dominance_name'])
			dominance_valueusd = dominance_valueusd / 1000000000
			defilockedusd = defilockedusd / 1000000000
		else:
			print("Error reading DeFiPulse Market. Error-code: " + str(status))
			errormessage = "Unknown error reading DeFiPulse Market"
	except:
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	https://docs.ethgasstation.info/gas-price
		status = 0
		ethgas_url = 'https://ethgasstation.info/api/ethgasAPI.json?'
		urltest = requests.get(ethgas_url)
		status = urltest.status_code
		marketdata = requests.get(ethgas_url).json()
		average_gasfee = marketdata['average']
		average_block_time = marketdata['block_time']
		average_wait_time = marketdata['avgWait']

		average_gasfee = average_gasfee / 10

	except:
		errormessage = "Error reading EthGasStation " + str(status)
		print(errormessage)
		time.sleep(10)
		hwg()
		
	try:
#	get blockchain data https://blockchair.com/api/docs#link_M03
		status = 0
		blockchair_url = 'https://api.blockchair.com/ethereum/stats'
		urltest = requests.get(blockchair_url)
		status = urltest.status_code

		blockchair_api_request = requests.get(blockchair_url).json()
		market_dominance_percentage = blockchair_api_request['data']['market_dominance_percentage']

		market_dominance_percentage = market_dominance_percentage / 100

	except:
		errormessage = "Error reading Blockchair: " + str(status)
		print(errormessage)
		time.sleep(10)
		hwg()
	
	try:
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/ethereum').read()	
		marketcap24h = float(loads(coingecko_api_request)['market_data']['market_cap_change_percentage_24h'])
		priceeth1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		priceeth24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		marketcapeth = float(loads(coingecko_api_request)['market_data']['market_cap']['usd'])
		priceeth = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/yearn-finance').read()	
		priceyfi = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		priceyfi24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])
		priceyfi1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/coins/uniswap').read()	
		priceuni = float(loads(coingecko_api_request)['market_data']['current_price']['usd'])
		priceuni1hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_1h_in_currency']['usd'])
		priceuni24hrchange = float(loads(coingecko_api_request)['market_data']['price_change_percentage_24h'])

		priceeth24hrchange = priceeth24hrchange / 100
		priceuni24hrchange = priceuni24hrchange / 100
		priceyfi24hrchange = priceyfi24hrchange / 100
		priceeth1hrchange = priceeth1hrchange / 100
		priceuni1hrchange = priceuni1hrchange / 100
		priceyfi1hrchange = priceyfi1hrchange / 100
		print(priceeth)

	except:
		print("Error reading Coingecko")
		time.sleep(10)
		hwg()
	
	try:
		coingecko_api_request = urlopen('https://api.coingecko.com/api/v3/global/decentralized_finance_defi').read()	
		defi_market_cap = float(loads(coingecko_api_request)['data']['defi_market_cap'])

	except:
		print("Error reading Coingecko Defi")
		time.sleep(10)
		hwg()

def internet_on(url='http://www.google.com/', timeout=5):
	try:
		_ = requests.get(url, timeout=timeout)
		return True
	except requests.ConnectionError:
		errormessage = "No internet connection available."
	return False



errormessage=""
LNDBTC=0
TVLBTC=0
defilockedusd=0
dominance_valueusd=0
dominance_name=0
total_value_locked=0
defilockedusd=0
root = Tk()
root.configure(cursor='none', bg='black')
root.attributes('-fullscreen', True)
logo = PhotoImage(file=r"ethlogo.png")
ethlogo = logo.subsample(26,26)
my_gui = ETHTicker(root)
ETHTicker.labels()
root.mainloop()
