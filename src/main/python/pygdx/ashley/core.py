from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.ashley.core.EntitySystem as __EntitySystem
__EntitySystem = __EntitySystem
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntitySystem(ABC):
    """com.badlogic.ashley.core.EntitySystem"""
 
    @staticmethod
    def __wrap(java_value: __EntitySystem) -> 'EntitySystem':
        return EntitySystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntitySystem):
        """
        Dynamic initializer for EntitySystem.
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
    def __init__(self, ):
        """public com.badlogic.ashley.core.EntitySystem()"""
        val = __EntitySystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.EntitySystem.update(float)"""
        super(__EntitySystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.EntitySystem()"""
        val = __EntitySystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEngine(self) -> 'Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'Engine'.__wrap(super(EntitySystem, self).getEngine())

    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.ashley.core.EntitySystem(int)"""
        val = __EntitySystem(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__EntitySystem, self).addedToEngine(arg0)

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
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__EntitySystem, self).removedFromEngine(arg0)

    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(EntitySystem, self).checkProcessing())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.ashley.core.EntitySystem
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.ashley.core.EntitySystem as __EntitySystem
__EntitySystem = __EntitySystem
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntitySystem(ABC):
    """com.badlogic.ashley.core.EntitySystem"""
 
    @staticmethod
    def __wrap(java_value: __EntitySystem) -> 'EntitySystem':
        return EntitySystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntitySystem):
        """
        Dynamic initializer for EntitySystem.
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
    def __init__(self, ):
        """public com.badlogic.ashley.core.EntitySystem()"""
        val = __EntitySystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.EntitySystem.update(float)"""
        super(__EntitySystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.EntitySystem()"""
        val = __EntitySystem()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getEngine(self) -> 'Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'Engine'.__wrap(super(EntitySystem, self).getEngine())

    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.ashley.core.EntitySystem(int)"""
        val = __EntitySystem(__int.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__EntitySystem, self).addedToEngine(arg0)

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
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__EntitySystem, self).removedFromEngine(arg0)

    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(EntitySystem, self).checkProcessing())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.ashley.core.EntitySystem 
 
 
# CLASS: com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
from typing import List
import com.badlogic.ashley.core.ComponentOperationHandler as __ComponentOperationHandler_ComponentOperation_Type
__Type = __ComponentOperationHandler_ComponentOperation_Type.ComponentOperation.Type
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type():
    """com.badlogic.ashley.core.ComponentOperationHandler.ComponentOperation.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type[] com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.ashley.core.Entity
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.core.Entity as __Entity
__Entity = __Entity
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
import com.badlogic.ashley.core.Component as __Component
__Component = __Component
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ashley import utils
except ImportError:
    utils = __import_once__("pygdx.ashley.utils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Entity():
    """com.badlogic.ashley.core.Entity"""
 
    @staticmethod
    def __wrap(java_value: __Entity) -> 'Entity':
        return Entity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Entity):
        """
        Dynamic initializer for Entity.
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
    def addAndReturn(self, arg0: 'Component') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Entity.addAndReturn(T)"""
        return 'Component'.__wrap(super(__Entity, self).addAndReturn(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def add(self, arg0: 'Component') -> 'Entity':
        """public com.badlogic.ashley.core.Entity com.badlogic.ashley.core.Entity.add(com.badlogic.ashley.core.Component)"""
        return 'Entity'.__wrap(super(__Entity, self).add(arg0))

    @overload
    def remove(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Entity.remove(java.lang.Class<T>)"""
        return 'Component'.__wrap(super(__Entity, self).remove(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.Entity()"""
        val = __Entity()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeAll(self):
        """public void com.badlogic.ashley.core.Entity.removeAll()"""
        super(Entity, self).removeAll()

    @overload
    def getComponents(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Component> com.badlogic.ashley.core.Entity.getComponents()"""
        return 'utils.ImmutableArray'.__wrap(super(Entity, self).getComponents())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isScheduledForRemoval(self) -> bool:
        """public boolean com.badlogic.ashley.core.Entity.isScheduledForRemoval()"""
        return bool.__wrap(super(Entity, self).isScheduledForRemoval())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getComponent(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Entity.getComponent(java.lang.Class<T>)"""
        return 'Component'.__wrap(super(__Entity, self).getComponent(arg0))

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

    @overload
    def isRemoving(self) -> bool:
        """public boolean com.badlogic.ashley.core.Entity.isRemoving()"""
        return bool.__wrap(super(Entity, self).isRemoving())

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.Entity()"""
        val = __Entity()
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.ashley.core.Family
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Family as __Family
__Family = __Family
import com.badlogic.ashley.core.Family as __Family_Builder
__Builder = __Family_Builder.Builder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Family():
    """com.badlogic.ashley.core.Family"""
 
    @staticmethod
    def __wrap(java_value: __Family) -> 'Family':
        return Family(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Family):
        """
        Dynamic initializer for Family.
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

    @staticmethod
    @overload
    def all(*arg0: 'type.Class') -> 'Builder':
        """public static final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family.all(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return Builder.__wrap(__Family.all(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def matches(self, arg0: 'Entity') -> bool:
        """public boolean com.badlogic.ashley.core.Family.matches(com.badlogic.ashley.core.Entity)"""
        return bool.__wrap(super(__Family, self).matches(arg0))

    @overload
    def getIndex(self) -> int:
        """public int com.badlogic.ashley.core.Family.getIndex()"""
        return int.__wrap(super(Family, self).getIndex())

    @staticmethod
    @overload
    def exclude(*arg0: 'type.Class') -> 'Builder':
        """public static final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family.exclude(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return Builder.__wrap(__Family.exclude(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.core.Family.equals(java.lang.Object)"""
        return bool.__wrap(super(__Family, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def one(*arg0: 'type.Class') -> 'Builder':
        """public static final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family.one(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return Builder.__wrap(__Family.one(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.core.Family.hashCode()"""
        return int.__wrap(super(Family, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.ashley.core.ComponentType
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.core.ComponentType as __ComponentType
__ComponentType = __ComponentType
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.Bits as __Bits
__Bits = __Bits
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ComponentType():
    """com.badlogic.ashley.core.ComponentType"""
 
    @staticmethod
    def __wrap(java_value: __ComponentType) -> 'ComponentType':
        return ComponentType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComponentType):
        """
        Dynamic initializer for ComponentType.
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

    @staticmethod
    @overload
    def getBitsFor(*arg0: 'type.Class') -> 'utils.Bits':
        """public static com.badlogic.gdx.utils.Bits com.badlogic.ashley.core.ComponentType.getBitsFor(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return utils.Bits.__wrap(__ComponentType.getBitsFor(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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

    @staticmethod
    @overload
    def getFor(arg0: 'Class') -> 'ComponentType':
        """public static com.badlogic.ashley.core.ComponentType com.badlogic.ashley.core.ComponentType.getFor(java.lang.Class<? extends com.badlogic.ashley.core.Component>)"""
        return ComponentType.__wrap(__ComponentType.getFor(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.core.ComponentType.hashCode()"""
        return int.__wrap(super(ComponentType, self).hashCode())

    @overload
    def getIndex(self) -> int:
        """public int com.badlogic.ashley.core.ComponentType.getIndex()"""
        return int.__wrap(super(ComponentType, self).getIndex())

    @staticmethod
    @overload
    def getIndexFor(arg0: 'Class') -> int:
        """public static int com.badlogic.ashley.core.ComponentType.getIndexFor(java.lang.Class<? extends com.badlogic.ashley.core.Component>)"""
        return int.__wrap(__ComponentType.getIndexFor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.core.ComponentType.equals(java.lang.Object)"""
        return bool.__wrap(super(__ComponentType, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.ashley.core.ComponentMapper
from builtins import str
import com.badlogic.ashley.core.Component as __Component
__Component = __Component
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.ComponentMapper as __ComponentMapper
__ComponentMapper = __ComponentMapper
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ComponentMapper():
    """com.badlogic.ashley.core.ComponentMapper"""
 
    @staticmethod
    def __wrap(java_value: __ComponentMapper) -> 'ComponentMapper':
        return ComponentMapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ComponentMapper):
        """
        Dynamic initializer for ComponentMapper.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def has(self, arg0: 'Entity') -> bool:
        """public boolean com.badlogic.ashley.core.ComponentMapper.has(com.badlogic.ashley.core.Entity)"""
        return bool.__wrap(super(__ComponentMapper, self).has(arg0))

    @overload
    def get(self, arg0: 'Entity') -> 'Component':
        """public T com.badlogic.ashley.core.ComponentMapper.get(com.badlogic.ashley.core.Entity)"""
        return 'Component'.__wrap(super(__ComponentMapper, self).get(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getFor(arg0: 'Class') -> 'ComponentMapper':
        """public static <T extends com.badlogic.ashley.core.Component> com.badlogic.ashley.core.ComponentMapper<T> com.badlogic.ashley.core.ComponentMapper.getFor(java.lang.Class<T>)"""
        return ComponentMapper.__wrap(__ComponentMapper.getFor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.ashley.core.EntityListener
import com.badlogic.ashley.core.EntityListener as __EntityListener
__EntityListener = __EntityListener
from abc import abstractmethod, ABC
 
class EntityListener(ABC):
    """com.badlogic.ashley.core.EntityListener"""
 
    @staticmethod
    def __wrap(java_value: __EntityListener) -> 'EntityListener':
        return EntityListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntityListener):
        """
        Dynamic initializer for EntityListener.
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
    def entityRemoved(self, arg0: 'Entity'):
        """public abstract void com.badlogic.ashley.core.EntityListener.entityRemoved(com.badlogic.ashley.core.Entity)"""
        pass

    @abstractmethod
    def entityAdded(self, arg0: 'Entity'):
        """public abstract void com.badlogic.ashley.core.EntityListener.entityAdded(com.badlogic.ashley.core.Entity)"""
        pass 
 
 
# CLASS: com.badlogic.ashley.core.EntityManager$EntityOperation$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.util.Optional as __Optional
__Optional = __Optional
import com.badlogic.ashley.core.EntityManager as __EntityManager_EntityOperation_Type
__Type = __EntityManager_EntityOperation_Type.EntityOperation.Type
from typing import List
import java.lang.Enum as Enum
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.util.Optional as Optional
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.Enum as __Enum
__Enum = __Enum
from builtins import bool
from builtins import int
 
class Type():
    """com.badlogic.ashley.core.EntityManager.EntityOperation.Type"""
 
    @staticmethod
    def __wrap(java_value: __Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Type):
        """
        Dynamic initializer for Type.
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

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum.__wrap(__Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str.__wrap(super(Enum, self).name())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.ashley.core.EntityManager$EntityOperation$Type[] com.badlogic.ashley.core.EntityManager$EntityOperation$Type.values()"""
        return List[Type].__wrap(__Type.values())

    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int.__wrap(super(Enum, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'.__wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int.__wrap(super(__Enum, self).compareTo(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.ashley.core.EntityManager$EntityOperation$Type com.badlogic.ashley.core.EntityManager$EntityOperation$Type.valueOf(java.lang.String)"""
        return Type.__wrap(__Type.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool.__wrap(super(__Enum, self).equals(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int.__wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str.__wrap(super(Enum, self).toString()) 
 
 
# CLASS: com.badlogic.ashley.core.Component
import com.badlogic.ashley.core.Component as __Component
__Component = __Component
 
class Component(ABC):
    """com.badlogic.ashley.core.Component"""
 
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
 
 
# CLASS: com.badlogic.ashley.core.Family$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Family as __Family
__Family = __Family
import com.badlogic.ashley.core.Family as __Family_Builder
__Builder = __Family_Builder.Builder
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """com.badlogic.ashley.core.Family.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def all(self, *arg0: 'type.Class') -> 'Builder':
        """public final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.all(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return 'Builder'.__wrap(super(__Builder, self).all(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def exclude(self, *arg0: 'type.Class') -> 'Builder':
        """public final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.exclude(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return 'Builder'.__wrap(super(__Builder, self).exclude(arg0))

    @overload
    def one(self, *arg0: 'type.Class') -> 'Builder':
        """public final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.one(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return 'Builder'.__wrap(super(__Builder, self).one(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def get(self) -> 'Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.core.Family$Builder.get()"""
        return 'Family'.__wrap(super(Builder, self).get())

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def reset(self) -> 'Builder':
        """public com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.reset()"""
        return 'Builder'.__wrap(super(Builder, self).reset())

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
 
 
# CLASS: com.badlogic.ashley.core.PooledEngine
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.core.Entity as __Entity
__Entity = __Entity
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
import com.badlogic.ashley.core.Component as __Component
__Component = __Component
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ashley import utils
except ImportError:
    utils = __import_once__("pygdx.ashley.utils")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.ashley.core.PooledEngine as __PooledEngine
__PooledEngine = __PooledEngine
import com.badlogic.ashley.core.EntitySystem as __EntitySystem
__EntitySystem = __EntitySystem
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PooledEngine():
    """com.badlogic.ashley.core.PooledEngine"""
 
    @staticmethod
    def __wrap(java_value: __PooledEngine) -> 'PooledEngine':
        return PooledEngine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PooledEngine):
        """
        Dynamic initializer for PooledEngine.
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
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.Engine.update(float)"""
        super(__Engine, self).update(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def createComponent(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.PooledEngine.createComponent(java.lang.Class<T>)"""
        return 'Component'.__wrap(super(__PooledEngine, self).createComponent(arg0))

    @override
    @overload
    def removeSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.removeSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(__Engine, self).removeSystem(arg0)

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.ashley.core.PooledEngine(int,int,int,int)"""
        val = __PooledEngine(__int.valueOf(arg0), __int.valueOf(arg1), __int.valueOf(arg2), __int.valueOf(arg3))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def removeEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.removeEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).removeEntityListener(arg0)

    @override
    @overload
    def addSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.addSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(__Engine, self).addSystem(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntities()"""
        return 'utils.ImmutableArray'.__wrap(super(Engine, self).getEntities())

    @override
    @overload
    def addEntityListener(self, arg0: 'Family', arg1: int, arg2: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,int,com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(arg0, __int.valueOf(arg1), arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getSystem(self, arg0: 'Class') -> 'EntitySystem':
        """public <T extends com.badlogic.ashley.core.EntitySystem> T com.badlogic.ashley.core.Engine.getSystem(java.lang.Class<T>)"""
        return 'EntitySystem'.__wrap(super(__Engine, self).getSystem(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def removeEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.removeEntity(com.badlogic.ashley.core.Entity)"""
        super(__Engine, self).removeEntity(arg0)

    @override
    @overload
    def removeAllEntities(self, arg0: 'Family'):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities(com.badlogic.ashley.core.Family)"""
        super(__Engine, self).removeAllEntities(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def createEntity(self) -> 'Entity':
        """public com.badlogic.ashley.core.Entity com.badlogic.ashley.core.PooledEngine.createEntity()"""
        return 'Entity'.__wrap(super(PooledEngine, self).createEntity())

    @override
    @overload
    def removeAllEntities(self):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities()"""
        super(Engine, self).removeAllEntities()

    @overload
    def getEntitiesFor(self, arg0: 'Family') -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntitiesFor(com.badlogic.ashley.core.Family)"""
        return 'utils.ImmutableArray'.__wrap(super(__Engine, self).getEntitiesFor(arg0))

    @override
    @overload
    def addEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(arg0)

    @overload
    def clearPools(self):
        """public void com.badlogic.ashley.core.PooledEngine.clearPools()"""
        super(PooledEngine, self).clearPools()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.PooledEngine()"""
        val = __PooledEngine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.PooledEngine()"""
        val = __PooledEngine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def removeAllSystems(self):
        """public void com.badlogic.ashley.core.Engine.removeAllSystems()"""
        super(Engine, self).removeAllSystems()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.addEntity(com.badlogic.ashley.core.Entity)"""
        super(__Engine, self).addEntity(arg0)

    @override
    @overload
    def addEntityListener(self, arg0: 'Family', arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getSystems(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.EntitySystem> com.badlogic.ashley.core.Engine.getSystems()"""
        return 'utils.ImmutableArray'.__wrap(super(Engine, self).getSystems())

    @override
    @overload
    def addEntityListener(self, arg0: int, arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(int,com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(__int.valueOf(arg0), arg1) 
 
 
# CLASS: com.badlogic.ashley.core.Engine
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
import com.badlogic.ashley.core.Entity as __Entity
__Entity = __Entity
from builtins import str
import com.badlogic.ashley.core.Component as __Component
__Component = __Component
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.ashley import utils
except ImportError:
    utils = __import_once__("pygdx.ashley.utils")

import java.lang.Object as __Object
__Object = __Object
import com.badlogic.ashley.core.EntitySystem as __EntitySystem
__EntitySystem = __EntitySystem
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Engine():
    """com.badlogic.ashley.core.Engine"""
 
    @staticmethod
    def __wrap(java_value: __Engine) -> 'Engine':
        return Engine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Engine):
        """
        Dynamic initializer for Engine.
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
    def addSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.addSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(__Engine, self).addSystem(arg0)

    @overload
    def removeAllEntities(self, arg0: 'Family'):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities(com.badlogic.ashley.core.Family)"""
        super(__Engine, self).removeAllEntities(arg0)

    @overload
    def createComponent(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Engine.createComponent(java.lang.Class<T>)"""
        return 'Component'.__wrap(super(__Engine, self).createComponent(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addEntityListener(self, arg0: 'Family', arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(arg0, arg1)

    @overload
    def addEntityListener(self, arg0: int, arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(int,com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(__int.valueOf(arg0), arg1)

    @overload
    def addEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.addEntity(com.badlogic.ashley.core.Entity)"""
        super(__Engine, self).addEntity(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def removeAllSystems(self):
        """public void com.badlogic.ashley.core.Engine.removeAllSystems()"""
        super(Engine, self).removeAllSystems()

    @overload
    def getSystem(self, arg0: 'Class') -> 'EntitySystem':
        """public <T extends com.badlogic.ashley.core.EntitySystem> T com.badlogic.ashley.core.Engine.getSystem(java.lang.Class<T>)"""
        return 'EntitySystem'.__wrap(super(__Engine, self).getSystem(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.Engine()"""
        val = __Engine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def addEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(arg0)

    @overload
    def getEntitiesFor(self, arg0: 'Family') -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntitiesFor(com.badlogic.ashley.core.Family)"""
        return 'utils.ImmutableArray'.__wrap(super(__Engine, self).getEntitiesFor(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.Engine.update(float)"""
        super(__Engine, self).update(__float.valueOf(arg0))

    @overload
    def removeEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.removeEntity(com.badlogic.ashley.core.Entity)"""
        super(__Engine, self).removeEntity(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.Engine()"""
        val = __Engine()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getSystems(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.EntitySystem> com.badlogic.ashley.core.Engine.getSystems()"""
        return 'utils.ImmutableArray'.__wrap(super(Engine, self).getSystems())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def addEntityListener(self, arg0: 'Family', arg1: int, arg2: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,int,com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).addEntityListener(arg0, __int.valueOf(arg1), arg2)

    @overload
    def createEntity(self) -> 'Entity':
        """public com.badlogic.ashley.core.Entity com.badlogic.ashley.core.Engine.createEntity()"""
        return 'Entity'.__wrap(super(Engine, self).createEntity())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def removeAllEntities(self):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities()"""
        super(Engine, self).removeAllEntities()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def removeSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.removeSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(__Engine, self).removeSystem(arg0)

    @overload
    def removeEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.removeEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(__Engine, self).removeEntityListener(arg0)

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntities()"""
        return 'utils.ImmutableArray'.__wrap(super(Engine, self).getEntities())