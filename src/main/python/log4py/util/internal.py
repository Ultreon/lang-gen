from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.io.ObjectOutputStream as ObjectOutputStream
import org.apache.logging.log4j.util.internal.SerializationUtil as _SerializationUtil
_SerializationUtil = _SerializationUtil
import java.io.ObjectInputStream as ObjectInputStream
import java.lang.Integer as _int
import java.io.Serializable as Serializable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SerializationUtil():
    """org.apache.logging.log4j.util.internal.SerializationUtil"""
 
    @staticmethod
    def _wrap(java_value: _SerializationUtil) -> 'SerializationUtil':
        return SerializationUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SerializationUtil):
        """
        Dynamic initializer for SerializationUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SerializationUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SerializationUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def writeWrappedObject(obj: 'Serializable', out: 'ObjectOutputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.writeWrappedObject(java.io.Serializable,java.io.ObjectOutputStream) throws java.io.IOException"""
        _SerializationUtil.writeWrappedObject(obj, out)

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
    def assertFiltered(stream: 'ObjectInputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.assertFiltered(java.io.ObjectInputStream)"""
        _SerializationUtil.assertFiltered(stream)

    @staticmethod
    @overload
    def readWrappedObject(in: 'ObjectInputStream') -> object:
        """public static java.lang.Object org.apache.logging.log4j.util.internal.SerializationUtil.readWrappedObject(java.io.ObjectInputStream) throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object._wrap(_SerializationUtil.readWrappedObject(in))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.logging.log4j.util.internal.SerializationUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.io.ObjectOutputStream as ObjectOutputStream
import org.apache.logging.log4j.util.internal.SerializationUtil as _SerializationUtil
_SerializationUtil = _SerializationUtil
import java.io.ObjectInputStream as ObjectInputStream
import java.lang.Integer as _int
import java.io.Serializable as Serializable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SerializationUtil():
    """org.apache.logging.log4j.util.internal.SerializationUtil"""
 
    @staticmethod
    def _wrap(java_value: _SerializationUtil) -> 'SerializationUtil':
        return SerializationUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SerializationUtil):
        """
        Dynamic initializer for SerializationUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SerializationUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SerializationUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def writeWrappedObject(obj: 'Serializable', out: 'ObjectOutputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.writeWrappedObject(java.io.Serializable,java.io.ObjectOutputStream) throws java.io.IOException"""
        _SerializationUtil.writeWrappedObject(obj, out)

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
    def assertFiltered(stream: 'ObjectInputStream'):
        """public static void org.apache.logging.log4j.util.internal.SerializationUtil.assertFiltered(java.io.ObjectInputStream)"""
        _SerializationUtil.assertFiltered(stream)

    @staticmethod
    @overload
    def readWrappedObject(in: 'ObjectInputStream') -> object:
        """public static java.lang.Object org.apache.logging.log4j.util.internal.SerializationUtil.readWrappedObject(java.io.ObjectInputStream) throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object._wrap(_SerializationUtil.readWrappedObject(in))

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.logging.log4j.util.internal.SerializationUtil