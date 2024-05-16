from __future__ import annotations
from overload import overload


 
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as __AbstractPropertiesFactory
__AbstractPropertiesFactory = __AbstractPropertiesFactory
from builtins import str
import java.net.URI as URI
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Properties as __Properties
__Properties = __Properties
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.net.URL as URL
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractPropertiesFactory(ABC):
    """org.apache.commons.collections4.properties.AbstractPropertiesFactory"""
 
    @staticmethod
    def __wrap(java_value: __AbstractPropertiesFactory) -> 'AbstractPropertiesFactory':
        return AbstractPropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractPropertiesFactory):
        """
        Dynamic initializer for AbstractPropertiesFactory.
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

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.properties.AbstractPropertiesFactory
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as __AbstractPropertiesFactory
__AbstractPropertiesFactory = __AbstractPropertiesFactory
from builtins import str
import java.net.URI as URI
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Properties as __Properties
__Properties = __Properties
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.net.URL as URL
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class AbstractPropertiesFactory(ABC):
    """org.apache.commons.collections4.properties.AbstractPropertiesFactory"""
 
    @staticmethod
    def __wrap(java_value: __AbstractPropertiesFactory) -> 'AbstractPropertiesFactory':
        return AbstractPropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __AbstractPropertiesFactory):
        """
        Dynamic initializer for AbstractPropertiesFactory.
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

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: org.apache.commons.collections4.properties.AbstractPropertiesFactory 
 
 
# CLASS: org.apache.commons.collections4.properties.PropertiesFactory
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as __AbstractPropertiesFactory
__AbstractPropertiesFactory = __AbstractPropertiesFactory
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as __object
import java.util.Properties as __Properties
__Properties = __Properties
from builtins import type
import java.io.File as File
import java.nio.file.Path as Path
import java.net.URL as URL
import java.lang.Long as __long
import org.apache.commons.collections4.properties.PropertiesFactory as __PropertiesFactory
__PropertiesFactory = __PropertiesFactory
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PropertiesFactory():
    """org.apache.commons.collections4.properties.PropertiesFactory"""
 
    @staticmethod
    def __wrap(java_value: __PropertiesFactory) -> 'PropertiesFactory':
        return PropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PropertiesFactory):
        """
        Dynamic initializer for PropertiesFactory.
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

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.collections4.properties.SortedProperties
import java.util.Enumeration as __Enumeration
__Enumeration = __Enumeration
import java.nio.charset.Charset as Charset
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.util.Collection as Collection
import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Class as __Class
__Class = __Class
import java.io.OutputStream as OutputStream
import java.lang.String as __string
import java.util.Enumeration as Enumeration
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Properties as __Properties
__Properties = __Properties
import java.util.Set as __Set
__Set = __Set
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.Set as Set
import java.lang.Long as __long
import java.io.PrintStream as PrintStream
import java.util.function.BiConsumer as BiConsumer
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.io.Writer as Writer
import org.apache.commons.collections4.properties.SortedProperties as __SortedProperties
__SortedProperties = __SortedProperties
import java.lang.Object as __Object
__Object = __Object
import java.io.InputStream as InputStream
import java.util.function.Function as Function
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class SortedProperties():
    """org.apache.commons.collections4.properties.SortedProperties"""
 
    @staticmethod
    def __wrap(java_value: __SortedProperties) -> 'SortedProperties':
        return SortedProperties(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedProperties):
        """
        Dynamic initializer for SortedProperties.
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
    def getProperty(self, arg0: str, arg1: str) -> str:
        """public java.lang.String java.util.Properties.getProperty(java.lang.String,java.lang.String)"""
        return str.__wrap(super(__Properties, self).getProperty(arg0, arg1))

    @overload
    def containsValue(self, arg0: object) -> bool:
        """public boolean java.util.Properties.containsValue(java.lang.Object)"""
        return bool.__wrap(super(__Properties, self).containsValue(arg0))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<java.lang.Object, java.lang.Object>> java.util.Properties.entrySet()"""
        return 'Set'.__wrap(super(Properties, self).entrySet())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def load(self, arg0: 'InputStream'):
        """public synchronized void java.util.Properties.load(java.io.InputStream) throws java.io.IOException"""
        super(__Properties, self).load(arg0)

    @overload
    def setProperty(self, arg0: str, arg1: str) -> object:
        """public synchronized java.lang.Object java.util.Properties.setProperty(java.lang.String,java.lang.String)"""
        return object.__wrap(super(__Properties, self).setProperty(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public synchronized void java.util.Properties.forEach(java.util.function.BiConsumer<? super java.lang.Object, ? super java.lang.Object>)"""
        super(__Properties, self).forEach(arg0)

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.replace(java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__Properties, self).replace(arg0, arg1))

    @override
    @overload
    def stringPropertyNames(self) -> 'Set':
        """public java.util.Set<java.lang.String> java.util.Properties.stringPropertyNames()"""
        return 'Set'.__wrap(super(Properties, self).stringPropertyNames())

    @override
    @overload
    def load(self, arg0: 'Reader'):
        """public synchronized void java.util.Properties.load(java.io.Reader) throws java.io.IOException"""
        super(__Properties, self).load(arg0)

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public synchronized boolean java.util.Properties.remove(java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Properties, self).remove(arg0, arg1))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public synchronized void java.util.Properties.replaceAll(java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        super(__Properties, self).replaceAll(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def loadFromXML(self, arg0: 'InputStream'):
        """public synchronized void java.util.Properties.loadFromXML(java.io.InputStream) throws java.io.IOException,java.util.InvalidPropertiesFormatException"""
        super(__Properties, self).loadFromXML(arg0)

    @override
    @overload
    def store(self, arg0: 'Writer', arg1: str):
        """public void java.util.Properties.store(java.io.Writer,java.lang.String) throws java.io.IOException"""
        super(__Properties, self).store(arg0, arg1)

    @override
    @overload
    def toString(self) -> str:
        """public synchronized java.lang.String java.util.Properties.toString()"""
        return str.__wrap(super(Properties, self).toString())

    @overload
    def put(self, arg0: object, arg1: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.put(java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__Properties, self).put(arg0, arg1))

    @override
    @overload
    def save(self, arg0: 'OutputStream', arg1: str):
        """public void java.util.Properties.save(java.io.OutputStream,java.lang.String)"""
        super(__Properties, self).save(arg0, arg1)

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public synchronized java.lang.Object java.util.Properties.merge(java.lang.Object,java.lang.Object,java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        return object.__wrap(super(__Properties, self).merge(arg0, arg1, arg2))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public java.lang.Object java.util.Properties.getOrDefault(java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__Properties, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def putAll(self, arg0: 'Map'):
        """public synchronized void java.util.Properties.putAll(java.util.Map<?, ?>)"""
        super(__Properties, self).putAll(arg0)

    @overload
    def remove(self, arg0: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.remove(java.lang.Object)"""
        return object.__wrap(super(__Properties, self).remove(arg0))

    @overload
    def getProperty(self, arg0: str) -> str:
        """public java.lang.String java.util.Properties.getProperty(java.lang.String)"""
        return str.__wrap(super(__Properties, self).getProperty(arg0))

    @override
    @overload
    def propertyNames(self) -> 'Enumeration':
        """public java.util.Enumeration<?> java.util.Properties.propertyNames()"""
        return 'Enumeration'.__wrap(super(Properties, self).propertyNames())

    @override
    @overload
    def size(self) -> int:
        """public int java.util.Properties.size()"""
        return int.__wrap(super(Properties, self).size())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public synchronized java.lang.Object java.util.Properties.computeIfAbsent(java.lang.Object,java.util.function.Function<? super java.lang.Object, ?>)"""
        return object.__wrap(super(__Properties, self).computeIfAbsent(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public synchronized int java.util.Properties.hashCode()"""
        return int.__wrap(super(Properties, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def elements(self) -> 'Enumeration':
        """public java.util.Enumeration<java.lang.Object> java.util.Properties.elements()"""
        return 'Enumeration'.__wrap(super(Properties, self).elements())

    @overload
    def __init__(self, ):
        """public org.apache.commons.collections4.properties.SortedProperties()"""
        val = __SortedProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public synchronized java.lang.Object java.util.Properties.putIfAbsent(java.lang.Object,java.lang.Object)"""
        return object.__wrap(super(__Properties, self).putIfAbsent(arg0, arg1))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public synchronized java.lang.Object java.util.Properties.computeIfPresent(java.lang.Object,java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        return object.__wrap(super(__Properties, self).computeIfPresent(arg0, arg1))

    @overload
    def get(self, arg0: object) -> object:
        """public java.lang.Object java.util.Properties.get(java.lang.Object)"""
        return object.__wrap(super(__Properties, self).get(arg0))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean java.util.Properties.isEmpty()"""
        return bool.__wrap(super(Properties, self).isEmpty())

    @override
    @overload
    def store(self, arg0: 'OutputStream', arg1: str):
        """public void java.util.Properties.store(java.io.OutputStream,java.lang.String) throws java.io.IOException"""
        super(__Properties, self).store(arg0, arg1)

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public synchronized boolean java.util.Properties.replace(java.lang.Object,java.lang.Object,java.lang.Object)"""
        return bool.__wrap(super(__Properties, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def list(self, arg0: 'PrintWriter'):
        """public void java.util.Properties.list(java.io.PrintWriter)"""
        super(__Properties, self).list(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public synchronized boolean java.util.Properties.equals(java.lang.Object)"""
        return bool.__wrap(super(__Properties, self).equals(arg0))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<java.lang.Object> java.util.Properties.values()"""
        return 'Collection'.__wrap(super(Properties, self).values())

    @overload
    def containsKey(self, arg0: object) -> bool:
        """public boolean java.util.Properties.containsKey(java.lang.Object)"""
        return bool.__wrap(super(__Properties, self).containsKey(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.collections4.properties.SortedProperties()"""
        val = __SortedProperties()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def storeToXML(self, arg0: 'OutputStream', arg1: str, arg2: 'Charset'):
        """public void java.util.Properties.storeToXML(java.io.OutputStream,java.lang.String,java.nio.charset.Charset) throws java.io.IOException"""
        super(__Properties, self).storeToXML(arg0, arg1, arg2)

    @overload
    def contains(self, arg0: object) -> bool:
        """public boolean java.util.Properties.contains(java.lang.Object)"""
        return bool.__wrap(super(__Properties, self).contains(arg0))

    @override
    @overload
    def storeToXML(self, arg0: 'OutputStream', arg1: str, arg2: str):
        """public void java.util.Properties.storeToXML(java.io.OutputStream,java.lang.String,java.lang.String) throws java.io.IOException"""
        super(__Properties, self).storeToXML(arg0, arg1, arg2)

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public synchronized java.lang.Object java.util.Properties.compute(java.lang.Object,java.util.function.BiFunction<? super java.lang.Object, ? super java.lang.Object, ?>)"""
        return object.__wrap(super(__Properties, self).compute(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<java.lang.Object> java.util.Properties.keySet()"""
        return 'Set'.__wrap(super(Properties, self).keySet())

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
    def keys(self) -> 'Enumeration':
        """public synchronized java.util.Enumeration<java.lang.Object> org.apache.commons.collections4.properties.SortedProperties.keys()"""
        return 'Enumeration'.__wrap(super(SortedProperties, self).keys())

    @override
    @overload
    def storeToXML(self, arg0: 'OutputStream', arg1: str):
        """public void java.util.Properties.storeToXML(java.io.OutputStream,java.lang.String) throws java.io.IOException"""
        super(__Properties, self).storeToXML(arg0, arg1)

    @override
    @overload
    def list(self, arg0: 'PrintStream'):
        """public void java.util.Properties.list(java.io.PrintStream)"""
        super(__Properties, self).list(arg0)

    @override
    @overload
    def clone(self) -> object:
        """public synchronized java.lang.Object java.util.Properties.clone()"""
        return object.__wrap(super(Properties, self).clone())

    @override
    @overload
    def clear(self):
        """public synchronized void java.util.Properties.clear()"""
        super(Properties, self).clear() 
 
 
# CLASS: org.apache.commons.collections4.properties.SortedPropertiesFactory
import org.apache.commons.collections4.properties.AbstractPropertiesFactory as __AbstractPropertiesFactory
__AbstractPropertiesFactory = __AbstractPropertiesFactory
from builtins import str
from pyquantum_helper import override
import java.net.URI as URI
import java.lang.Object as __object
import java.util.Properties as __Properties
__Properties = __Properties
from builtins import type
import java.io.File as File
import org.apache.commons.collections4.properties.SortedPropertiesFactory as __SortedPropertiesFactory
__SortedPropertiesFactory = __SortedPropertiesFactory
import java.nio.file.Path as Path
import java.net.URL as URL
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.io.Reader as Reader
import java.lang.ClassLoader as ClassLoader
import java.io.InputStream as InputStream
import java.lang.Object as __Object
__Object = __Object
import java.util.Properties as Properties
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SortedPropertiesFactory():
    """org.apache.commons.collections4.properties.SortedPropertiesFactory"""
 
    @staticmethod
    def __wrap(java_value: __SortedPropertiesFactory) -> 'SortedPropertiesFactory':
        return SortedPropertiesFactory(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SortedPropertiesFactory):
        """
        Dynamic initializer for SortedPropertiesFactory.
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

    @overload
    def load(self, arg0: 'URL') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URL) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'InputStream') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.InputStream) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def load(self, arg0: 'URI') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.net.URI) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

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
    def load(self, arg0: 'Path') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.nio.file.Path) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'Reader') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.Reader) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def load(self, arg0: 'ClassLoader', arg1: str) -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.lang.ClassLoader,java.lang.String) throws java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0, arg1))

    @overload
    def load(self, arg0: 'File') -> 'Properties':
        """public T org.apache.commons.collections4.properties.AbstractPropertiesFactory.load(java.io.File) throws java.io.FileNotFoundException,java.io.IOException"""
        return 'Properties'.__wrap(super(__AbstractPropertiesFactory, self).load(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))