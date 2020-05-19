# Install Stanford CoreNLP
echo "Downloading Stanford CoreNLP.."
wget http://nlp.stanford.edu/software/stanford-corenlp-4.0.0.zip

echo "Extracting files.."
unzip stanford-corenlp-4.0.0.zip

# Move the extracted folder
mv $(zipinfo -1 stanford-corenlp-4.0.0.zip | head -1) resources

# Clear.
rm -r stanford-corenlp-4.0.0.zip
