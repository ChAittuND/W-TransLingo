# Hindi Language;
hindi_svar = ("अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ए", "ऐ", "ओ", "औ", "अं", "अः" )
hindi_matraem = ("ा","ि",'ी','ु','ू','ृ','ॄ','ॆ','े','ै','ॉ','ॊ','ो',"ौ")
hindi_vyanjan = ("क",'ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द','ध','न','प','फ','ब','भ','म','य','र','ल','व','श','ष','स','ह','क्ष','त्र',"ज्ञ")
hindi_ubayaksar =("ं", "ः", 'ॅ')

hindi_ginati =("१", '२', '३', '४', '५', '६', '७', '८', '९', "०")

# Telugu Language


# Language Sets
hindi_letters = (hindi_matraem, hindi_svar, hindi_ubayaksar, hindi_vyanjan)
listofLetters = (hindi_letters)

orderArrangements = ("Hindi")

def check_char_presence(char, *lists):
    found_in_list = []
    for lst in lists:
        if char in lst:
            found_in_list.append(lst)
    if len(found_in_list) == 1:
        return True
    else:
        return False


def DetectLingo(text):
    for the_lingo_being_checked in listofLetters:
        for the_set_being_checked in the_lingo_being_checked:
            if check_char_presence(text[0], the_set_being_checked):
                return orderArrangements[listofLetters.index(the_lingo_being_checked)]
    else:
        return False
