from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import com.badlogic.ashley.core.Family as __Family
__Family = __Family
import java.util.Comparator as Comparator
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
import com.badlogic.ashley.systems.SortedIteratingSystem as __SortedIteratingSystem
__SortedIteratingSystem = __SortedIteratingSystem
from builtins import bool
try:
    from pygdx.ashley import core
except ImportError:
    core = __import_once__("pygdx.ashley.core")

from builtins import int
 
class SortedIteratingSystem(ABC, ashley.__EntitySystem, core.EntitySystem, ashley.__EntityListener, core.EntityListener):
    """com.badlogic.ashley.systems.SortedIteratingSystem"""
 
    @staticmethod
    def __wrap(java_value: __SortedIteratingSystem) -> 'SortedIteratingSystem':
        return SortedIteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedIteratingSystem):
        """
        Dynamic initializer for SortedIteratingSystem.
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
 
    @overload
    def forceSort(self):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.forceSort()"""
        super(SortedIteratingSystem, self).forceSort()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def entityRemoved(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.entityRemoved(com.badlogic.ashley.core.Entity)"""
        super(__SortedIteratingSystem, self).entityRemoved(arg0)

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__core.EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

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
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__SortedIteratingSystem, self).removedFromEngine(arg0)

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
    def __init__(self, arg0: 'Family', arg1: 'Comparator'):
        """public com.badlogic.ashley.systems.SortedIteratingSystem(com.badlogic.ashley.core.Family,java.util.Comparator<com.badlogic.ashley.core.Entity>)"""
        val = __SortedIteratingSystem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(core.EntitySystem, self).checkProcessing())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.SortedIteratingSystem.getFamily()"""
        return 'core.Family'.__wrap(super(SortedIteratingSystem, self).getFamily())

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.SortedIteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'.__wrap(super(SortedIteratingSystem, self).getEntities())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Family', arg1: 'Comparator', arg2: int):
        """public com.badlogic.ashley.systems.SortedIteratingSystem(com.badlogic.ashley.core.Family,java.util.Comparator<com.badlogic.ashley.core.Entity>,int)"""
        val = __SortedIteratingSystem(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.update(float)"""
        super(__SortedIteratingSystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def entityAdded(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.entityAdded(com.badlogic.ashley.core.Entity)"""
        super(__SortedIteratingSystem, self).entityAdded(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__SortedIteratingSystem, self).addedToEngine(arg0)

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'.__wrap(super(core.EntitySystem, self).getEngine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.ashley.systems.SortedIteratingSystem
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import com.badlogic.ashley.core.Family as __Family
__Family = __Family
import java.util.Comparator as Comparator
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
import com.badlogic.ashley.systems.SortedIteratingSystem as __SortedIteratingSystem
__SortedIteratingSystem = __SortedIteratingSystem
from builtins import bool
try:
    from pygdx.ashley import core
except ImportError:
    core = __import_once__("pygdx.ashley.core")

from builtins import int
 
class SortedIteratingSystem(ABC, ashley.__EntitySystem, core.EntitySystem, ashley.__EntityListener, core.EntityListener):
    """com.badlogic.ashley.systems.SortedIteratingSystem"""
 
    @staticmethod
    def __wrap(java_value: __SortedIteratingSystem) -> 'SortedIteratingSystem':
        return SortedIteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedIteratingSystem):
        """
        Dynamic initializer for SortedIteratingSystem.
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
 
    @overload
    def forceSort(self):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.forceSort()"""
        super(SortedIteratingSystem, self).forceSort()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def entityRemoved(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.entityRemoved(com.badlogic.ashley.core.Entity)"""
        super(__SortedIteratingSystem, self).entityRemoved(arg0)

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__core.EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

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
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__SortedIteratingSystem, self).removedFromEngine(arg0)

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
    def __init__(self, arg0: 'Family', arg1: 'Comparator'):
        """public com.badlogic.ashley.systems.SortedIteratingSystem(com.badlogic.ashley.core.Family,java.util.Comparator<com.badlogic.ashley.core.Entity>)"""
        val = __SortedIteratingSystem(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(core.EntitySystem, self).checkProcessing())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.SortedIteratingSystem.getFamily()"""
        return 'core.Family'.__wrap(super(SortedIteratingSystem, self).getFamily())

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.SortedIteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'.__wrap(super(SortedIteratingSystem, self).getEntities())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'Family', arg1: 'Comparator', arg2: int):
        """public com.badlogic.ashley.systems.SortedIteratingSystem(com.badlogic.ashley.core.Family,java.util.Comparator<com.badlogic.ashley.core.Entity>,int)"""
        val = __SortedIteratingSystem(arg0, arg1, __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.update(float)"""
        super(__SortedIteratingSystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def entityAdded(self, arg0: 'Entity'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.entityAdded(com.badlogic.ashley.core.Entity)"""
        super(__SortedIteratingSystem, self).entityAdded(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.SortedIteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__SortedIteratingSystem, self).addedToEngine(arg0)

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'.__wrap(super(core.EntitySystem, self).getEngine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.ashley.systems.SortedIteratingSystem 
 
 
# CLASS: com.badlogic.ashley.systems.IntervalIteratingSystem
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import com.badlogic.ashley.core.Family as __Family
__Family = __Family
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.ashley.systems.IntervalSystem as __IntervalSystem
__IntervalSystem = __IntervalSystem
import java.lang.String as __String
__String = __String
import com.badlogic.ashley.systems.IntervalIteratingSystem as __IntervalIteratingSystem
__IntervalIteratingSystem = __IntervalIteratingSystem
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
try:
    from pygdx.ashley import core
except ImportError:
    core = __import_once__("pygdx.ashley.core")

from builtins import int
 
class IntervalIteratingSystem(ABC, __IntervalSystem, IntervalSystem):
    """com.badlogic.ashley.systems.IntervalIteratingSystem"""
 
    @staticmethod
    def __wrap(java_value: __IntervalIteratingSystem) -> 'IntervalIteratingSystem':
        return IntervalIteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntervalIteratingSystem):
        """
        Dynamic initializer for IntervalIteratingSystem.
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
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IntervalSystem.update(float)"""
        super(__IntervalSystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__core.EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.IntervalIteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'.__wrap(super(IntervalIteratingSystem, self).getEntities())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IntervalIteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__IntervalIteratingSystem, self).addedToEngine(arg0)

    @overload
    def __init__(self, arg0: 'Family', arg1: float, arg2: int):
        """public com.badlogic.ashley.systems.IntervalIteratingSystem(com.badlogic.ashley.core.Family,float,int)"""
        val = __IntervalIteratingSystem(arg0, __float.valueOf(arg1), __int.valueOf(arg2))
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def getInterval(self) -> float:
        """public float com.badlogic.ashley.systems.IntervalSystem.getInterval()"""
        return float.__wrap(super(IntervalSystem, self).getInterval())

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(core.EntitySystem, self).checkProcessing())

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
    def __init__(self, arg0: 'Family', arg1: float):
        """public com.badlogic.ashley.systems.IntervalIteratingSystem(com.badlogic.ashley.core.Family,float)"""
        val = __IntervalIteratingSystem(arg0, __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.IntervalIteratingSystem.getFamily()"""
        return 'core.Family'.__wrap(super(IntervalIteratingSystem, self).getFamily())

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'.__wrap(super(core.EntitySystem, self).getEngine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__core.EntitySystem, self).removedFromEngine(arg0) 
 
 
# CLASS: com.badlogic.ashley.systems.IteratingSystem
from pyquantum_helper import import_once as __import_once__
import com.badlogic.ashley.utils.ImmutableArray as __ImmutableArray
__ImmutableArray = __ImmutableArray
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
import com.badlogic.ashley.systems.IteratingSystem as __IteratingSystem
__IteratingSystem = __IteratingSystem
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import com.badlogic.ashley.core.Family as __Family
__Family = __Family
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
try:
    from pygdx.ashley import core
except ImportError:
    core = __import_once__("pygdx.ashley.core")

from builtins import int
 
class IteratingSystem(ABC, ashley.__EntitySystem, core.EntitySystem):
    """com.badlogic.ashley.systems.IteratingSystem"""
 
    @staticmethod
    def __wrap(java_value: __IteratingSystem) -> 'IteratingSystem':
        return IteratingSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IteratingSystem):
        """
        Dynamic initializer for IteratingSystem.
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
    def getEntities(self) -> 'utils.ImmutableArray':
        """public com.badlogic.ashley.utils.ImmutableArray<com.badlogic.ashley.core.Entity> com.badlogic.ashley.systems.IteratingSystem.getEntities()"""
        return 'utils.ImmutableArray'.__wrap(super(IteratingSystem, self).getEntities())

    @overload
    def __init__(self, arg0: 'Family', arg1: int):
        """public com.badlogic.ashley.systems.IteratingSystem(com.badlogic.ashley.core.Family,int)"""
        val = __IteratingSystem(arg0, __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IteratingSystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__IteratingSystem, self).addedToEngine(arg0)

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__core.EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IteratingSystem.update(float)"""
        super(__IteratingSystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.systems.IteratingSystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__IteratingSystem, self).removedFromEngine(arg0)

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

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(core.EntitySystem, self).checkProcessing())

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
    def __init__(self, arg0: 'Family'):
        """public com.badlogic.ashley.systems.IteratingSystem(com.badlogic.ashley.core.Family)"""
        val = __IteratingSystem(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'.__wrap(super(core.EntitySystem, self).getEngine())

    @overload
    def getFamily(self) -> 'core.Family':
        """public com.badlogic.ashley.core.Family com.badlogic.ashley.systems.IteratingSystem.getFamily()"""
        return 'core.Family'.__wrap(super(IteratingSystem, self).getFamily())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.ashley.systems.IntervalSystem
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Boolean as __boolean
import java.lang.Object as __object
from builtins import type
from builtins import float
import com.badlogic.ashley.core.Engine as __Engine
__Engine = __Engine
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.ashley.systems.IntervalSystem as __IntervalSystem
__IntervalSystem = __IntervalSystem
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.ashley.core.EntitySystem as __EntitySystem
__EntitySystem = __EntitySystem
import java.lang.Integer as __int
from builtins import bool
try:
    from pygdx.ashley import core
except ImportError:
    core = __import_once__("pygdx.ashley.core")

from builtins import int
 
class IntervalSystem(ABC, ashley.__EntitySystem, core.EntitySystem):
    """com.badlogic.ashley.systems.IntervalSystem"""
 
    @staticmethod
    def __wrap(java_value: __IntervalSystem) -> 'IntervalSystem':
        return IntervalSystem(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntervalSystem):
        """
        Dynamic initializer for IntervalSystem.
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
    def update(self, arg0: float):
        """public void com.badlogic.ashley.systems.IntervalSystem.update(float)"""
        super(__IntervalSystem, self).update(__float.valueOf(arg0))

    @override
    @overload
    def setProcessing(self, arg0: bool):
        """public void com.badlogic.ashley.core.EntitySystem.setProcessing(boolean)"""
        super(__core.EntitySystem, self).setProcessing(__boolean.valueOf(arg0))

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: float, arg1: int):
        """public com.badlogic.ashley.systems.IntervalSystem(float,int)"""
        val = __IntervalSystem(__float.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def checkProcessing(self) -> bool:
        """public boolean com.badlogic.ashley.core.EntitySystem.checkProcessing()"""
        return bool.__wrap(super(core.EntitySystem, self).checkProcessing())

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
    def __init__(self, arg0: float):
        """public com.badlogic.ashley.systems.IntervalSystem(float)"""
        val = __IntervalSystem(__float.valueOf(arg0))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def addedToEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.addedToEngine(com.badlogic.ashley.core.Engine)"""
        super(__core.EntitySystem, self).addedToEngine(arg0)

    @overload
    def getInterval(self) -> float:
        """public float com.badlogic.ashley.systems.IntervalSystem.getInterval()"""
        return float.__wrap(super(IntervalSystem, self).getInterval())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getEngine(self) -> 'core.Engine':
        """public com.badlogic.ashley.core.Engine com.badlogic.ashley.core.EntitySystem.getEngine()"""
        return 'core.Engine'.__wrap(super(core.EntitySystem, self).getEngine())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def removedFromEngine(self, arg0: 'Engine'):
        """public void com.badlogic.ashley.core.EntitySystem.removedFromEngine(com.badlogic.ashley.core.Engine)"""
        super(__core.EntitySystem, self).removedFromEngine(arg0)