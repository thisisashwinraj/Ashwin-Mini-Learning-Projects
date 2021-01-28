# Import Python Packages

import os
import spacy
import streamlit as st

from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer

from textblob import TextBlob
from gensim.summarization import summarize

# Function to Perform Sumy Summarization
def sumySummarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lexRankSummarizer = LexRankSummarizer()
	summary = lexRankSummarizer(parser.document,3)
	list = [str(sentence) for sentence in summary]
	summaryResult = ' '.join(list)
	return summaryResult

# Function to Extract Token and Lemma
@st.cache
def tokenAndLemma(enterText):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(enterText)
	data = [('"Token":{},\n"Lemma":{}'.format(token.text,token.lemma_)) for token in docx ]
	return data

# Function to Extract Named Entities
@st.cache
def namedEntity(enterText):
	nlp = spacy.load('en_core_web_sm')
	docx = nlp(enterText)
	tokens = [token.text for token in docx]
	entities = [(entity.text,entity.label_) for entity in docx.ents]
	data = ['"Token":{},\n"Entity":{}'.format(tokens,entities)]
	return data

# Main Function - WebApp
def main():
	"""Process Your Text With NLP"""
	
	# Title and Sub-Header
	st.title("PandoraNLP")
	st.subheader("Perform NLP on Your Text\nSelect the NLP Operation you Want to Perform\n")
	

	# Text Tokenization and Lemma Display
	if st.checkbox("Display Tokens and Lemma"):
		st.subheader("Tokenize your Text and Extract Lemma")
		input = st.text_area("Enter Your Text","Enter the text to be tokenized")
		
		if st.button("Analyze Text"):
			tokenize = tokenAndLemma(input)
			st.json(tokenize)
	
	# Entity Extraction
	if st.checkbox("Extract Entities from Text"):
		st.subheader("Analyze the Text and Extract Entities")
		input = st.text_area("Enter Your Text","Enter the text to be analyzed")
		
		if st.button("Extract Entities"):
			entity = namedEntity(input)
			st.json(entity)

	# Sentiment Analysis
	if st.checkbox("Sentiment Analysis"):
		st.subheader("Analyze the Underlying Sentiment ")
		input = st.text_area("Enter Your Text","Enter the text to be analyzed")

		if st.button("Extract Sentiment"):
			blob = TextBlob(input)
			sentiment = blob.sentiment
			st.success(sentiment)

	# Text Summarization
	if st.checkbox("Summarize the Text"):
		st.subheader("Create a short and Descriptive Summary")
		input = st.text_area("Enter Your Text","Enter the text to be summarized")

		summarizer = st.selectbox("Choose Summarizer",['Sumy','Gensim'])

		if st.button("Summarize Text"):
      
      			# Using Sumy Summarizer
			if summarizer == 'sumy':
				st.text("You have Selected Sumy Summarizer")
				result = sumySummarizer(input)
			
      			# Using Gensim Summarizer
			elif summarizer == 'gensim':
				st.text("You have Selected Sumy Summarizer")
				result = gensim(input)

			# Default Summarizer, When No Choice is Made
			else:
				result = sumySummarizer(input)
	
			st.success(result)
			
	st.sidebar.subheader("PandoraNLP")
	st.sidebar.text("Perform NLP tasks using Spacy, Textblob, Sumy and Gensim Module")

	st.sidebar.subheader("Developed By")
	st.sidebar.text("Ashwin Raj")

if __name__ == '__main__':
	main()
