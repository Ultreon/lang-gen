from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Long as __long
import dev.ultreon.quantum.cs.GuiPosition as __GuiPosition
__GuiPosition = __GuiPosition
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GuiPosition(__Component, Component):
    """dev.ultreon.quantum.cs.GuiPosition"""
 
    @staticmethod
    def __wrap(java_value: __GuiPosition) -> 'GuiPosition':
        return GuiPosition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GuiPosition):
        """
        Dynamic initializer for GuiPosition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setY(int)"""
        super(__GuiPosition, self).setY(__int.valueOf(arg0))

    @overload
    def subtract(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).subtract(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subtract(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(int,int)"""
        super(__GuiPosition, self).subtract(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def add(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(int,int)"""
        super(__GuiPosition, self).add(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.cs.GuiPosition(int,int)"""
        val = __GuiPosition(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.cs.GuiPosition.toString()"""
        return str.__wrap(super(GuiPosition, self).toString())

    @overload
    def add(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).add(arg0)

    @override
    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onTick()"""
        super(GuiPosition, self).onTick()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.cs.GuiPosition.equals(java.lang.Object)"""
        return bool.__wrap(super(__GuiPosition, self).equals(arg0))

    @override
    @overload
    def onCreate(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onCreate()"""
        super(GuiPosition, self).onCreate()

    @overload
    def set(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(int,int)"""
        super(__GuiPosition, self).set(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getY()"""
        return int.__wrap(super(GuiPosition, self).getY())

    @overload
    def set(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).set(arg0)

    @overload
    def multiply(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(int,int)"""
        super(__GuiPosition, self).multiply(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setX(int)"""
        super(__GuiPosition, self).setX(__int.valueOf(arg0))

    @override
    @overload
    def onDestroy(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onDestroy()"""
        super(GuiPosition, self).onDestroy()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def multiply(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).multiply(arg0)

    @overload
    def divide(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).divide(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def divide(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(int,int)"""
        super(__GuiPosition, self).divide(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getX()"""
        return int.__wrap(super(GuiPosition, self).getX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.hashCode()"""
        return int.__wrap(super(GuiPosition, self).hashCode())

    @overload
    def copy(self) -> 'GuiPosition':
        """public dev.ultreon.quantum.cs.GuiPosition dev.ultreon.quantum.cs.GuiPosition.copy()"""
        return 'GuiPosition'.__wrap(super(GuiPosition, self).copy())

 
 
 
# CLASS: dev.ultreon.quantum.cs.GuiPosition
from builtins import str
import java.lang.Long as __long
import dev.ultreon.quantum.cs.GuiPosition as __GuiPosition
__GuiPosition = __GuiPosition
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class GuiPosition(__Component, Component):
    """dev.ultreon.quantum.cs.GuiPosition"""
 
    @staticmethod
    def __wrap(java_value: __GuiPosition) -> 'GuiPosition':
        return GuiPosition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GuiPosition):
        """
        Dynamic initializer for GuiPosition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setY(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setY(int)"""
        super(__GuiPosition, self).setY(__int.valueOf(arg0))

    @overload
    def subtract(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).subtract(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def subtract(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.subtract(int,int)"""
        super(__GuiPosition, self).subtract(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def add(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(int,int)"""
        super(__GuiPosition, self).add(__int.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.quantum.cs.GuiPosition(int,int)"""
        val = __GuiPosition(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.cs.GuiPosition.toString()"""
        return str.__wrap(super(GuiPosition, self).toString())

    @overload
    def add(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.add(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).add(arg0)

    @override
    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onTick()"""
        super(GuiPosition, self).onTick()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.cs.GuiPosition.equals(java.lang.Object)"""
        return bool.__wrap(super(__GuiPosition, self).equals(arg0))

    @override
    @overload
    def onCreate(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onCreate()"""
        super(GuiPosition, self).onCreate()

    @overload
    def set(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(int,int)"""
        super(__GuiPosition, self).set(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getY(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getY()"""
        return int.__wrap(super(GuiPosition, self).getY())

    @overload
    def set(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.set(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).set(arg0)

    @overload
    def multiply(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(int,int)"""
        super(__GuiPosition, self).multiply(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def setX(self, arg0: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.setX(int)"""
        super(__GuiPosition, self).setX(__int.valueOf(arg0))

    @override
    @overload
    def onDestroy(self):
        """public void dev.ultreon.quantum.cs.GuiPosition.onDestroy()"""
        super(GuiPosition, self).onDestroy()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def multiply(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.multiply(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).multiply(arg0)

    @overload
    def divide(self, arg0: 'GuiPosition'):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(dev.ultreon.quantum.cs.GuiPosition)"""
        super(__GuiPosition, self).divide(arg0)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def divide(self, arg0: int, arg1: int):
        """public void dev.ultreon.quantum.cs.GuiPosition.divide(int,int)"""
        super(__GuiPosition, self).divide(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getX(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.getX()"""
        return int.__wrap(super(GuiPosition, self).getX())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.cs.GuiPosition.hashCode()"""
        return int.__wrap(super(GuiPosition, self).hashCode())

    @overload
    def copy(self) -> 'GuiPosition':
        """public dev.ultreon.quantum.cs.GuiPosition dev.ultreon.quantum.cs.GuiPosition.copy()"""
        return 'GuiPosition'.__wrap(super(GuiPosition, self).copy())

 
 
 
# CLASS: dev.ultreon.quantum.cs.GuiPosition 
 
 
# CLASS: dev.ultreon.quantum.cs.Component
from abc import abstractmethod, ABC
import dev.ultreon.quantum.cs.Component as __Component
__Component = __Component
 
class Component(ABC):
    """dev.ultreon.quantum.cs.Component"""
 
    @staticmethod
    def __wrap(java_value: __Component) -> 'Component':
        return Component(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Component):
        """
        Dynamic initializer for Component.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
import dev.ultreon.quantum.cs.WorldPosition as __WorldPosition
__WorldPosition = __WorldPosition
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class WorldPosition(__Component, Component):
    """dev.ultreon.quantum.cs.WorldPosition"""
 
    @staticmethod
    def __wrap(java_value: __WorldPosition) -> 'WorldPosition':
        return WorldPosition(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WorldPosition):
        """
        Dynamic initializer for WorldPosition.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def onCreate(self):
        """public void dev.ultreon.quantum.cs.WorldPosition.onCreate()"""
        super(WorldPosition, self).onCreate()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.cs.WorldPosition()"""
        val = __WorldPosition()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.cs.WorldPosition()"""
        val = __WorldPosition()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.cs.ComponentSystem
from builtins import str
import dev.ultreon.quantum.cs.ComponentSystem as __ComponentSystem
__ComponentSystem = __ComponentSystem
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Map as __Map
__Map = __Map
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import bool
import dev.ultreon.quantum.cs.Component as __Component
__Component = __Component
from builtins import int
 
class ComponentSystem():
    """dev.ultreon.quantum.cs.ComponentSystem"""
 
    @staticmethod
    def __wrap(java_value: __ComponentSystem) -> 'ComponentSystem':
        return ComponentSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComponentSystem):
        """
        Dynamic initializer for ComponentSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def clear(self):
        """public void dev.ultreon.quantum.cs.ComponentSystem.clear()"""
        super(ComponentSystem, self).clear()

    @overload
    def getComponent(self, arg0: str, *arg1: 'Component') -> 'Component':
        """public final <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.getComponent(java.lang.String,T...)"""
        return 'Component'.__wrap(super(__ComponentSystem, self).getComponent(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeComponent(self, arg0: str, *arg1: 'Component') -> 'Component':
        """public <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.removeComponent(java.lang.String,T...)"""
        return 'Component'.__wrap(super(__ComponentSystem, self).removeComponent(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getComponent(self, arg0: str, arg1: 'Class') -> 'Component':
        """public <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.getComponent(java.lang.String,java.lang.Class<T>)"""
        return 'Component'.__wrap(super(__ComponentSystem, self).getComponent(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.cs.ComponentSystem()"""
        val = __ComponentSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.cs.ComponentSystem()"""
        val = __ComponentSystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def addComponent(self, arg0: str, arg1: 'Component') -> 'Component':
        """public <T extends dev.ultreon.quantum.cs.Component> T dev.ultreon.quantum.cs.ComponentSystem.addComponent(java.lang.String,T)"""
        return 'Component'.__wrap(super(__ComponentSystem, self).addComponent(arg0, arg1))

    @overload
    def onTick(self):
        """public void dev.ultreon.quantum.cs.ComponentSystem.onTick()"""
        super(ComponentSystem, self).onTick()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getComponents(self) -> 'Map':
        """public java.util.Map<java.lang.String, dev.ultreon.quantum.cs.Component> dev.ultreon.quantum.cs.ComponentSystem.getComponents()"""
        return 'Map'.__wrap(super(ComponentSystem, self).getComponents())