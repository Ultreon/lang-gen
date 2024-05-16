from __future__ import annotations
from overload import overload


 
from builtins import str
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntitySize():
    """dev.ultreon.quantum.entity.util.EntitySize"""
 
    @staticmethod
    def __wrap(java_value: __EntitySize) -> 'EntitySize':
        return EntitySize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntitySize):
        """
        Dynamic initializer for EntitySize.
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
    def height(self) -> float:
        """public float dev.ultreon.quantum.entity.util.EntitySize.height()"""
        return float.__wrap(super(EntitySize, self).height())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.entity.util.EntitySize(float,float)"""
        val = __EntitySize(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.util.EntitySize.hashCode()"""
        return int.__wrap(super(EntitySize, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.util.EntitySize.toString()"""
        return str.__wrap(super(EntitySize, self).toString())

    @overload
    def width(self) -> float:
        """public float dev.ultreon.quantum.entity.util.EntitySize.width()"""
        return float.__wrap(super(EntitySize, self).width())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.util.EntitySize.equals(java.lang.Object)"""
        return bool.__wrap(super(__EntitySize, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.entity.util.EntitySize
from builtins import str
import dev.ultreon.quantum.entity.util.EntitySize as __EntitySize
__EntitySize = __EntitySize
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.Float as __float
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class EntitySize():
    """dev.ultreon.quantum.entity.util.EntitySize"""
 
    @staticmethod
    def __wrap(java_value: __EntitySize) -> 'EntitySize':
        return EntitySize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __EntitySize):
        """
        Dynamic initializer for EntitySize.
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
    def height(self) -> float:
        """public float dev.ultreon.quantum.entity.util.EntitySize.height()"""
        return float.__wrap(super(EntitySize, self).height())

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.quantum.entity.util.EntitySize(float,float)"""
        val = __EntitySize(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.entity.util.EntitySize.hashCode()"""
        return int.__wrap(super(EntitySize, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.entity.util.EntitySize.toString()"""
        return str.__wrap(super(EntitySize, self).toString())

    @overload
    def width(self) -> float:
        """public float dev.ultreon.quantum.entity.util.EntitySize.width()"""
        return float.__wrap(super(EntitySize, self).width())

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.entity.util.EntitySize.equals(java.lang.Object)"""
        return bool.__wrap(super(__EntitySize, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: dev.ultreon.quantum.entity.util.EntitySize