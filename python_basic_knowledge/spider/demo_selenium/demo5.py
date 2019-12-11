#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-12-03 19:21:03
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-12-04 11:43:10

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import base64, random, sys
from PIL import Image
import cv2
import numpy as np

class Zufang():

	def __init__(self):
		self.url = ""
		self.browser = webdriver.Chrome()
		self.wait = WebDriverWait(self.browser, 20)

	def __del__(self):
		self.browser.close()


	def main(self):
		self.browser.get("https://callback.58.com/antibot/verifycode?serialId=39bbb682f2ff21ac949aa72805d03dcf_5e738e40332c42b089f21104cd3cbe5d&code=22&sign=ce71bb0aa8b87e798d8cb76cd56870e2&namespace=chuzulistphp&url=sh.58.com%2Fchuzu%2F0%2Fpn2%2F%3FPGTID%3D0d3090a7-0000-2201-2009-77e8c4e12ce2%26ClickID%3D4")
		# btnSubmit
		button1 = self.wait.until(EC.element_to_be_clickable((By.ID, 'btnSubmit')))
		button1.click()

		time.sleep(1.5) # sleep2秒

		JS_TEM = 'document.getElementsByClassName("dvc-captcha__puzzleImg")[0].style.display="none"'
		JS_TEM_RE = 'document.getElementsByClassName("dvc-captcha__puzzleImg")[0].style.display="inline-block"'
		JS_BG = 'document.getElementsByClassName("dvc-captcha__bgImg")[0].style.display="none"'
		JS_BG_RE = 'document.getElementsByClassName("dvc-captcha__bgImg")[0].style.display="inline-block"'
		self.browser.execute_script(JS_TEM)
		time.sleep(0.5)

		img_bg = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.dvc-captcha__bgImg')))
		img_bg.screenshot('captcha58.png') # 截图带缺口的图片

		# 截取滑块的图片逻辑
		self.browser.execute_script(JS_TEM_RE)
		self.browser.execute_script(JS_BG)
		time.sleep(0.49)
		img_slider = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.dvc-captcha__puzzleImg')))
		img_slider.screenshot('slider.png') # 截取滑块的图片
		time.sleep(0.2)
		self.browser.execute_script(JS_BG_RE)
		self.slider_translate()

	def template_match(self, img_target, img_template):
		tpl = self.handle_img1(img_template) # 误差来源就在于滑块的背景图为白色
		blurred = cv2.GaussianBlur(img_target, (3, 3), 0)  # 目标图高斯滤波
		gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
		ret, target = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # 目标图二值化
		cv2.imshow("template", tpl)
		cv2.imshow("target", target)
		method = cv2.TM_CCOEFF_NORMED
		width, height = tpl.shape[:2]
		result = cv2.matchTemplate(target, tpl, method)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
		left_up = max_loc
		right_down = (left_up[0] + height, left_up[1] + width)
		cv2.rectangle(img_target, left_up, right_down, (0, 0, 255), 2)
		print("show ing the res")
		cv2.imshow('res', img_target)

	# 对滑块进行二值化处理
	def handle_img1(self, image):
		kernel = np.ones((8, 8), np.uint8)  # 去滑块的前景噪声内核
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		width, heigth = gray.shape


		for h in range(heigth):
			for w in range(width):
				if gray[w, h] == 0:
					gray[w, h] = 96

		binary = cv2.inRange(gray, 96, 96)
		res = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 开运算去除白色噪点
		
		cv2.imshow('gray', gray)
		cv2.imshow('res', res)
		return gray
		print("gray.......")
		print(width, heigth)
		time.sleep(20)
		return res

	def do_opencv(self):
		img0 = cv2.imread("./captcha58.png")
		img1 = cv2.imread("./slider.png", -1)
		self.template_match(img0, img1)
		print('endd')
		time.sleep(45)
		# cv2.waitKey(0)
		cv2.destroyAllWindows()

	def slider_translate(self):
		"""滑块背景白色变成透明色
		
		"""
		img = Image.open("./slider.png")
		l, h = img.size
		color_white = (255, 255, 255, 255)
		for hh in range(h):
			for ll in range(l):
				dot = (ll, hh)
				color_1 = img.getpixel(dot)
				if color_1 == color_white: # 白色背景
					color_1 = color_white[:-1] + (0,)
					img.putpixel(dot, color_1)
		print("save to new png")
		img.save("./slider.png", "PNG")



if __name__ == "__main__":
	
	fo = Zufang()
	fo.main()
	fo.do_opencv()



















