#!/usr/bin/python2.7
# -*- coding=utf-8 -*-
#本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
#教主QQ:605658506
#亁颐堂官网www.qytang.com
#乾颐盾是由亁颐堂现任明教教主开发的综合性安全课程
#包括传统网络安全（防火墙，IPS...）与Python语言和黑客渗透课程！

import os

def run(**args):
	print "[*] In dirlister module."
	files = os.listdir(".")

	return str(files)

if __name__ == '__main__':
	print(run())
