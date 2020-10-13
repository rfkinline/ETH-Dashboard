#!/usr/bin/env python3
from tkinter import *
import requests
import sys
import time
import datetime
from urllib.request import urlopen
from json import loads
# your defipulse API key. 
defipulseApikey = "93c078480f89a7fa220f2b91a7244ea17b5bab77e3cff6b0fa1e2d0ed22c"
#"e61b012ae1c05cd4f84bd87c86826ec28f2fde511db9e73fddf9a0a510d"
#display tresholds (change color if x value increased more than y%). 
price1hrchangediff = 1    # checked once / hr
price24hrchangediff = 5    # checked once / hr

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


		currency = "{:,.2%}".format(priceeth24hrchange)
		text2 = "24hr change: " + str(currency)
		down_label = Label(text=(text2),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = "white")
		down_label.grid(row=6, column=1, sticky=W)

		currency = "{:,.2%}".format(market_dominance_percentage)
		text3 = "ETH Dominance: " + str(currency)
		down_label = Label(text=(text3),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		down_label.grid(row=7, column=1, sticky=W)

		currency = "{:,.0f}".format(marketcapeth)
		text4 = "Marketcap: $" + str(currency)
		down_label = Label(text=(text4 + '\n'),anchor=NW, justify=LEFT,font=('Helvetica',20), bg='black', fg = 'white')
		down_label.grid(row=8, column=1, sticky=W)

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
		down_label = Label(text=(text98),anchor=NW, justify=LEFT,font=('Helvetica',12), bg='black', fg='red')
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
	global TVLBTC
	global LNDBTC
	global status
	global average_block_time
	global average_wait_time
	global priceyfi1hrchange
	global priceuni1hrchange

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
	except:
		print("Error reading DeFiPulse. Error-code: " + str(status))
		errormessage = "Error reading DeFiPulse Project"
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
	except:
		print("Error reading DeFiPulse. Error-code: " + str(status))
		errormessage = "Error reading DeFiPulse Market"
		if status == 204:
			time.sleep(5)
			hwg()

	try:
#	https://docs.ethgasstation.info/gas-price
		marketdata = requests.get('https://ethgasstation.info/api/ethgasAPI.json?').json()
		average_gasfee = marketdata['average']
		average_block_time = marketdata['block_time']
		average_wait_time = marketdata['avgWait']

		average_gasfee = average_gasfee / 10

	except:
		print("Error reading Ethgasstation.info")
		time.sleep(10)
		hwg()

	try:
#	get blockchain data https://blockchair.com/api/docs#link_M03
		blockchair_api_request = urlopen('https://api.blockchair.com/ethereum/stats').read()	
		market_dominance_percentage = float(loads(blockchair_api_request)['data']['market_dominance_percentage'])

		market_dominance_percentage = market_dominance_percentage / 100

	except:
		print("Error reading Blockchair")
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
