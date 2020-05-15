#!/usr/bin/env python
# -*- coding: utf-8 -*-

from deepnlpf.core.iplugin import IPlugin

from corenlp.corenlp import StanfordCoreNLP


class Plugin(IPlugin):

    from os import path
    PATH_OR_HOST = path.abspath(path.dirname(__file__)) + "/resources"

    def __init__(self, document, pipeline):
        self._document = document

        self._processors = pipeline["tools"]["stanfordcorenlp"]["processors"]
        self._lang = pipeline["lang"]

        self.nlp = StanfordCoreNLP(self.PATH_OR_HOST)

    def run(self):
        from deepnlpf.core.boost import Boost
        doc = Boost().multithreading(self.wrapper, self._document)
        self.nlp.close()
        return doc

    def wrapper(self, sentence):
        """
            @param annotators : more: https://stanfordnlp.github.io/CoreNLP/annotators.html
            @param pipelineLanguage : en, zh, ar, fr, de, es
            @param outputFormat : json, xml, text, more: https://stanfordnlp.github.io/CoreNLP/human-languages.html
            @param memory : 8g
        """

        props = {
            "timeout": "1500000",
            "annotators": ", ".join(self._processors),
            "pipelineLanguage": "en",
            "outputFormat": "json",
        }

        return self.nlp.annotate(sentence, properties=props)

    def out_format(self, doc):
        pass
