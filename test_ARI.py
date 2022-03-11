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
     assert ret==5
