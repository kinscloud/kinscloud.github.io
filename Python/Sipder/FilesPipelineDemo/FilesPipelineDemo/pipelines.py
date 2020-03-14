'''
@Author: your name
@Date: 2020-03-12 09:15:56
@LastEditTime: 2020-03-12 09:53:18
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \FilesPipelineDemo\FilesPipelineDemo\pipelines.py
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline

class SaveFilePipeline(FilesPipeline):
    
    def file_path(self,request,response=None,info=None):
        return request.url.split(r'/')[-1]
