from pandac.PandaModules import GeoMipTerrain
from pandac.PandaModules import GeoMipTerrain, Filename

class gameLocation():   
   def __init__(self):   
       self.terrain=GeoMipTerrain("Terrain") 


   def loadTerrain(self,hfFile):   
       self.terrain.setHeightfield(Filename(hfFile))   
       self.terrain.setBlockSize(32)   
       self.terrain.setFactor(64)   
       self.terrain.setMinLevel(2)   
       self.terrain.getRoot().reparentTo(render)   
       self.terrain.getRoot( ).setSz (30)   
       self.terrain.generate()   
       self.terrain.setFocalPoint(base.camera)  

def update(self,task):   
    self.terrain.update()   
       #self.terrain.getRoot().setRenderModeWireframe()   
    return task.cont  