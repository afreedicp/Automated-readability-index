import ARI
def test_ari_emptychar():
     ret=ARI.ari_emptychar('')
     assert ret==0
def test_ari_alphanumeric():
     ret=ARI.ari_alphanumeric('!@##$%^')
     assert ret ==False
def test_ari_emptywords():
     ret=ARI.ari_emptyword('asdf')
     assert ret==None
def test_ari_numword():
     ret=ARI.ari_numword('i am a sick dog')
     assert ret==4
def test_ari_emptysentence():
     ret=ARI.ari_emptysentence('asdasfdasfasuhcbweucb asfdawfawfawf asfafaewf')
     assert ret==None
def test_ari_sentence():
     ret=ARI.ari_sentences('i am an idiot. what you think of me? dont feel bad. we are one!')
     assert ret==4
