#!/usr/bin/env python
# -*- coding: utf-8 -*-

import exrex
import sys

'''
传入一个host，形如:demo.webdic.com
那么，demo，webdic都可以作为生成字典的一部分
'''

web_white = ['com','cn','edu','gov','www','org']

def host_para(host):
	#对输入的原始host内容进行处理
	if '://' in host:
		host = host.split('://')[1].replace('/','')
	if '/' in host:
		host = host.replace('/','')
	#f返回一个纯粹的host
	return host

def dic_creat(hosts):
	web_dics = hosts.split('.')
	#取出每一个可能的字符串，如demo，webdic，分别放入字典生成的地方，生成字典
	#把生成字典的规则，写在配置文件里，易于后期修改使用
	rule_ini = open('web_dic.ini','r')
	for i in rule_ini:
		if '#' not in i:
			rule = i

	f_pass = open('pass_1.txt','w')
	f_pass.close()

	# print i
	rule_ini.close()

	for web_dic in web_dics:
		if web_dic not in web_white:
			f = open('name.txt','r')
			# print rule
			for i in f:
				dics = list(exrex.generate(rule.format(web_dic=web_dic,name=i.strip('\n'))))

				for dic in dics:
					try:
						if len(dic)==0 or int(dic):
							pass
					except:
						# print dic
						f_pass = open('pass_1.txt','a+')
						f_pass.write(dic+'\n')
						f_pass.close()
						
			f.close()

	print '[*]Create dic complete!'
# dic_creat(host_para('http://demo.webdic.com'))

if __name__ == '__main__':
	if len(sys.argv) == 2:
		dic_creat(host_para(sys.argv[1]))
		sys.exit(0)
	else:
		print ("usage: %s www.demo.com.cn" % sys.argv[0])
		sys.exit(-1)