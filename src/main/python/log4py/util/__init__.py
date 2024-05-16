from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.util.ProcessIdUtil as _ProcessIdUtil
_ProcessIdUtil = _ProcessIdUtil
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProcessIdUtil():
    """org.apache.logging.log4j.util.ProcessIdUtil"""
 
    @staticmethod
    def _wrap(java_value: _ProcessIdUtil) -> 'ProcessIdUtil':
        return ProcessIdUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProcessIdUtil):
        """
        Dynamic initializer for ProcessIdUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProcessIdUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProcessIdUtil__wrapper":
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

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.ProcessIdUtil()"""
        val = _ProcessIdUtil()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.ProcessIdUtil()"""
        val = _ProcessIdUtil()
        self.__wrapper = val

    @staticmethod
    @overload
    def getProcessId() -> str:
        """public static java.lang.String org.apache.logging.log4j.util.ProcessIdUtil.getProcessId()"""
        return str._wrap(_ProcessIdUtil.getProcessId())

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

 
 
 
# CLASS: org.apache.logging.log4j.util.ProcessIdUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.util.ProcessIdUtil as _ProcessIdUtil
_ProcessIdUtil = _ProcessIdUtil
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProcessIdUtil():
    """org.apache.logging.log4j.util.ProcessIdUtil"""
 
    @staticmethod
    def _wrap(java_value: _ProcessIdUtil) -> 'ProcessIdUtil':
        return ProcessIdUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProcessIdUtil):
        """
        Dynamic initializer for ProcessIdUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProcessIdUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProcessIdUtil__wrapper":
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

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.ProcessIdUtil()"""
        val = _ProcessIdUtil()
        self.__wrapper = val

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

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.ProcessIdUtil()"""
        val = _ProcessIdUtil()
        self.__wrapper = val

    @staticmethod
    @overload
    def getProcessId() -> str:
        """public static java.lang.String org.apache.logging.log4j.util.ProcessIdUtil.getProcessId()"""
        return str._wrap(_ProcessIdUtil.getProcessId())

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

 
 
 
# CLASS: org.apache.logging.log4j.util.ProcessIdUtil 
 
 
# CLASS: org.apache.logging.log4j.util.LazyBoolean
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.function.BooleanSupplier as BooleanSupplier
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.util.LazyBoolean as _LazyBoolean
_LazyBoolean = _LazyBoolean
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LazyBoolean():
    """org.apache.logging.log4j.util.LazyBoolean"""
 
    @staticmethod
    def _wrap(java_value: _LazyBoolean) -> 'LazyBoolean':
        return LazyBoolean(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LazyBoolean):
        """
        Dynamic initializer for LazyBoolean.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LazyBoolean__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LazyBoolean__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getAsBoolean(self) -> bool:
        """public boolean org.apache.logging.log4j.util.LazyBoolean.getAsBoolean()"""
        return bool._wrap(super(LazyBoolean, self).getAsBoolean())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setAsBoolean(self, b: bool):
        """public void org.apache.logging.log4j.util.LazyBoolean.setAsBoolean(boolean)"""
        super(_LazyBoolean, self).setAsBoolean(_boolean.valueOf(b))

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
    def reset(self):
        """public void org.apache.logging.log4j.util.LazyBoolean.reset()"""
        super(LazyBoolean, self).reset()

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, supplier: 'BooleanSupplier'):
        """public org.apache.logging.log4j.util.LazyBoolean(java.util.function.BooleanSupplier)"""
        val = _LazyBoolean(supplier)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.Base64Util
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.logging.log4j.util.Base64Util as _Base64Util
_Base64Util = _Base64Util
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Base64Util():
    """org.apache.logging.log4j.util.Base64Util"""
 
    @staticmethod
    def _wrap(java_value: _Base64Util) -> 'Base64Util':
        return Base64Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Base64Util):
        """
        Dynamic initializer for Base64Util.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Base64Util__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Base64Util__wrapper":
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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def encode(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Base64Util.encode(java.lang.String)"""
        return str._wrap(_Base64Util.encode(str))

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
 
 
# CLASS: org.apache.logging.log4j.util.BiConsumer
import org.apache.logging.log4j.util.BiConsumer as _BiConsumer
_BiConsumer = _BiConsumer
from abc import abstractmethod, ABC
 
class BiConsumer():
    """org.apache.logging.log4j.util.BiConsumer"""
 
    @staticmethod
    def _wrap(java_value: _BiConsumer) -> 'BiConsumer':
        return BiConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiConsumer):
        """
        Dynamic initializer for BiConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, k: object, v: object):
        """public abstract void org.apache.logging.log4j.util.BiConsumer.accept(K,V)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.ServiceLoaderUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.logging.log4j.util.ServiceLoaderUtil as _ServiceLoaderUtil
_ServiceLoaderUtil = _ServiceLoaderUtil
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Long as _long
import java.lang.invoke.MethodHandles.Lookup as Lookup
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ServiceLoaderUtil():
    """org.apache.logging.log4j.util.ServiceLoaderUtil"""
 
    @staticmethod
    def _wrap(java_value: _ServiceLoaderUtil) -> 'ServiceLoaderUtil':
        return ServiceLoaderUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ServiceLoaderUtil):
        """
        Dynamic initializer for ServiceLoaderUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ServiceLoaderUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ServiceLoaderUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup') -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.ServiceLoaderUtil.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup)"""
        return Stream._wrap(_ServiceLoaderUtil.loadServices(serviceType, lookup))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup', useTccl: bool) -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.ServiceLoaderUtil.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup,boolean)"""
        return Stream._wrap(_ServiceLoaderUtil.loadServices(serviceType, lookup, _boolean.valueOf(useTccl)))

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
 
 
# CLASS: org.apache.logging.log4j.util.PropertiesUtil
import java.lang.Double as _double
import java.lang.Long as Long
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import org.apache.logging.log4j.util.PropertiesUtil as _PropertiesUtil
_PropertiesUtil = _PropertiesUtil
import java.util.Properties as _Properties
_Properties = _Properties
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.time.Duration as _Duration
_Duration = _Duration
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.time.Duration as Duration
import java.lang.String as _String
_String = _String
import java.nio.charset.Charset as _Charset
_Charset = _Charset
import java.lang.Integer as _int
import java.lang.Integer as Integer
import java.util.Properties as Properties
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PropertiesUtil():
    """org.apache.logging.log4j.util.PropertiesUtil"""
 
    @staticmethod
    def _wrap(java_value: _PropertiesUtil) -> 'PropertiesUtil':
        return PropertiesUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PropertiesUtil):
        """
        Dynamic initializer for PropertiesUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PropertiesUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PropertiesUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getBooleanProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Boolean':
        """public java.lang.Boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.Boolean>)"""
        return 'Boolean'._wrap(super(_PropertiesUtil, self).getBooleanProperty(prefixes, key, supplier))

    @staticmethod
    @overload
    def partitionOnCommonPrefixes(properties: 'Properties', includeBaseKey: bool) -> 'Map':
        """public static java.util.Map<java.lang.String, java.util.Properties> org.apache.logging.log4j.util.PropertiesUtil.partitionOnCommonPrefixes(java.util.Properties,boolean)"""
        return Map._wrap(_PropertiesUtil.partitionOnCommonPrefixes(properties, _boolean.valueOf(includeBaseKey)))

    @overload
    def getCharsetProperty(self, name: str, defaultValue: 'Charset') -> 'Charset':
        """public java.nio.charset.Charset org.apache.logging.log4j.util.PropertiesUtil.getCharsetProperty(java.lang.String,java.nio.charset.Charset)"""
        return 'Charset'._wrap(super(_PropertiesUtil, self).getCharsetProperty(name, defaultValue))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDoubleProperty(self, name: str, defaultValue: float) -> float:
        """public double org.apache.logging.log4j.util.PropertiesUtil.getDoubleProperty(java.lang.String,double)"""
        return float._wrap(super(_PropertiesUtil, self).getDoubleProperty(name, _double.valueOf(defaultValue)))

    @overload
    def hasProperty(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.hasProperty(java.lang.String)"""
        return bool._wrap(super(_PropertiesUtil, self).hasProperty(name))

    @overload
    def getStringProperty(self, name: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesUtil.getStringProperty(java.lang.String)"""
        return str._wrap(super(_PropertiesUtil, self).getStringProperty(name))

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
    def getBooleanProperty(self, name: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String)"""
        return bool._wrap(super(_PropertiesUtil, self).getBooleanProperty(name))

    @overload
    def getLongProperty(self, name: str, defaultValue: int) -> int:
        """public long org.apache.logging.log4j.util.PropertiesUtil.getLongProperty(java.lang.String,long)"""
        return int._wrap(super(_PropertiesUtil, self).getLongProperty(name, _long.valueOf(defaultValue)))

    @overload
    def isOsWindows(self) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.isOsWindows()"""
        return bool._wrap(super(PropertiesUtil, self).isOsWindows())

    @staticmethod
    @overload
    def partitionOnCommonPrefixes(properties: 'Properties') -> 'Map':
        """public static java.util.Map<java.lang.String, java.util.Properties> org.apache.logging.log4j.util.PropertiesUtil.partitionOnCommonPrefixes(java.util.Properties)"""
        return Map._wrap(_PropertiesUtil.partitionOnCommonPrefixes(properties))

    @overload
    def getLongProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Long':
        """public java.lang.Long org.apache.logging.log4j.util.PropertiesUtil.getLongProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.Long>)"""
        return _transform(super(_PropertiesUtil, self).getLongProperty(prefixes, key, supplier)).'Long'Value()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def getProperties() -> 'PropertiesUtil':
        """public static org.apache.logging.log4j.util.PropertiesUtil org.apache.logging.log4j.util.PropertiesUtil.getProperties()"""
        return PropertiesUtil._wrap(_PropertiesUtil.getProperties())

    @overload
    def __init__(self, props: 'Properties'):
        """public org.apache.logging.log4j.util.PropertiesUtil(java.util.Properties)"""
        val = _PropertiesUtil(props)
        self.__wrapper = val

    @overload
    def getBooleanProperty(self, name: str, defaultValueIfAbsent: bool, defaultValueIfPresent: bool) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String,boolean,boolean)"""
        return bool._wrap(super(_PropertiesUtil, self).getBooleanProperty(name, _boolean.valueOf(defaultValueIfAbsent), _boolean.valueOf(defaultValueIfPresent)))

    @overload
    def addPropertySource(self, propertySource: 'PropertySource'):
        """public void org.apache.logging.log4j.util.PropertiesUtil.addPropertySource(org.apache.logging.log4j.util.PropertySource)"""
        super(_PropertiesUtil, self).addPropertySource(propertySource)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, propertiesFileName: str):
        """public org.apache.logging.log4j.util.PropertiesUtil(java.lang.String)"""
        val = _PropertiesUtil(propertiesFileName)
        self.__wrapper = val

    @overload
    def getStringProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesUtil.getStringProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.String>)"""
        return str._wrap(super(_PropertiesUtil, self).getStringProperty(prefixes, key, supplier))

    @staticmethod
    @overload
    def extractSubset(properties: 'Properties', prefix: str) -> 'Properties':
        """public static java.util.Properties org.apache.logging.log4j.util.PropertiesUtil.extractSubset(java.util.Properties,java.lang.String)"""
        return Properties._wrap(_PropertiesUtil.extractSubset(properties, prefix))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getDurationProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Duration':
        """public java.time.Duration org.apache.logging.log4j.util.PropertiesUtil.getDurationProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.time.Duration>)"""
        return 'Duration'._wrap(super(_PropertiesUtil, self).getDurationProperty(prefixes, key, supplier))

    @overload
    def getIntegerProperty(self, prefixes: 'String', key: str, supplier: 'Supplier') -> 'Integer':
        """public java.lang.Integer org.apache.logging.log4j.util.PropertiesUtil.getIntegerProperty(java.lang.String[],java.lang.String,org.apache.logging.log4j.util.Supplier<java.lang.Integer>)"""
        return _transform(super(_PropertiesUtil, self).getIntegerProperty(prefixes, key, supplier)).'Integer'Value()

    @overload
    def getIntegerProperty(self, name: str, defaultValue: int) -> int:
        """public int org.apache.logging.log4j.util.PropertiesUtil.getIntegerProperty(java.lang.String,int)"""
        return int._wrap(super(_PropertiesUtil, self).getIntegerProperty(name, _int.valueOf(defaultValue)))

    @overload
    def getBooleanProperty(self, name: str, defaultValue: bool) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesUtil.getBooleanProperty(java.lang.String,boolean)"""
        return bool._wrap(super(_PropertiesUtil, self).getBooleanProperty(name, _boolean.valueOf(defaultValue)))

    @staticmethod
    @overload
    def getSystemProperties() -> 'Properties':
        """public static java.util.Properties org.apache.logging.log4j.util.PropertiesUtil.getSystemProperties()"""
        return Properties._wrap(_PropertiesUtil.getSystemProperties())

    @overload
    def reload(self):
        """public void org.apache.logging.log4j.util.PropertiesUtil.reload()"""
        super(PropertiesUtil, self).reload()

    @overload
    def getCharsetProperty(self, name: str) -> 'Charset':
        """public java.nio.charset.Charset org.apache.logging.log4j.util.PropertiesUtil.getCharsetProperty(java.lang.String)"""
        return 'Charset'._wrap(super(_PropertiesUtil, self).getCharsetProperty(name))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getDurationProperty(self, name: str, defaultValue: 'Duration') -> 'Duration':
        """public java.time.Duration org.apache.logging.log4j.util.PropertiesUtil.getDurationProperty(java.lang.String,java.time.Duration)"""
        return 'Duration'._wrap(super(_PropertiesUtil, self).getDurationProperty(name, defaultValue))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getStringProperty(self, name: str, defaultValue: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesUtil.getStringProperty(java.lang.String,java.lang.String)"""
        return str._wrap(super(_PropertiesUtil, self).getStringProperty(name, defaultValue))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.Strings
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import org.apache.logging.log4j.util.Strings as _Strings
_Strings = _Strings
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Strings():
    """org.apache.logging.log4j.util.Strings"""
 
    @staticmethod
    def _wrap(java_value: _Strings) -> 'Strings':
        return Strings(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Strings):
        """
        Dynamic initializer for Strings.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Strings__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Strings__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isNotBlank(s: str) -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isNotBlank(java.lang.String)"""
        return bool._wrap(_Strings.isNotBlank(s))

    @staticmethod
    @overload
    def isBlank(s: str) -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isBlank(java.lang.String)"""
        return bool._wrap(_Strings.isBlank(s))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def repeat(str: str, count: int) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.repeat(java.lang.String,int)"""
        return str._wrap(_Strings.repeat(str, _int.valueOf(count)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def isEmpty(cs: 'CharSequence') -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isEmpty(java.lang.CharSequence)"""
        return bool._wrap(_Strings.isEmpty(cs))

    @staticmethod
    @overload
    def join(iterable: 'Iterable', separator: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.join(java.lang.Iterable<?>,char)"""
        return str._wrap(_Strings.join(iterable, _char.valueOf(separator)))

    @staticmethod
    @overload
    def isNotEmpty(cs: 'CharSequence') -> bool:
        """public static boolean org.apache.logging.log4j.util.Strings.isNotEmpty(java.lang.CharSequence)"""
        return bool._wrap(_Strings.isNotEmpty(cs))

    @staticmethod
    @overload
    def join(iterator: 'Iterator', separator: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.join(java.util.Iterator<?>,char)"""
        return str._wrap(_Strings.join(iterator, _char.valueOf(separator)))

    @staticmethod
    @overload
    def toRootUpperCase(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.toRootUpperCase(java.lang.String)"""
        return str._wrap(_Strings.toRootUpperCase(str))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def quote(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.quote(java.lang.String)"""
        return str._wrap(_Strings.quote(str))

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
    def dquote(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.dquote(java.lang.String)"""
        return str._wrap(_Strings.dquote(str))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def splitList(string: str) -> List[str]:
        """public static java.lang.String[] org.apache.logging.log4j.util.Strings.splitList(java.lang.String)"""
        return List[str]._wrap(_Strings.splitList(string))

    @staticmethod
    @overload
    def concat(str1: str, str2: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.concat(java.lang.String,java.lang.String)"""
        return str._wrap(_Strings.concat(str1, str2))

    @staticmethod
    @overload
    def trimToNull(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.trimToNull(java.lang.String)"""
        return str._wrap(_Strings.trimToNull(str))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def left(str: str, len: int) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.left(java.lang.String,int)"""
        return str._wrap(_Strings.left(str, _int.valueOf(len)))

    @staticmethod
    @overload
    def toRootLowerCase(str: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.Strings.toRootLowerCase(java.lang.String)"""
        return str._wrap(_Strings.toRootLowerCase(str))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.InternalException
from builtins import str
import org.apache.logging.log4j.util.InternalException as _InternalException
_InternalException = _InternalException
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InternalException():
    """org.apache.logging.log4j.util.InternalException"""
 
    @staticmethod
    def _wrap(java_value: _InternalException) -> 'InternalException':
        return InternalException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InternalException):
        """
        Dynamic initializer for InternalException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InternalException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InternalException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, message: str):
        """public org.apache.logging.log4j.util.InternalException(java.lang.String)"""
        val = _InternalException(message)
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, message: str, cause: 'Throwable'):
        """public org.apache.logging.log4j.util.InternalException(java.lang.String,java.lang.Throwable)"""
        val = _InternalException(message, cause)
        self.__wrapper = val

    @overload
    def __init__(self, cause: 'Throwable'):
        """public org.apache.logging.log4j.util.InternalException(java.lang.Throwable)"""
        val = _InternalException(cause)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.StackLocator
import java.util.function.Predicate as Predicate
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Deque as Deque
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import java.lang.String as _string
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
import org.apache.logging.log4j.util.StackLocator as _StackLocator
_StackLocator = _StackLocator
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class StackLocator():
    """org.apache.logging.log4j.util.StackLocator"""
 
    @staticmethod
    def _wrap(java_value: _StackLocator) -> 'StackLocator':
        return StackLocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StackLocator):
        """
        Dynamic initializer for StackLocator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StackLocator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StackLocator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getCallerClass(self, anchor: 'Class') -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.Class<?>)"""
        return 'type.Class'._wrap(super(_StackLocator, self).getCallerClass(anchor))

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
    def getCallerClass(self, depth: int) -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(int)"""
        return 'type.Class'._wrap(super(_StackLocator, self).getCallerClass(_int.valueOf(depth)))

    @overload
    def getCallerClass(self, sentinelClass: 'Class', callerPredicate: 'Predicate') -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.Class<?>,java.util.function.Predicate<java.lang.Class<?>>)"""
        return 'type.Class'._wrap(super(_StackLocator, self).getCallerClass(sentinelClass, callerPredicate))

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

    @staticmethod
    @overload
    def getInstance() -> 'StackLocator':
        """public static org.apache.logging.log4j.util.StackLocator org.apache.logging.log4j.util.StackLocator.getInstance()"""
        return StackLocator._wrap(_StackLocator.getInstance())

    @overload
    def getCallerClass(self, fqcn: str, pkg: str) -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.String,java.lang.String)"""
        return 'type.Class'._wrap(super(_StackLocator, self).getCallerClass(fqcn, pkg))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getCurrentStackTrace(self) -> 'Deque':
        """public java.util.Deque<java.lang.Class<?>> org.apache.logging.log4j.util.StackLocator.getCurrentStackTrace()"""
        return 'Deque'._wrap(super(StackLocator, self).getCurrentStackTrace())

    @overload
    def getCallerClass(self, fqcn: str) -> 'type.Class':
        """public java.lang.Class<?> org.apache.logging.log4j.util.StackLocator.getCallerClass(java.lang.String)"""
        return 'type.Class'._wrap(super(_StackLocator, self).getCallerClass(fqcn))

    @overload
    def calcLocation(self, fqcnOfLogger: str) -> 'StackTraceElement':
        """public java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocator.calcLocation(java.lang.String)"""
        return 'StackTraceElement'._wrap(super(_StackLocator, self).calcLocation(fqcnOfLogger))

    @overload
    def getStackTraceElement(self, depth: int) -> 'StackTraceElement':
        """public java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocator.getStackTraceElement(int)"""
        return 'StackTraceElement'._wrap(super(_StackLocator, self).getStackTraceElement(_int.valueOf(depth)))

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
 
 
# CLASS: org.apache.logging.log4j.util.ReadOnlyStringMap
import org.apache.logging.log4j.util.ReadOnlyStringMap as _ReadOnlyStringMap
_ReadOnlyStringMap = _ReadOnlyStringMap
from abc import abstractmethod, ABC
 
class ReadOnlyStringMap():
    """org.apache.logging.log4j.util.ReadOnlyStringMap"""
 
    @staticmethod
    def _wrap(java_value: _ReadOnlyStringMap) -> 'ReadOnlyStringMap':
        return ReadOnlyStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReadOnlyStringMap):
        """
        Dynamic initializer for ReadOnlyStringMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReadOnlyStringMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReadOnlyStringMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.SortedArrayStringMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.logging.log4j.util.SortedArrayStringMap as _SortedArrayStringMap
_SortedArrayStringMap = _SortedArrayStringMap
import java.lang.Object as _object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import java.lang.Integer as _int
from builtins import bool
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SortedArrayStringMap():
    """org.apache.logging.log4j.util.SortedArrayStringMap"""
 
    @staticmethod
    def _wrap(java_value: _SortedArrayStringMap) -> 'SortedArrayStringMap':
        return SortedArrayStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedArrayStringMap):
        """
        Dynamic initializer for SortedArrayStringMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedArrayStringMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedArrayStringMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def clear(self):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.clear()"""
        super(SortedArrayStringMap, self).clear()

    @override
    @overload
    def putValue(self, key: str, value: object):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.putValue(java.lang.String,java.lang.Object)"""
        super(_SortedArrayStringMap, self).putValue(key, value)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.util.SortedArrayStringMap.toString()"""
        return str._wrap(super(SortedArrayStringMap, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.SortedArrayStringMap()"""
        val = _SortedArrayStringMap()
        self.__wrapper = val

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.equals(java.lang.Object)"""
        return bool._wrap(super(_SortedArrayStringMap, self).equals(obj))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.util.SortedArrayStringMap.hashCode()"""
        return int._wrap(super(SortedArrayStringMap, self).hashCode())

    @overload
    def __init__(self, map: 'Map'):
        """public org.apache.logging.log4j.util.SortedArrayStringMap(java.util.Map<java.lang.String, ?>)"""
        val = _SortedArrayStringMap(map)
        self.__wrapper = val

    @override
    @overload
    def toMap(self) -> 'Map':
        """public java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.SortedArrayStringMap.toMap()"""
        return 'Map'._wrap(super(SortedArrayStringMap, self).toMap())

    @override
    @overload
    def remove(self, key: str):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.remove(java.lang.String)"""
        super(_SortedArrayStringMap, self).remove(key)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int org.apache.logging.log4j.util.SortedArrayStringMap.size()"""
        return int._wrap(super(SortedArrayStringMap, self).size())

    @override
    @overload
    def putAll(self, source: 'ReadOnlyStringMap'):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.putAll(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        super(_SortedArrayStringMap, self).putAll(source)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getValue(self, key: str) -> object:
        """public <V> V org.apache.logging.log4j.util.SortedArrayStringMap.getValue(java.lang.String)"""
        return object._wrap(super(_SortedArrayStringMap, self).getValue(key))

    @overload
    def getValueAt(self, index: int) -> object:
        """public <V> V org.apache.logging.log4j.util.SortedArrayStringMap.getValueAt(int)"""
        return object._wrap(super(_SortedArrayStringMap, self).getValueAt(_int.valueOf(index)))

    @overload
    def __init__(self, initialCapacity: int):
        """public org.apache.logging.log4j.util.SortedArrayStringMap(int)"""
        val = _SortedArrayStringMap(_int.valueOf(initialCapacity))
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.isEmpty()"""
        return bool._wrap(super(SortedArrayStringMap, self).isEmpty())

    @overload
    def indexOfKey(self, key: str) -> int:
        """public int org.apache.logging.log4j.util.SortedArrayStringMap.indexOfKey(java.lang.String)"""
        return int._wrap(super(_SortedArrayStringMap, self).indexOfKey(key))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.SortedArrayStringMap()"""
        val = _SortedArrayStringMap()
        self.__wrapper = val

    @overload
    def __init__(self, other: 'ReadOnlyStringMap'):
        """public org.apache.logging.log4j.util.SortedArrayStringMap(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        val = _SortedArrayStringMap(other)
        self.__wrapper = val

    @override
    @overload
    def forEach(self, action: 'TriConsumer', state: object):
        """public <V,T> void org.apache.logging.log4j.util.SortedArrayStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, T>,T)"""
        super(_SortedArrayStringMap, self).forEach(action, state)

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public <V> void org.apache.logging.log4j.util.SortedArrayStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        super(_SortedArrayStringMap, self).forEach(action)

    @override
    @overload
    def isFrozen(self) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.isFrozen()"""
        return bool._wrap(super(SortedArrayStringMap, self).isFrozen())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def containsKey(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.SortedArrayStringMap.containsKey(java.lang.String)"""
        return bool._wrap(super(_SortedArrayStringMap, self).containsKey(key))

    @overload
    def getKeyAt(self, index: int) -> str:
        """public java.lang.String org.apache.logging.log4j.util.SortedArrayStringMap.getKeyAt(int)"""
        return str._wrap(super(_SortedArrayStringMap, self).getKeyAt(_int.valueOf(index)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def freeze(self):
        """public void org.apache.logging.log4j.util.SortedArrayStringMap.freeze()"""
        super(SortedArrayStringMap, self).freeze() 
 
 
# CLASS: org.apache.logging.log4j.util.Timer
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.util.Timer as _Timer_Status
_Status = _Timer_Status.Status
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import org.apache.logging.log4j.util.Timer as _Timer
_Timer = _Timer
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Timer():
    """org.apache.logging.log4j.util.Timer"""
 
    @staticmethod
    def _wrap(java_value: _Timer) -> 'Timer':
        return Timer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Timer):
        """
        Dynamic initializer for Timer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Timer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Timer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def formatTo(self, buffer: 'StringBuilder'):
        """public void org.apache.logging.log4j.util.Timer.formatTo(java.lang.StringBuilder)"""
        super(_Timer, self).formatTo(buffer)

    @overload
    def equals(self, o: object) -> bool:
        """public boolean org.apache.logging.log4j.util.Timer.equals(java.lang.Object)"""
        return bool._wrap(super(_Timer, self).equals(o))

    @overload
    def start(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.start()"""
        super(Timer, self).start()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def startOrResume(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.startOrResume()"""
        super(Timer, self).startOrResume()

    @overload
    def __init__(self, name: str, iterations: int):
        """public org.apache.logging.log4j.util.Timer(java.lang.String,int)"""
        val = _Timer(name, _int.valueOf(iterations))
        self.__wrapper = val

    @overload
    def pause(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.pause()"""
        super(Timer, self).pause()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, name: str):
        """public org.apache.logging.log4j.util.Timer(java.lang.String)"""
        val = _Timer(name)
        self.__wrapper = val

    @overload
    def getName(self) -> str:
        """public java.lang.String org.apache.logging.log4j.util.Timer.getName()"""
        return str._wrap(super(Timer, self).getName())

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
    def getStatus(self) -> 'Status':
        """public org.apache.logging.log4j.util.Timer$Status org.apache.logging.log4j.util.Timer.getStatus()"""
        return 'Status'._wrap(super(Timer, self).getStatus())

    @overload
    def stop(self) -> str:
        """public synchronized java.lang.String org.apache.logging.log4j.util.Timer.stop()"""
        return str._wrap(super(Timer, self).stop())

    @overload
    def resume(self):
        """public synchronized void org.apache.logging.log4j.util.Timer.resume()"""
        super(Timer, self).resume()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.logging.log4j.util.Timer.toString()"""
        return str._wrap(super(Timer, self).toString())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getElapsedNanoTime(self) -> int:
        """public long org.apache.logging.log4j.util.Timer.getElapsedNanoTime()"""
        return int._wrap(super(Timer, self).getElapsedNanoTime())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.logging.log4j.util.Timer.hashCode()"""
        return int._wrap(super(Timer, self).hashCode())

    @overload
    def getElapsedTime(self) -> int:
        """public long org.apache.logging.log4j.util.Timer.getElapsedTime()"""
        return int._wrap(super(Timer, self).getElapsedTime()) 
 
 
# CLASS: org.apache.logging.log4j.util.TriConsumer
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.TriConsumer as _TriConsumer
_TriConsumer = _TriConsumer
 
class TriConsumer():
    """org.apache.logging.log4j.util.TriConsumer"""
 
    @staticmethod
    def _wrap(java_value: _TriConsumer) -> 'TriConsumer':
        return TriConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriConsumer):
        """
        Dynamic initializer for TriConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, k: object, v: object, s: object):
        """public abstract void org.apache.logging.log4j.util.TriConsumer.accept(K,V,S)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.FilteredObjectInputStream
import java.io.ObjectInputFilter as _ObjectInputFilter
_ObjectInputFilter = _ObjectInputFilter
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Collection as Collection
import java.io.ObjectInputStream as _ObjectInputStream
_ObjectInputStream = _ObjectInputStream
import java.io.OutputStream as OutputStream
import java.io.ObjectInputValidation as ObjectInputValidation
import java.io.ObjectInputStream.GetField as GetField
import java.io.ObjectInputFilter as ObjectInputFilter
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import org.apache.logging.log4j.util.FilteredObjectInputStream as _FilteredObjectInputStream
_FilteredObjectInputStream = _FilteredObjectInputStream
import java.io.InputStream as _InputStream
_InputStream = _InputStream
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.io.InputStream as InputStream
import java.io.ObjectInputStream as _ObjectInputStream_GetField
_GetField = _ObjectInputStream_GetField.GetField
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FilteredObjectInputStream():
    """org.apache.logging.log4j.util.FilteredObjectInputStream"""
 
    @staticmethod
    def _wrap(java_value: _FilteredObjectInputStream) -> 'FilteredObjectInputStream':
        return FilteredObjectInputStream(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FilteredObjectInputStream):
        """
        Dynamic initializer for FilteredObjectInputStream.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FilteredObjectInputStream__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FilteredObjectInputStream__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def readLine(self) -> str:
        """public java.lang.String java.io.ObjectInputStream.readLine() throws java.io.IOException"""
        return str._wrap(super(ObjectInputStream, self).readLine())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def readFields(self) -> 'GetField.ObjectInputStream$GetField':
        """public java.io.ObjectInputStream$GetField java.io.ObjectInputStream.readFields() throws java.io.IOException,java.lang.ClassNotFoundException"""
        return 'GetField.ObjectInputStream$GetField'._wrap(super(ObjectInputStream, self).readFields())

    @overload
    def transferTo(self, arg0: 'OutputStream') -> int:
        """public long java.io.InputStream.transferTo(java.io.OutputStream) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).transferTo(arg0))

    @override
    @overload
    def getObjectInputFilter(self) -> 'ObjectInputFilter':
        """public final java.io.ObjectInputFilter java.io.ObjectInputStream.getObjectInputFilter()"""
        return 'ObjectInputFilter'._wrap(super(ObjectInputStream, self).getObjectInputFilter())

    @override
    @overload
    def reset(self):
        """public void java.io.InputStream.reset() throws java.io.IOException"""
        super(InputStream, self).reset()

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
    def readInt(self) -> int:
        """public int java.io.ObjectInputStream.readInt() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).readInt())

    @override
    @overload
    def readAllBytes(self) -> List[int]:
        """public byte[] java.io.InputStream.readAllBytes() throws java.io.IOException"""
        return List[int]._wrap(super(InputStream, self).readAllBytes())

    @override
    @overload
    def registerValidation(self, arg0: 'ObjectInputValidation', arg1: int):
        """public void java.io.ObjectInputStream.registerValidation(java.io.ObjectInputValidation,int) throws java.io.NotActiveException,java.io.InvalidObjectException"""
        super(_ObjectInputStream, self).registerValidation(arg0, _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream() throws java.io.IOException,java.lang.SecurityException"""
        val = _FilteredObjectInputStream()
        self.__wrapper = val

    @override
    @overload
    def readByte(self) -> int:
        """public byte java.io.ObjectInputStream.readByte() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).readByte())

    @overload
    def read(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.ObjectInputStream.read(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_ObjectInputStream, self).read(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def readChar(self) -> str:
        """public char java.io.ObjectInputStream.readChar() throws java.io.IOException"""
        return str._wrap(super(ObjectInputStream, self).readChar())

    @overload
    def read(self, arg0: bytes) -> int:
        """public int java.io.InputStream.read(byte[]) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).read(bytes))

    @staticmethod
    @overload
    def nullInputStream() -> 'InputStream':
        """public static java.io.InputStream java.io.InputStream.nullInputStream()"""
        return InputStream._wrap(_InputStream.nullInputStream())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def readNBytes(self, arg0: bytes, arg1: int, arg2: int) -> int:
        """public int java.io.InputStream.readNBytes(byte[],int,int) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).readNBytes(bytes, _int.valueOf(arg1), _int.valueOf(arg2)))

    @override
    @overload
    def markSupported(self) -> bool:
        """public boolean java.io.InputStream.markSupported()"""
        return bool._wrap(super(InputStream, self).markSupported())

    @override
    @overload
    def defaultReadObject(self):
        """public void java.io.ObjectInputStream.defaultReadObject() throws java.io.IOException,java.lang.ClassNotFoundException"""
        super(ObjectInputStream, self).defaultReadObject()

    @override
    @overload
    def available(self) -> int:
        """public int java.io.ObjectInputStream.available() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).available())

    @overload
    def readNBytes(self, arg0: int) -> List[int]:
        """public byte[] java.io.InputStream.readNBytes(int) throws java.io.IOException"""
        return List[int]._wrap(super(_InputStream, self).readNBytes(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, inputStream: 'InputStream', allowedExtraClasses: 'Collection'):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream(java.io.InputStream,java.util.Collection<java.lang.String>) throws java.io.IOException"""
        val = _FilteredObjectInputStream(inputStream, allowedExtraClasses)
        self.__wrapper = val

    @overload
    def getAllowedClasses(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.FilteredObjectInputStream.getAllowedClasses()"""
        return 'Collection'._wrap(super(FilteredObjectInputStream, self).getAllowedClasses())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def readFully(self, arg0: bytes, arg1: int, arg2: int):
        """public void java.io.ObjectInputStream.readFully(byte[],int,int) throws java.io.IOException"""
        super(_ObjectInputStream, self).readFully(bytes, _int.valueOf(arg1), _int.valueOf(arg2))

    @override
    @overload
    def readUnsignedByte(self) -> int:
        """public int java.io.ObjectInputStream.readUnsignedByte() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).readUnsignedByte())

    @overload
    def skip(self, arg0: int) -> int:
        """public long java.io.InputStream.skip(long) throws java.io.IOException"""
        return int._wrap(super(_InputStream, self).skip(_long.valueOf(arg0)))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream() throws java.io.IOException,java.lang.SecurityException"""
        val = _FilteredObjectInputStream()
        self.__wrapper = val

    @override
    @overload
    def readShort(self) -> int:
        """public short java.io.ObjectInputStream.readShort() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).readShort())

    @override
    @overload
    def readFloat(self) -> float:
        """public float java.io.ObjectInputStream.readFloat() throws java.io.IOException"""
        return float._wrap(super(ObjectInputStream, self).readFloat())

    @override
    @overload
    def setObjectInputFilter(self, arg0: 'ObjectInputFilter'):
        """public final void java.io.ObjectInputStream.setObjectInputFilter(java.io.ObjectInputFilter)"""
        super(_ObjectInputStream, self).setObjectInputFilter(arg0)

    @override
    @overload
    def readObject(self) -> object:
        """public final java.lang.Object java.io.ObjectInputStream.readObject() throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object._wrap(super(ObjectInputStream, self).readObject())

    @overload
    def __init__(self, allowedExtraClasses: 'Collection'):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream(java.util.Collection<java.lang.String>) throws java.io.IOException,java.lang.SecurityException"""
        val = _FilteredObjectInputStream(allowedExtraClasses)
        self.__wrapper = val

    @override
    @overload
    def readFully(self, arg0: bytes):
        """public void java.io.ObjectInputStream.readFully(byte[]) throws java.io.IOException"""
        super(_ObjectInputStream, self).readFully(bytes)

    @override
    @overload
    def close(self):
        """public void java.io.ObjectInputStream.close() throws java.io.IOException"""
        super(ObjectInputStream, self).close()

    @override
    @overload
    def skipNBytes(self, arg0: int):
        """public void java.io.InputStream.skipNBytes(long) throws java.io.IOException"""
        super(_InputStream, self).skipNBytes(_long.valueOf(arg0))

    @overload
    def __init__(self, inputStream: 'InputStream'):
        """public org.apache.logging.log4j.util.FilteredObjectInputStream(java.io.InputStream) throws java.io.IOException"""
        val = _FilteredObjectInputStream(inputStream)
        self.__wrapper = val

    @override
    @overload
    def readLong(self) -> int:
        """public long java.io.ObjectInputStream.readLong() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).readLong())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def readUTF(self) -> str:
        """public java.lang.String java.io.ObjectInputStream.readUTF() throws java.io.IOException"""
        return str._wrap(super(ObjectInputStream, self).readUTF())

    @override
    @overload
    def readBoolean(self) -> bool:
        """public boolean java.io.ObjectInputStream.readBoolean() throws java.io.IOException"""
        return bool._wrap(super(ObjectInputStream, self).readBoolean())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def readUnshared(self) -> object:
        """public java.lang.Object java.io.ObjectInputStream.readUnshared() throws java.io.IOException,java.lang.ClassNotFoundException"""
        return object._wrap(super(ObjectInputStream, self).readUnshared())

    @override
    @overload
    def readUnsignedShort(self) -> int:
        """public int java.io.ObjectInputStream.readUnsignedShort() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).readUnsignedShort())

    @override
    @overload
    def readDouble(self) -> float:
        """public double java.io.ObjectInputStream.readDouble() throws java.io.IOException"""
        return float._wrap(super(ObjectInputStream, self).readDouble())

    @override
    @overload
    def mark(self, arg0: int):
        """public void java.io.InputStream.mark(int)"""
        super(_InputStream, self).mark(_int.valueOf(arg0))

    @override
    @overload
    def read(self) -> int:
        """public int java.io.ObjectInputStream.read() throws java.io.IOException"""
        return int._wrap(super(ObjectInputStream, self).read())

    @overload
    def skipBytes(self, arg0: int) -> int:
        """public int java.io.ObjectInputStream.skipBytes(int) throws java.io.IOException"""
        return int._wrap(super(_ObjectInputStream, self).skipBytes(_int.valueOf(arg0))) 
 
 
# CLASS: org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable
import org.apache.logging.log4j.util.StringBuilderFormattable as _StringBuilderFormattable
_StringBuilderFormattable = _StringBuilderFormattable
import org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable as _MultiFormatStringBuilderFormattable
_MultiFormatStringBuilderFormattable = _MultiFormatStringBuilderFormattable
from builtins import str
import org.apache.logging.log4j.message.MultiformatMessage as _MultiformatMessage
_MultiformatMessage = _MultiformatMessage
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
 
class MultiFormatStringBuilderFormattable():
    """org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable"""
 
    @staticmethod
    def _wrap(java_value: _MultiFormatStringBuilderFormattable) -> 'MultiFormatStringBuilderFormattable':
        return MultiFormatStringBuilderFormattable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultiFormatStringBuilderFormattable):
        """
        Dynamic initializer for MultiFormatStringBuilderFormattable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultiFormatStringBuilderFormattable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultiFormatStringBuilderFormattable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getFormats(self, ):
        """public abstract java.lang.String[] org.apache.logging.log4j.message.MultiformatMessage.getFormats()"""
        pass

    @abstractmethod
    def getFormat(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormat()"""
        pass

    @abstractmethod
    def getFormattedMessage(self, ):
        """public abstract java.lang.String org.apache.logging.log4j.message.Message.getFormattedMessage()"""
        pass

    @abstractmethod
    def getThrowable(self, ):
        """public abstract java.lang.Throwable org.apache.logging.log4j.message.Message.getThrowable()"""
        pass

    @abstractmethod
    def formatTo(self, formats: 'String', buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.MultiFormatStringBuilderFormattable.formatTo(java.lang.String[],java.lang.StringBuilder)"""
        pass

    @abstractmethod
    def getFormattedMessage(self, formats: 'String'):
        """public abstract java.lang.String org.apache.logging.log4j.message.MultiformatMessage.getFormattedMessage(java.lang.String[])"""
        pass

    @abstractmethod
    def formatTo(self, buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.StringBuilderFormattable.formatTo(java.lang.StringBuilder)"""
        pass

    @abstractmethod
    def getParameters(self, ):
        """public abstract java.lang.Object[] org.apache.logging.log4j.message.Message.getParameters()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.Constants
import org.apache.logging.log4j.util.Constants as _Constants
_Constants = _Constants
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Constants():
    """org.apache.logging.log4j.util.Constants"""
 
    @staticmethod
    def _wrap(java_value: _Constants) -> 'Constants':
        return Constants(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Constants):
        """
        Dynamic initializer for Constants.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Constants__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Constants__wrapper":
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
 
 
# CLASS: org.apache.logging.log4j.util.StringBuilderFormattable
import org.apache.logging.log4j.util.StringBuilderFormattable as _StringBuilderFormattable
_StringBuilderFormattable = _StringBuilderFormattable
import java.lang.StringBuilder as StringBuilder
from abc import abstractmethod, ABC
 
class StringBuilderFormattable():
    """org.apache.logging.log4j.util.StringBuilderFormattable"""
 
    @staticmethod
    def _wrap(java_value: _StringBuilderFormattable) -> 'StringBuilderFormattable':
        return StringBuilderFormattable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringBuilderFormattable):
        """
        Dynamic initializer for StringBuilderFormattable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringBuilderFormattable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringBuilderFormattable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def formatTo(self, buffer: 'StringBuilder'):
        """public abstract void org.apache.logging.log4j.util.StringBuilderFormattable.formatTo(java.lang.StringBuilder)"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.LambdaUtil
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.util.LambdaUtil as _LambdaUtil
_LambdaUtil = _LambdaUtil
try:
    from log4py import message
except ImportError:
    message = _import_once("log4py.message")

from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
import org.apache.logging.log4j.message.Message as _Message
_Message = _Message
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class LambdaUtil():
    """org.apache.logging.log4j.util.LambdaUtil"""
 
    @staticmethod
    def _wrap(java_value: _LambdaUtil) -> 'LambdaUtil':
        return LambdaUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LambdaUtil):
        """
        Dynamic initializer for LambdaUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LambdaUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LambdaUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def get(supplier: 'MessageSupplier') -> 'message.Message':
        """public static org.apache.logging.log4j.message.Message org.apache.logging.log4j.util.LambdaUtil.get(org.apache.logging.log4j.util.MessageSupplier)"""
        return message.Message._wrap(_LambdaUtil.get(supplier))

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

    @staticmethod
    @overload
    def getMessage(supplier: 'Supplier', messageFactory: 'MessageFactory') -> 'message.Message':
        """public static org.apache.logging.log4j.message.Message org.apache.logging.log4j.util.LambdaUtil.getMessage(org.apache.logging.log4j.util.Supplier<?>,org.apache.logging.log4j.message.MessageFactory)"""
        return message.Message._wrap(_LambdaUtil.getMessage(supplier, messageFactory))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(supplier: 'Supplier') -> object:
        """public static java.lang.Object org.apache.logging.log4j.util.LambdaUtil.get(org.apache.logging.log4j.util.Supplier<?>)"""
        return object._wrap(_LambdaUtil.get(supplier))

    @staticmethod
    @overload
    def getAll(*suppliers: 'Supplier') -> List[object]:
        """public static java.lang.Object[] org.apache.logging.log4j.util.LambdaUtil.getAll(org.apache.logging.log4j.util.Supplier<?>...)"""
        return List[object]._wrap(_LambdaUtil.getAll(suppliers))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.ProviderUtil
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.util.ProviderUtil as _ProviderUtil
_ProviderUtil = _ProviderUtil
import java.lang.ClassLoader as _ClassLoader
_ClassLoader = _ClassLoader
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ProviderUtil():
    """org.apache.logging.log4j.util.ProviderUtil"""
 
    @staticmethod
    def _wrap(java_value: _ProviderUtil) -> 'ProviderUtil':
        return ProviderUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ProviderUtil):
        """
        Dynamic initializer for ProviderUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ProviderUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ProviderUtil__wrapper":
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

    @staticmethod
    @overload
    def getProviders() -> 'Iterable':
        """public static java.lang.Iterable<org.apache.logging.log4j.spi.Provider> org.apache.logging.log4j.util.ProviderUtil.getProviders()"""
        return Iterable._wrap(_ProviderUtil.getProviders())

    @staticmethod
    @overload
    def hasProviders() -> bool:
        """public static boolean org.apache.logging.log4j.util.ProviderUtil.hasProviders()"""
        return bool._wrap(_ProviderUtil.hasProviders())

    @staticmethod
    @overload
    def findClassLoader() -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.ProviderUtil.findClassLoader()"""
        return ClassLoader._wrap(_ProviderUtil.findClassLoader())

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
 
 
# CLASS: org.apache.logging.log4j.util.InternalApi
import org.apache.logging.log4j.util.InternalApi as _InternalApi
_InternalApi = _InternalApi
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class InternalApi():
    """org.apache.logging.log4j.util.InternalApi"""
 
    @staticmethod
    def _wrap(java_value: _InternalApi) -> 'InternalApi':
        return InternalApi(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InternalApi):
        """
        Dynamic initializer for InternalApi.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InternalApi__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InternalApi__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.PropertySource$Util
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import org.apache.logging.log4j.util.PropertySource as _PropertySource_Util
_Util = _PropertySource_Util.Util
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Util():
    """org.apache.logging.log4j.util.PropertySource.Util"""
 
    @staticmethod
    def _wrap(java_value: _Util) -> 'Util':
        return Util(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Util):
        """
        Dynamic initializer for Util.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Util__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Util__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def tokenize(value: 'CharSequence') -> 'List':
        """public static java.util.List<java.lang.CharSequence> org.apache.logging.log4j.util.PropertySource$Util.tokenize(java.lang.CharSequence)"""
        return List._wrap(_Util.tokenize(value))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def joinAsCamelCase(tokens: 'Iterable') -> 'CharSequence':
        """public static java.lang.CharSequence org.apache.logging.log4j.util.PropertySource$Util.joinAsCamelCase(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return CharSequence._wrap(_Util.joinAsCamelCase(tokens))

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
 
 
# CLASS: org.apache.logging.log4j.util.PropertyFilePropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import org.apache.logging.log4j.util.PropertyFilePropertySource as _PropertyFilePropertySource
_PropertyFilePropertySource = _PropertyFilePropertySource
import org.apache.logging.log4j.util.PropertiesPropertySource as _PropertiesPropertySource
_PropertiesPropertySource = _PropertiesPropertySource
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PropertyFilePropertySource():
    """org.apache.logging.log4j.util.PropertyFilePropertySource"""
 
    @staticmethod
    def _wrap(java_value: _PropertyFilePropertySource) -> 'PropertyFilePropertySource':
        return PropertyFilePropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PropertyFilePropertySource):
        """
        Dynamic initializer for PropertyFilePropertySource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PropertyFilePropertySource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PropertyFilePropertySource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.PropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'._wrap(super(_PropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, fileName: str):
        """public org.apache.logging.log4j.util.PropertyFilePropertySource(java.lang.String)"""
        val = _PropertyFilePropertySource(fileName)
        self.__wrapper = val

    @override
    @overload
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.PropertiesPropertySource.getPriority()"""
        return int._wrap(super(PropertiesPropertySource, self).getPriority())

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.PropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(_PropertiesPropertySource, self).forEach(action)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesPropertySource.getProperty(java.lang.String)"""
        return str._wrap(super(_PropertiesPropertySource, self).getProperty(key))

    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool._wrap(super(_PropertiesPropertySource, self).containsProperty(key))

    @overload
    def __init__(self, fileName: str, useTccl: bool):
        """public org.apache.logging.log4j.util.PropertyFilePropertySource(java.lang.String,boolean)"""
        val = _PropertyFilePropertySource(fileName, _boolean.valueOf(useTccl))
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertiesPropertySource.getPropertyNames()"""
        return 'Collection'._wrap(super(PropertiesPropertySource, self).getPropertyNames())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.OsgiServiceLocator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import org.apache.logging.log4j.util.OsgiServiceLocator as _OsgiServiceLocator
_OsgiServiceLocator = _OsgiServiceLocator
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
from builtins import bool
import java.lang.Long as _long
import java.lang.invoke.MethodHandles.Lookup as Lookup
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class OsgiServiceLocator():
    """org.apache.logging.log4j.util.OsgiServiceLocator"""
 
    @staticmethod
    def _wrap(java_value: _OsgiServiceLocator) -> 'OsgiServiceLocator':
        return OsgiServiceLocator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _OsgiServiceLocator):
        """
        Dynamic initializer for OsgiServiceLocator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_OsgiServiceLocator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_OsgiServiceLocator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.OsgiServiceLocator()"""
        val = _OsgiServiceLocator()
        self.__wrapper = val

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup') -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.OsgiServiceLocator.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup)"""
        return Stream._wrap(_OsgiServiceLocator.loadServices(serviceType, lookup))

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

    @staticmethod
    @overload
    def isAvailable() -> bool:
        """public static boolean org.apache.logging.log4j.util.OsgiServiceLocator.isAvailable()"""
        return bool._wrap(_OsgiServiceLocator.isAvailable())

    @staticmethod
    @overload
    def loadServices(serviceType: 'Class', lookup: 'Lookup', verbose: bool) -> 'Stream':
        """public static <T> java.util.stream.Stream<T> org.apache.logging.log4j.util.OsgiServiceLocator.loadServices(java.lang.Class<T>,java.lang.invoke.MethodHandles$Lookup,boolean)"""
        return Stream._wrap(_OsgiServiceLocator.loadServices(serviceType, lookup, _boolean.valueOf(verbose)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.OsgiServiceLocator()"""
        val = _OsgiServiceLocator()
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
 
 
# CLASS: org.apache.logging.log4j.util.EnvironmentPropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import org.apache.logging.log4j.util.EnvironmentPropertySource as _EnvironmentPropertySource
_EnvironmentPropertySource = _EnvironmentPropertySource
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EnvironmentPropertySource():
    """org.apache.logging.log4j.util.EnvironmentPropertySource"""
 
    @staticmethod
    def _wrap(java_value: _EnvironmentPropertySource) -> 'EnvironmentPropertySource':
        return EnvironmentPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnvironmentPropertySource):
        """
        Dynamic initializer for EnvironmentPropertySource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnvironmentPropertySource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnvironmentPropertySource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.EnvironmentPropertySource.containsProperty(java.lang.String)"""
        return bool._wrap(super(_EnvironmentPropertySource, self).containsProperty(key))

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
    def __init__(self):
        """public org.apache.logging.log4j.util.EnvironmentPropertySource()"""
        val = _EnvironmentPropertySource()
        self.__wrapper = val

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.EnvironmentPropertySource.getProperty(java.lang.String)"""
        return str._wrap(super(_EnvironmentPropertySource, self).getProperty(key))

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.EnvironmentPropertySource.getPropertyNames()"""
        return 'Collection'._wrap(super(EnvironmentPropertySource, self).getPropertyNames())

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.EnvironmentPropertySource()"""
        val = _EnvironmentPropertySource()
        self.__wrapper = val

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
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.EnvironmentPropertySource.getPriority()"""
        return int._wrap(super(EnvironmentPropertySource, self).getPriority())

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
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.EnvironmentPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(_EnvironmentPropertySource, self).forEach(action)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.EnvironmentPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'._wrap(super(_EnvironmentPropertySource, self).getNormalForm(tokens))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.IndexedStringMap
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as _IndexedReadOnlyStringMap
_IndexedReadOnlyStringMap = _IndexedReadOnlyStringMap
import org.apache.logging.log4j.util.IndexedStringMap as _IndexedStringMap
_IndexedStringMap = _IndexedStringMap
import org.apache.logging.log4j.util.StringMap as _StringMap
_StringMap = _StringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as _ReadOnlyStringMap
_ReadOnlyStringMap = _ReadOnlyStringMap
 
class IndexedStringMap():
    """org.apache.logging.log4j.util.IndexedStringMap"""
 
    @staticmethod
    def _wrap(java_value: _IndexedStringMap) -> 'IndexedStringMap':
        return IndexedStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedStringMap):
        """
        Dynamic initializer for IndexedStringMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedStringMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedStringMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.apache.logging.log4j.util.StringMap.hashCode()"""
        pass

    @abstractmethod
    def freeze(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.freeze()"""
        pass

    @abstractmethod
    def putAll(self, source: 'ReadOnlyStringMap'):
        """public abstract void org.apache.logging.log4j.util.StringMap.putAll(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.clear()"""
        pass

    @abstractmethod
    def indexOfKey(self, key: str):
        """public abstract int org.apache.logging.log4j.util.IndexedReadOnlyStringMap.indexOfKey(java.lang.String)"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def getKeyAt(self, index: int):
        """public abstract java.lang.String org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getKeyAt(int)"""
        pass

    @abstractmethod
    def putValue(self, key: str, value: object):
        """public abstract void org.apache.logging.log4j.util.StringMap.putValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def getValueAt(self, index: int):
        """public abstract <V> V org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getValueAt(int)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.util.StringMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass

    @abstractmethod
    def isFrozen(self, ):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.isFrozen()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.PerformanceSensitive
import org.apache.logging.log4j.util.PerformanceSensitive as _PerformanceSensitive
_PerformanceSensitive = _PerformanceSensitive
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class PerformanceSensitive():
    """org.apache.logging.log4j.util.PerformanceSensitive"""
 
    @staticmethod
    def _wrap(java_value: _PerformanceSensitive) -> 'PerformanceSensitive':
        return PerformanceSensitive(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PerformanceSensitive):
        """
        Dynamic initializer for PerformanceSensitive.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PerformanceSensitive__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PerformanceSensitive__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def value(self, ):
        """public abstract java.lang.String[] org.apache.logging.log4j.util.PerformanceSensitive.value()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.Cast
from builtins import str
import org.apache.logging.log4j.util.Cast as _Cast
_Cast = _Cast
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Cast():
    """org.apache.logging.log4j.util.Cast"""
 
    @staticmethod
    def _wrap(java_value: _Cast) -> 'Cast':
        return Cast(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Cast):
        """
        Dynamic initializer for Cast.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Cast__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Cast__wrapper":
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

    @staticmethod
    @overload
    def cast(o: object) -> object:
        """public static <T> T org.apache.logging.log4j.util.Cast.cast(java.lang.Object)"""
        return object._wrap(_Cast.cast(o))

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
 
 
# CLASS: org.apache.logging.log4j.util.StringMap
import org.apache.logging.log4j.util.StringMap as _StringMap
_StringMap = _StringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as _ReadOnlyStringMap
_ReadOnlyStringMap = _ReadOnlyStringMap
 
class StringMap():
    """org.apache.logging.log4j.util.StringMap"""
 
    @staticmethod
    def _wrap(java_value: _StringMap) -> 'StringMap':
        return StringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringMap):
        """
        Dynamic initializer for StringMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def hashCode(self, ):
        """public abstract int org.apache.logging.log4j.util.StringMap.hashCode()"""
        pass

    @abstractmethod
    def freeze(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.freeze()"""
        pass

    @abstractmethod
    def putAll(self, source: 'ReadOnlyStringMap'):
        """public abstract void org.apache.logging.log4j.util.StringMap.putAll(org.apache.logging.log4j.util.ReadOnlyStringMap)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void org.apache.logging.log4j.util.StringMap.clear()"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def equals(self, obj: object):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def putValue(self, key: str, value: object):
        """public abstract void org.apache.logging.log4j.util.StringMap.putValue(java.lang.String,java.lang.Object)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def remove(self, key: str):
        """public abstract void org.apache.logging.log4j.util.StringMap.remove(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def isFrozen(self, ):
        """public abstract boolean org.apache.logging.log4j.util.StringMap.isFrozen()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.Timer$Status
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.util.Timer as _Timer_Status
_Status = _Timer_Status.Status
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
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Status():
    """org.apache.logging.log4j.util.Timer.Status"""
 
    @staticmethod
    def _wrap(java_value: _Status) -> 'Status':
        return Status(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Status):
        """
        Dynamic initializer for Status.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Status__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Status__wrapper":
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

    @staticmethod
    @overload
    def values() -> List['Status']:
        """public static org.apache.logging.log4j.util.Timer$Status[] org.apache.logging.log4j.util.Timer$Status.values()"""
        return List[Status]._wrap(_Status.values())

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

    @staticmethod
    @overload
    def valueOf(name: str) -> 'Status':
        """public static org.apache.logging.log4j.util.Timer$Status org.apache.logging.log4j.util.Timer$Status.valueOf(java.lang.String)"""
        return Status._wrap(_Status.valueOf(name)) 
 
 
# CLASS: org.apache.logging.log4j.util.LoaderUtil
import java.util.function.Supplier as Supplier
from builtins import str
import org.apache.logging.log4j.util.LoaderUtil as _LoaderUtil
_LoaderUtil = _LoaderUtil
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.ClassLoader as _ClassLoader
_ClassLoader = _ClassLoader
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class LoaderUtil():
    """org.apache.logging.log4j.util.LoaderUtil"""
 
    @staticmethod
    def _wrap(java_value: _LoaderUtil) -> 'LoaderUtil':
        return LoaderUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LoaderUtil):
        """
        Dynamic initializer for LoaderUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LoaderUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LoaderUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newInstanceOfUnchecked(className: str) -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOfUnchecked(java.lang.String)"""
        return object._wrap(_LoaderUtil.newInstanceOfUnchecked(className))

    @staticmethod
    @overload
    def newInstanceOfUnchecked(className: str, supertype: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOfUnchecked(java.lang.String,java.lang.Class<T>)"""
        return object._wrap(_LoaderUtil.newInstanceOfUnchecked(className, supertype))

    @staticmethod
    @overload
    def findResources(resource: str) -> 'Collection':
        """public static java.util.Collection<java.net.URL> org.apache.logging.log4j.util.LoaderUtil.findResources(java.lang.String)"""
        return Collection._wrap(_LoaderUtil.findResources(resource))

    @staticmethod
    @overload
    def loadClass(className: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.LoaderUtil.loadClass(java.lang.String) throws java.lang.ClassNotFoundException"""
        return type.Class._wrap(_LoaderUtil.loadClass(className))

    @staticmethod
    @overload
    def getThreadContextClassLoader() -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.LoaderUtil.getThreadContextClassLoader()"""
        return ClassLoader._wrap(_LoaderUtil.getThreadContextClassLoader())

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

    @staticmethod
    @overload
    def getClassLoader() -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.LoaderUtil.getClassLoader()"""
        return ClassLoader._wrap(_LoaderUtil.getClassLoader())

    @staticmethod
    @overload
    def newInstanceOf(className: str) -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOf(java.lang.String) throws java.lang.ClassNotFoundException,java.lang.IllegalAccessException,java.lang.InstantiationException,java.lang.reflect.InvocationTargetException,java.lang.NoSuchMethodException"""
        return object._wrap(_LoaderUtil.newInstanceOf(className))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def newCheckedInstanceOf(className: str, clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newCheckedInstanceOf(java.lang.String,java.lang.Class<T>) throws java.lang.ClassNotFoundException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.NoSuchMethodException"""
        return object._wrap(_LoaderUtil.newCheckedInstanceOf(className, clazz))

    @staticmethod
    @overload
    def newCheckedInstanceOfProperty(propertyName: str, clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newCheckedInstanceOfProperty(java.lang.String,java.lang.Class<T>) throws java.lang.ClassNotFoundException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.NoSuchMethodException"""
        return object._wrap(_LoaderUtil.newCheckedInstanceOfProperty(propertyName, clazz))

    @staticmethod
    @overload
    def isClassAvailable(className: str) -> bool:
        """public static boolean org.apache.logging.log4j.util.LoaderUtil.isClassAvailable(java.lang.String)"""
        return bool._wrap(_LoaderUtil.isClassAvailable(className))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def loadClassUnchecked(className: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.LoaderUtil.loadClassUnchecked(java.lang.String)"""
        return type.Class._wrap(_LoaderUtil.loadClassUnchecked(className))

    @staticmethod
    @overload
    def newInstanceOfUnchecked(clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOfUnchecked(java.lang.Class<T>)"""
        return object._wrap(_LoaderUtil.newInstanceOfUnchecked(clazz))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getClassLoader(class1: 'Class', class2: 'Class') -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.LoaderUtil.getClassLoader(java.lang.Class<?>,java.lang.Class<?>)"""
        return ClassLoader._wrap(_LoaderUtil.getClassLoader(class1, class2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def newInstanceOf(clazz: 'Class') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newInstanceOf(java.lang.Class<T>) throws java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.NoSuchMethodException"""
        return object._wrap(_LoaderUtil.newInstanceOf(clazz))

    @staticmethod
    @overload
    def newCheckedInstanceOfProperty(propertyName: str, clazz: 'Class', defaultSupplier: 'Supplier') -> object:
        """public static <T> T org.apache.logging.log4j.util.LoaderUtil.newCheckedInstanceOfProperty(java.lang.String,java.lang.Class<T>,java.util.function.Supplier<T>) throws java.lang.ClassNotFoundException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException,java.lang.IllegalAccessException,java.lang.NoSuchMethodException"""
        return object._wrap(_LoaderUtil.newCheckedInstanceOfProperty(propertyName, clazz, defaultSupplier))

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
 
 
# CLASS: org.apache.logging.log4j.util.Chars
import org.apache.logging.log4j.util.Chars as _Chars
_Chars = _Chars
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Chars():
    """org.apache.logging.log4j.util.Chars"""
 
    @staticmethod
    def _wrap(java_value: _Chars) -> 'Chars':
        return Chars(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Chars):
        """
        Dynamic initializer for Chars.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Chars__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Chars__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getUpperCaseHex(digit: int) -> str:
        """public static char org.apache.logging.log4j.util.Chars.getUpperCaseHex(int)"""
        return str._wrap(_Chars.getUpperCaseHex(_int.valueOf(digit)))

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

    @staticmethod
    @overload
    def getLowerCaseHex(digit: int) -> str:
        """public static char org.apache.logging.log4j.util.Chars.getLowerCaseHex(int)"""
        return str._wrap(_Chars.getLowerCaseHex(_int.valueOf(digit)))

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
 
 
# CLASS: org.apache.logging.log4j.util.PropertySource$Comparator
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
import org.apache.logging.log4j.util.PropertySource as _PropertySource_Comparator
_Comparator = _PropertySource_Comparator.Comparator
import java.util.Comparator as _Comparator
_Comparator = _Comparator
import java.util.function.ToIntFunction as ToIntFunction
import java.util.function.ToLongFunction as ToLongFunction
import java.util.function.Function as Function
import java.util.function.ToDoubleFunction as ToDoubleFunction
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Comparator():
    """org.apache.logging.log4j.util.PropertySource.Comparator"""
 
    @staticmethod
    def _wrap(java_value: _Comparator) -> 'Comparator':
        return Comparator(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Comparator):
        """
        Dynamic initializer for Comparator.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Comparator__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Comparator__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def thenComparingDouble(self, arg0: 'ToDoubleFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingDouble(java.util.function.ToDoubleFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingDouble(arg0))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.PropertySource$Comparator()"""
        val = _Comparator()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Comparator') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.Comparator<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

    @overload
    def compare(self, o1: 'PropertySource', o2: 'PropertySource') -> int:
        """public int org.apache.logging.log4j.util.PropertySource$Comparator.compare(org.apache.logging.log4j.util.PropertySource,org.apache.logging.log4j.util.PropertySource)"""
        return int._wrap(super(_Comparator, self).compare(o1, o2))

    @overload
    def thenComparingInt(self, arg0: 'ToIntFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingInt(java.util.function.ToIntFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingInt(arg0))

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
    def __init__(self, ):
        """public org.apache.logging.log4j.util.PropertySource$Comparator()"""
        val = _Comparator()
        self.__wrapper = val

    @overload
    def thenComparing(self, arg0: 'Function') -> 'Comparator':
        """public default <U extends java.lang.Comparable<? super U>> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0))

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
    def thenComparing(self, arg0: 'Function', arg1: 'Comparator') -> 'Comparator':
        """public default <U> java.util.Comparator<T> java.util.Comparator.thenComparing(java.util.function.Function<? super T, ? extends U>,java.util.Comparator<? super U>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparing(arg0, arg1))

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
    def reversed(self) -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.reversed()"""
        return 'Comparator'._wrap(super(Comparator, self).reversed())

    @overload
    def thenComparingLong(self, arg0: 'ToLongFunction') -> 'Comparator':
        """public default java.util.Comparator<T> java.util.Comparator.thenComparingLong(java.util.function.ToLongFunction<? super T>)"""
        return 'Comparator'._wrap(super(_Comparator, self).thenComparingLong(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.Lazy
import java.util.function.Supplier as Supplier
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
import org.apache.logging.log4j.util.Lazy as _Lazy
_Lazy = _Lazy
from builtins import object
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Lazy():
    """org.apache.logging.log4j.util.Lazy"""
 
    @staticmethod
    def _wrap(java_value: _Lazy) -> 'Lazy':
        return Lazy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Lazy):
        """
        Dynamic initializer for Lazy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Lazy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Lazy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def lazy(supplier: 'Supplier') -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.lazy(java.util.function.Supplier<T>)"""
        return Lazy._wrap(_Lazy.lazy(supplier))

    @overload
    def map(self, function: 'Function') -> 'Lazy':
        """public default <R> org.apache.logging.log4j.util.Lazy<R> org.apache.logging.log4j.util.Lazy.map(java.util.function.Function<? super T, ? extends R>)"""
        return 'Lazy'._wrap(super(_Lazy, self).map(function))

    @abstractmethod
    def set(self, newValue: object):
        """public abstract void org.apache.logging.log4j.util.Lazy.set(T)"""
        pass

    @staticmethod
    @overload
    def value(value: object) -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.value(T)"""
        return Lazy._wrap(_Lazy.value(value))

    @abstractmethod
    def value(self, ):
        """public abstract T org.apache.logging.log4j.util.Lazy.value()"""
        pass

    @override
    @overload
    def get(self) -> object:
        """public default T org.apache.logging.log4j.util.Lazy.get()"""
        return object._wrap(super(Lazy, self).get())

    @staticmethod
    @overload
    def pure(supplier: 'Supplier') -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.pure(java.util.function.Supplier<T>)"""
        return Lazy._wrap(_Lazy.pure(supplier))

    @staticmethod
    @overload
    def weak(value: object) -> 'Lazy':
        """public static <T> org.apache.logging.log4j.util.Lazy<T> org.apache.logging.log4j.util.Lazy.weak(T)"""
        return Lazy._wrap(_Lazy.weak(value))

    @abstractmethod
    def isInitialized(self, ):
        """public abstract boolean org.apache.logging.log4j.util.Lazy.isInitialized()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.PropertySource
import java.lang.String as _string
from builtins import str
import org.apache.logging.log4j.util.PropertySource as _PropertySource
_PropertySource = _PropertySource
import java.lang.CharSequence as CharSequence
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Iterable as Iterable
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
from builtins import bool
 
class PropertySource():
    """org.apache.logging.log4j.util.PropertySource"""
 
    @staticmethod
    def _wrap(java_value: _PropertySource) -> 'PropertySource':
        return PropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PropertySource):
        """
        Dynamic initializer for PropertySource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PropertySource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PropertySource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getProperty(self, key: str) -> str:
        """public default java.lang.String org.apache.logging.log4j.util.PropertySource.getProperty(java.lang.String)"""
        return str._wrap(super(_PropertySource, self).getProperty(key))

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public default java.lang.CharSequence org.apache.logging.log4j.util.PropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'._wrap(super(_PropertySource, self).getNormalForm(tokens))

    @abstractmethod
    def getPriority(self, ):
        """public abstract int org.apache.logging.log4j.util.PropertySource.getPriority()"""
        pass

    @overload
    def containsProperty(self, key: str) -> bool:
        """public default boolean org.apache.logging.log4j.util.PropertySource.containsProperty(java.lang.String)"""
        return bool._wrap(super(_PropertySource, self).containsProperty(key))

    @overload
    def getPropertyNames(self) -> 'Collection':
        """public default java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertySource.getPropertyNames()"""
        return 'Collection'._wrap(super(PropertySource, self).getPropertyNames())

    @overload
    def forEach(self, action: 'BiConsumer'):
        """public default void org.apache.logging.log4j.util.PropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(_PropertySource, self).forEach(action) 
 
 
# CLASS: org.apache.logging.log4j.util.IndexedReadOnlyStringMap
import org.apache.logging.log4j.util.IndexedReadOnlyStringMap as _IndexedReadOnlyStringMap
_IndexedReadOnlyStringMap = _IndexedReadOnlyStringMap
from abc import abstractmethod, ABC
import org.apache.logging.log4j.util.ReadOnlyStringMap as _ReadOnlyStringMap
_ReadOnlyStringMap = _ReadOnlyStringMap
 
class IndexedReadOnlyStringMap():
    """org.apache.logging.log4j.util.IndexedReadOnlyStringMap"""
 
    @staticmethod
    def _wrap(java_value: _IndexedReadOnlyStringMap) -> 'IndexedReadOnlyStringMap':
        return IndexedReadOnlyStringMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IndexedReadOnlyStringMap):
        """
        Dynamic initializer for IndexedReadOnlyStringMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IndexedReadOnlyStringMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IndexedReadOnlyStringMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def indexOfKey(self, key: str):
        """public abstract int org.apache.logging.log4j.util.IndexedReadOnlyStringMap.indexOfKey(java.lang.String)"""
        pass

    @abstractmethod
    def toMap(self, ):
        """public abstract java.util.Map<java.lang.String, java.lang.String> org.apache.logging.log4j.util.ReadOnlyStringMap.toMap()"""
        pass

    @abstractmethod
    def getValue(self, key: str):
        """public abstract <V> V org.apache.logging.log4j.util.ReadOnlyStringMap.getValue(java.lang.String)"""
        pass

    @abstractmethod
    def getKeyAt(self, index: int):
        """public abstract java.lang.String org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getKeyAt(int)"""
        pass

    @abstractmethod
    def getValueAt(self, index: int):
        """public abstract <V> V org.apache.logging.log4j.util.IndexedReadOnlyStringMap.getValueAt(int)"""
        pass

    @abstractmethod
    def containsKey(self, key: str):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.containsKey(java.lang.String)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean org.apache.logging.log4j.util.ReadOnlyStringMap.isEmpty()"""
        pass

    @abstractmethod
    def forEach(self, action: 'BiConsumer'):
        """public abstract <V> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, ? super V>)"""
        pass

    @abstractmethod
    def forEach(self, action: 'TriConsumer', state: object):
        """public abstract <V,S> void org.apache.logging.log4j.util.ReadOnlyStringMap.forEach(org.apache.logging.log4j.util.TriConsumer<java.lang.String, ? super V, S>,S)"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int org.apache.logging.log4j.util.ReadOnlyStringMap.size()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.PropertiesPropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.Iterable as Iterable
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.Properties as Properties
from builtins import bool
import org.apache.logging.log4j.util.PropertiesPropertySource as _PropertiesPropertySource
_PropertiesPropertySource = _PropertiesPropertySource
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PropertiesPropertySource():
    """org.apache.logging.log4j.util.PropertiesPropertySource"""
 
    @staticmethod
    def _wrap(java_value: _PropertiesPropertySource) -> 'PropertiesPropertySource':
        return PropertiesPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PropertiesPropertySource):
        """
        Dynamic initializer for PropertiesPropertySource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PropertiesPropertySource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PropertiesPropertySource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def __init__(self, properties: 'Properties'):
        """public org.apache.logging.log4j.util.PropertiesPropertySource(java.util.Properties)"""
        val = _PropertiesPropertySource(properties)
        self.__wrapper = val

    @overload
    def __init__(self, properties: 'Properties', priority: int):
        """public org.apache.logging.log4j.util.PropertiesPropertySource(java.util.Properties,int)"""
        val = _PropertiesPropertySource(properties, _int.valueOf(priority))
        self.__wrapper = val

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

    @overload
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.PropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'._wrap(super(_PropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.PropertiesPropertySource.getPriority()"""
        return int._wrap(super(PropertiesPropertySource, self).getPriority())

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.PropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(_PropertiesPropertySource, self).forEach(action)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.PropertiesPropertySource.getProperty(java.lang.String)"""
        return str._wrap(super(_PropertiesPropertySource, self).getProperty(key))

    @overload
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.PropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool._wrap(super(_PropertiesPropertySource, self).containsProperty(key))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.PropertiesPropertySource.getPropertyNames()"""
        return 'Collection'._wrap(super(PropertiesPropertySource, self).getPropertyNames())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.StringBuilders
from builtins import str
import java.lang.CharSequence as CharSequence
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import org.apache.logging.log4j.util.StringBuilders as _StringBuilders
_StringBuilders = _StringBuilders
import java.lang.String as _string
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StringBuilders():
    """org.apache.logging.log4j.util.StringBuilders"""
 
    @staticmethod
    def _wrap(java_value: _StringBuilders) -> 'StringBuilders':
        return StringBuilders(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StringBuilders):
        """
        Dynamic initializer for StringBuilders.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StringBuilders__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StringBuilders__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def escapeXml(toAppendTo: 'StringBuilder', start: int):
        """public static void org.apache.logging.log4j.util.StringBuilders.escapeXml(java.lang.StringBuilder,int)"""
        _StringBuilders.escapeXml(toAppendTo, _int.valueOf(start))

    @staticmethod
    @overload
    def appendKeyDqValue(sb: 'StringBuilder', key: str, value: object) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.StringBuilders.appendKeyDqValue(java.lang.StringBuilder,java.lang.String,java.lang.Object)"""
        return StringBuilder._wrap(_StringBuilders.appendKeyDqValue(sb, key, value))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def appendSpecificTypes(stringBuilder: 'StringBuilder', obj: object) -> bool:
        """public static boolean org.apache.logging.log4j.util.StringBuilders.appendSpecificTypes(java.lang.StringBuilder,java.lang.Object)"""
        return bool._wrap(_StringBuilders.appendSpecificTypes(stringBuilder, obj))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def appendDqValue(sb: 'StringBuilder', value: object) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.StringBuilders.appendDqValue(java.lang.StringBuilder,java.lang.Object)"""
        return StringBuilder._wrap(_StringBuilders.appendDqValue(sb, value))

    @staticmethod
    @overload
    def appendKeyDqValue(sb: 'StringBuilder', entry: 'Entry') -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.StringBuilders.appendKeyDqValue(java.lang.StringBuilder,java.util.Map$Entry<java.lang.String, java.lang.String>)"""
        return StringBuilder._wrap(_StringBuilders.appendKeyDqValue(sb, entry))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def appendValue(stringBuilder: 'StringBuilder', obj: object):
        """public static void org.apache.logging.log4j.util.StringBuilders.appendValue(java.lang.StringBuilder,java.lang.Object)"""
        _StringBuilders.appendValue(stringBuilder, obj)

    @staticmethod
    @overload
    def trimToMaxSize(stringBuilder: 'StringBuilder', maxSize: int):
        """public static void org.apache.logging.log4j.util.StringBuilders.trimToMaxSize(java.lang.StringBuilder,int)"""
        _StringBuilders.trimToMaxSize(stringBuilder, _int.valueOf(maxSize))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def equalsIgnoreCase(left: 'CharSequence', leftOffset: int, leftLength: int, right: 'CharSequence', rightOffset: int, rightLength: int) -> bool:
        """public static boolean org.apache.logging.log4j.util.StringBuilders.equalsIgnoreCase(java.lang.CharSequence,int,int,java.lang.CharSequence,int,int)"""
        return bool._wrap(_StringBuilders.equalsIgnoreCase(left, _int.valueOf(leftOffset), _int.valueOf(leftLength), right, _int.valueOf(rightOffset), _int.valueOf(rightLength)))

    @staticmethod
    @overload
    def escapeJson(toAppendTo: 'StringBuilder', start: int):
        """public static void org.apache.logging.log4j.util.StringBuilders.escapeJson(java.lang.StringBuilder,int)"""
        _StringBuilders.escapeJson(toAppendTo, _int.valueOf(start))

    @staticmethod
    @overload
    def equals(left: 'CharSequence', leftOffset: int, leftLength: int, right: 'CharSequence', rightOffset: int, rightLength: int) -> bool:
        """public static boolean org.apache.logging.log4j.util.StringBuilders.equals(java.lang.CharSequence,int,int,java.lang.CharSequence,int,int)"""
        return bool._wrap(_StringBuilders.equals(left, _int.valueOf(leftOffset), _int.valueOf(leftLength), right, _int.valueOf(rightOffset), _int.valueOf(rightLength)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.Supplier
import org.apache.logging.log4j.util.Supplier as _Supplier
_Supplier = _Supplier
from abc import abstractmethod, ABC
 
class Supplier():
    """org.apache.logging.log4j.util.Supplier"""
 
    @staticmethod
    def _wrap(java_value: _Supplier) -> 'Supplier':
        return Supplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Supplier):
        """
        Dynamic initializer for Supplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Supplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Supplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract T org.apache.logging.log4j.util.Supplier.get()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.MessageSupplier
import org.apache.logging.log4j.util.MessageSupplier as _MessageSupplier
_MessageSupplier = _MessageSupplier
from abc import abstractmethod, ABC
 
class MessageSupplier():
    """org.apache.logging.log4j.util.MessageSupplier"""
 
    @staticmethod
    def _wrap(java_value: _MessageSupplier) -> 'MessageSupplier':
        return MessageSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MessageSupplier):
        """
        Dynamic initializer for MessageSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MessageSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MessageSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract org.apache.logging.log4j.message.Message org.apache.logging.log4j.util.MessageSupplier.get()"""
        pass 
 
 
# CLASS: org.apache.logging.log4j.util.EnglishEnums
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import org.apache.logging.log4j.util.EnglishEnums as _EnglishEnums
_EnglishEnums = _EnglishEnums
import java.lang.String as _String
_String = _String
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Enum as _Enum
_Enum = _Enum
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class EnglishEnums():
    """org.apache.logging.log4j.util.EnglishEnums"""
 
    @staticmethod
    def _wrap(java_value: _EnglishEnums) -> 'EnglishEnums':
        return EnglishEnums(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EnglishEnums):
        """
        Dynamic initializer for EnglishEnums.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EnglishEnums__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EnglishEnums__wrapper":
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

    @staticmethod
    @overload
    def valueOf(enumType: 'Class', name: str, defaultValue: 'Enum') -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T org.apache.logging.log4j.util.EnglishEnums.valueOf(java.lang.Class<T>,java.lang.String,T)"""
        return Enum._wrap(_EnglishEnums.valueOf(enumType, name, defaultValue))

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

    @staticmethod
    @overload
    def valueOf(enumType: 'Class', name: str) -> 'Enum':
        """public static <T extends java.lang.Enum<T>> T org.apache.logging.log4j.util.EnglishEnums.valueOf(java.lang.Class<T>,java.lang.String)"""
        return Enum._wrap(_EnglishEnums.valueOf(enumType, name))

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
 
 
# CLASS: org.apache.logging.log4j.util.SystemPropertiesPropertySource
from builtins import str
import java.lang.CharSequence as CharSequence
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.logging.log4j.util.SystemPropertiesPropertySource as _SystemPropertiesPropertySource
_SystemPropertiesPropertySource = _SystemPropertiesPropertySource
import java.lang.Iterable as Iterable
import java.lang.CharSequence as _CharSequence
_CharSequence = _CharSequence
import java.util.Collection as Collection
import java.lang.String as _String
_String = _String
import java.lang.String as _string
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SystemPropertiesPropertySource():
    """org.apache.logging.log4j.util.SystemPropertiesPropertySource"""
 
    @staticmethod
    def _wrap(java_value: _SystemPropertiesPropertySource) -> 'SystemPropertiesPropertySource':
        return SystemPropertiesPropertySource(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SystemPropertiesPropertySource):
        """
        Dynamic initializer for SystemPropertiesPropertySource.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SystemPropertiesPropertySource__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SystemPropertiesPropertySource__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getPriority(self) -> int:
        """public int org.apache.logging.log4j.util.SystemPropertiesPropertySource.getPriority()"""
        return int._wrap(super(SystemPropertiesPropertySource, self).getPriority())

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
    def getNormalForm(self, tokens: 'Iterable') -> 'CharSequence':
        """public java.lang.CharSequence org.apache.logging.log4j.util.SystemPropertiesPropertySource.getNormalForm(java.lang.Iterable<? extends java.lang.CharSequence>)"""
        return 'CharSequence'._wrap(super(_SystemPropertiesPropertySource, self).getNormalForm(tokens))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def forEach(self, action: 'BiConsumer'):
        """public void org.apache.logging.log4j.util.SystemPropertiesPropertySource.forEach(org.apache.logging.log4j.util.BiConsumer<java.lang.String, java.lang.String>)"""
        super(_SystemPropertiesPropertySource, self).forEach(action)

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
    def containsProperty(self, key: str) -> bool:
        """public boolean org.apache.logging.log4j.util.SystemPropertiesPropertySource.containsProperty(java.lang.String)"""
        return bool._wrap(super(_SystemPropertiesPropertySource, self).containsProperty(key))

    @overload
    def __init__(self):
        """public org.apache.logging.log4j.util.SystemPropertiesPropertySource()"""
        val = _SystemPropertiesPropertySource()
        self.__wrapper = val

    @staticmethod
    @overload
    def getSystemProperty(key: str, defaultValue: str) -> str:
        """public static java.lang.String org.apache.logging.log4j.util.SystemPropertiesPropertySource.getSystemProperty(java.lang.String,java.lang.String)"""
        return str._wrap(_SystemPropertiesPropertySource.getSystemProperty(key, defaultValue))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getPropertyNames(self) -> 'Collection':
        """public java.util.Collection<java.lang.String> org.apache.logging.log4j.util.SystemPropertiesPropertySource.getPropertyNames()"""
        return 'Collection'._wrap(super(SystemPropertiesPropertySource, self).getPropertyNames())

    @overload
    def getProperty(self, key: str) -> str:
        """public java.lang.String org.apache.logging.log4j.util.SystemPropertiesPropertySource.getProperty(java.lang.String)"""
        return str._wrap(super(_SystemPropertiesPropertySource, self).getProperty(key))

    @overload
    def __init__(self, ):
        """public org.apache.logging.log4j.util.SystemPropertiesPropertySource()"""
        val = _SystemPropertiesPropertySource()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.StackLocatorUtil
import java.util.function.Predicate as Predicate
from builtins import str
import org.apache.logging.log4j.util.StackLocatorUtil as _StackLocatorUtil
_StackLocatorUtil = _StackLocatorUtil
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Deque as Deque
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
import java.lang.ClassLoader as _ClassLoader
_ClassLoader = _ClassLoader
import java.lang.String as _string
import java.util.Deque as _Deque
_Deque = _Deque
import java.lang.Integer as _int
import java.lang.ClassLoader as ClassLoader
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class StackLocatorUtil():
    """org.apache.logging.log4j.util.StackLocatorUtil"""
 
    @staticmethod
    def _wrap(java_value: _StackLocatorUtil) -> 'StackLocatorUtil':
        return StackLocatorUtil(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StackLocatorUtil):
        """
        Dynamic initializer for StackLocatorUtil.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StackLocatorUtil__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StackLocatorUtil__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getCallerClass(sentinelClass: 'Class', callerPredicate: 'Predicate') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.Class<?>,java.util.function.Predicate<java.lang.Class<?>>)"""
        return type.Class._wrap(_StackLocatorUtil.getCallerClass(sentinelClass, callerPredicate))

    @staticmethod
    @overload
    def calcLocation(fqcnOfLogger: str) -> 'StackTraceElement':
        """public static java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocatorUtil.calcLocation(java.lang.String)"""
        return StackTraceElement._wrap(_StackLocatorUtil.calcLocation(fqcnOfLogger))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getCallerClass(fqcn: str, pkg: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.String,java.lang.String)"""
        return type.Class._wrap(_StackLocatorUtil.getCallerClass(fqcn, pkg))

    @staticmethod
    @overload
    def getCurrentStackTrace() -> 'Deque':
        """public static java.util.Deque<java.lang.Class<?>> org.apache.logging.log4j.util.StackLocatorUtil.getCurrentStackTrace()"""
        return Deque._wrap(_StackLocatorUtil.getCurrentStackTrace())

    @staticmethod
    @overload
    def getCallerClassLoader(depth: int) -> 'ClassLoader':
        """public static java.lang.ClassLoader org.apache.logging.log4j.util.StackLocatorUtil.getCallerClassLoader(int)"""
        return ClassLoader._wrap(_StackLocatorUtil.getCallerClassLoader(_int.valueOf(depth)))

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

    @staticmethod
    @overload
    def getStackTraceElement(depth: int) -> 'StackTraceElement':
        """public static java.lang.StackTraceElement org.apache.logging.log4j.util.StackLocatorUtil.getStackTraceElement(int)"""
        return StackTraceElement._wrap(_StackLocatorUtil.getStackTraceElement(_int.valueOf(depth)))

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getCallerClass(fqcn: str) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.String)"""
        return type.Class._wrap(_StackLocatorUtil.getCallerClass(fqcn))

    @staticmethod
    @overload
    def getCallerClass(anchor: 'Class') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(java.lang.Class<?>)"""
        return type.Class._wrap(_StackLocatorUtil.getCallerClass(anchor))

    @staticmethod
    @overload
    def getCallerClass(depth: int) -> 'type.Class':
        """public static java.lang.Class<?> org.apache.logging.log4j.util.StackLocatorUtil.getCallerClass(int)"""
        return type.Class._wrap(_StackLocatorUtil.getCallerClass(_int.valueOf(depth)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.logging.log4j.util.Unbox
from builtins import str
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.StringBuilder as _StringBuilder
_StringBuilder = _StringBuilder
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.lang.StringBuilder as StringBuilder
from builtins import bool
import java.lang.Long as _long
import org.apache.logging.log4j.util.Unbox as _Unbox
_Unbox = _Unbox
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Unbox():
    """org.apache.logging.log4j.util.Unbox"""
 
    @staticmethod
    def _wrap(java_value: _Unbox) -> 'Unbox':
        return Unbox(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Unbox):
        """
        Dynamic initializer for Unbox.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Unbox__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Unbox__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(long)"""
        return StringBuilder._wrap(_Unbox.box(_long.valueOf(value)))

    @staticmethod
    @overload
    def box(value: str) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(char)"""
        return StringBuilder._wrap(_Unbox.box(_char.valueOf(value)))

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

    @staticmethod
    @overload
    def box(value: float) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(double)"""
        return StringBuilder._wrap(_Unbox.box(_double.valueOf(value)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def box(value: bool) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(boolean)"""
        return StringBuilder._wrap(_Unbox.box(_boolean.valueOf(value)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(byte)"""
        return StringBuilder._wrap(_Unbox.box(_byte.valueOf(value)))

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(int)"""
        return StringBuilder._wrap(_Unbox.box(_int.valueOf(value)))

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

    @staticmethod
    @overload
    def box(value: float) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(float)"""
        return StringBuilder._wrap(_Unbox.box(_float.valueOf(value)))

    @staticmethod
    @overload
    def box(value: int) -> 'StringBuilder':
        """public static java.lang.StringBuilder org.apache.logging.log4j.util.Unbox.box(short)"""
        return StringBuilder._wrap(_Unbox.box(_short.valueOf(value)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())