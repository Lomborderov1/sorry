from direct.showbase.DirectObject import DirectObject   
import direct.directbase.DirectStart   
from pandac.PandaModules import *  

# Выполняем импорт нужных классов из модуля физики   
from panda3d.bullet import BulletWorld   
from panda3d.bullet import BulletPlaneShape   
from panda3d.bullet import BulletRigidBodyNode   
from panda3d.bullet import BulletBoxShape   
  
# Установим камеру.   
base.cam.setPos(0, -10, 0)   
base.cam.lookAt(0, 0, 0)  

# Дополнительно класс для отладки, с помочью его мы можем выполнить визуализацию объектов Bullet, это я    
#добавил для лучшего восприятия. Можно обойтись и без этого.   
  
from panda3d.bullet import BulletDebugNode   
  
# Создадим объект для отображения физической геометрии.   
debugNode = BulletDebugNode('Debug')   
debugNP = render.attachNewNode(debugNode)   
  
# Теперь функцию для управления объектом     
def toggleDebug():   
    if debugNP.isHidden(): # Проверка состояния, скрыт или отображен.   
       debugNP.show() # Если скрыт, то отображаем.   
    else:   
        debugNP.hide() # Если отображен, то скрываем.   
  
# Функцию будем выполнять по нажатию кнопки F1.   
press_f1 = DirectObject()   
press_f1.accept('f1', toggleDebug) 

# Собственно создаем мир.   
world = BulletWorld()   
# Устанавливаем режим отладки миру.   
world.setDebugNode(debugNP.node())   
# Устанвливем силу гравитации и вектор для создания земного притяжения   
world.setGravity(Vec3(0, 0, -9.81))


#Создаем плоскость, условно назовём её землёй.   
# Устанавливаем в горизонтальное положение .   
shape = BulletPlaneShape(Vec3(0, 0, 1), 0)   
# Создаем нод тела для физических объектов.   
node = BulletRigidBodyNode('Ground')   
# Добавляем к ноду плоскость   
node.addShape(shape)   
np = render.attachNewNode(node)   
# Устанавливаем начальную позицию.   
np.setPos(0, 0, -2)   
# Добавляем настроенный объект в физический мир.   
world.attachRigidBody(node)  


# Создаем геометрию бокса(кубика) размером 0.5   
shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))   
# Нод   
node = BulletRigidBodyNode('Box')   
# Задаем массу, тем самым делаем его динамическим.   
node.setMass(1.0)   
# Добавляем к ноду геометрию бокса   
node.addShape(shape)   
np = render.attachNewNode(node)   
np.setPos(0, 0, 0)   
  
# Добавляем настроенный объект в физический мир.   
world.attachRigidBody(node)   
  
# Загружаем модель кубика   
model = loader.loadModel('models/box.egg')   
model.setPos(-0.5, -0.5, -0.5)   
model.flattenLight()   
model.reparentTo(np)

def update(task):   
    dt = globalClock.getDt() # Берем время рендеринга предыдущего кадра.   
    world.doPhysics(dt) # И передаем аргументом функции которая запускает шаг симуляции физики в указанном мире.   
    return task.cont   
      
taskMgr.add(update, 'update')     
  
# И как всегда.   
run()  