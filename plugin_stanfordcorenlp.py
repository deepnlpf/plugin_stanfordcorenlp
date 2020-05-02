#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.core.iplugin import IPlugin
from deepnlpf.core.boost import Boost
from deepnlpf.core.output_format import OutputFormat

import json

from os import path
from corenlp.corenlp import StanfordCoreNLP

class Plugin(IPlugin):
    
    def __init__(self, id_pool, lang, document, pipeline):
        self._id_pool = id_pool
        self._document = document
        self._pipeline = pipeline

        path_or_host = path.abspath(path.dirname(__file__)) + "/stanford-corenlp-full-2018-10-05"
        self.nlp = StanfordCoreNLP(path_or_host)

    def run(self):
        annotation = Boost().multithreading(self.wrapper, self._document['sentences'])
        self.nlp.close()
        return self.out_format(annotation)

    def wrapper(self, sentence):
        '''
            @param annotators : more: https://stanfordnlp.github.io/CoreNLP/annotators.html
            @param pipelineLanguage : en, zh, ar, fr, de, es
            @param outputFormat : json, xml, text, more: https://stanfordnlp.github.io/CoreNLP/human-languages.html
            @param memory : 8g
        '''

        props = {
            'timeout': '1500000',
            'annotators': ', '.join(self._pipeline),
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }
        return json.loads(self.nlp.annotate(sentence, properties=props))

    def out_format(self, annotation):
        try:
            return OutputFormat().doc_annotation(_id_pool=self._id_pool, _id_dataset=self._document['_id_dataset'],
            _id_document=self._document['_id'], tool="stanfordcorenlp", annotation=annotation)
        except Exception as err:
            return annotation
