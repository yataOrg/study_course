#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yanzhipeng
# @Date:   2019-12-04 11:43:22
# @Last Modified by:   yanzhipeng
# @Last Modified time: 2019-12-04 18:08:21

import cv2
import time


def get_pos(image):
	blurred = cv2.GaussianBlur(image, (5, 5), 0)
	canny = cv2.Canny(blurred, 100, 400)
	cv2.imshow('canny', canny)
	
	contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	# print(">>>>>", type(contours), len(contours), "@@@@@@@@@", contours)
	for i, contour in enumerate(contours):
		M = cv2.moments(contour)

		'''
		if M['m00'] == 0:
			cx = cy = 0
		else:
			cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
		'''
		print("----->", cv2.contourArea(contour), cv2.arcLength(contour, True))
		if 1550 < cv2.contourArea(contour) < 1900 and 150 < cv2.arcLength(contour, True) < 230:


			draw_img = image.copy()
			# print(">>>>>", type(contour), contour)
			ret = cv2.drawContours(draw_img, [contour], -1, (0, 0, 255), 1)
			cv2.imshow('ret', ret)
			contour.sort(axis=0)

			min_x_road = contour[0, 0][0] - 7

			print("min load is -", min_x_road)
			cv2.waitKey(0)
			time.sleep(7)
			cv2.destroyAllWindows()
			'''
			if cx < 400:
				continue
			
			
			x, y, w, h = cv2.boundingRect(contour)  # 外接矩形
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
			cv2.imshow('image', image)
			print("show image")
			return x
			'''
	return 0


if __name__ == '__main__':
	img0 = cv2.imread('./captcha_58.png')
	get_pos(img0)
	print("end")
	time.sleep(27)
	cv2.destroyAllWindows()
	# cv2.waitKey(0)
	