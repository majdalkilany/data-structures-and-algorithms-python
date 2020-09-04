from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation 

def test_curly () : 
    expected = True 
    actual = multi_bracket_validation('{majd}')
    assert expected == actual 


def test_curly__l_false () : 
    expected = False 
    actual = multi_bracket_validation('{majd}}')
    assert expected == actual 

def test_curly__r_false () : 
    expected = False 
    actual = multi_bracket_validation('{{{majd}}')
    assert expected == actual 




def test_sec_b () : 
    expected = True 
    actual = multi_bracket_validation('[]')
    assert expected == actual 


def test_sec__l_false () : 
    expected = False 
    actual = multi_bracket_validation('[')
    assert expected == actual 

def test_sec__r_false () : 
    expected = False 
    actual = multi_bracket_validation('[]]')
    assert expected == actual 


# =========
def test_b () : 
    expected = True 
    actual = multi_bracket_validation('(majd)')
    assert expected == actual 


def test_b__l_false () : 
    expected = False 
    actual = multi_bracket_validation('{]')
    assert expected == actual 

def test_b__r_false () : 
    expected = False 
    actual = multi_bracket_validation('[)')
    assert expected == actual 


def test_whithout () : 
    expected = False 
    actual = multi_bracket_validation('{(})')
    assert expected == actual 

def test_all_ () : 
    expected = True 
    actual = multi_bracket_validation('[{()}]')
    assert expected == actual 
