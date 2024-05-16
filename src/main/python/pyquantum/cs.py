from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.cs.GuiPosition as _GuiPosition
_GuiPosition = _GuiPosition
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GuiPosition():
    """dev.ultreon.quantum.cs.GuiPosition"""
 
    @staticmethod
    def _wrap(java_value: _GuiPosition) -> 'GuiPosition':
        return GuiPosition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GuiPosition):
        """
        Dynamic initializer for GuiPosition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GuiPosition__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GuiPosition__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setX(int)"""
        super(_GuiPosition, self).setX(_int.valueOf(arg0))

    @overload
    def add(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).add(arg0)

    @overload
    def subtract(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).subtract(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.hashCode()"""
        return int._wrap(super(GuiPosition, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def multiply(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(int,int)"""
        super(_GuiPosition, self).multiply(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def multiply(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).multiply(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getX()"""
        return int._wrap(super(GuiPosition, self).getX())

    @override
    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onTick()"""
        super(GuiPosition, self).onTick()

    @overload
    def set(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(int,int)"""
        super(_GuiPosition, self).set(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onCreate(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onCreate()"""
        super(GuiPosition, self).onCreate()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.cs.GuiPosition(int,int)"""
        val = _GuiPosition(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.cs.GuiPosition.toString()"""
        return str._wrap(super(GuiPosition, self).toString())

    @overload
    def set(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).set(arg0)

    @overload
    def subtract(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(int,int)"""
        super(_GuiPosition, self).subtract(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def copy(self) -> 'GuiPosition':
        """public dev.ultreon.quantum.cs.GuiPosition dev.ultreon.quantum.cs.GuiPosition.copy()"""
        return 'GuiPosition'._wrap(super(GuiPosition, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def divide(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).divide(arg0)

    @override
    @overload
    def onDestroy(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onDestroy()"""
        super(GuiPosition, self).onDestroy()

    @overload
    def add(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(int,int)"""
        super(_GuiPosition, self).add(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setY(int)"""
        super(_GuiPosition, self).setY(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def divide(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(int,int)"""
        super(_GuiPosition, self).divide(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.cs.GuiPosition.equals(java.lang.Object)"""
        return bool._wrap(super(_GuiPosition, self).equals(arg0))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getY()"""
        return int._wrap(super(GuiPosition, self).getY())

 
 
 
# CLASS: dev.ultreon.quantum.cs.GuiPosition
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.cs.GuiPosition as _GuiPosition
_GuiPosition = _GuiPosition
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GuiPosition():
    """dev.ultreon.quantum.cs.GuiPosition"""
 
    @staticmethod
    def _wrap(java_value: _GuiPosition) -> 'GuiPosition':
        return GuiPosition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GuiPosition):
        """
        Dynamic initializer for GuiPosition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GuiPosition__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GuiPosition__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setX(int)"""
        super(_GuiPosition, self).setX(_int.valueOf(arg0))

    @overload
    def add(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).add(arg0)

    @overload
    def subtract(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).subtract(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.hashCode()"""
        return int._wrap(super(GuiPosition, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def multiply(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(int,int)"""
        super(_GuiPosition, self).multiply(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def multiply(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).multiply(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getX()"""
        return int._wrap(super(GuiPosition, self).getX())

    @override
    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onTick()"""
        super(GuiPosition, self).onTick()

    @overload
    def set(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(int,int)"""
        super(_GuiPosition, self).set(_int.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def onCreate(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onCreate()"""
        super(GuiPosition, self).onCreate()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.cs.GuiPosition(int,int)"""
        val = _GuiPosition(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.cs.GuiPosition.toString()"""
        return str._wrap(super(GuiPosition, self).toString())

    @overload
    def set(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).set(arg0)

    @overload
    def subtract(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(int,int)"""
        super(_GuiPosition, self).subtract(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def copy(self) -> 'GuiPosition':
        """public dev.ultreon.quantum.cs.GuiPosition dev.ultreon.quantum.cs.GuiPosition.copy()"""
        return 'GuiPosition'._wrap(super(GuiPosition, self).copy())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def divide(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(dev.ultreon.quantum.cs.GuiPosition)"""
        super(_GuiPosition, self).divide(arg0)

    @override
    @overload
    def onDestroy(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onDestroy()"""
        super(GuiPosition, self).onDestroy()

    @overload
    def add(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(int,int)"""
        super(_GuiPosition, self).add(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setY(int)"""
        super(_GuiPosition, self).setY(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def divide(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(int,int)"""
        super(_GuiPosition, self).divide(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.cs.GuiPosition.equals(java.lang.Object)"""
        return bool._wrap(super(_GuiPosition, self).equals(arg0))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getY()"""
        return int._wrap(super(GuiPosition, self).getY())

 
 
 
# CLASS: dev.ultreon.quantum.cs.GuiPosition 
 
 
# CLASS: dev.ultreon.quantum.cs.Component
import dev.ultreon.quantum.cs.Component as _Component
_Component = _Component
from abc import abstractmethod, ABC
 
class Component():
    """dev.ultreon.quantum.cs.Component"""
 
    @staticmethod
    def _wrap(java_value: _Component) -> 'Component':
        return Component(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Component):
        """
        Dynamic initializer for Component.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Component__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Component__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def onCreate(self, ):
        """public abstract void dev.ultreon.quantum.cs.Component.onCreate()"""
        pass

    @abstractmethod
    def onDestroy(self, ):
        """public abstract void dev.ultreon.quantum.cs.Component.onDestroy()"""
        pass

    @abstractmethod
    def onTick(self, ):
        """public abstract void dev.ultreon.quantum.cs.Component.onTick()"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.cs.WorldPosition
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.quantum.cs.WorldPosition as _WorldPosition
_WorldPosition = _WorldPosition
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WorldPosition():
    """dev.ultreon.quantum.cs.WorldPosition"""
 
    @staticmethod
    def _wrap(java_value: _WorldPosition) -> 'WorldPosition':
        return WorldPosition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WorldPosition):
        """
        Dynamic initializer for WorldPosition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WorldPosition__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WorldPosition__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.cs.WorldPosition()"""
        val = _WorldPosition()
        self.__wrapper = val

    @override
    @overload
    def onCreate(self):
        """public void dev.ultreon.quantum.cs.WorldPosition.onCreate()"""
        super(WorldPosition, self).onCreate()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.WorldPosition.onTick()"""
        super(WorldPosition, self).onTick()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def onDestroy(self):
        """public void dev.ultreon.quantum.cs.WorldPosition.onDestroy()"""
        super(WorldPosition, self).onDestroy()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.cs.WorldPosition()"""
        val = _WorldPosition()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: dev.ultreon.quantum.cs.ComponentSystem
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
import dev.ultreon.quantum.cs.Component as _Component
_Component = _Component
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import dev.ultreon.quantum.cs.ComponentSystem as _ComponentSystem
_ComponentSystem = _ComponentSystem
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComponentSystem():
    """dev.ultreon.quantum.cs.ComponentSystem"""
 
    @staticmethod
    def _wrap(java_value: _ComponentSystem) -> 'ComponentSystem':
        return ComponentSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComponentSystem):
        """
        Dynamic initializer for ComponentSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComponentSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComponentSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getComponent(self, arg0: str, arg1: 'Class') -> 'Component':
        """public <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.getComponent(java.lang.String,java.lang.Class<T>)"""
        return 'Component'._wrap(super(_ComponentSystem, self).getComponent(arg0, arg1))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.cs.ComponentSystem()"""
        val = _ComponentSystem()
        self.__wrapper = val

    @overload
    def clear(self):
        """public void dev.ultreon.quantum.cs.ComponentSystem.clear()"""
        super(ComponentSystem, self).clear()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.cs.ComponentSystem()"""
        val = _ComponentSystem()
        self.__wrapper = val

    @overload
    def getComponent(self, arg0: str, *arg1: 'Component') -> 'Component':
        """public final <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.getComponent(java.lang.String,T...)"""
        return 'Component'._wrap(super(_ComponentSystem, self).getComponent(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def addComponent(self, arg0: str, arg1: 'Component') -> 'Component':
        """public <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.addComponent(java.lang.String,T)"""
        return 'Component'._wrap(super(_ComponentSystem, self).addComponent(arg0, arg1))

    @overload
    def getComponents(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.cs.Component> dev.ultreon.quantum.cs.ComponentSystem.getComponents()"""
        return 'Map'._wrap(super(ComponentSystem, self).getComponents())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeComponent(self, arg0: str, *arg1: 'Component') -> 'Component':
        """public <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.removeComponent(java.lang.String,T...)"""
        return 'Component'._wrap(super(_ComponentSystem, self).removeComponent(arg0, arg1))

    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.ComponentSystem.onTick()"""
        super(ComponentSystem, self).onTick()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())