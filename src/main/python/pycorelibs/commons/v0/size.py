from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.Dimension as Dimension
import dev.ultreon.libs.commons.v0.size.IntSize as __IntSize
__IntSize = __IntSize
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntSize():
    """dev.ultreon.libs.commons.v0.size.IntSize"""
 
    @staticmethod
    def __wrap(java_value: __IntSize) -> 'IntSize':
        return IntSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntSize):
        """
        Dynamic initializer for IntSize.
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
    def grown(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.grown(int)"""
        return 'IntSize'.__wrap(super(__IntSize, self).grown(__int.valueOf(arg0)))

    @overload
    def shrunk(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.shrunk(int)"""
        return 'IntSize'.__wrap(super(__IntSize, self).shrunk(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.hashCode()"""
        return int.__wrap(super(IntSize, self).hashCode())

    @overload
    def __init__(self, arg0: 'Dimension'):
        """public dev.ultreon.libs.commons.v0.size.IntSize(java.awt.Dimension)"""
        val = __IntSize(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.IntSize.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntSize, self).equals(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.size.IntSize(int,int)"""
        val = __IntSize(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.size.IntSize.toString()"""
        return str.__wrap(super(IntSize, self).toString())

    @overload
    def width(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.width()"""
        return int.__wrap(super(IntSize, self).width())

    @overload
    def height(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.height()"""
        return int.__wrap(super(IntSize, self).height())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.IntSize
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.awt.Dimension as Dimension
import dev.ultreon.libs.commons.v0.size.IntSize as __IntSize
__IntSize = __IntSize
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class IntSize():
    """dev.ultreon.libs.commons.v0.size.IntSize"""
 
    @staticmethod
    def __wrap(java_value: __IntSize) -> 'IntSize':
        return IntSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntSize):
        """
        Dynamic initializer for IntSize.
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
    def grown(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.grown(int)"""
        return 'IntSize'.__wrap(super(__IntSize, self).grown(__int.valueOf(arg0)))

    @overload
    def shrunk(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.shrunk(int)"""
        return 'IntSize'.__wrap(super(__IntSize, self).shrunk(__int.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.hashCode()"""
        return int.__wrap(super(IntSize, self).hashCode())

    @overload
    def __init__(self, arg0: 'Dimension'):
        """public dev.ultreon.libs.commons.v0.size.IntSize(java.awt.Dimension)"""
        val = __IntSize(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.IntSize.equals(java.lang.Object)"""
        return bool.__wrap(super(__IntSize, self).equals(arg0))

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
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.size.IntSize(int,int)"""
        val = __IntSize(__int.valueOf(arg0), __int.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.size.IntSize.toString()"""
        return str.__wrap(super(IntSize, self).toString())

    @overload
    def width(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.width()"""
        return int.__wrap(super(IntSize, self).width())

    @overload
    def height(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.height()"""
        return int.__wrap(super(IntSize, self).height())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.IntSize 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.DoubleSize
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import dev.ultreon.libs.commons.v0.size.DoubleSize as __DoubleSize
__DoubleSize = __DoubleSize
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DoubleSize():
    """dev.ultreon.libs.commons.v0.size.DoubleSize"""
 
    @staticmethod
    def __wrap(java_value: __DoubleSize) -> 'DoubleSize':
        return DoubleSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleSize):
        """
        Dynamic initializer for DoubleSize.
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
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def height(self) -> float:
        """public double dev.ultreon.libs.commons.v0.size.DoubleSize.height()"""
        return float.__wrap(super(DoubleSize, self).height())

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
    def width(self) -> float:
        """public double dev.ultreon.libs.commons.v0.size.DoubleSize.width()"""
        return float.__wrap(super(DoubleSize, self).width())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.size.DoubleSize.toString()"""
        return str.__wrap(super(DoubleSize, self).toString())

    @overload
    def shrunk(self, arg0: float) -> 'DoubleSize':
        """public dev.ultreon.libs.commons.v0.size.DoubleSize dev.ultreon.libs.commons.v0.size.DoubleSize.shrunk(double)"""
        return 'DoubleSize'.__wrap(super(__DoubleSize, self).shrunk(__double.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def grown(self, arg0: float) -> 'DoubleSize':
        """public dev.ultreon.libs.commons.v0.size.DoubleSize dev.ultreon.libs.commons.v0.size.DoubleSize.grown(double)"""
        return 'DoubleSize'.__wrap(super(__DoubleSize, self).grown(__double.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.size.DoubleSize(double,double)"""
        val = __DoubleSize(__double.valueOf(arg0), __double.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.DoubleSize.equals(java.lang.Object)"""
        return bool.__wrap(super(__DoubleSize, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.DoubleSize.hashCode()"""
        return int.__wrap(super(DoubleSize, self).hashCode()) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.FloatSize
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import float
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import dev.ultreon.libs.commons.v0.size.FloatSize as __FloatSize
__FloatSize = __FloatSize
from builtins import bool
from builtins import int
 
class FloatSize():
    """dev.ultreon.libs.commons.v0.size.FloatSize"""
 
    @staticmethod
    def __wrap(java_value: __FloatSize) -> 'FloatSize':
        return FloatSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatSize):
        """
        Dynamic initializer for FloatSize.
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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.FloatSize.equals(java.lang.Object)"""
        return bool.__wrap(super(__FloatSize, self).equals(arg0))

    @overload
    def grown(self, arg0: float) -> 'FloatSize':
        """public dev.ultreon.libs.commons.v0.size.FloatSize dev.ultreon.libs.commons.v0.size.FloatSize.grown(float)"""
        return 'FloatSize'.__wrap(super(__FloatSize, self).grown(__float.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.FloatSize.hashCode()"""
        return int.__wrap(super(FloatSize, self).hashCode())

    @overload
    def height(self) -> float:
        """public float dev.ultreon.libs.commons.v0.size.FloatSize.height()"""
        return float.__wrap(super(FloatSize, self).height())

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
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.size.FloatSize.toString()"""
        return str.__wrap(super(FloatSize, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def width(self) -> float:
        """public float dev.ultreon.libs.commons.v0.size.FloatSize.width()"""
        return float.__wrap(super(FloatSize, self).width())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def shrunk(self, arg0: float) -> 'FloatSize':
        """public dev.ultreon.libs.commons.v0.size.FloatSize dev.ultreon.libs.commons.v0.size.FloatSize.shrunk(float)"""
        return 'FloatSize'.__wrap(super(__FloatSize, self).shrunk(__float.valueOf(arg0)))

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.size.FloatSize(float,float)"""
        val = __FloatSize(__float.valueOf(arg0), __float.valueOf(arg1))
        self.__dict__ = val.__dict__
        self.__wrapper = val