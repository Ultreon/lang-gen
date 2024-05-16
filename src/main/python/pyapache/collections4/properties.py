from __future__ import annotations
from overload import overload


 
from builtins import str
import java.net.URI as URI
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.util.Properties as _Properties
_Properties = _Properties
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as _AbstractPropertiesFactory
_AbstractPropertiesFactory = _AbstractPropertiesFactory
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.util.Properties as Properties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractPropertiesFactory():
    """org.apache.commons.collections4.properties.AbstractPropertiesFactory"""
 
    @staticmethod
    def _wrap(java_value: _AbstractPropertiesFactory) -> 'AbstractPropertiesFactory':
        return AbstractPropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractPropertiesFactory):
        """
        Dynamic initializer for AbstractPropertiesFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractPropertiesFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractPropertiesFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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

 
 
 
# CLASS: org.apache.commons.collections4.properties.AbstractPropertiesFactory
from builtins import str
import java.net.URI as URI
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.util.Properties as _Properties
_Properties = _Properties
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as _AbstractPropertiesFactory
_AbstractPropertiesFactory = _AbstractPropertiesFactory
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.util.Properties as Properties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractPropertiesFactory():
    """org.apache.commons.collections4.properties.AbstractPropertiesFactory"""
 
    @staticmethod
    def _wrap(java_value: _AbstractPropertiesFactory) -> 'AbstractPropertiesFactory':
        return AbstractPropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractPropertiesFactory):
        """
        Dynamic initializer for AbstractPropertiesFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractPropertiesFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractPropertiesFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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

 
 
 
# CLASS: org.apache.commons.collections4.properties.AbstractPropertiesFactory 
 
 
# CLASS: org.apache.commons.collections4.properties.PropertiesFactory
from builtins import str
import org.apache.commons.collections4.properties.PropertiesFactory as _PropertiesFactory
_PropertiesFactory = _PropertiesFactory
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.util.Properties as _Properties
_Properties = _Properties
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as _AbstractPropertiesFactory
_AbstractPropertiesFactory = _AbstractPropertiesFactory
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.util.Properties as Properties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PropertiesFactory():
    """org.apache.commons.collections4.properties.PropertiesFactory"""
 
    @staticmethod
    def _wrap(java_value: _PropertiesFactory) -> 'PropertiesFactory':
        return PropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PropertiesFactory):
        """
        Dynamic initializer for PropertiesFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PropertiesFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PropertiesFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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
 
 
# CLASS: org.apache.commons.collections4.properties.SortedProperties
import java.nio.charset.Charset as Charset
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.collections4.properties.SortedProperties as _SortedProperties
_SortedProperties = _SortedProperties
import java.io.PrintWriter as PrintWriter
import java.util.Properties as _Properties
_Properties = _Properties
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.io.OutputStream as OutputStream
import java.util.Enumeration as Enumeration
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.Enumeration as _Enumeration
_Enumeration = _Enumeration
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.io.PrintStream as PrintStream
import java.util.function.BiConsumer as BiConsumer
import java.lang.Integer as _int
import java.io.Reader as Reader
import java.io.Writer as Writer
import java.io.InputStream as InputStream
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SortedProperties():
    """org.apache.commons.collections4.properties.SortedProperties"""
 
    @staticmethod
    def _wrap(java_value: _SortedProperties) -> 'SortedProperties':
        return SortedProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedProperties):
        """
        Dynamic initializer for SortedProperties.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedProperties__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedProperties__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<java.lang.Object> java.util.Properties.values()"""
        return 'Collection'._wrap(super(Properties, self).values())

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public synchronized void java.util.Properties.forEach(java.util.function.BiConsumer<? super java.lang.Object, ? super java.lang.Object>)"""
        super(_Properties, self).forEach(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public synchronized java.lang.String java.util.Properties.toString()"""
        return str._wrap(super(Properties, self).toString())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public synchronized java.lang.Object java.util.Properties.merge(java.lang.Object,java.lang.Object,java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        return object._wrap(super(_Properties, self).merge(arg0, arg1, arg2))

    @override
    @overload
    def load(self, arg0: 'InputStream'):
        """public synchronized void java.util.Properties.load(java.io.InputStream) throws java.io.IOException"""
        super(_Properties, self).load(arg0)

    @override
    @overload
    def storeToXML(self, arg0: 'OutputStream', arg1: str, arg2: str):
        """public void java.util.Properties.storeToXML(java.io.OutputStream,java.lang.String,java.lang.String) throws java.io.IOException"""
        super(_Properties, self).storeToXML(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getProperty(self, arg0: str, arg1: str) -> str:
        """public java.lang.String java.util.Properties.getProperty(java.lang.String,java.lang.String)"""
        return str._wrap(super(_Properties, self).getProperty(arg0, arg1))

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
    def load(self, arg0: 'Reader'):
        """public synchronized void java.util.Properties.load(java.io.Reader) throws java.io.IOException"""
        super(_Properties, self).load(arg0)

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public synchronized void java.util.Properties.putAll(java.util.Map<?, ?>)"""
        super(_Properties, self).putAll(arg0)

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public synchronized boolean java.util.Properties.replace(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Properties, self).replace(arg0, arg1, arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.properties.SortedProperties()"""
        val = _SortedProperties()
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public synchronized int java.util.Properties.hashCode()"""
        return int._wrap(super(Properties, self).hashCode())

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.putIfAbsent(java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_Properties, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public synchronized boolean java.util.Properties.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Properties, self).remove(arg0, arg1))

    @overload
    def remove(self, arg0: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.remove(java.lang.Object)"""
        return object._wrap(super(_Properties, self).remove(arg0))

    @override
    @overload
    def size(self) -> int:
        """public int java.util.Properties.size()"""
        return int._wrap(super(Properties, self).size())

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<java.lang.Object> java.util.Properties.keySet()"""
        return 'Set'._wrap(super(Properties, self).keySet())

    @override
    @overload
    def keys(self) -> 'Enumeration':
        """public synchronized java.util.Enumeration<java.lang.Object> org.apache.commons.collections4.properties.SortedProperties.keys()"""
        return 'Enumeration'._wrap(super(SortedProperties, self).keys())

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<java.lang.Object, java.lang.Object>> java.util.Properties.entrySet()"""
        return 'Set'._wrap(super(Properties, self).entrySet())

    @override
    @overload
    def loadFromXML(self, arg0: 'InputStream'):
        """public synchronized void java.util.Properties.loadFromXML(java.io.InputStream) throws java.io.IOException,java.util.InvalidPropertiesFormatException"""
        super(_Properties, self).loadFromXML(arg0)

    @override
    @overload
    def storeToXML(self, arg0: 'OutputStream', arg1: str, arg2: 'Charset'):
        """public void java.util.Properties.storeToXML(java.io.OutputStream,java.lang.String,java.nio.charset.Charset) throws java.io.IOException"""
        super(_Properties, self).storeToXML(arg0, arg1, arg2)

    @override
    @overload
    def store(self, arg0: 'Writer', arg1: str):
        """public void java.util.Properties.store(java.io.Writer,java.lang.String) throws java.io.IOException"""
        super(_Properties, self).store(arg0, arg1)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public synchronized boolean java.util.Properties.equals(java.lang.Object)"""
        return bool._wrap(super(_Properties, self).equals(arg0))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.replace(java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_Properties, self).replace(arg0, arg1))

    @override
    @overload
    def list(self, arg0: 'PrintStream'):
        """public void java.util.Properties.list(java.io.PrintStream)"""
        super(_Properties, self).list(arg0)

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public synchronized java.lang.Object java.util.Properties.computeIfAbsent(java.lang.Object,java.util.function.Function<? super java.lang.Object, ?>)"""
        return object._wrap(super(_Properties, self).computeIfAbsent(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.Properties.containsValue(java.lang.Object)"""
        return bool._wrap(super(_Properties, self).containsValue(arg0))

    @override
    @overload
    def elements(self) -> 'Enumeration':
        """public java.util.Enumeration<java.lang.Object> java.util.Properties.elements()"""
        return 'Enumeration'._wrap(super(Properties, self).elements())

    @overload
    def setProperty(self, arg0: str, arg1: str) -> object:
        """public synchronized java.lang.Object java.util.Properties.setProperty(java.lang.String,java.lang.String)"""
        return object._wrap(super(_Properties, self).setProperty(arg0, arg1))

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.put(java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_Properties, self).put(arg0, arg1))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.Properties.isEmpty()"""
        return bool._wrap(super(Properties, self).isEmpty())

    @override
    @overload
    def store(self, arg0: 'OutputStream', arg1: str):
        """public void java.util.Properties.store(java.io.OutputStream,java.lang.String) throws java.io.IOException"""
        super(_Properties, self).store(arg0, arg1)

    @overload
    def getProperty(self, arg0: str) -> str:
        """public java.lang.String java.util.Properties.getProperty(java.lang.String)"""
        return str._wrap(super(_Properties, self).getProperty(arg0))

    @override
    @overload
    def clone(self) -> object:
        """public synchronized java.lang.Object java.util.Properties.clone()"""
        return object._wrap(super(Properties, self).clone())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.properties.SortedProperties()"""
        val = _SortedProperties()
        self.__wrapper = val

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.Properties.contains(java.lang.Object)"""
        return bool._wrap(super(_Properties, self).contains(arg0))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public synchronized java.lang.Object java.util.Properties.compute(java.lang.Object,java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        return object._wrap(super(_Properties, self).compute(arg0, arg1))

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean java.util.Properties.containsKey(java.lang.Object)"""
        return bool._wrap(super(_Properties, self).containsKey(arg0))

    @override
    @overload
    def storeToXML(self, arg0: 'OutputStream', arg1: str):
        """public void java.util.Properties.storeToXML(java.io.OutputStream,java.lang.String) throws java.io.IOException"""
        super(_Properties, self).storeToXML(arg0, arg1)

    @override
    @overload
    def list(self, arg0: 'PrintWriter'):
        """public void java.util.Properties.list(java.io.PrintWriter)"""
        super(_Properties, self).list(arg0)

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public java.lang.Object java.util.Properties.getOrDefault(java.lang.Object,java.lang.Object)"""
        return object._wrap(super(_Properties, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def propertyNames(self) -> 'Enumeration':
        """public java.util.Enumeration<?> java.util.Properties.propertyNames()"""
        return 'Enumeration'._wrap(super(Properties, self).propertyNames())

    @override
    @overload
    def stringPropertyNames(self) -> 'Set':
        """public java.util.Set<java.lang.String> java.util.Properties.stringPropertyNames()"""
        return 'Set'._wrap(super(Properties, self).stringPropertyNames())

    @override
    @overload
    def save(self, arg0: 'OutputStream', arg1: str):
        """public void java.util.Properties.save(java.io.OutputStream,java.lang.String)"""
        super(_Properties, self).save(arg0, arg1)

    @overload
    def get(self, arg0: object) -> object:
        """public java.lang.Object java.util.Properties.get(java.lang.Object)"""
        return object._wrap(super(_Properties, self).get(arg0))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public synchronized void java.util.Properties.replaceAll(java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        super(_Properties, self).replaceAll(arg0)

    @override
    @overload
    def clear(self):
        """public synchronized void java.util.Properties.clear()"""
        super(Properties, self).clear()

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public synchronized java.lang.Object java.util.Properties.computeIfPresent(java.lang.Object,java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        return object._wrap(super(_Properties, self).computeIfPresent(arg0, arg1)) 
 
 
# CLASS: org.apache.commons.collections4.properties.SortedPropertiesFactory
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.util.Properties as _Properties
_Properties = _Properties
import java.lang.String as _String
_String = _String
import org.apache.commons.collections4.properties.SortedPropertiesFactory as _SortedPropertiesFactory
_SortedPropertiesFactory = _SortedPropertiesFactory
import java.net.URL as URL
import java.lang.String as _string
import java.lang.Integer as _int
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as _AbstractPropertiesFactory
_AbstractPropertiesFactory = _AbstractPropertiesFactory
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.util.Properties as Properties
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SortedPropertiesFactory():
    """org.apache.commons.collections4.properties.SortedPropertiesFactory"""
 
    @staticmethod
    def _wrap(java_value: _SortedPropertiesFactory) -> 'SortedPropertiesFactory':
        return SortedPropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SortedPropertiesFactory):
        """
        Dynamic initializer for SortedPropertiesFactory.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SortedPropertiesFactory__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SortedPropertiesFactory__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'._wrap(super(_AbstractPropertiesFactory, self).load(arg0))

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