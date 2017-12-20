#!/usr/bin/env python3
from flask import Flask, render_template, abort
import json
import os


app = Flask(__name__)


@app.route('/')
def index():
	filepath = '/home/shiyanlou/louPlus/week2/challenge6/file'
	file_context = get_file_info(filepath)
	file_tar = []

	for context in file_context:
		file_tar.append(context['title'])
	return render_template('index.html', file_tar=file_tar)
	# 显示文章名称的列表
	# 页面中需要显示 `/home/shiyanlou/files/` 目录下所有 json 文件中的 `title` 信息列表


@app.route('/files/<filename>')
def file(filename):
	filename = str(filename.strip())
	filepath = '/home/shiyanlou/louPlus/week2/challenge6/file'
	new_filename = filepath + '/' + filename + '.json'
	if os.path.exists(new_filename):
		contextlist = get_file_info(filename=new_filename)
		return render_template('file.html', contextlist=contextlist)
	else:
		return error('shiyanlou 404')
	# 读取并显示 filename.json 中的文章内容
	# 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
	# 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面

@app.errorhandler(404)
def error(error_msg):
	return render_template('404.html', restr=error_msg)


def get_file_info(filepath='', filename=''):
	file_context = []
	if filepath != '':
		os.chdir(filepath)
		lis = os.listdir()

		for file in lis:
			with open(file) as f:
				file_context.append(json.load(f))
	elif filename != '':
		with open(filename) as f:
			file_context.append(json.load(f))
	else:
		pass

	return file_context
