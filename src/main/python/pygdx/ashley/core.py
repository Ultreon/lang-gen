from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.badlogic.ashley.core.ComponentMapper as _ComponentMapper
_ComponentMapper = _ComponentMapper
import java.lang.String as _String
_String = _String
import com.badlogic.ashley.core.Component as _Component
_Component = _Component
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComponentMapper():
    """com.badlogic.ashley.core.ComponentMapper"""
 
    @staticmethod
    def _wrap(java_value: _ComponentMapper) -> 'ComponentMapper':
        return ComponentMapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComponentMapper):
        """
        Dynamic initializer for ComponentMapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComponentMapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComponentMapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @overload
    def get(self, arg0: 'Entity') -> 'Component':
        """public T com.badlogic.ashley.core.ComponentMapper.get(com.badlogic.ashley.core.Entity)"""
        return 'Component'._wrap(super(_ComponentMapper, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def has(self, arg0: 'Entity') -> bool:
        """public boolean com.badlogic.ashley.core.ComponentMapper.has(com.badlogic.ashley.core.Entity)"""
        return bool._wrap(super(_ComponentMapper, self).has(arg0))

    @staticmethod
    @overload
    def getFor(arg0: 'Class') -> 'ComponentMapper':
        """public static <T extends com.badlogic.ashley.core.Component> com.badlogic.ashley.core.ComponentMapper<T> com.badlogic.ashley.core.ComponentMapper.getFor(java.lang.Class<T>)"""
        return ComponentMapper._wrap(_ComponentMapper.getFor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.ashley.core.ComponentMapper
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.badlogic.ashley.core.ComponentMapper as _ComponentMapper
_ComponentMapper = _ComponentMapper
import java.lang.String as _String
_String = _String
import com.badlogic.ashley.core.Component as _Component
_Component = _Component
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComponentMapper():
    """com.badlogic.ashley.core.ComponentMapper"""
 
    @staticmethod
    def _wrap(java_value: _ComponentMapper) -> 'ComponentMapper':
        return ComponentMapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComponentMapper):
        """
        Dynamic initializer for ComponentMapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComponentMapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComponentMapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @overload
    def get(self, arg0: 'Entity') -> 'Component':
        """public T com.badlogic.ashley.core.ComponentMapper.get(com.badlogic.ashley.core.Entity)"""
        return 'Component'._wrap(super(_ComponentMapper, self).get(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def has(self, arg0: 'Entity') -> bool:
        """public boolean com.badlogic.ashley.core.ComponentMapper.has(com.badlogic.ashley.core.Entity)"""
        return bool._wrap(super(_ComponentMapper, self).has(arg0))

    @staticmethod
    @overload
    def getFor(arg0: 'Class') -> 'ComponentMapper':
        """public static <T extends com.badlogic.ashley.core.Component> com.badlogic.ashley.core.ComponentMapper<T> com.badlogic.ashley.core.ComponentMapper.getFor(java.lang.Class<T>)"""
        return ComponentMapper._wrap(_ComponentMapper.getFor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.badlogic.ashley.core.ComponentMapper 
 
 
# CLASS: com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import com.badlogic.ashley.core.ComponentOperationHandler as _ComponentOperationHandler_ComponentOperation_Type
_Type = _ComponentOperationHandler_ComponentOperation_Type.ComponentOperation.Type
import java.util.Optional as Optional
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """com.badlogic.ashley.core.ComponentOperationHandler.ComponentOperation.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type[] com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type com.badlogic.ashley.core.ComponentOperationHandler$ComponentOperation$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.ashley.core.ComponentType
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.ashley.core.ComponentType as _ComponentType
_ComponentType = _ComponentType
import java.lang.Integer as _int
import com.badlogic.gdx.utils.Bits as _Bits
_Bits = _Bits
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ComponentType():
    """com.badlogic.ashley.core.ComponentType"""
 
    @staticmethod
    def _wrap(java_value: _ComponentType) -> 'ComponentType':
        return ComponentType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ComponentType):
        """
        Dynamic initializer for ComponentType.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ComponentType__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ComponentType__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.core.ComponentType.equals(java.lang.Object)"""
        return bool._wrap(super(_ComponentType, self).equals(arg0))

    @staticmethod
    @overload
    def getFor(arg0: 'Class') -> 'ComponentType':
        """public static com.badlogic.ashley.core.ComponentType com.badlogic.ashley.core.ComponentType.getFor(java.lang.Class<? extends com.badlogic.ashley.core.Component>)"""
        return ComponentType._wrap(_ComponentType.getFor(arg0))

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

    @staticmethod
    @overload
    def getIndexFor(arg0: 'Class') -> int:
        """public static int com.badlogic.ashley.core.ComponentType.getIndexFor(java.lang.Class<? extends com.badlogic.ashley.core.Component>)"""
        return int._wrap(_ComponentType.getIndexFor(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.core.ComponentType.hashCode()"""
        return int._wrap(super(ComponentType, self).hashCode())

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

    @staticmethod
    @overload
    def getBitsFor(*arg0: 'type.Class') -> 'utils.Bits':
        """public static com.badlogic.gdx.utils.Bits com.badlogic.ashley.core.ComponentType.getBitsFor(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return utils.Bits._wrap(_ComponentType.getBitsFor(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getIndex(self) -> int:
        """public int com.badlogic.ashley.core.ComponentType.getIndex()"""
        return int._wrap(super(ComponentType, self).getIndex()) 
 
 
# CLASS: com.badlogic.ashley.core.Entity
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import com.badlogic.ashley.core.Component as _Component
_Component = _Component
import java.lang.Integer as _int
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.core.Entity as _Entity
_Entity = _Entity
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Entity():
    """com.badlogic.ashley.core.Entity"""
 
    @staticmethod
    def _wrap(java_value: _Entity) -> 'Entity':
        return Entity(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Entity):
        """
        Dynamic initializer for Entity.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Entity__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Entity__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getComponent(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Entity.getComponent(java.lang.Class<T>)"""
        return 'Component'._wrap(super(_Entity, self).getComponent(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getComponents(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Component> com.badlogic.ashley.core.Entity.getComponents()"""
        return 'utils.ImmutableArray'._wrap(super(Entity, self).getComponents())

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
    def isScheduledForRemoval(self) -> bool:
        """public boolean com.badlogic.ashley.core.Entity.isScheduledForRemoval()"""
        return bool._wrap(super(Entity, self).isScheduledForRemoval())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.Entity()"""
        val = _Entity()
        self.__wrapper = val

    @overload
    def remove(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Entity.remove(java.lang.Class<T>)"""
        return 'Component'._wrap(super(_Entity, self).remove(arg0))

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
    def add(self, arg0: 'Component') -> 'Entity':
        """public com.badlogic.ashley.core.Entity com.badlogic.ashley.core.Entity.add(com.badlogic.ashley.core.Component)"""
        return 'Entity'._wrap(super(_Entity, self).add(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.Entity()"""
        val = _Entity()
        self.__wrapper = val

    @overload
    def addAndReturn(self, arg0: 'Component') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Entity.addAndReturn(T)"""
        return 'Component'._wrap(super(_Entity, self).addAndReturn(arg0))

    @overload
    def isRemoving(self) -> bool:
        """public boolean com.badlogic.ashley.core.Entity.isRemoving()"""
        return bool._wrap(super(Entity, self).isRemoving())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.ashley.core.EntitySystem
import com.badlogic.ashley.core.Engine as _Engine
_Engine = _Engine
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EntitySystem():
    """com.badlogic.ashley.core.EntitySystem"""
 
    @staticmethod
    def _wrap(java_value: _EntitySystem) -> 'EntitySystem':
        return EntitySystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntitySystem):
        """
        Dynamic initializer for EntitySystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntitySystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntitySystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.EntitySystem()"""
        val = _EntitySystem()
        self.__wrapper = val

    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(_EntitySystem, self).addedToEngine(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool._wrap(super(EntitySystem, self).checkProcessing())

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.EntitySystem.update(float)"""
        super(_EntitySystem, self).update(_float.valueOf(arg0))

    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(_EntitySystem, self).removedFromEngine(arg0)

    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(_EntitySystem, self).setProcessing(_boolean.valueOf(arg0))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.EntitySystem()"""
        val = _EntitySystem()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int):
        """public com.badlogic.ashley.core.EntitySystem(int)"""
        val = _EntitySystem(_int.valueOf(arg0))
        self.__wrapper = val

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
    def getEngine(self) -> 'Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'Engine'._wrap(super(EntitySystem, self).getEngine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.ashley.core.Component
import com.badlogic.ashley.core.Component as _Component
_Component = _Component
 
class Component():
    """com.badlogic.ashley.core.Component"""
 
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
 
 
# CLASS: com.badlogic.ashley.core.Engine
from pyquantum_helper import import_once as _import_once
import com.badlogic.ashley.core.Engine as _Engine
_Engine = _Engine
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import com.badlogic.ashley.core.Component as _Component
_Component = _Component
import java.lang.Float as _float
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.core.Entity as _Entity
_Entity = _Entity
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Engine():
    """com.badlogic.ashley.core.Engine"""
 
    @staticmethod
    def _wrap(java_value: _Engine) -> 'Engine':
        return Engine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Engine):
        """
        Dynamic initializer for Engine.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Engine__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Engine__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def addEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.addEntity(com.badlogic.ashley.core.Entity)"""
        super(_Engine, self).addEntity(arg0)

    @overload
    def addEntityListener(self, arg0: 'Family', arg1: int, arg2: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,int,com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(arg0, _int.valueOf(arg1), arg2)

    @overload
    def addSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.addSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(_Engine, self).addSystem(arg0)

    @overload
    def getEntitiesFor(self, arg0: 'Family') -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntitiesFor(com.badlogic.ashley.core.Family)"""
        return 'utils.ImmutableArray'._wrap(super(_Engine, self).getEntitiesFor(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSystems(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.EntitySystem> com.badlogic.ashley.core.Engine.getSystems()"""
        return 'utils.ImmutableArray'._wrap(super(Engine, self).getSystems())

    @overload
    def removeAllEntities(self, arg0: 'Family'):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities(com.badlogic.ashley.core.Family)"""
        super(_Engine, self).removeAllEntities(arg0)

    @overload
    def removeSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.removeSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(_Engine, self).removeSystem(arg0)

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntities()"""
        return 'utils.ImmutableArray'._wrap(super(Engine, self).getEntities())

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

    @overload
    def removeAllSystems(self):
        """public void com.badlogic.ashley.core.Engine.removeAllSystems()"""
        super(Engine, self).removeAllSystems()

    @overload
    def addEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(arg0)

    @overload
    def createComponent(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.Engine.createComponent(java.lang.Class<T>)"""
        return 'Component'._wrap(super(_Engine, self).createComponent(arg0))

    @overload
    def removeEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.removeEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).removeEntityListener(arg0)

    @overload
    def createEntity(self) -> 'Entity':
        """public com.badlogic.ashley.core.Entity com.badlogic.ashley.core.Engine.createEntity()"""
        return 'Entity'._wrap(super(Engine, self).createEntity())

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.Engine()"""
        val = _Engine()
        self.__wrapper = val

    @overload
    def addEntityListener(self, arg0: int, arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(int,com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(_int.valueOf(arg0), arg1)

    @overload
    def addEntityListener(self, arg0: 'Family', arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(arg0, arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.Engine.update(float)"""
        super(_Engine, self).update(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.Engine()"""
        val = _Engine()
        self.__wrapper = val

    @overload
    def getSystem(self, arg0: 'Class') -> 'EntitySystem':
        """public <T extends com.badlogic.ashley.core.EntitySystem> T com.badlogic.ashley.core.Engine.getSystem(java.lang.Class<T>)"""
        return 'EntitySystem'._wrap(super(_Engine, self).getSystem(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def removeEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.removeEntity(com.badlogic.ashley.core.Entity)"""
        super(_Engine, self).removeEntity(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.ashley.core.Family$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.ashley.core.Family as _Family_Builder
_Builder = _Family_Builder.Builder
import com.badlogic.ashley.core.Family as _Family
_Family = _Family
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.badlogic.ashley.core.Family.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def exclude(self, *arg0: 'type.Class') -> 'Builder':
        """public final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.exclude(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return 'Builder'._wrap(super(_Builder, self).exclude(arg0))

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

    @overload
    def one(self, *arg0: 'type.Class') -> 'Builder':
        """public final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.one(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return 'Builder'._wrap(super(_Builder, self).one(arg0))

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

    @overload
    def reset(self) -> 'Builder':
        """public com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.reset()"""
        return 'Builder'._wrap(super(Builder, self).reset())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def get(self) -> 'Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.core.Family$Builder.get()"""
        return 'Family'._wrap(super(Builder, self).get())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def all(self, *arg0: 'type.Class') -> 'Builder':
        """public final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family$Builder.all(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return 'Builder'._wrap(super(_Builder, self).all(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.ashley.core.EntityManager$EntityOperation$Type
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
import java.util.Optional as _Optional
_Optional = _Optional
import java.util.Optional as Optional
import com.badlogic.ashley.core.EntityManager as _EntityManager_EntityOperation_Type
_Type = _EntityManager_EntityOperation_Type.EntityOperation.Type
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Type():
    """com.badlogic.ashley.core.EntityManager.EntityOperation.Type"""
 
    @staticmethod
    def _wrap(java_value: _Type) -> 'Type':
        return Type(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Type):
        """
        Dynamic initializer for Type.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Type__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Type__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public final int java.lang.Enum.hashCode()"""
        return int._wrap(super(Enum, self).hashCode())

    @staticmethod
    @overload
    def valueOf(arg0: 'Class', arg1: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T java.lang.Enum.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_Enum.valueOf(arg0, arg1))

    @staticmethod
    @overload
    def valueOf(arg0: str) -> 'Type':
        """public static com.badlogic.ashley.core.EntityManager$EntityOperation$Type com.badlogic.ashley.core.EntityManager$EntityOperation$Type.valueOf(java.lang.String)"""
        return Type._wrap(_Type.valueOf(arg0))

    @override
    @overload
    def name(self) -> str:
        """public final java.lang.String java.lang.Enum.name()"""
        return str._wrap(super(Enum, self).name())

    @override
    @overload
    def describeConstable(self) -> 'Optional':
        """public final java.util.Optional<java.lang.Enum$EnumDesc<E>> java.lang.Enum.describeConstable()"""
        return 'Optional'._wrap(super(Enum, self).describeConstable())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Enum.toString()"""
        return str._wrap(super(Enum, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def ordinal(self) -> int:
        """public final int java.lang.Enum.ordinal()"""
        return int._wrap(super(Enum, self).ordinal())

    @staticmethod
    @overload
    def values() -> List['Type']:
        """public static com.badlogic.ashley.core.EntityManager$EntityOperation$Type[] com.badlogic.ashley.core.EntityManager$EntityOperation$Type.values()"""
        return List[Type]._wrap(_Type.values())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Enum, self).getDeclaringClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean java.lang.Enum.equals(java.lang.Object)"""
        return bool._wrap(super(_Enum, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def compareTo(self, arg0: 'Enum') -> int:
        """public final int java.lang.Enum.compareTo(E)"""
        return int._wrap(super(_Enum, self).compareTo(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.ashley.core.PooledEngine
from pyquantum_helper import import_once as _import_once
import com.badlogic.ashley.core.Engine as _Engine
_Engine = _Engine
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import com.badlogic.ashley.core.PooledEngine as _PooledEngine
_PooledEngine = _PooledEngine
import com.badlogic.ashley.core.Component as _Component
_Component = _Component
import java.lang.Float as _float
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.core.Entity as _Entity
_Entity = _Entity
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PooledEngine():
    """com.badlogic.ashley.core.PooledEngine"""
 
    @staticmethod
    def _wrap(java_value: _PooledEngine) -> 'PooledEngine':
        return PooledEngine(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PooledEngine):
        """
        Dynamic initializer for PooledEngine.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PooledEngine__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PooledEngine__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getSystems(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.EntitySystem> com.badlogic.ashley.core.Engine.getSystems()"""
        return 'utils.ImmutableArray'._wrap(super(Engine, self).getSystems())

    @override
    @overload
    def addEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(arg0)

    @override
    @overload
    def createEntity(self) -> 'Entity':
        """public com.badlogic.ashley.core.Entity com.badlogic.ashley.core.PooledEngine.createEntity()"""
        return 'Entity'._wrap(super(PooledEngine, self).createEntity())

    @overload
    def getEntitiesFor(self, arg0: 'Family') -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntitiesFor(com.badlogic.ashley.core.Family)"""
        return 'utils.ImmutableArray'._wrap(super(_Engine, self).getEntitiesFor(arg0))

    @override
    @overload
    def addEntityListener(self, arg0: 'Family', arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(arg0, arg1)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.core.Engine.getEntities()"""
        return 'utils.ImmutableArray'._wrap(super(Engine, self).getEntities())

    @override
    @overload
    def addEntityListener(self, arg0: int, arg1: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(int,com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.ashley.core.PooledEngine()"""
        val = _PooledEngine()
        self.__wrapper = val

    @overload
    def __init__(self, arg0: int, arg1: int, arg2: int, arg3: int):
        """public com.badlogic.ashley.core.PooledEngine(int,int,int,int)"""
        val = _PooledEngine(_int.valueOf(arg0), _int.valueOf(arg1), _int.valueOf(arg2), _int.valueOf(arg3))
        self.__wrapper = val

    @overload
    def createComponent(self, arg0: 'Class') -> 'Component':
        """public <T extends com.badlogic.ashley.core.Component> T com.badlogic.ashley.core.PooledEngine.createComponent(java.lang.Class<T>)"""
        return 'Component'._wrap(super(_PooledEngine, self).createComponent(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def removeSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.removeSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(_Engine, self).removeSystem(arg0)

    @override
    @overload
    def removeAllEntities(self, arg0: 'Family'):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities(com.badlogic.ashley.core.Family)"""
        super(_Engine, self).removeAllEntities(arg0)

    @override
    @overload
    def addEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.addEntity(com.badlogic.ashley.core.Entity)"""
        super(_Engine, self).addEntity(arg0)

    @overload
    def __init__(self):
        """public com.badlogic.ashley.core.PooledEngine()"""
        val = _PooledEngine()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def removeAllEntities(self):
        """public void com.badlogic.ashley.core.Engine.removeAllEntities()"""
        super(Engine, self).removeAllEntities()

    @override
    @overload
    def addEntityListener(self, arg0: 'Family', arg1: int, arg2: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.addEntityListener(com.badlogic.ashley.core.Family,int,com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).addEntityListener(arg0, _int.valueOf(arg1), arg2)

    @overload
    def clearPools(self):
        """public void com.badlogic.ashley.core.PooledEngine.clearPools()"""
        super(PooledEngine, self).clearPools()

    @override
    @overload
    def removeEntity(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.core.Engine.removeEntity(com.badlogic.ashley.core.Entity)"""
        super(_Engine, self).removeEntity(arg0)

    @override
    @overload
    def removeEntityListener(self, arg0: 'EntityListener'):
        """public void com.badlogic.ashley.core.Engine.removeEntityListener(com.badlogic.ashley.core.EntityListener)"""
        super(_Engine, self).removeEntityListener(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getSystem(self, arg0: 'Class') -> 'EntitySystem':
        """public <T extends com.badlogic.ashley.core.EntitySystem> T com.badlogic.ashley.core.Engine.getSystem(java.lang.Class<T>)"""
        return 'EntitySystem'._wrap(super(_Engine, self).getSystem(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def removeAllSystems(self):
        """public void com.badlogic.ashley.core.Engine.removeAllSystems()"""
        super(Engine, self).removeAllSystems()

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.core.Engine.update(float)"""
        super(_Engine, self).update(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def addSystem(self, arg0: 'EntitySystem'):
        """public void com.badlogic.ashley.core.Engine.addSystem(com.badlogic.ashley.core.EntitySystem)"""
        super(_Engine, self).addSystem(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.ashley.core.Family
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.badlogic.ashley.core.Family as _Family_Builder
_Builder = _Family_Builder.Builder
import com.badlogic.ashley.core.Family as _Family
_Family = _Family
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Family():
    """com.badlogic.ashley.core.Family"""
 
    @staticmethod
    def _wrap(java_value: _Family) -> 'Family':
        return Family(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Family):
        """
        Dynamic initializer for Family.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Family__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Family__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def matches(self, arg0: 'Entity') -> bool:
        """public boolean com.badlogic.ashley.core.Family.matches(com.badlogic.ashley.core.Entity)"""
        return bool._wrap(super(_Family, self).matches(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getIndex(self) -> int:
        """public int com.badlogic.ashley.core.Family.getIndex()"""
        return int._wrap(super(Family, self).getIndex())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.ashley.core.Family.hashCode()"""
        return int._wrap(super(Family, self).hashCode())

    @staticmethod
    @overload
    def exclude(*arg0: 'type.Class') -> 'Builder':
        """public static final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family.exclude(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return Builder._wrap(_Family.exclude(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.ashley.core.Family.equals(java.lang.Object)"""
        return bool._wrap(super(_Family, self).equals(arg0))

    @staticmethod
    @overload
    def one(*arg0: 'type.Class') -> 'Builder':
        """public static final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family.one(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return Builder._wrap(_Family.one(arg0))

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

    @staticmethod
    @overload
    def all(*arg0: 'type.Class') -> 'Builder':
        """public static final com.badlogic.ashley.core.Family$Builder com.badlogic.ashley.core.Family.all(java.lang.Class<? extends com.badlogic.ashley.core.Component>...)"""
        return Builder._wrap(_Family.all(arg0))

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
 
 
# CLASS: com.badlogic.ashley.core.EntityListener
from abc import abstractmethod, ABC
import com.badlogic.ashley.core.EntityListener as _EntityListener
_EntityListener = _EntityListener
 
class EntityListener():
    """com.badlogic.ashley.core.EntityListener"""
 
    @staticmethod
    def _wrap(java_value: _EntityListener) -> 'EntityListener':
        return EntityListener(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EntityListener):
        """
        Dynamic initializer for EntityListener.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EntityListener__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EntityListener__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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