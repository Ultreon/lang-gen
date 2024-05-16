from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
import com.badlogic.ashley.core.Engine as _Engine
_Engine = _Engine
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.ashley.systems.IntervalSystem as _IntervalSystem
_IntervalSystem = _IntervalSystem
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.systems.IntervalIteratingSystem as _IntervalIteratingSystem
_IntervalIteratingSystem = _IntervalIteratingSystem
import com.badlogic.ashley.core.Family as _Family
_Family = _Family
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
try:
    from pygdx.ashley import core
except ImportError:
    core = _import_once("pygdx.ashley.core")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntervalIteratingSystem():
    """com.badlogic.ashley.systems.IntervalIteratingSystem"""
 
    @staticmethod
    def _wrap(java_value: _IntervalIteratingSystem) -> 'IntervalIteratingSystem':
        return IntervalIteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntervalIteratingSystem):
        """
        Dynamic initializer for IntervalIteratingSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntervalIteratingSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntervalIteratingSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(_core.EntitySystem, self).setProcessing(_boolean.valueOf(arg0))

    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(_core.EntitySystem, self).removedFromEngine(arg0)

    @overload
    def __init__(self, arg0: 'Family', arg1: float, arg2: int):
        """public com.badlogic.ashley.systems.IntervalIteratingSystem(com.badlogic.ashley.core.Family,float,int)"""
        val = _IntervalIteratingSystem(arg0, _float.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Family', arg1: float):
        """public com.badlogic.ashley.systems.IntervalIteratingSystem(com.badlogic.ashley.core.Family,float)"""
        val = _IntervalIteratingSystem(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool._wrap(super(core.EntitySystem, self).checkProcessing())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.IntervalIteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'._wrap(super(IntervalIteratingSystem, self).getEntities())

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IntervalIteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(_IntervalIteratingSystem, self).addedToEngine(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.IntervalIteratingSystem.getFamily()"""
        return 'core.Family'._wrap(super(IntervalIteratingSystem, self).getFamily())

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'._wrap(super(core.EntitySystem, self).getEngine())

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
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IntervalSystem.update(float)"""
        super(_IntervalSystem, self).update(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getInterval(self) -> float:
        """public float com.badlogic.ashley.systems.IntervalSystem.getInterval()"""
        return float._wrap(super(IntervalSystem, self).getInterval())

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

 
 
 
# CLASS: com.badlogic.ashley.systems.IntervalIteratingSystem
from pyquantum_helper import import_once as _import_once
import com.badlogic.ashley.core.Engine as _Engine
_Engine = _Engine
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.ashley.systems.IntervalSystem as _IntervalSystem
_IntervalSystem = _IntervalSystem
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.systems.IntervalIteratingSystem as _IntervalIteratingSystem
_IntervalIteratingSystem = _IntervalIteratingSystem
import com.badlogic.ashley.core.Family as _Family
_Family = _Family
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
try:
    from pygdx.ashley import core
except ImportError:
    core = _import_once("pygdx.ashley.core")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntervalIteratingSystem():
    """com.badlogic.ashley.systems.IntervalIteratingSystem"""
 
    @staticmethod
    def _wrap(java_value: _IntervalIteratingSystem) -> 'IntervalIteratingSystem':
        return IntervalIteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntervalIteratingSystem):
        """
        Dynamic initializer for IntervalIteratingSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntervalIteratingSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntervalIteratingSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(_core.EntitySystem, self).setProcessing(_boolean.valueOf(arg0))

    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(_core.EntitySystem, self).removedFromEngine(arg0)

    @overload
    def __init__(self, arg0: 'Family', arg1: float, arg2: int):
        """public com.badlogic.ashley.systems.IntervalIteratingSystem(com.badlogic.ashley.core.Family,float,int)"""
        val = _IntervalIteratingSystem(arg0, _float.valueOf(arg1), _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'Family', arg1: float):
        """public com.badlogic.ashley.systems.IntervalIteratingSystem(com.badlogic.ashley.core.Family,float)"""
        val = _IntervalIteratingSystem(arg0, _float.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool._wrap(super(core.EntitySystem, self).checkProcessing())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.IntervalIteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'._wrap(super(IntervalIteratingSystem, self).getEntities())

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IntervalIteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(_IntervalIteratingSystem, self).addedToEngine(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.IntervalIteratingSystem.getFamily()"""
        return 'core.Family'._wrap(super(IntervalIteratingSystem, self).getFamily())

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'._wrap(super(core.EntitySystem, self).getEngine())

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
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IntervalSystem.update(float)"""
        super(_IntervalSystem, self).update(_float.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def getInterval(self) -> float:
        """public float com.badlogic.ashley.systems.IntervalSystem.getInterval()"""
        return float._wrap(super(IntervalSystem, self).getInterval())

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

 
 
 
# CLASS: com.badlogic.ashley.systems.IntervalIteratingSystem 
 
 
# CLASS: com.badlogic.ashley.systems.SortedIteratingSystem
from pyquantum_helper import import_once as _import_once
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
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
import com.badlogic.ashley.systems.SortedIteratingSystem as _SortedIteratingSystem
_SortedIteratingSystem = _SortedIteratingSystem
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.core.Family as _Family
_Family = _Family
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
try:
    from pygdx.ashley import core
except ImportError:
    core = _import_once("pygdx.ashley.core")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SortedIteratingSystem():
    """com.badlogic.ashley.systems.SortedIteratingSystem"""
 
    @staticmethod
    def _wrap(java_value: _SortedIteratingSystem) -> 'SortedIteratingSystem':
        return SortedIteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedIteratingSystem):
        """
        Dynamic initializer for SortedIteratingSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedIteratingSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedIteratingSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(_SortedIteratingSystem, self).removedFromEngine(arg0)

    @overload
    def forceSort(self):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.forceSort()"""
        super(SortedIteratingSystem, self).forceSort()

    @overload
    def __init__(self, arg0: 'Family', arg1: 'Comparator', arg2: int):
        """public com.badlogic.ashley.systems.SortedIteratingSystem(com.badlogic.ashley.core.Family,java.util.Comparator<com.badlogic.ashley.core.Entity>,int)"""
        val = _SortedIteratingSystem(arg0, arg1, _int.valueOf(arg2))
        self.__wrapper = val

    @override
    @overload
    def entityAdded(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.entityAdded(com.badlogic.ashley.core.Entity)"""
        super(_SortedIteratingSystem, self).entityAdded(arg0)

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(_core.EntitySystem, self).setProcessing(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool._wrap(super(core.EntitySystem, self).checkProcessing())

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
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'._wrap(super(core.EntitySystem, self).getEngine())

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(_SortedIteratingSystem, self).addedToEngine(arg0)

    @overload
    def __init__(self, arg0: 'Family', arg1: 'Comparator'):
        """public com.badlogic.ashley.systems.SortedIteratingSystem(com.badlogic.ashley.core.Family,java.util.Comparator<com.badlogic.ashley.core.Entity>)"""
        val = _SortedIteratingSystem(arg0, arg1)
        self.__wrapper = val

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.SortedIteratingSystem.getFamily()"""
        return 'core.Family'._wrap(super(SortedIteratingSystem, self).getFamily())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.SortedIteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'._wrap(super(SortedIteratingSystem, self).getEntities())

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
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.update(float)"""
        super(_SortedIteratingSystem, self).update(_float.valueOf(arg0))

    @override
    @overload
    def entityRemoved(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.entityRemoved(com.badlogic.ashley.core.Entity)"""
        super(_SortedIteratingSystem, self).entityRemoved(arg0)

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
 
 
# CLASS: com.badlogic.ashley.systems.IteratingSystem
from pyquantum_helper import import_once as _import_once
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
try:
    from pygdx.ashley import utils
except ImportError:
    utils = _import_once("pygdx.ashley.utils")

import com.badlogic.ashley.core.Family as _Family
_Family = _Family
import com.badlogic.ashley.systems.IteratingSystem as _IteratingSystem
_IteratingSystem = _IteratingSystem
from builtins import bool
import com.badlogic.ashley.utils.ImmutableArray as _ImmutableArray
_ImmutableArray = _ImmutableArray
import java.lang.Long as _long
try:
    from pygdx.ashley import core
except ImportError:
    core = _import_once("pygdx.ashley.core")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IteratingSystem():
    """com.badlogic.ashley.systems.IteratingSystem"""
 
    @staticmethod
    def _wrap(java_value: _IteratingSystem) -> 'IteratingSystem':
        return IteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IteratingSystem):
        """
        Dynamic initializer for IteratingSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IteratingSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IteratingSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IteratingSystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(_IteratingSystem, self).removedFromEngine(arg0)

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(_core.EntitySystem, self).setProcessing(_boolean.valueOf(arg0))

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.IteratingSystem.getFamily()"""
        return 'core.Family'._wrap(super(IteratingSystem, self).getFamily())

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IteratingSystem.update(float)"""
        super(_IteratingSystem, self).update(_float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'Family', arg1: int):
        """public com.badlogic.ashley.systems.IteratingSystem(com.badlogic.ashley.core.Family,int)"""
        val = _IteratingSystem(arg0, _int.valueOf(arg1))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool._wrap(super(core.EntitySystem, self).checkProcessing())

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
    def __init__(self, arg0: 'Family'):
        """public com.badlogic.ashley.systems.IteratingSystem(com.badlogic.ashley.core.Family)"""
        val = _IteratingSystem(arg0)
        self.__wrapper = val

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'._wrap(super(core.EntitySystem, self).getEngine())

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
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(_IteratingSystem, self).addedToEngine(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.IteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'._wrap(super(IteratingSystem, self).getEntities())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.ashley.systems.IntervalSystem
from pyquantum_helper import import_once as _import_once
import com.badlogic.ashley.core.Engine as _Engine
_Engine = _Engine
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import com.badlogic.ashley.systems.IntervalSystem as _IntervalSystem
_IntervalSystem = _IntervalSystem
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import com.badlogic.ashley.core.EntitySystem as _EntitySystem
_EntitySystem = _EntitySystem
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
try:
    from pygdx.ashley import core
except ImportError:
    core = _import_once("pygdx.ashley.core")

from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntervalSystem():
    """com.badlogic.ashley.systems.IntervalSystem"""
 
    @staticmethod
    def _wrap(java_value: _IntervalSystem) -> 'IntervalSystem':
        return IntervalSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntervalSystem):
        """
        Dynamic initializer for IntervalSystem.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntervalSystem__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntervalSystem__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(_core.EntitySystem, self).addedToEngine(arg0)

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(_core.EntitySystem, self).setProcessing(_boolean.valueOf(arg0))

    @overload
    def getInterval(self) -> float:
        """public float com.badlogic.ashley.systems.IntervalSystem.getInterval()"""
        return float._wrap(super(IntervalSystem, self).getInterval())

    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(_core.EntitySystem, self).removedFromEngine(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool._wrap(super(core.EntitySystem, self).checkProcessing())

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
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'._wrap(super(core.EntitySystem, self).getEngine())

    @overload
    def __init__(self, arg0: float, arg1: int):
        """public com.badlogic.ashley.systems.IntervalSystem(float,int)"""
        val = _IntervalSystem(_float.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

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
    def __init__(self, arg0: float):
        """public com.badlogic.ashley.systems.IntervalSystem(float)"""
        val = _IntervalSystem(_float.valueOf(arg0))
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IntervalSystem.update(float)"""
        super(_IntervalSystem, self).update(_float.valueOf(arg0))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())