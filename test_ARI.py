import ARI
def test_ari_emptychar():
     ret=ARI.ari_emptychar('')
     assert ret==0
def test_ari_alphanumeric():
     ret=ARI.ari_alphanumeric('!@##$%^')
     assert ret ==False