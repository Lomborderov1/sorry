import pickle
shoplistfile = 'prototip.dat'
name = 'Мансур'
age = '16'
shoplist = ['яблоки', 'манго','морковь']
with open(shoplistfile,'wb') as f:
    pickle.dump(shoplist, f )

with open(shoplistfile,'rb') as f:
    storedlist = pickle.load(f)