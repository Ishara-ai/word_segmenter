from wordsegment import load, segment
def segment_words(sentence):
    """
    Used to segment a string to its components
    Args:
        sentence: The sentence to be segmented
    input: ihaveanapple
    output: i have an apple
    """
    load()
    sen_length = len(sentence)

    # string is greater than 249 characters
    if sen_length > 249:
        word_list = [] # will store the words segmented
        start = 0 # holds integer where to start extracting from
        stop = 247 # holds integer where to end extracting from
        new_sentence = sentence[start:stop]
        while len(new_sentence) > 0:
            word_list += segment(new_sentence)
            start = stop
            stop += 247
            last_word = word_list[-1] # stores the last letter
            word_list.pop() # removes the last word in the list
            new_sentence = last_word + sentence[start:stop]
            if len(new_sentence) == len(last_word):
                break
        return " ".join(word_list)
    else:
        return " ".join(segment(sentence))
sentence1 = "Thesunroseintheeastandpaintedtheskywithwarmcolors,birdssoaredabovethehorizon,andthegentlewindsrustledthetreesleaves,creatinganidyllicmorninglandscape.Theflowingriverglistenedunderthesun'sgentlegaze,whilepeoplestrolledalongitsbanks,absorbingthebeautyofnature'smasterpiece.Childrenplayedjoyfullyintheplayground,theirlaughterfillingtheairwithhappiness.Acrossfromthepark,anoldmanrestedonabench,enjoyingthesereneatmosphereandreflectingonyearsoflifelived.Inthecafénearby,baristascrafteddeliciouscoffeesandpastries,fillingtheroomwithirresistiblearomas.Thiscitywasbustlingwithenergyandlife,amicrocosmofdiverseculturesandpeoplecomingtogetherindailyharmony,asanotherdayunfoldsinitsexquisitebeauty"
print(segment_words(sentence1))
