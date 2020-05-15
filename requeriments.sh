# Install Stanford CoreNLP
echo "Downloading Stanford CoreNLP.."
wget http://nlp.stanford.edu/software/stanford-corenlp-4.0.0.zip

echo "Extracting files.."
unzip stanford-corenlp-4.0.0.zip

mv stanford-corenlp-full-2020-04-20 resources

# Clear.
rm -r stanford-corenlp-4.0.0.zip
