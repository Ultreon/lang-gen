from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.size.IntSize as _IntSize
_IntSize = _IntSize
import java.lang.Integer as _int
import java.awt.Dimension as Dimension
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntSize():
    """dev.ultreon.libs.commons.v0.size.IntSize"""
 
    @staticmethod
    def _wrap(java_value: _IntSize) -> 'IntSize':
        return IntSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntSize):
        """
        Dynamic initializer for IntSize.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntSize__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntSize__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def grown(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.grown(int)"""
        return 'IntSize'._wrap(super(_IntSize, self).grown(_int.valueOf(arg0)))

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
        """public java.lang.String dev.ultreon.libs.commons.v0.size.IntSize.toString()"""
        return str._wrap(super(IntSize, self).toString())

    @overload
    def width(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.width()"""
        return int._wrap(super(IntSize, self).width())

    @overload
    def shrunk(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.shrunk(int)"""
        return 'IntSize'._wrap(super(_IntSize, self).shrunk(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.hashCode()"""
        return int._wrap(super(IntSize, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.IntSize.equals(java.lang.Object)"""
        return bool._wrap(super(_IntSize, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.size.IntSize(int,int)"""
        val = _IntSize(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Dimension'):
        """public dev.ultreon.libs.commons.v0.size.IntSize(java.awt.Dimension)"""
        val = _IntSize(arg0)
        self.__wrapper = val

    @overload
    def height(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.height()"""
        return int._wrap(super(IntSize, self).height())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.IntSize
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import dev.ultreon.libs.commons.v0.size.IntSize as _IntSize
_IntSize = _IntSize
import java.lang.Integer as _int
import java.awt.Dimension as Dimension
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class IntSize():
    """dev.ultreon.libs.commons.v0.size.IntSize"""
 
    @staticmethod
    def _wrap(java_value: _IntSize) -> 'IntSize':
        return IntSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntSize):
        """
        Dynamic initializer for IntSize.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntSize__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntSize__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def grown(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.grown(int)"""
        return 'IntSize'._wrap(super(_IntSize, self).grown(_int.valueOf(arg0)))

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
        """public java.lang.String dev.ultreon.libs.commons.v0.size.IntSize.toString()"""
        return str._wrap(super(IntSize, self).toString())

    @overload
    def width(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.width()"""
        return int._wrap(super(IntSize, self).width())

    @overload
    def shrunk(self, arg0: int) -> 'IntSize':
        """public dev.ultreon.libs.commons.v0.size.IntSize dev.ultreon.libs.commons.v0.size.IntSize.shrunk(int)"""
        return 'IntSize'._wrap(super(_IntSize, self).shrunk(_int.valueOf(arg0)))

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.hashCode()"""
        return int._wrap(super(IntSize, self).hashCode())

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
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.IntSize.equals(java.lang.Object)"""
        return bool._wrap(super(_IntSize, self).equals(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public dev.ultreon.libs.commons.v0.size.IntSize(int,int)"""
        val = _IntSize(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def __init__(self, arg0: 'Dimension'):
        """public dev.ultreon.libs.commons.v0.size.IntSize(java.awt.Dimension)"""
        val = _IntSize(arg0)
        self.__wrapper = val

    @overload
    def height(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.IntSize.height()"""
        return int._wrap(super(IntSize, self).height())

 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.IntSize 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.FloatSize
from builtins import str
import dev.ultreon.libs.commons.v0.size.FloatSize as _FloatSize
_FloatSize = _FloatSize
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FloatSize():
    """dev.ultreon.libs.commons.v0.size.FloatSize"""
 
    @staticmethod
    def _wrap(java_value: _FloatSize) -> 'FloatSize':
        return FloatSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatSize):
        """
        Dynamic initializer for FloatSize.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatSize__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatSize__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.FloatSize.hashCode()"""
        return int._wrap(super(FloatSize, self).hashCode())

    @overload
    def height(self) -> float:
        """public float dev.ultreon.libs.commons.v0.size.FloatSize.height()"""
        return float._wrap(super(FloatSize, self).height())

    @overload
    def shrunk(self, arg0: float) -> 'FloatSize':
        """public dev.ultreon.libs.commons.v0.size.FloatSize dev.ultreon.libs.commons.v0.size.FloatSize.shrunk(float)"""
        return 'FloatSize'._wrap(super(_FloatSize, self).shrunk(_float.valueOf(arg0)))

    @overload
    def width(self) -> float:
        """public float dev.ultreon.libs.commons.v0.size.FloatSize.width()"""
        return float._wrap(super(FloatSize, self).width())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.size.FloatSize(float,float)"""
        val = _FloatSize(_float.valueOf(arg0), _float.valueOf(arg1))
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.size.FloatSize.toString()"""
        return str._wrap(super(FloatSize, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.FloatSize.equals(java.lang.Object)"""
        return bool._wrap(super(_FloatSize, self).equals(arg0))

    @overload
    def grown(self, arg0: float) -> 'FloatSize':
        """public dev.ultreon.libs.commons.v0.size.FloatSize dev.ultreon.libs.commons.v0.size.FloatSize.grown(float)"""
        return 'FloatSize'._wrap(super(_FloatSize, self).grown(_float.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.commons.v0.size.DoubleSize
import dev.ultreon.libs.commons.v0.size.DoubleSize as _DoubleSize
_DoubleSize = _DoubleSize
from builtins import str
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DoubleSize():
    """dev.ultreon.libs.commons.v0.size.DoubleSize"""
 
    @staticmethod
    def _wrap(java_value: _DoubleSize) -> 'DoubleSize':
        return DoubleSize(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleSize):
        """
        Dynamic initializer for DoubleSize.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleSize__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleSize__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def height(self) -> float:
        """public double dev.ultreon.libs.commons.v0.size.DoubleSize.height()"""
        return float._wrap(super(DoubleSize, self).height())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.libs.commons.v0.size.DoubleSize.toString()"""
        return str._wrap(super(DoubleSize, self).toString())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, arg0: float, arg1: float):
        """public dev.ultreon.libs.commons.v0.size.DoubleSize(double,double)"""
        val = _DoubleSize(_double.valueOf(arg0), _double.valueOf(arg1))
        self.__wrapper = val

    @overload
    def shrunk(self, arg0: float) -> 'DoubleSize':
        """public dev.ultreon.libs.commons.v0.size.DoubleSize dev.ultreon.libs.commons.v0.size.DoubleSize.shrunk(double)"""
        return 'DoubleSize'._wrap(super(_DoubleSize, self).shrunk(_double.valueOf(arg0)))

    @overload
    def grown(self, arg0: float) -> 'DoubleSize':
        """public dev.ultreon.libs.commons.v0.size.DoubleSize dev.ultreon.libs.commons.v0.size.DoubleSize.grown(double)"""
        return 'DoubleSize'._wrap(super(_DoubleSize, self).grown(_double.valueOf(arg0)))

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
    def hashCode(self) -> int:
        """public int dev.ultreon.libs.commons.v0.size.DoubleSize.hashCode()"""
        return int._wrap(super(DoubleSize, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.libs.commons.v0.size.DoubleSize.equals(java.lang.Object)"""
        return bool._wrap(super(_DoubleSize, self).equals(arg0))

    @overload
    def width(self) -> float:
        """public double dev.ultreon.libs.commons.v0.size.DoubleSize.width()"""
        return float._wrap(super(DoubleSize, self).width())