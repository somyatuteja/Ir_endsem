from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import nltk.data

#nltk.download('stopwords')

class SimpleSummarizer:
    def reorder_sentences(self, output_sentences, input):
        output_sentences.sort(key=lambda s1:
                              input.find(s1))
        return output_sentences

    def get_summarized(self, input, num_sentences, query):
        # TODO: allow the caller to specify the tokenizer they want
        # TODO: allow the user to specify the sentence tokenizer they want

        tokenizer = RegexpTokenizer('\w+')

        # get the frequency of each word in the input
        base_words = [word.lower()
                      for word in tokenizer.tokenize(input)]
        words = [word for word in base_words if word not in stopwords.words()]
        word_frequencies = FreqDist(words)
      #  print (words)
       # print (word_frequencies.items())
        # now create a set of the most frequent words
        most_frequent_words = [pair[0] for pair in
                               list(word_frequencies.items()) if pair[1] > 10 and pair[0] != query]
       # print(most_frequent_words)
        # break the input up into sentences.  working_sentences is used
        # for the analysis, but actual_sentences is used in the results
        # so capitalization will be correct.


        sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
        actual_sentences = sent_detector.tokenize(input)
        working_sentences = [sentence.lower()
                             for sentence in actual_sentences]

        # iterate over the most frequent words, and add the first sentence
        # that inclues each word to the result.
        output_sentences = []

        for word in most_frequent_words:
            for i in range(0, len(working_sentences)):
                if (word in working_sentences[i]
                and actual_sentences[i] not in output_sentences):
                    output_sentences.append(actual_sentences[i])
                    break
                if len(output_sentences) >= num_sentences: break
            if len(output_sentences) >= num_sentences: break

        # sort the output sentences back to their original order
        return output_sentences

    def summarize(self, input, num_sentences, query):
        return " ".join(self.get_summarized(input, num_sentences, query))